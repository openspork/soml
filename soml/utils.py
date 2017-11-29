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
from werkzeug.datastructures import FileStorage

def thumbify(in_image):
	in_image.seek(0)
	image = Image.open(in_image)
	size = 128, 128
	image.thumbnail(size)
	out_image = StringIO()
	image.save(out_image, 'JPEG', quality=70)
	out_image.seek(0)
	werkzeug_data = FileStorage(out_image)
	return werkzeug_data
