#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: __init__.py
# Project: product
# Created Date: Thursday, April 1st 2021, 2:08:33 pm
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

from flask_restful import Resource
from flask import current_app
from flask_restful_swagger import swagger
from flask import request
from sqlalchemy import or_
from ....tools import *
from app.tools import APIReturn


class InsertProduct(Resource):
    "爬蟲新增租屋資訊用"
    @swagger.operation(
        notes="新增租屋用",
        nickname="insert post",
        parameters=[
            {
                "name": "region",
                "description": "區域(region webId)",
                "required": True,
                "allowMultiple": False,
                "dataType": "string",
                "paramType": "query",
            }, {
                "name": "pageName",
                "description": "資訊頁面URL",
                "required": True,
                "allowMultiple": False,
                "dataType": "string",
                "paramType": "query",
            },  {
                "name": "sName",
                "description": "出租者名稱",
                "required": True,
                "allowMultiple": False,
                "dataType": "string",
                "paramType": "query",
            }, {
                "name": "sType",
                "description": "出租者身分 1:自售 2:非自售 3:其他",
                "required": True,
                "allowMultiple": False,
                "dataType": "int",
                "paramType": "query",
            }, {
                "name": "sPhone",
                "description": "連絡電話",
                "required": True,
                "allowMultiple": False,
                "dataType": "string",
                "paramType": "query",
            }, {
                "name": "pType",
                "description": "型態 1:公寓 2:電梯大樓 3:透天厝 4:別墅 ",
                "required": True,
                "allowMultiple": False,
                "dataType": "int",
                "paramType": "query",
            }, {
                "name": "pStatus",
                "description": "現況 1:整層住家 2:獨立套房 3:分租套房 4:雅房 5:車位",
                "required": True,
                "allowMultiple": False,
                "dataType": "int",
                "paramType": "query",
            }, {
                "name": "pSexReq",
                "description": "性別要求",
                "required": True,
                "allowMultiple": False,
                "dataType": "int",
                "paramType": "query",
            },
        ]
    )
    def post(self):
        try:
            # print(request.form.get(''))
            region = request.form.get('region')
            if region == None or region == '':
                return APIReturn(status=False, message="need region")

            pageName = request.form.get('pageName')
            if pageName == None or pageName == '':
                return APIReturn(status=False, message="need pageName")

            sName = request.form.get('sName')
            if sName == None or sName == '':
                return APIReturn(status=False, message="need sName")
            sType = request.form.get('sType')
            if sType == None or sType == '':
                return APIReturn(status=False, message="need sType")

            sPhone = request.form.get('sPhone')
            if sPhone == None or sPhone == '':
                return APIReturn(status=False, message="need sPhone")

            pStatus = request.form.get('pStatus')
            if pStatus == None or pStatus == '':
                return APIReturn(status=False, message="need pStatus")

            pType = request.form.get('pType')
            if pType == None or pType == '':
                return APIReturn(status=False, message="need pType")

            pSexReq = request.form.get('pSexReq')
            if pSexReq == None or pSexReq == '':
                return APIReturn(status=False, message="need pSexReq")

            from app.models import Product

            oldP: Product = Product.query.filter_by(pageName=pageName).first()
            if oldP != None:
                oldP.sName = sName
                oldP.sType = sType
                oldP.sPhone = sPhone
                oldP.pType = pType
                oldP.pStatus = pStatus
                oldP.pSexReq = pSexReq
                oldP.region = region
                oldP.update()
            else:
                p = Product(
                    sName=sName,
                    sType=sType,
                    sPhone=sPhone,
                    pType=pType,
                    pStatus=pStatus,
                    pSexReq=pSexReq, pageName=pageName, region=region
                )
                p.save()
            return APIReturn(status=True)
        except Exception as e:
            print(e)
            return APIReturn(status=False)


