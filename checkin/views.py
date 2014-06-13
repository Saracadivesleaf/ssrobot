#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
import datetime

from checkin.models import checkin
# Create your views here.
def checkin_write(msg_get):
	openId = msg_get.FromUserName.text
	if is_checked(openId):
		checkin_user = checkin(openId = openId)
		checkin_user.save()
		msg_content = {
			'msg_type': 'text',
			'content': u'签到成功！',
		}
		return msg_content

	else:
		msg_content = {
			'msg_type': 'text',
			'content': u'你已经签到过了！',
		}
		return msg_content

def show_checkin(request):
	checkin_list = checkin.objects.all()
	return render_to_response('checkin.html', {'checkin_to_show': checkin_list})


def is_checked(openId):
	today_obj = datetime.date.today()
	today = today_obj.strftime('%Y-%m-%d')
	checkin_record = checkin.objects.filter(openId=openId, checkin_date=today)

	if checkin_record:
		return False
	else:
		return True