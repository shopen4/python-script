import time
# import redis

from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
# redis.Redis(host='redis', port=6379)



@app.route('/', methods=['POST', 'GET'])
def sum():
	if request.method == 'POST':
		firstVal = request.form.get('firstVal')
		secondVal = request.form.get('secondVal')
		result = float(firstVal) + float(secondVal)
		return render_template('result.html', result=result)
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)
