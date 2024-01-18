import random
import string
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

shortend_urls = {}