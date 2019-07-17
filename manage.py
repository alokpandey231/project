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

list =  ['$ -$ 1,031.6$ -',
 '-64.5-',
 '-614.8-',
 '761.124.1-',
 '-392.6-',
 '583.82.0-',
 '-176.0-',
 '527.7--',
 '487.1--',
 '-279.7-',
 '-8.0-',
 '342.47.2-',
 '-130.1-',
 '-64.2-',
 '-187.7-',
 '237.30.4-',
 '217.82.8-',
 '198.8--',
 '169.217.6-',
 '176.51.3-',
 '130.845.7-',
 'nan',
 '-43.3-',
 '-15.2-',
 '139.7--',
 '128.00.3-',
 '115.8--',
 '94.6--',
 '-6.4-',
 '85.0--',
 '56.12.3-',
 '-0.4-',
 '50.9--',
 '71.0--',
 '49.0--',
 '-6.3-',
 '-0.7-',
 '9.5--',
 '690.8379.539.5',
 '$ 5,322.9$ 3,504.7$ 39.5']
#process the list
print ("lenght of list is",len(list))
for i in range(0,len(list)):
    list[i] = list[i].replace("$","").replace(" ","")
    list[i] = list[i].split("-")
final_list = []
#change the values
for i in list:
    print (len(i))
    if len(i) == 3:
        print (len(i))
        sub_list = []
        sub_list.insert(0,i[0])
        sub_list.insert(1,i[1])
        sub_list.insert(2,i[2])
        final_list.append(sub_list)
print (final_list)
print ("lenght of final list is",len(final_list))


#print (list)
