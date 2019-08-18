from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')

'''
@app.route('/', methods=['POST'])
def getvalue():
	message = request.form['message']
	print(message)
	return render_template('pass.html', m=message)
'''

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

    
