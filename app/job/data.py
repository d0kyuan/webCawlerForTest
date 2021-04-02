#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: data.py
# Project: job
# Created Date: Thursday, April 1st 2021, 1:25:15 pm
# Author: Ray
# -----
# Last Modified:
# Modified By:
# -----
# Copyright (c) 2021 Ray
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
###
#
import requests
from bs4 import BeautifulSoup

from enum import Enum
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import random
import json
import pprint
options = Options()
options.add_argument("--disable-notifications")  # 取消所有的alert彈出視窗

browser = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=options)


doJob: bool = True


def onePageDataSave(pageName="https://rent.591.com.tw/rent-detail-10650272.html", region=0):
    sName = ""
    sType = 0
    sPhone = ""
    pStatus = 0
    pType = 0
    pSexReq = 0

    response = requests.get(
        pageName)
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())
    userInfoDIV = soup.find('div', class_="infoOne clearfix")
    avatarRightDIV = userInfoDIV.find('div', class_="avatarRight")

    for o in soup.find('div', class_="detailInfo clearfix").find(
            'ul', class_="attr").find_all('li'):
        dataText = o.text
        if '型態' in dataText:
            if '公寓' in dataText:
                pType = 1
            elif '電梯大樓' in dataText:
                pType = 2
            elif '透天厝' in dataText:
                pType = 3
            elif '別墅' in dataText:
                pType = 4
            else:
                pType = 0
        elif '現況' in dataText:
            if '整層住家' in dataText:
                pStatus = 1
            elif '獨立套房' in dataText:
                pStatus = 2
            elif '分租套房' in dataText:
                pStatus = 3
            elif '雅房' in dataText:
                pStatus = 4
            elif '車位' in dataText:
                pStatus = 5
            else:
                pStatus = 0
    data = avatarRightDIV.findChildren()[0].text

    if '屋主聲明：仲介勿擾' in data:
        sType = 1
        sName = data.replace('（屋主聲明：仲介勿擾）', '')
    else:
        sType = 2
        sName = data.replace('（代理人）', '')
    sPhone = soup.find('span', class_="dialPhoneNum").attrs['data-value']

    allData = soup.find(
        'ul', class_="clearfix labelList labelList-1").find_all('li', class_="clearfix")
    for o in allData:
        textData = o.text
        if '性別要求' in textData:
            if '男女生皆可' in textData:
                pSexReq = 1
                break
            elif '女生' in textData:
                pSexReq = 2
            elif '男生' in textData:
                pSexReq = 3
            else:
                pSexReq = 0
    requests.post('http://192.168.0.4:8080/api/product/insert',
                  data=dict(
                      sName=sName,
                      sType=sType,
                      sPhone=sPhone,
                      pStatus=pStatus,
                      pType=pType,
                      pSexReq=pSexReq,
                      pageName=pageName, region=region
                  )
                  )


r = requests.get("http://192.168.0.4:8080/api/region/get")


data = json.loads(r.json())

for o in data['data']:
    # print(o)
    region = o['webId']
    browser.get(f"https://rent.591.com.tw/?kind=0&region={region}")
    try:
        area = browser.find_element_by_id("area-box-close")
        if area != None:
            area.click()
    except:
        pass
    # NOTE: FOR DEBUG
    i = 0

    while doJob:
        # content
        soup = BeautifulSoup(browser.page_source, "html.parser")
        elements = soup.find_all('ul', class_="listInfo clearfix j-house")
        for ele in elements:
            a = ele.find('li', class_="infoContent").find('a').attrs['href']
            pageName = f'https:{a}'
            pageName = pageName.replace(' ', '')
            onePageDataSave(pageName, region)

        # NOTE: FOR DEBUG
        i += 1
        if i == 4:
            break

        pageNext = browser.find_element_by_class_name("pageNext")
        if pageNext != None:
            try:
                pageNext.click()
            except:
                pass
        else:
            break
        sleepTime = random.randint(0, 10)
        time.sleep(sleepTime)
    pageSleepTime = random.randint(0, 10)
    time.sleep(pageSleepTime)
browser.close()
