from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return "Flask hekoru app123."

if __name__=="__main__":
	app.run()