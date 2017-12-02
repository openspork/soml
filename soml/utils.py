from urlparse import urlparse, urljoin
from flask import request

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

def get_redirect_target():
	for target in request.values.get('next'), request.referrer:
	    if not target:
	        continue
	    if is_safe_url(target):
	        return target

#image processing
from PIL import Image
from StringIO import StringIO

def thumbify(in_image):
	in_image.seek(0)
	image = Image.open(in_image)
	size = 128, 128
	image.thumbnail(size)
	out_image = StringIO()
	image.save(out_image, image.format)
	out_image.seek(0)
	return out_image, image.format

#image downloading

import requests

def validate_image_url(url):
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    print header
    content_type = header.get('content-type')
    content_length = header.get('content-length')

    if 'image' not in content_type.lower():
        return False, 'Not an image!'

    if content_length and int(content_length) > 102400:
    	return False, 'Image too large!'

    return True, 'URL Valid'