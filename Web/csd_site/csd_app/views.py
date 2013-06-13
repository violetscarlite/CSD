from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.models import User
import datetime
from django.core.exceptions import ObjectDoesNotExist
from custom_helper import commonResponse, getUserProfile
from csd_app import models
from csd_app.lists import dataTypes, dataSetups

def home(request):
	return commonResponse(request, 'home.html')

@login_required(login_url='/login/') 
def manageSetups(request, createdSetup = False):
	return commonResponse(request, 'manageSetups.html')

@login_required(login_url='/login/') 
def createSetup(request):
	if request.method == 'POST':
		data = request.POST
		user = request.user
		team = getUserProfile(user).team
		competition = models.Competition.objects.get(pk=int(data['competition']))
		teamDataSetup = models.TeamDataSetup(creator = team, competition = competition)
		teamDataSetup.save()
		createdSetups = []
		dataSetupNumbers = data['dataSetups'].split(',')
		groups = {}
		for number in dataSetupNumbers:
			typeOfData = data['{}-type'.format(number)]
			createdSetups.append( (dataSetups[typeOfData])['create'](data, number, groups, teamDataSetup) )

		for dataSetup in createdSetups:
			dataSetup.save()

		return HttpResponseRedirect(reverse(manageSetups))
	else:
		competitions = models.Competition.objects.order_by('dateCreated')
		return commonResponse(request, 'createSetup.html', {"dataTypes": dataTypes, 'competitions': competitions})

def authLogin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse(loginSuccess))
			else: #no longer active
				return HttpResponseRedirect(reverse(home))
		else: #failed login
			return HttpResponseRedirect(reverse(home))
	else:
		return commonResponse(request, 'login.html')
	
def ajaxAuthLogin(requset):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponse('login success');
		else: #no longer active
			return HttpResponseForbidden() # catch invalid ajax and all non ajax
	else: #failed login
		return HttpResponseForbidden() # catch invalid ajax and all non ajax

@login_required(login_url='/login/')        
def loginSuccess(request):
	return commonResponse(request, 'loginSuccess.html')

def loginFail(request):
	return commonResponse(request, 'loginFail.html')

@login_required(login_url='/login/') 		
def logoutUser(request):
	#django logout method
	logout(request)
	return HttpResponseRedirect(reverse(home))