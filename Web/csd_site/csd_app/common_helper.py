from django.contrib.auth.models import User
from achievements.models import Achievement, UserProfile, Request
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from django.shortcuts import render_to_response
from django.template import RequestContext

"""
Creates a paginated version of the list that you inputed by using the Django paginator class. 
list - the list to create a paginated list from
numPerPage - the number of items to display on a page
request - the HTML request that received in a views.py class
"""
def createPaginator(list, numPerPage, request):
	paginator = Paginator(list, numPerPage)
	
	newList = []
	page = request.GET.get('page')
	try:
		newList = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		newList = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		newList = paginator.page(paginator.num_pages)
		
	return newList
	
def getUserProfile(user):
	try:
		profile = user.get_profile()
		return profile
	except ObjectDoesNotExist:
		#this will need to be customized in case other parameters are required
		profile = UserProfile(user=user) 
		profile.save()
		return profile

"""
This sets up the HTML response that all views.py methods should return because it includes many of the values needed for every page of the website. Some of these are the user, points totals, and number of pending achievements. If you do not use this method, many things will break on the website. This currently calculates the total user points and achievement points on every single call. If the website slows down, it can be changes to store point totals in a session and only recalculate the totals when necessary.
This method is used at the end of a views.py method to replace a render_to_response line. To use it, create a dictionary of any extra arguments, call this method, and return the results.
request - the HTML request received by a views.py method.
template - the location of the html template that will be rendered for this request. This has to be sent in because the rendering happens withing this method.
argsDict - any extra arguments to be used in rendering the html template
"""
def commonResponse(request, template, argsDict={}):
	user = request.user
	loggedIn = user.is_authenticated()
	
	#things to always add to a page
	argsDict["user"] = user
	argsDict["logged_in"] = loggedIn
	
	#things to add to a page when the person is logged in
	if loggedIn:
		

	#things to add to a page when the user is not logged in
	else:
		
	
	return render_to_response(template, argsDict, context_instance=RequestContext(request))


