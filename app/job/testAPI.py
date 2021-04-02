#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: testAPI.py
# Project: job
# Created Date: Friday, April 2nd 2021, 2:20:54 pm
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


r = requests.post('http://192.168.0.4:8080/api/product/get', data={
    "region": [1, 2, 3, 4, 5, 14]
})
print(r.text)
