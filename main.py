#!/usr/bin/python3

from flask import Flask, render_template, request
from datetime import datetime
import os
import yaml

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

vocabfilepath = 'vocab.yaml'
xxx = 3
oldvocabmodtime = 0
vocab = dict()
monthnames = {1: 'Január', 2: 'Február', 3: 'Március', 4: 'Április', 5: 'Május', 6: 'Június', 7: 'Július', 8: 'Augusztus', 9: 'Szeptember', 10: 'Október', 11: 'November', 12: 'December'}

@app.route("/")
def index():
	global oldvocabmodtime, vocab
	newvocabmodtime = os.path.getmtime(vocabfilepath)
	if oldvocabmodtime != newvocabmodtime:
		vocab = yaml.load(open(vocabfilepath))
		oldvocabmodtime = newvocabmodtime
	sortedkeys=tuple(sorted([key for key in vocab if key <= datetime.today().date()], reverse=True))
	return render_template('index.html', vocab=vocab, sortedkeys=sortedkeys, dateformatter=dateformatter)

@app.route('/<path:path>')
def static_file(path):
	return app.send_static_file(path)

def dateformatter(thedate):
	return '{} {}.'.format(monthnames[thedate.month], thedate.day)
