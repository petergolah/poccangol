#!/usr/bin/python

import base64
from pprint import pprint as pp


encoded = {
	'': '',
}

decoded = dict()

for word, encodedref in encoded.items():
	decoded[word] = 'https://audio00.forvo.com/audios/mp3/{}'.format(
		base64.b64decode(bytes(encodedref.replace("-","+").replace("_","/"), 'utf-8')).decode(encoding='utf-8')
	)

pp(decoded)
