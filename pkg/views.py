from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist


from pkg.models import Package
# Create your views here.
def get_pkg(key_word):
	try:
		pkg_get = Package.objects.get(key_word = key_word, status = True)
	except ObjectDoesNotExist:
		return ''