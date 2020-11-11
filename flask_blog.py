from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)

posts = [
	{
		'title': 'Blog 1',
		'author': 'Sanjeev',
		'content': 'this is the content of the blog 11111111',
		'date_posted': 'Apr 20, 2018'
	},
	{
		'title': 'Blog 2',
		'author': 'Reddy',
		'content': 'This is the content of blog 22222 by Reddy',
		'date_posted': 'Mar 30, 2020'
	}
]

@app.route('/')
@app.route('/index')
def home():
	return render_template('index.html', posts=posts)

@app.route('/about')
def about():
	return render_template('about.html')



if __name__ == '__main__':
	app.run(debug=True)