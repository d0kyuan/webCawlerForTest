#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: region.py
# Project: models
# Created Date: Thursday, April 1st 2021, 11:16:15 am
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
from flask import current_app
db = current_app.config['db']
BaseModel = current_app.config['BaseModel']


class Region(BaseModel):
    __tablename__ = 'tb_region'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    webId = db.Column(db.Integer, unique=True)
    _default_fields = [
        "id",
        "webId",
        "name",
    ]

    def __init__(self, name, webId):
        self.name = name
        self.webId = webId

    def delete(self):
      #  self.deletedAt = datetime.datetime.now()
        db.session.commit()

    def update(self):
     #   self.updatedAt = datetime.datetime.now()
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()
