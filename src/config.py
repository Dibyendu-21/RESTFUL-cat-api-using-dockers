# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 16:56:45 2020

@author: Sonu
"""

import os

user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
database = os.environ['POSTGRES_DB']
port = os.environ['POSTGRES_PORT']

DATABASE_CONNECTION_URI = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'