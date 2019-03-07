import os, sys
from django.core.management.base import BaseCommand, CommandError
from catalog.models import Publication
from bs4 import BeautifulSoup
import urllib.request

# Open a file
html_files_path = "/home/ds/cyser/journals/html/"
txt_file = '/home/ds/cyser/journals/url_list4.txt'

journals = ["arion", "vestnik", "volga", "druzhba", "zvezda", "znamia", "inostran", "neva", "nov_yun", "nj", "novyi_mi",
            "october", "ural", "voplit", "nlo", "nz", "homo_legens", "prosodia", "sp", "din", "ra", "zerkalo", "ier",
            "interpoezia", "kreschatik", "bereg", "volga21", "zz", "continent", "km", "logos", "nrk", "nlik", "oz",
            "sib", "slovo", "slo", "studio", "urnov"]



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


def create_dictionary(html_files_path, txt_file):
    """
    For each file in a list of file paths, reads the text file with the original URL for relevant data.  Also uses
    beautifulsoup to parse the html for relevant features.
    :param txt_file: path to the text file with filename and sentence data
    :param image_path: A string with the location of the image files on server.
    :return:a dictionary with a key, and 'author' and 'path'
    """
    #Need title, author, edition, text, date

    data = {}
    test = []
    html_files = files_list(html_files_path)

    # Create a dictionary with keys for all of the files and their file paths on the server.
    for name in html_files:
        key = name.split('/')[-1].replace('.html','')
        test.append(key)
        html = open(name.replace('\n', ''), 'r').read()
        data[key] = {}
        data[key]['file_path'] = name
        data[key]['html'] = html

    #Read the txt file to get data from the original URL and add it to the dictionary given the keys set above.
    with open(txt_file, 'r') as f:
        for line in f:
            key = line.split('/')[-1].replace('.html','')

            # example http://magazines.russ.ru/novyi_mi/2016/12/mariya-galina-hyperfiction.html
            #html = urllib.request.urlopen('http://magazines.russ.ru/novyi_mi/2016/12/mariya-galina-hyperfiction.html')
            #html = html.read()
            #soup = BeautifulSoup(html, 'html.parser')
            #title = soup.title.string
            #soup.findAll("meta", {"property": "og:title"})
            
            if any(journal in journals for journal in line):
                for journal in journals:
                    if path.find(journal) != -1:
                        this_journal = journal

                if re.match(r"\d{4}", line):
                    year = re.match(\d{4}, line)

                if re.match((r"\d{2}", line):
                    pass

    return data, test
    """
    with open(txt_file, 'r') as f:
        for line in f:
            if line[0] == '#':
                pass
            else:
                try:

                    key = line.split()[0]
                    sentence = line.split()[-1]

                    my_dict[key]['sentence'] = sentence.replace('|', ' ')

                except KeyError:
                    print('key error: {}'.format(key))

    """

class Command(BaseCommand):
    help = "Load html or text into the database"

    def handle(self, *args, **options):
        data, test = create_dictionary(html_files_path, txt_file)
        #print(data)
        #print("Check for unique keys", len(test), len(set(test)))
        #for file in dirs:

            #Publication.objects.update_or_create(
                # title = ,
                # author = ,
                # edition = ,
                #text = file,
                # date = ,
            #
