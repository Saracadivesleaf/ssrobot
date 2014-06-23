from django.shortcuts import render


from pkg.models import Package
# Create your views here.
def get_pkg(key_word):
	pkg_get = Package.objects.get(key_word = key_word, status = True)

	if pkg_get:
		return pkg_get.name
	else:
		return ''