#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: config.py
# Project: src
# Created Date: Thursday, April 1st 2021, 10:51:08 am
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


class SQLConfig:
    SQLALCHEMY_DATABASE_URI = url = 'postgresql+psycopg2://postgres:VqU2dzidIy@localhost:5432/demo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
