"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls), 
    url(r'^catalog/', include('catalog.urls')),
    url(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#Add Django site authentication urls (for login, logout, password management)
#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

 import requests
from bs4 import BeautifulSoup

def get_data(keyword):
    # api-endpoint
    try:
        URL = "https://www.whocc.no/atc_ddd_index/"

        # location given here
        code = 'ATC code'
        name = keyword.lower()
        namesearchtype = 'containing'

        # defining a params dict for the parameters to be sent to the API
        PARAMS = {'code':code,'name':name,'namesearchtype':namesearchtype}

        # sending get request and saving the response as response object
        r = requests.get(url = URL, params = PARAMS)
        r = r.content
        html = BeautifulSoup(r, 'html.parser')
        #print (html)
        table = html.find('div', attrs= {'id': 'content'})
        table = html.findAll('tr')
        #print (table)
        dict = {}
        for i in table:
            r = i.findAll('td')[1].text
            a = i.find('a',href=True)['href'].split('=')[1]
            if name == r:
                get_url = URL + i.find('a',href=True)['href']
                r2 = requests.get(url=get_url).content
                html2 = BeautifulSoup(r2, 'html.parser')
                table = html2.find('div', attrs= {'id': 'content'})
                table = table.findAll('b')[-1]
                atc_code = table.find('a')['href'].split('=')[1]
                description = table.find('a').text
                #print ("ATC_CODE: " ,atc_code,"Description: ",description)
                dict[atc_code] = description
        if dict == {}:
            return None
        else:
            return dict
    except Exception as e:
        print (e)
        return None


#main function starts from here
import pandas as pd
df=pd.read_csv('/home/tcs/Downloads/products_patents_exclusivity.csv',sep='~').drop_duplicates(['Ingredient'])
print (len(df))
sf =  df['Ingredient'].str.split(";")
count = 0
ccount = 0
list=[]
for item in sf:
    #print (type(item))
    #process the single data
    if len(item) == 1:
        print (item[0])
        atc_data = get_data(item[0])
        #print (atc_data)
        atc_data = [item[0],atc_data]
        #print ("1data",atc_data)
        #check if you got any data
        if atc_data[1] is None and item[0].find(' ')!= -1:
            new_data =  item[0].split(" ")           
            for word in new_data:
                    atc_data = get_data(word)
                    atc_data = [word,atc_data]
                    if atc_data[1] is not None:
                        break
            if atc_data[1] is  None:
                atc_data = "Not found"      
        else:
            if atc_data[1] is None:
                atc_data = "Not found"
            else:
                atc_data = atc_data
                    

            
    elif len(item) ==2:
        atc_data = None
    else:
        atc_data = None
    list.append(atc_data)
df['Atc_code '] = list
df.to_csv('/home/tcs/output.csv')
