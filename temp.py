from flask import Flask, render_template

app=Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    render_template('temp.html')

if(__name__=='__main__'):
    app.run(host='0.0.0.0', port=5000, debug=True)
