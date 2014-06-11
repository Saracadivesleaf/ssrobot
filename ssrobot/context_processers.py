#-*- coding:utf-8 -*-

from msg_board.views import add_to_board
import time


def midware(msg_get):
	msg_reply = msg_filter(msg_get)

	return msg_reply


def msg_filter(msg_get):
	msg_text = msg_get.Content.text
	msg_splited = msg_text.split(' ', 1)
	print msg_splited
	msg_key = msg_splited[0]
	msg_body = msg_splited[1]

	if msg_key == u'留言':
		is_write = add_to_board(msg_body)
		
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