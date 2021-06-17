# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 22:21:11 2021

@author: melanija
"""

from flask import Flask

app = Flask(__name__, template_folder='app/templates')

from app import run
