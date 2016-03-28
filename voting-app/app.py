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
from random import randint

requestURL = "http://thecatapi.com/api/images/get?format=xml&results_per_page=50&size=med"

def get_images(url):
    root = ET.parse(urllib2.urlopen(requestURL)).getroot()
    images = root[0][0]
    cat_images = []

    for image in images:
        cat ={}
        cat['id'] =  image.find('id').text
        cat['url'] =  image.find('url').text
        cat_images.append(cat)
    return cat_images

def stored_images():
    # print get_images(requestURL)
    return [
        {'url': 'http://25.media.tumblr.com/tumblr_m72ekibnkX1r6i9kzo1_500.jpg', 'id': 'MTg0ODgxNQ'},
        {'url': 'http://24.media.tumblr.com/tumblr_m27d81MFrA1qze0hyo1_500.jpg', 'id': 'a9b'},
        {'url': 'http://25.media.tumblr.com/tumblr_mbfqag6mvZ1qhwmnpo1_500.jpg', 'id': 'MTYxMDU0MA'},
        {'url': 'http://24.media.tumblr.com/tumblr_mauz929mFV1qhwmnpo1_500.jpg', 'id': 'MTYyNTY0MA'},
        {'url': 'http://24.media.tumblr.com/tumblr_m9mbcwiWyU1qejbiro1_400.jpg', 'id': 'MjAzOTQ2MA'},
        {'url': 'http://24.media.tumblr.com/tumblr_lutojo6Vrn1qbhms5o1_400.jpg', 'id': '6fo'},
        {'url': 'http://25.media.tumblr.com/tumblr_m1hn70ZQQx1qze0hyo1_500.jpg', 'id': 'aci'},
        {'url': 'http://25.media.tumblr.com/tumblr_m4b6un29tV1qjc1a7o1_500.jpg', 'id': '8j7'},
        {'url': 'http://25.media.tumblr.com/tumblr_m3ful7TZRv1qbxi45o1_r1_500.gif', 'id': 'MTcxMTI2Ng'},
        {'url': 'http://25.media.tumblr.com/tumblr_m1xyxxF6wP1qgjltdo1_500.jpg', 'id': 'c4j'},
        {'url': 'http://24.media.tumblr.com/tumblr_m1agea0x8f1qze0hyo1_500.jpg', 'id': 'ad8'},
        {'url': 'http://27.media.tumblr.com/ZabOTt2mpnds1s79T10e7oz2o1_400.jpg', 'id': '157'},
        {'url': 'http://24.media.tumblr.com/tumblr_m374e1GKtv1qejbiro1_500.jpg', 'id': 'duo'},
        {'url': 'http://24.media.tumblr.com/tumblr_m1jooi3rBN1qzex9io1_500.jpg', 'id': '5uq'},
        {'url': 'http://29.media.tumblr.com/tumblr_lu1uds6BGT1qi23vmo1_500.jpg', 'id': '38c'},
        {'url': 'http://25.media.tumblr.com/tumblr_lt66xm2eVg1qzaxi1o1_500.jpg', 'id': '66t'},
        {'url': 'http://25.media.tumblr.com/tumblr_m3gerxIivE1qhdif9o1_500.gif', 'id': '8s8'},
        {'url': 'http://24.media.tumblr.com/tumblr_m48xbtbkTR1rtuomto1_500.jpg', 'id': '46n'},
        {'url': 'http://25.media.tumblr.com/tumblr_lkr7m9vnuL1qdvbl3o1_500.jpg', 'id': '7j8'},
        {'url': 'http://24.media.tumblr.com/tumblr_lhugnqpXVM1qfyzelo1_500.jpg', 'id': '24k'},
        {'url': 'http://28.media.tumblr.com/tumblr_m2pppwjMnW1qhwmnpo1_500.jpg', 'id': '305'},
        {'url': 'http://24.media.tumblr.com/tumblr_lsqu2saHnf1qbe5pxo1_500.jpg', 'id': '9eq'},
        {'url': 'http://26.media.tumblr.com/tumblr_lv0tadCXmC1r4xjo2o1_500.gif', 'id': '45'},
        {'url': 'http://24.media.tumblr.com/tumblr_m1mp54OQv91qzxrnuo1_500.jpg', 'id': '1d6'},
        {'url': 'http://25.media.tumblr.com/tumblr_kqahaqEKyE1qzv5pwo1_500.jpg', 'id': '1hm'},
        {'url': 'http://30.media.tumblr.com/tumblr_m2dgrhJmqO1qzjc9co1_500.jpg', 'id': 'tp'},
        {'url': 'http://24.media.tumblr.com/tumblr_m45yojxGDY1qzf8xpo1_500.jpg', 'id': '45j'},
        {'url': 'http://24.media.tumblr.com/rvvSvbiO5o00gthuVVXXXJbuo1_500.jpg', 'id': '2ab'},
        {'url': 'http://24.media.tumblr.com/Jjkybd3nSk17ovz0T3guT78go1_500.jpg', 'id': '2bd'},
        {'url': 'http://25.media.tumblr.com/tumblr_loh7yaKoCi1qbhms5o1_500.jpg', 'id': '6lk'},
        {'url': 'http://24.media.tumblr.com/tumblr_mbqh4kGBN71qhwmnpo1_500.jpg', 'id': 'MTYwNDQ1OQ'},
        {'url': 'http://24.media.tumblr.com/tumblr_lhc5d3gwZ01qgnva2o1_500.jpg', 'id': 'beg'},
        {'url': 'http://25.media.tumblr.com/tumblr_m2vjjeEUQ71qbe5pxo1_500.jpg', 'id': '99m'},
        {'url': 'http://25.media.tumblr.com/tumblr_m2ms9rO7rV1qbe5pxo1_500.jpg', 'id': '99q'},
        {'url': 'http://24.media.tumblr.com/tumblr_lg8yokP6wE1qfyzelo1_500.jpg', 'id': '6va'},
        {'url': 'http://26.media.tumblr.com/tumblr_lms248vgxo1qjmniro1_400.gif', 'id': '14e'},
        {'url': 'http://24.media.tumblr.com/tumblr_lmaq9ehjDv1qcj1yvo1_400.jpg', 'id': '544'},
        {'url': 'http://28.media.tumblr.com/tumblr_m1tn9cMHwf1rr6z2oo1_250.gif', 'id': '1u1'},
        {'url': 'http://25.media.tumblr.com/tumblr_m2zr0xKHB61qbe5pxo1_500.jpg', 'id': '99g'},
        {'url': 'http://25.media.tumblr.com/tumblr_lns5u2l9TC1qcn249o1_500.gif', 'id': '4bd'},
        {'url': 'http://24.media.tumblr.com/tumblr_ln5sa8Z0So1qbt33io1_500.jpg', 'id': '5rj'},
        {'url': 'http://24.media.tumblr.com/tumblr_m1u6hlV1sd1qze0hyo1_500.jpg', 'id': 'aaq'},
        {'url': 'http://25.media.tumblr.com/tumblr_lpsjouwBwQ1qzu51vo1_500.jpg', 'id': 'bm0'},
        {'url': 'http://25.media.tumblr.com/tumblr_l6an0muyI51qzbxjgo1_500.jpg', 'id': 'agl'},
        {'url': 'http://25.media.tumblr.com/tumblr_m84nn4rep31qze0hyo1_500.jpg', 'id': 'MTg5ODU1MQ'},
        {'url': 'http://25.media.tumblr.com/tumblr_ltk22frFvD1qdth8zo1_400.jpg', 'id': 'cg9'},
        {'url': 'http://24.media.tumblr.com/tumblr_lp251wwjgy1qjgt9to1_500.jpg', 'id': 'cic'}
    ]


def random_images(images):
    count = len(images)
    print count

    rand = randint(0, count)
    rand2 = randint(0, count)
    while(rand == rand2):
        rand2 = randint(0, count)
    return [images[rand], images[rand2]]


hostname = socket.gethostname()

redis = connect_to_redis("redis")
app = Flask(__name__)


@app.route("/", methods=['POST','GET'])
def hello():
    images = random_images(stored_images())
    voter_id = hex(random.getrandbits(64))[2:-1]
    vote = None

    if request.method == 'POST':
        vote = request.form['vote']
        data = json.dumps({'voter_id': voter_id, 'vote': vote})
        redis.rpush('votes', data)

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
    app.run(host='0.0.0.0', port=80)
