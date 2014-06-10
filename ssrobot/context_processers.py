from msg_board.views import add_to_board


def midware(msg_get):
	is_write = add_to_board(msg_get)
	if is_write:
		msg_reply = 'OK'
		return msg_reply
