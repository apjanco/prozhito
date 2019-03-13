"""
This script gathers information from three sources and writes the data to a csv file.
Source #1 is a directory of cleaned text files, which are written to the text column.
Source #2 is a directory of raw html files with metadata that is scraped with beautiful soup for author and title
Source #3 is a text file of the original URLs which contain journal, year and issue
"""

import os
import csv
from tqdm import tqdm
from bs4 import BeautifulSoup
from catalog.models import Publication
from django.core.management.base import BaseCommand, CommandError

text_files_path = "/home/ds/cyser/journals/cleaned"  # Source #1
html_files_path = "/home/ds/cyser/journals/html"  # Source #2
txt_file = '/home/ds/cyser/journals/url_list4.txt'  # Source #3

journals = ["arion", "vestnik", "volga", "druzhba", "zvezda", "znamia", "inostran", "neva", "nov_yun", "nj", "novyi_mi",
            "october", "ural", "voplit", "nlo", "nz", "homo_legens", "prosodia", "sp", "din", "ra", "zerkalo", "ier",
            "interpoezia", "kreschatik", "bereg", "volga21", "zz", "continent", "km", "logos", "nrk", "nlik", "oz",
            "sib", "slovo", "slo", "studio", "urnov"]


# This is needed to load really large fields in the csv
import sys
import csv
maxInt = sys.maxsize
decrement = True

while decrement:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True


def files_list(path):
    """
    A function that takes a directory str as input and returns a list of all files in that directory and subdirectories.
    This is similar to os.listdir, but returns the full path to the file rather than just the filename.
    :param path: str, path on the server to the files directory
    :return: paths: list, a list of all files and their complete paths on the server
    """
    paths = []
    for root, dirs, files in os.walk(path):
        for name in files:
            paths.append(os.path.join(root, name))
    return paths


def find_path(filename, txt_file_list):
    """
    Given an html filename, return the full URL if it exists in the text file list.

    :param filename: str
    :param txt_file_list: list
    :return: URL: str
    """
    path = None
    while path is None:
        for line in txt_file_list:
            try:
                if line.split('/')[-1].find(filename) != -1:
                    path = line.replace('\n','')
            except Exception as e:
                print(e)
    return path


def scrape_author(html_file):
    # <meta name="author" content="С.Костырко">
    with open(html_file, errors="ignore") as html_file:
        soup = BeautifulSoup(html_file, 'lxml')
        try:
            author = soup.find('meta', property='article:author')['content']
            return author
        except TypeError:
            author = ''
            return author


def scrape_title(html_file):
    with open(html_file, errors="ignore") as html_file:
        soup = BeautifulSoup(html_file, 'lxml')
        try:
            publication_name = soup.find('meta', property='og:title')['content']
            return publication_name
        except TypeError:
            publication_name = ''
            return publication_name


def create_row(csv_filename, field_names, name, text, journal, title, author, year, issue):
    with open(csv_filename, "a") as fd:
        writer = csv.DictWriter(fd, field_names)

        row = {}
        row['filename'] = name.split('/')[-1]
        row['text'] = text
        row['journal'] = journal
        row['author'] = author
        row['title'] = title
        row['year'] = year
        row['issue'] = issue
        writer.writerow(row)


def create_csv(text_files_path, txt_file, csv_filename, field_names):
    """
    For each file in a list of file paths, reads the text file with the original URL for relevant data.  Also uses
    beautifulsoup to parse the html for relevant features.
    :param txt_file: path to the text file with filename and sentence data
    :param image_path: A string with the location of the image files on server.
    :return:a dictionary with a key, and 'author' and 'path'
    """


    text_files = files_list(text_files_path)
    html_files = files_list(html_files_path)
    assert len(text_files) != 0

    current_db = Publication.objects.all()
    existing_files = [file.url.split('/')[-1] for file in current_db]

    def create_txt_file_list(txt_file):
        with open(txt_file, 'r') as f:
                txt_file_list = f.readlines()
                assert len(txt_file_list) != 0
                return txt_file_list

    txt_file_list = create_txt_file_list(txt_file)

    # There are 160k urls in the text_file_list.  Many of them are dead links.
    # Remove all paths that do not correspond to a file in text_files_path
    # new_text_files = [file.split('/')[-1] for file in text_files]
    # new_txt_file_list = [file.split('/')[-1].replace('\n','') for file in txt_file_list]
    # txt_file_list = set(new_txt_file_list).intersection(set(new_text_files))
    # Problem: how to get back from the intersection to list of urls?
    # TODO Try find_path(txt_file_list)

    for name in tqdm(text_files):

        if name.split('/')[-1] in existing_files:
            #print('existing record {}'.format(name))
            pass
        else:
            try:
                if '\n' in name:
                    name = name.replace('\n', '')
                try:
                    text = open(name, 'r').read()
                except UnicodeDecodeError:
                    print('unicode error')
                    text = ''

                # Get the original URL for the file
                url = find_path(name.split('/')[-1], txt_file_list)

                # Get the html file path for the file
                html_file = find_path(name.split('/')[-1], html_files)

                # extract the journal name from the url
                for journal in journals:
                    if url.find(journal) != -1:
                        journal_name = journal
                    else:
                        pass

                # Try to extract author and title information from the html
                author = scrape_author(html_file)
                if author:
                    author = author
                else:
                    author = ''

                title = scrape_title(html_file)

                if title:
                    title = title

                else:
                    title = ''

                try:
                    year = int(url.split('/')[4])

                except (ValueError, IndexError):
                    year = None

                try:
                    issue = int(url.split('/')[5])

                except (ValueError, IndexError):
                    issue = None

                """title = models.CharField(max_length=200)
                   author = models.CharField(max_length=200)
                   journal = models.CharField(max_length=200)
                   text = models.TextField(help_text='Text of the publication')
                   year = models.DateField(auto_now_add = True, help_text='Date when publication was published')
                   url = models.TextField(help_text='Text of the publication')
                """
                Publication.objects.update_or_create(
                    title=title,
                    author=author,
                    journal=journal_name,
                    text=text,
                    year=year,
                    issue=issue,
                    url=url,
                )
                #create_row(csv_filename, field_names, name, text, journal_name, title, author, year, issue)

            except Exception as e:
                print('error: {}'.format(e))
                pass


class Command(BaseCommand):
    help = "Load html or text into the database"

    def handle(self, *args, **options):
        field_names = ['filename', 'text', 'journal', 'author', 'title', 'year', 'issue']
        csv_filename = "full_journals_data.csv"

        create_csv(text_files_path, txt_file, csv_filename, field_names)