class GetProduct(Resource):
    "查詢租屋資訊用"
    @swagger.operation(
        notes="查詢租屋用",
        nickname="get post",
        parameters=[
            {
                "name": "region",
                "description": "區域(region webId)",
                "required": False,
                "allowMultiple": True,
                "dataType": "array",
                "paramType": "query",
                "items": {
                 "type": "integer",
                },
            }, {
                "name": "sName",
                "description": "出租者名稱",
                "allowMultiple": False,
                "dataType": "string",
                "paramType": "query",
            }, {
                "name": "sSex",
                "description": "出租者性別 1:男性 2:女性",
                "allowMultiple": False,
                "dataType": "array",
                "paramType": "query",
                "items": {
                    "type": "integer",
                }
            },
            {
                "name": "sType",
                "description": "出租者身分 1:自售 2:非自售 3:其他",
                "allowMultiple": True,
                "dataType": "array",
                "paramType": "query",
                "items": {
                    "type": "integer",
                },
            },  {
                "name": "sPhone",
                "description": "連絡電話",
                "allowMultiple": True,
                "dataType": "string",
                "paramType": "query",
            }, {
                "name": "pType",
                "description": "型態 1:公寓 2:電梯大樓 3:透天厝 4:別墅 ",
                "allowMultiple": True,
                "dataType": "array",
                "paramType": "query",
                "items": {
                    "type": "integer",
                },
            }, {
                "name": "pStatus",
                "description": "現況 1:整層住家 2:獨立套房 3:分租套房 4:雅房 5:車位",
                "allowMultiple": True,
                "dataType": "array",
                "paramType": "query",
                "items": {
                    "type": "integer",
                },
            },
            {
                "name": "pSexReq",
                "description": "性別要求",
                "allowMultiple": False,
                "dataType": "int",
                "paramType": "query",
            },

        ]
    )
    def post(self):
        try:
            from app.models import Product, Region
            db = current_app.config['db']

            query = db.session.query(Product, Region).outerjoin(
                Region, Region.webId == Product.region)

            sSex = request.values.getlist('sSex')
            if sSex != None and type(sSex) is list and len(sSex) > 0:
                if sSex == 1:

                    query = query.filter(Product.sName == f"%先生")
                elif sSex == 2:
                    query = query.filter(
                        (Product.sName == f"%小姐") | (Product.sName == f"%太太"))
            region = request.values.getlist('region')
            if region != None and type(region) is list and len(region) > 0:
                print("123")
                query = query.filter(Product.region.in_(region))
            print(request.values)
            sName = request.values.get('sName')
            if sName != None and sName != '':
                print("sName")
                query = query.filter(Product.sName.like(f"%{sName}%"))

            sType = request.values.getlist('sType')
            if sType != None and type(sType) is list and len(sType) > 0:
                query = query.filter(Product.sType.in_(sType))

            sPhone = request.values.get('sPhone')
            if sPhone != None and sPhone != '':
                query = query.filter(Product.sPhone.like(f"%{sPhone}%"))

            pStatus = request.values.getlist('pStatus')
            if pStatus != None and type(pStatus) is list and len(pStatus) > 0:
                query = query.filter(Product.pStatus.in_(pStatus))

            pType = request.values.getlist('pType')
            if pType != None and type(pType) is list and len(pType) > 0:
                query = query.filter(Product.pType.in_(pType))

            pSexReq = request.values.get('pSexReq')
            if pSexReq != None and pSexReq != '':
                query = query.filter(Product.pSexReq == pSexReq)
            output = []
            for _p, _r in query.all():
                _p: Product
                _r: Region
                oldP = _p.to_dict()
                sTypeName = ""
                if _p.sType == 1:
                    sTypeName = "自售"
                elif _p.sType == 2:
                    sTypeName = "非自售"
                elif _p.sType == 3:
                    sTypeName = "其他"
                else:
                    sTypeName = "其他"

                pTypeName = ""
                if _p.pType == 1:
                    pTypeName = "公寓"
                elif _p.pType == 2:
                    pTypeName = "電梯大樓"
                elif _p.pType == 3:
                    pTypeName = "透天厝"
                elif _p.pType == 4:
                    pTypeName = "透天厝"
                else:
                    pTypeName = "其他"

                pStatusName = ""
                if _p.pStatus == 1:
                    pStatusName = "整層住家"
                elif _p.pStatus == 2:
                    pStatusName = "獨立套房"
                elif _p.pStatus == 3:
                    pStatusName = "分租套房"
                elif _p.pStatus == 4:
                    pStatusName = "雅房"
                elif _p.pStatus == 5:
                    pStatusName = "車位"
                else:
                    pStatusName = "其他"
                # region
                # sName
                # sType
                # sPhone
                # pType
                # pStatus
                # pSexReq
                output.append(
                    dict(
                        regionName=_r.name,
                        regionId=_r.webId,
                        sellerName=_p.sName,
                        sellerPhone=_p.sPhone,
                        sellerTypeName=sTypeName,
                        sellerTypeId=_p.sType,
                        productStatusName=pStatusName,
                        productStatusId=_p.pStatus,
                        productTypeName=pTypeName,
                        productTypeId=_p.pType,
                    )
                )
            return APIReturn(status=True, data=output)
        except Exception as e:
            return APIReturn(status=False, message=str(e))
