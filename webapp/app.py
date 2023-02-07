from __future__ import unicode_literals
from flask import Flask, render_template, request, Response, session, redirect, url_for

import requests
import json



app = Flask(__name__)

@app.route("/")
def scrape():
    params = {
        'spider_name' : 'Thespider',
        'start_requests' : True,
    }
    response = requests.get('http://localhost:9080/crawl.json', params)
    data = json.loads(response.text)
    df=pd.DataFrame(data=data['items'], columns=['Product_Name','Stock_Status'])
    return render_template('simple.html',  tables=[df.to_html(classes='data',  index=False)], titles=df.columns.values)
    # return render_template('index.html')