try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse
import os
from flask import Flask, request, abort
import requests
from io import BytesIO
from wand.image import Image
from tempfile import NamedTemporaryFile
try:
	import commands
except ImportError:
	import subprocess as commands
import logging


url_tmpfile_dict = {}
app = Flask(__name__)
# handler = logging.FileHandler('flask.log')
# handler.setLevel(logging.INFO)
# app.logger.addHandler(handler)

@app.route("/")
def home():
	return "To use this API: [ip_address]/api/num_colors?src=https://www.wikipedia.org/portal/wikipedia.org/assets/img/Wikipedia-logo-v2@2x.png`."

@app.route("/api/num_colors")
def num_colors():
	global url_tmpfile_dict
	tmpfilepath = ""
	url = request.args.get('src')
	# if not cached
	if url not in url_tmpfile_dict:
		app.logger.info("cache: miss")
		r = requests.get(url, timeout=0.1)
		f, file_ext = os.path.splitext(os.path.basename(urlparse(url).path))
		if 'image' not in r.headers['content-type']:
			app.logger.error(url + " is not an image.")
			abort(400, url + " is not an image.")
		with Image(file=BytesIO(r.content)) as img:
			with  NamedTemporaryFile(mode='w+b',suffix=img.format, delete=False) as temp_file:
				img.save(file=temp_file)
				temp_file.seek(0,0)
				url_tmpfile_dict[url] = temp_file.name
				tmpfilepath = temp_file.name
	# if cached
	else: #
		app.logger.info("cache: hit at")
		tmpfilepath = url_tmpfile_dict[url]
	app.logger.info(tmpfilepath)
	command = "/usr/bin/identify -format %k " + tmpfilepath
	color_count = commands.getoutput(command)
	return color_count

if __name__ == "__main__":
	app.run() #if run locally ane exposed to public network
