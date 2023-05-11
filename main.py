#!/usr/bin/env python
# coding: utf-8
# 版权所有 (c) 华为技术有限公司 2012-2022
""" 模型自动化流程中的数据采集

"""

import numpy as np
import uvicorn
from fastapi import FastAPI

from DataCollection.api import api_router
from DataCollection.data_collection import data_collection

app = FastAPI()

app.include_router(api_router)

np.random.seed(42)

if __name__ == '__main__':
    data_collection()
    uvicorn.run("main:app", host='0.0.0.0', port=8080)
