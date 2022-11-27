import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import sys
import numpy as np
from firebase import* 
driver= webdriver.Chrome()## zapytac





def run_web(driver):
    url='https://www.vinted.pl/'
    web=driver.get(url)
    return web


def get_url(search_term):
    """Generate a url from search term"""
    template ='https://www.vinted.pl/catalog?search_text={}'
    search_term=search_term.replace(' ', '+')
    return template.format(search_term)

def parse_ssr(goal_url, driver):
    driver.get(goal_url)
    soup= BeautifulSoup(driver.page_source, 'html.parser')
    results=soup.find_all("div", class_="web_ui__ItemBox__box")
    return  results

def get_info(results):
    item=results
    main_info_arr=[]
    for manga in item:
        for info in manga.find_all("a", attrs={"class": 'web_ui__ItemBox__overlay'}): 
             url=info.get('href')
             price=info.get('title')
             results=url,price
             result_3 = [item.split(',') for item in results]
             result_3_flat = [item for l in result_3 for item in l]
             del result_3_flat[3]
             main_info_arr.extend(result_3_flat)
    return main_info_arr, url



def get_likess(results):
    item=results
    like_items=[]
    for i in item:
        for items in i.select('.web_ui__Cell__suffix'):
            like=items.find('h4').text
            like_items.append(like)
    return like_items

def item_description (url):
    time_add=[]
    driver.get(url)
    soup= BeautifulSoup(driver.page_source, 'html.parser')
    for time in soup.find_all("time", class_="relative"):
        time_of_add=time.get('title')
    time_add.append(time_of_add)  
    return time_add

def join(parse):
    join_info,url=get_info(parse)
    join_info.extend(get_likess(parse))
    join_info.extend(item_description(url))

    return join_info
#----------------------------------------------------------------------------------------------
#Record info
def rec_info(parse):
    record_info=[]
    for item in parse:
        record_info.append(join(item))
    return record_info



#----------------------------------------------------------------------------------------------
#Convert to dict
def dict_conv(record_info):
    mydict={}
    print(type(mydict))
    n=0
    ini_list=['Link', 'Title', 'Cost', 'Marka', 'Size', 'Stars', 'Date']
    for it in record_info:
        for index, i in enumerate(it):
            mydict[index]=f"{i}"
            final_dict = dict(zip(ini_list, list(mydict.values())))
        n+=1
        print(n)   
        print('----------------------------------------------------------')
        print(final_dict)
        
        database.child('Data').child(f'Item_{n}').set(final_dict)
     


def main():
    
    run_web(driver)
    # goal_url=get_url(sys.argv[1])
    goal_url=get_url('puma')
    parse=parse_ssr(goal_url, driver)
    record_info=rec_info(parse)
    dict_conv(record_info)
    
    # print(record_info)
    # print(len(record_info))
    # print(record_info[0])
    # mydict={}
    # print(type(mydict))
    # for index, i in enumerate(record_info[0]):
    #     mydict[index]=f"{i}"
   



    

    
  












if __name__ == '__main__':
    main()
    

