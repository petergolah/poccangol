#!/usr/bin/python

import base64
import requests
from os import path
from pprint import pprint as pp


downloaddir = 'downloads'

encoded = {
	'': '',
}

decoded = dict()

for word, encodedref in encoded.items():
	if not word:
		continue
	_path = base64.b64decode(bytes(encodedref.replace("-","+").replace("_","/"), 'utf-8')).decode(encoding='utf-8')
	_file = _path.split('/')[-1]
	_url = 'https://audio00.forvo.com/audios/mp3/{}'.format(_path)
	decoded[word] = _file
	response = requests.get(_url)
	open(path.join(downloaddir, _file) , 'wb').write(response.content)

pp(decoded)
