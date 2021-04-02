#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: __init__.py
# Project: region
# Created Date: Friday, April 2nd 2021, 12:02:43 pm
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
from ....tools import *
from app.tools import APIReturn


class GetRegion(Resource):
    "爬蟲取得區域用"
    @swagger.operation(
        notes="爬蟲取得區域用",
        nickname="GetRegion",
        # Parameters can be automatically extracted from URLs.
        #   For Example: <string:id>
        # but you could also override them here, or add other parameters.
        parameters=[
        ], responseMessages=[
            {
                "code": 200,
                "status": "boolean",
                "message": ""
            },
        ]
    )
    def get(self):
        from ....models import Region
        regions: list[Region] = Region.query.all()
        return APIReturn(data=[o.to_dict() for o in regions])
