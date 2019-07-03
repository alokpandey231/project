#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "locallibrary.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import csv
import pandas as pd
def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just #prints them, but you can
    make it do anything.
    """
    #print(e)

from bs4 import BeautifulSoup
raw_html = simple_get('https://www.fda.gov/news-events/fda-newsroom/press-announcements')
html = BeautifulSoup(raw_html, 'html.parser')

#print ("no issues")
table = html.find('div', attrs = {'class':'view-content'})
date = []
news = []
parag = []
rel_dates = []
for row in table.findAll('div', attrs = {'class':'item-list'}):

    for num,li in enumerate(row.findAll('a')):
        print (num)
        raw_html1 = simple_get('https://www.fda.gov/' + (li.get('href')) )
        ##print ('https://www.fda.gov' + (li.get('href')))

        html1 = BeautifulSoup(raw_html1, 'html.parser')

        #html_start = html1.find('div', attrs = {'class':'field field--name-field-person-entity field--type-entity-reference field--label-above'})
        ##print (html_start)
        #exit()
        rel_date  = html1.find('dd', attrs = {'class':'cell-2_1'})
        if rel_date.text is not None:
            rel_dates.append(rel_date.text)
        else:
            rel_dates.append("null")
        print ("here")
        html1 = html1.find('div', attrs = {'class':'col-md-8 col-md-push-2'})
        text_data = " "
        #print (html1)
        for para in html1.findAll('p'):

            text_data +=  para.text + " "

        date.append(row.h3.text)
        news.append(li.text)
        parag.append(text_data)
        #print (type(parag))
#print (len(date),print(news),print (rel_date))
print("here1")
##print (li.text)
df = pd.DataFrame({'Date':date,'Press announcements':news,'Details':parag,'Release dates':rel_dates})
df.to_csv('press_announcements.csv', index=False,encoding='utf-8-sig')
