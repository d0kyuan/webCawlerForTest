#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: product.py
# Project: models
# Created Date: Thursday, April 1st 2021, 2:01:50 pm
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
import datetime
db = current_app.config['db']
BaseModel = current_app.config['BaseModel']


class Product(BaseModel):
    __tablename__ = 'tb_product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    region = db.Column(db.Integer)
    sName = db.Column(db.String(20))
    sType = db.Column(db.Integer)
    sPhone = db.Column(db.String(40))
    pType = db.Column(db.Integer)
    pStatus = db.Column(db.Integer)
    pSexReq = db.Column(db.Integer)
    pageName = db.Column(db.String(50))
    updatedAt = db.Column(db.DateTime(timezone=True))
    deletedAt = db.Column(db.DateTime(timezone=True))
    createdAt = db.Column(db.DateTime(timezone=True),
                          default=datetime.datetime.now())
    _default_fields = [
        "id",
        "sName",
        "sType",
        "sPhone",
        "pType",
        "pStatus",
        "pSexReq",
        "pageName",
        "region"
    ]

    def __init__(self, sName, sType,
                 sPhone, pType, pStatus, pSexReq, pageName, region):
        self.sName = sName
        self.sType = sType
        self.sPhone = sPhone
        self.pType = pType
        self.pStatus = pStatus
        self.pSexReq = pSexReq
        self.pageName = pageName
        self.region = region

    def delete(self):
        self.deletedAt = datetime.datetime.now()
        db.session.commit()

    def update(self):
        self.updatedAt = datetime.datetime.now()
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()
