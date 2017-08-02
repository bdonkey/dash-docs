# -*- coding: utf-8 -*-
import dash
from dash import Dash
import dash_html_components as html
import dash_core_components as dcc
from flask import Flask, request
import json
import plotly.graph_objs as go
import os

server = Flask(__name__)
server.secret_key = os.environ.get('secret_key', 'secret')
# app = Dash(__name__, server=server, url_base_pathname='/dash/', csrf_protect=False)
app = Dash(__name__, server=server,  csrf_protect=False)

app.config.supress_callback_exceptions = True
