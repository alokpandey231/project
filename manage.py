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
    print(e)

def get_data(url):
    raw_html = simple_get(url)
    html = BeautifulSoup(raw_html, 'html.parser')
    #pagination js-pager__items

    #print ("no issues")
    table = html.find('div', attrs = {'class':'view-content'})

    for row in table.findAll('div', attrs = {'class':'item-list'}):

        for num,li in enumerate(row.findAll('a')):
            print (li.get('href').replace('/index.php/index.php',''))
            raw_html1 = simple_get('https://www.fda.gov/' + li.get('href').replace('/index.php/index.php',''))
            #print (raw_html1)
            ##print ('https://www.fda.gov' + (li.get('href')))

            html1 = BeautifulSoup(raw_html1, 'html.parser')
            print (html)

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

date = []
news = []
parag = []
rel_dates = []

raw_html = simple_get('https://www.fda.gov/news-events/fda-newsroom/press-announcements')
html = BeautifulSoup(raw_html, 'html.parser')
last_page = html.find('a', attrs = {'rel':'last'})

total_page = int(last_page.get('href').split('=')[1] ) + 1
#get_data('https://www.fda.gov/news-events/fda-newsroom/press-announcements?page=5')

for i in range(0,total_page):
    print (i,"round")
    if i != 5:
        get_data('https://www.fda.gov/news-events/fda-newsroom/press-announcements?page={}'.format(i))

#print (len(date),print(news),print (rel_date))
print("here1")
##print (li.text)
df = pd.DataFrame({'Date':date,'Press announcements':news,'Details':parag,'Release dates':rel_dates})
df.to_csv('press_announcements.csv', index=False,encoding='utf-8-sig')

