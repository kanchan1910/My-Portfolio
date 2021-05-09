from django.shortcuts import render

# Create your views here.

def home(request):
	context = {'home':'active'}
	return render(request, 'core/home.html', context)

def education(request):
	context = {'edu':'active'}
	return render(request, 'core/education.html', context)


def skills(request):
	context = {'skill':'active'}
	return render(request, 'core/skill.html', context)

def programming(request):
	context = {'pro':'active'}
	return render(request, 'core/programming.html', context)

def projects(request):
	context = {'projects':'active'}
	return render(request, 'core/projects.html', context)

def experience(request):
	context = {'ex':'active'}
	return render(request, 'core/experience.html', context)

def resume(request):
	context = {'resume':'active'}
	return render(request, 'core/resume.html', context)

def github(request):
	context = {'github':'active'}
	return render(request, 'core/github.html', context)


def certi(request):
	context = {'certi':'active'}
	return render(request, 'core/accomplishments.html', context)


def contact(request):
	context = {'contact':'active'}
	return render(request, 'core/contact.html', context)
