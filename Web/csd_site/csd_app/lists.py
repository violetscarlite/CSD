from csd_app.setupHelpers.creators import createIntegerSetup, createCheckboxSetup, createRadioSetup, createIntegerSetup, createNumberSetup

dataTypes = {
	'inc': {'longName': 'Incrementor', 'htmlFile': 'dataTypesHTML/inc.html'},
	'checkbox' : {'longName': 'Checkboxes', 'htmlFile': 'dataTypesHTML/checkbox.html'},
	'radio' : {'longName': 'Radio Buttons', 'htmlFile': 'dataTypesHTML/radio.html'},
	'int' : {'longName': 'Integer', 'htmlFile': 'dataTypesHTML/int.html'},
	'num' : {'longName': 'Number', 'htmlFile' : 'dataTypesHTML/num.html'}
}

dataSetups = {
	'inc' : {'className': 'IncrementorSetup', 'create' : createIntegerSetup},
	'checkbox' : {'className':'CheckboxSetup', 'create' : createCheckboxSetup},
	'radio' : {'className': 'RadioSetup', 'create': createRadioSetup},
	'int': {'className': 'IntegerSetup', 'create': createIntegerSetup},
	'num' : {'className': 'NumberSetup','create': createNumberSetup}
}

dataModels= {
	'inc' : {'className': 'IncrementorData', },
	'checkbox' : {'className':'CheckboxData', },
	'radio' : {'className': 'RadioData', },
	'int': {'className': 'IntegerData', },
	'num' : {'className': 'NumberData', }
}
