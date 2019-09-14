from flask import Flask, request, render_template, redirect
import nicovideo
import webbrowser
import time

app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/')
def logout():
    return render_template('view.html', data=nicovideo.search_nicovideo())

if __name__ == "__main__":
    app.run(debug=True, threaded=True, processes=1)