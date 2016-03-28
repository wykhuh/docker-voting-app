from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from utils import connect_to_redis
import os
import socket
import random
import json
import json
import urllib2
import xml.etree.ElementTree as ET

requestURL = "http://thecatapi.com/api/images/get?format=xml&results_per_page=2"

def get_images(url):
    root = ET.parse(urllib2.urlopen(requestURL)).getroot()
    images = root[0][0]
    cat_images = []

    for image in images:
        cat = {}
        cat['id'] =  image.find('id').text
        cat['url'] =  image.find('url').text
        cat_images.append(cat)
    return cat_images


# print root

# images = root[0][0]
#
# # print images.tag, images.attrib
#
# for child in images:
#     print child.tag, child.attrib
#
# response.close()  # best practice to close the file
#

print '========='

option_a = os.getenv('OPTION_A', "Python")
option_b = os.getenv('OPTION_B', "s")

hostname = socket.gethostname()

# redis = connect_to_redis("redis")
app = Flask(__name__)


@app.route("/", methods=['POST','GET'])
def hello():
    images = get_images(requestURL)
    voter_id = request.cookies.get('voter_id')

    if not voter_id:
        voter_id = hex(random.getrandbits(64))[2:-1]

    vote = None

    if request.method == 'POST':
        vote = request.form['vote']
        data = json.dumps({'voter_id': voter_id, 'vote': vote})
        # redis.rpush('votes', data)

    resp = make_response(render_template(
        'index.html',
        option_a=images[0],
        option_b=images[1],
        hostname=hostname,
        vote=vote,
    ))
    resp.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0';
    resp.set_cookie('voter_id', voter_id)
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
