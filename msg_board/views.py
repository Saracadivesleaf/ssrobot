from django.shortcuts import render_to_response
from msg_board.models import board_content


# Create your views here.
def add_to_board(msg_text):
	msg_to_save = board_content(msg = msg_text)
	msg_to_save.save()
	print 'Save'
	return True

def show_msg_board(request):
	msg_to_show = board_content.objects.all()
	print msg_to_show
	return render_to_response('msg_board.html', {'msg_to_show': msg_to_show})
