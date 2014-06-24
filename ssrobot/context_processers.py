#-*- coding:utf-8 -*-
import time

from pkg.views import get_pkg


def midware(msg_get):
	msg_reply = msg_filter(msg_get)

	return msg_reply


def msg_filter(msg_get):
	msg_text = msg_get.Content.text
	msg_splited = msg_text.split(' ', 1)
	msg_key = msg_splited[0]

	pkg_name = get_pkg(msg_key)

	if pkg_name:
		try:
			pkg_object = __import__(pkg_name)
			msg_content = pkg_object.views.run(msg_get)
		except AttributeError:
			msg_content = {
				'msg_type': 'text',
				'content': 'AttributeError',
			}
	else:
		msg_content = {
			'msg_type': 'text',
			'content': 'No Module!',
		}

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