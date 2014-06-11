from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
import hashlib

from bs4 import BeautifulSoup
import time

from ssrobot import context_processers

token = 'token'
     
def validate(request):
    signature = request.REQUEST.get('signature', '')
    timestamp = request.REQUEST.get('timestamp', '')
    nonce = request.REQUEST.get('nonce',  '')

    tmp_str = hashlib.sha1(''.join(sorted([token, timestamp, nonce]))).hexdigest()
    if tmp_str == signature:
        return True

    return False
     
def get(request):
    if validate(request):
        return HttpResponse(request.REQUEST.get('echostr', ''))

    raise PermissionDenied

@csrf_exempt
def post(request):
#    print request
    msg_get = BeautifulSoup(request.body, features='xml')
    
    if msg_get.MsgType.text != 'text':
        return ''

    msg_reply = context_processers.midware(msg_get)
#    print msg_reply

#    if msg_get.MsgType:
#        context = {
#                'to_user': msg_get.FromUserName.text,
#                'from_user': msg_get.ToUserName.text,
#                'create_time': int(time.time()),
#                'msg_type': 'text',
#                'content': msg_reply,
#            }
#        print context
    render = render_to_string('text.xml', msg_reply)
    print render
    return HttpResponse(render)

    return ''