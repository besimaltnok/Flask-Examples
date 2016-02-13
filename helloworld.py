from flask import Flask
app = Flask(__name__)

@app.route('/besim')
def page():
	return "<center><h2>http://www.besimaltinok.com</h2></center>"

if __name__ == "__main__":
	app.run(debug=True, port=1337)
	


