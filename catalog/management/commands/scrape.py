from django.core.management.base import BaseCommand
from catalog.models import *
from bs4 import BeautifulSoup, NavigableString, Tag
import urllib.request

domain = 'http://magazines.russ.ru/'

class CurrentCategory:
    def __init__(self, category, journal, year, issue):
        self.category = ''
        self.journal = journal
        self.year = year
        self.issue = issue


def make_toc_list(journal):
    with urllib.request.urlopen(domain + journal + '/') as response:
        html = response.read()
        soup = BeautifulSoup(html, 'lxml')
        toc = soup.find('table')
        toc = toc.findAll('a')
        toc_list = [a['href'] for a in toc]
        return toc_list


def remove_comments(text):
    start = text.find('<!--')
    end = text.find('-->')
    remove = text[start:end+3]
    text = text.replace(remove, '')
    return text


def scrape_text(url):
    with urllib.request.urlopen(domain + url) as response:
        html = response.read()
        soup = BeautifulSoup(html,'lxml')
        if soup.find("div",{"class":"article"}):
            text = soup.find("div",{"class":"article"})
            text = text.text

            text = text.replace("""Версия для печати


            (function (d, s, id) {
                    var js, fjs = d.getElementsByTagName(s)[0];
                    if (d.getElementById(id)) return;
                    js = d.createElement(s);
                    js.id = id;
                    js.src = "//connect.facebook.net/ru_RU/sdk.js#xfbml=1&appId=469951869692317&version=v2.0";
                    fjs.parentNode.insertBefore(js, fjs);
                }(document, 'script', 'facebook-jssdk'));


            Tweet
            !function (d, s, id) {
                    var js, fjs = d.getElementsByTagName(s)[0], p = /^http:/.test(d.location) ? 'http' : 'https';
                    if (!d.getElementById(id)) {
                        js = d.createElement(s);
                        js.id = id;
                        js.src = p + '://platform.twitter.com/widgets.js';
                        fjs.parentNode.insertBefore(js, fjs);
                    }
                }(document, 'script', 'twitter-wjs');""", '')
            text = remove_comments(text)
            return text
        else:
            text = ''
            return text

def read_toc(toc):
    print(domain + toc)
    with urllib.request.urlopen(domain + toc) as response:

        # Create a current_category object to retain information as we read down the TOC
        current_category = CurrentCategory
        current_category.category = ''
        html = response.read()
        soup = BeautifulSoup(html, 'lxml')
        toc_html = soup.find('div', attrs={'class': 'jrn_right'})
        current_category.journal = toc_html.find('h5').string

        counter = 0

        for row in toc_html:

            if isinstance(row, NavigableString):
                pass
            if isinstance(row, Tag):
                if row.name == 'h6':
                    current_category.category = row.string
                try:
                    author = row.find('strong').string
                except AttributeError:
                    author = ''
                    pass
                try:
                    link = row.find('a')['href']
                except TypeError:
                    link = ''
                    pass
                try:
                    title = row.a.string
                except AttributeError:
                    title = ''
                    pass
                try:
                    genre = row.i.string
                except AttributeError:
                    genre = ''
                    pass

                if author != '':
                    counter += 1
                    category = current_category.category
                    journal = current_category.journal
                    year = toc.split('/')[2]
                    issue = toc.split('/')[3]

                    text = scrape_text(link)

                    TableofContents.objects.update_or_create(
                        order=counter,
                        journal=journal,
                        year=year,
                        issue=issue,
                        category=category,
                        author=author,
                        link=link,
                        title=title,
                        genre=genre,
                        text=text,
                    )
                    #print(counter,journal, year, issue, category, author, link,title,genre, text)

        current_category.category = ''

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('journal', nargs='+', type=str)

    def handle(self, *args, **options):
        journal = options['journal'][0]
        toc_list = make_toc_list(journal)
        for toc in toc_list:
            read_toc(toc)
