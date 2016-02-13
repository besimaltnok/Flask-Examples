#!/usr/bin/env python
# -*- coding: urf-8 -*-

from flask import Flask
from flask import request
	
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'pcap'])

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
			ext = file.filename.rsplit('.', 1)[1]
			content = file.read()
			new  = open('/root/flask/'+file.filename, "a")
			new.write(content)
			new.close()
			return "File upload successful"
		else:
			return "Ivaild File Extension, please check file ext"
			
	return '''
	<!doctype html>
	<title>File Upload Page</title>
	<h1>Please select the correct file extensions</h1>
	<form action="" method=post enctype=multipart/form-data>
	  <p><input type=file name=file>
		 <input type=submit value=Upload>
	</form>
	'''
    
if __name__ == '__main__':
	app.run(debug=True, port=1337)
