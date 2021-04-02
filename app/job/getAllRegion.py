#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: getAllRegion.py
# Project: job
# Created Date: Thursday, April 1st 2021, 12:57:12 pm
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
import requests
from bs4 import BeautifulSoup
from ..models import Region
from flask import current_app


def getRegion():
    app = current_app.config['app']
    with app.app_context():
        response = requests.get(
            "https://rent.591.com.tw/?kind=0&region=1")
        soup = BeautifulSoup(response.text, "html.parser")
        optionBox = soup.find("p", class_="clearfix changRegion")
        for ele in optionBox:
            if ele.name == "a":
                r = Region(
                    name=ele.text,
                    webId=ele.attrs['data-text']
                )
                r.save()
