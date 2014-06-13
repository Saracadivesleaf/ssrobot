#-*- coding:utf-8 -*-

from msg_board.views import add_to_board
from weather.views import weather_query
from checkin.views import checkin_write
import time


def midware(msg_get):
	msg_reply = msg_filter(msg_get)

	return msg_reply


def msg_filter(msg_get):
	msg_text = msg_get.Content.text
	msg_splited = msg_text.split(' ', 1)
	msg_key = msg_splited[0]
	try:
		msg_body = msg_splited[1]
	except IndexError:
		msg_body = ''

	
	if msg_key == u'留言':
		from_user = msg_get.FromUserName.text
		is_write = add_to_board(from_user, msg_body)
		
		if is_write == True:
			msg_content = {
				'msg_type': 'text',
				'content': 'OK',
			}
		else:
			msg_content = {
				'msg_type': 'text',
				'content': 'Error!',
			}

	elif msg_key == u'天气':
		if msg_body:
			pass
		else:
			msg_body = u'保定'
		msg_content = weather_query(msg_body)

	elif msg_key == u'签到':
		msg_content = checkin_write(msg_get)
	
	return msg_response(msg_get, msg_content)


def msg_response(msg_get, msg_content):
	to_user = msg_get.FromUserName.text
	from_user = msg_get.ToUserName.text
	create_time = int(time.time())
	msg_head = {
		'to_user': to_user,
		'from_user': from_user,
		'create_time': create_time,
	}

	msg_content.update(msg_head)

	return msg_content