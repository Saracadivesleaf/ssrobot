def get_msg_body(msg_get):

	if msg_get.MsgType.text == 'text':
		msg_text = msg_get.Content.text
		msg_splited = msg_text.split(' ', 1)

		try:
			msg_body = msg_splited[1]
		except IndexError:
			msg_body = ''

		return msg_body


def render_msg_content(msg_type, content):
	if msg_type == 'text':
		msg_content = {
			'msg_type': msg_type,
			'content': content,
		}
	return msg_content
