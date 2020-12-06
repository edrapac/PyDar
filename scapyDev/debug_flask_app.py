from flask import Flask, Response, jsonify, render_template, request,    redirect, url_for

import time
from time import sleep

app = Flask(__name__)
@app.route('/')
def index():
    if request.headers.get('accept') == 'text/event-stream':
        def script():
            #a lot of code goes here
            yield "data: Part A completed.\n\n"

            #more code
            sleep(1)
            yield "data: Part B completed.\n\n"

            #more code
            sleep(1)
            yield "data: Part C completed.\n\n"

        return Response(script(), content_type='text/event-stream')
    return redirect(url_for('static', filename='debug_index.html'))

if __name__ == '__main__':
    app.run()