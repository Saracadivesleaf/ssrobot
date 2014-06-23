from django.shortcuts import render_to_response
from utils.msg_tools import get_msg_body 
from utils.msg_tools import render_msg_content
from msg_board.models import messages


# Create your views here.

def run(msg_get):
	from_user = msg_get.FromUserName.text
	msg_body = get_msg_body(msg_get)

	if msg_body:
		try:
			is_written = add_to_board(from_user, msg_body)
		except:
			return render_msg_content('text', 'DataBase Error!')
			
		if is_written:
			return render_msg_content('text', 'OK')
		else:
			return render_msg_content('text', 'Error!')
	else:
		return render_msg_content('text', 'No input')

def add_to_board(from_user, msg_text):

	msg_to_save = messages(openId = from_user, msg = msg_text)
	msg_to_save.save()
	print 'Save'
	return True

def show_msg_board(request):
	msg_to_show = messages.objects.all()
	return render_to_response('msg_board.html', {'msg_to_show': msg_to_show})
