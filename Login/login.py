
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/login', methods=['POST','GET'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] == 'besim' and request.form['password'] == 'admin':
			return "<br><center>Success Login</center>"
		else:
			return "<br><center><b>WARNING</b></center>"
	return render_template('login.html')

if __name__ == "__main__":
	app.run(debug=True, port=1337)
	
