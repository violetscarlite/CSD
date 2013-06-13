from csd_app import models

def createIncrementorSetup(formData, number, groups, teamDataSetup):
	commonVars = getCommonSetupVars(formData, number, groups, teamDataSetup)
	startValue = formData['{}-startValue'.format(number)]
	incAmount = formData['{}-incAmount'.format(number)]
	setup = models.IncrementorSetup(startValue = startValue, incAmount = incAmount)
	setup.parseCommonVars(commonVars)
	return setup

def createCheckboxSetup(formData, number, groups, teamDataSetup):
	commonVars = getCommonSetupVars(formData, number, groups, teamDataSetup)
	options = formData['{}-longName'.format(number)]
	setup = models.CheckboxSetup(options = options)
	setup.parseCommonVars(commonVars)
	return setup

def createRadioSetup(formData, number, groups, teamDataSetup):
	commonVars = getCommonSetupVars(formData, number, groups, teamDataSetup)
	options = formData['{}-longName'.format(number)]
	setup = models.RadioSetup(options = options)
	setup.parseCommonVars(commonVars)
	return setup

def createIntegerSetup(formData, number, groups, teamDataSetup):
	commonVars = getCommonSetupVars(formData, number, groups, teamDataSetup)
	setup = models.IntegerSetup()
	setup.parseCommonVars(commonVars)
	return setup

def createNumberSetup(formData, number, groups, teamDataSetup):
	commonVars = getCommonSetupVars(formData, number, groups, teamDataSetup)
	setup = models.NumberSetup()
	setup.parseCommonVars(commonVars)
	return setup

def getCommonSetupVars(formData, number, groups, teamDataSetup):
	longName = formData['{}-longName'.format(number)]
	shortName = formData['{}-shortName'.format(number)]
	typeOfData = formData['{}-type'.format(number)]
	#desc = formData['{}-desc'.format(number)]
	groupName = formData['{}-group'.format(number)]
	if groupName in groups:
		group = groups[groupName]
	else:
		group = models.DataGroup(name = groupName, teamDataSetup = teamDataSetup)
		group.save()
		groups[groupName] = group

	return {'longName': longName, 'shortName': shortName, 'typeOfData': typeOfData, 'group': group}