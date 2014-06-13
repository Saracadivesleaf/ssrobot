from django.shortcuts import render_to_response
from msg_board.models import messages


# Create your views here.
def add_to_board(from_user, msg_text):

	msg_to_save = messages(openId = from_user, msg = msg_text)
	msg_to_save.save()
	print 'Save'
	return True

def show_msg_board(request):
	msg_to_show = messages.objects.all()
	return render_to_response('msg_board.html', {'msg_to_show': msg_to_show})
