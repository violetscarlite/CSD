from django.db import models
from common_models import DateAware
from django.contrib.auth.models import User
#from lists import dataTypes#, dataSetups, dataClasses

#Note: what fields can be null

class Team(DateAware):
	name = models.CharField(max_length=200)
	number = models.IntegerField(primary_key=True)
	rookieYear = models.IntegerField(null=True)
	admin = models.ForeignKey(User, null=True)

	def __unicode__(self):
		return "Team #{}: {}".format(self.number, self.name)

# Create your models here.
class UserProfile(models.Model):
	team = models.ForeignKey(Team)
	teamRole = models.CharField(max_length=200, null=True)
	dateJoined = models.DateTimeField(null=True)
	user = models.OneToOneField(User)

	def __unicode__(self):
		return self.user.username

class GeneralTeamData(DateAware):
	commentor = models.ForeignKey(Team, related_name="commenterGeneralTeamData")
	about = models.ForeignKey(Team, related_name="aboutGeneralTeamData")
	comments = models.TextField()

	def __unicode__(self):
		return 'Data about {} by {}'.format(self.about.name, self.commentor.name) 

class Competition(DateAware):
	gameName = models.CharField(max_length = 200)
	year = models.IntegerField()

class Regional(DateAware):
	competition = models.ForeignKey(Competition)
	#place
	startDate = models.DateField()
	endDate = models.DateField()

class Robot(DateAware):
	team = models.ForeignKey(Team)
	competition = models.ForeignKey(Competition)
	name = models.CharField(max_length=200)
	regionals = models.ManyToManyField(Regional,null=True)
	#description = models.TextField()   #who defines this? there won't always be someone on the team to do this

class TeamDataSetup(DateAware):
	creator = models.ForeignKey(Team)
	competition = models.ForeignKey(Competition)
	#permissions

class Match(DateAware):
	dataSetup = models.ForeignKey(TeamDataSetup)
	regional = models.ForeignKey(Regional)
	matchType = models.IntegerField(null=True) #0 = practice, 1 = qualifier, 2 = elimination

class Alliance(DateAware):
	match = models.ForeignKey(Match)
	color = models.IntegerField() #0 = red, 1 = blue
	robots = models.ManyToManyField(Robot, null=True)
	winner = models.BooleanField()
	score = models.IntegerField(null=True)
	penalties = models.IntegerField(null=True)

class MatchRobot(DateAware):
	robot = models.ForeignKey(Robot)
	match = models.ForeignKey(Match)

class DataGroup(DateAware):
	name = models.CharField(max_length=200)
	description = models.TextField(null=True)
	teamDataSetup = models.ForeignKey(TeamDataSetup)


################################################
#Data Setup classes
class DataSetup(DateAware):
	dataGroup = models.ForeignKey(DataGroup)
	typeOfData = models.CharField(max_length=20)
	longName = models.CharField(max_length=200)
	shortName = models.CharField(max_length = 30)
	desc = models.TextField(null=True)

	def parseCommonVars(self, commonVars):
		self.dataGroup = commonVars['group']
		self.typeOfData = commonVars['typeOfData']
		if 'desc' in commonVars:
			self.desc = commonVars['desc']
		self.longName = commonVars['longName']
		if 'shortName' in commonVars:
			self.shortName = commonVars['shortName']
		else:
			pass

class IncrementorSetup(DataSetup):
	startValue = models.IntegerField()
	incAmount = models.IntegerField()

	def getHTML(self, enteringData = False, value = 0):
		htmlString = ""
		SN = self.shortName
		LN = self.longName
		inc = self.incAmount
		start = self.startAmount

		if enteringData:
			start = value

		htmlString += """%s: <input type="text" disabled='true' class="incInp %s" value="%d">
<button type="button" class="incButton" incName="%s" incAmount="%d">increment</button>
<button type="button" class="decButton" incName="%s" incAmount="%d">decrement</button>""" % (LN, SN, start, SN, inc, SN, inc)

		return htmlString



class CheckBoxSetup(DataSetup):
	options = models.TextField() #expected to be ':' delineated for options, each option has a long name and then a short name, delineated by ","
	optionsList = []

	def parseOptions(self):
		if not self.optionsList:
			tempList = self.options.split(":")
			for option in tempList:
				option.strip()

				optionLN = optionParts[0].strip() #Long Name
				optionSN = optionParts[1].strip() #Short Name
				optionsList.append([optionLN, optionSN])

		return self.optionsList

	def getHTML(self, enteringData = False, selected = ""):
		htmlString = ""
		optionsList = self.optionsList
		for option in optionsList:
			htmlString += "<input type='checkbox' name='%s' value='%s'>%S" % (self.shortName, option[1], option[0])

		return htmlString



class RadioSetup(DataSetup):
	options = models.TextField() #expected to be ':' delineated for options, each option has a long name and then a short name, delineated by ","
	optionsList = []

	def parseOptions(self):
		if not self.optionsList:
			tempList = self.options.split(':')

			for option in tempList:
				option.strip()
				optionParts = option.split(',')

				if len(optionsParts) < 2:
					#something is wrong, skip
					continue

				optionLN = optionParts[0].strip() #Long Name
				optionSN = optionParts[1].strip() #Short Name
				optionsList.append([optionLN, optionSN])

		return self.optionsList

	def getHTML(self, enteringData = False, selected = ""):
		htmlString = ""
		optionsList = self.optionsList
		for option in optionsList:
			htmlString += "<input type='radio' name='%s' value='%s'>%S" % (self.shortName, option[1], option[0])

		return htmlString


#Only Integers
class IntegerSetup(DataSetup):

	def getHTML(self, enteringData = False, value = 0):
		if enteringData:
			return """%s: <input type='text' name='%s' value='%d'>""" % (self.datasetup.longName, self.datasetup.shortName, value)
		else:
			return """%s: <input type='text' name='%s'>""" % (self.datasetup.longName, self.datasetup.shortName)



#Any type of number
class NumberSetup(DataSetup):

	def getHTML(self, enteringData = False, value = 0):
		if enteringData:
			return """%s: <input type='text' name='%s' value='%s'>""" % (self.datasetup.longName, self.datasetup.shortName, value)

		else:
			return """%s: <input type='text' name='%s'>""" % (self.datasetup.longName, self.datasetup.shortName)


###############################################
#The Data
class DataModel(models.Model):
	typeOfData = models.CharField(max_length=20)
	matchRobot = models.ForeignKey(MatchRobot)

class IncrementorData(DataModel):
	data = models.IntegerField()
	setup = models.ForeignKey(IncrementorSetup)

	def getEditingHTML(self):
		self.setup.getHTML(True, self.data)

class CheckBoxData(DataModel):
	data = models.TextField()
	setup = models.ForeignKey(CheckBoxSetup)

	def getEditingHTML(self):
		self.setup.getHTML(True, self.data)

class RadioData(DataModel):
	data = models.TextField()
	setup = models.ForeignKey(RadioSetup)

	def getEditingHTML(self):
		self.setup.getHTML(True, self.data)

class IntegerData(DataModel):
	data = models.IntegerField()
	setup = models.ForeignKey(IntegerSetup)

	def getEditingHTML(self):
		self.setup.getHTML(True, self.data)

class NumberData(DataModel):
	data = models.DecimalField(max_digits = 8, decimal_places=2)
	setup = models.ForeignKey(NumberSetup)

	def getEditingHTML(self):
		self.setup.getHTML(True, self.data)
