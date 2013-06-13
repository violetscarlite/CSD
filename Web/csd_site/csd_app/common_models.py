from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class DateAware(models.Model):
	dateCreated = models.DateTimeField(null = True)
	lastModified = models.DateTimeField(null = True)
	objectCreator = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_related", null=True)

	def save(self, *args, **kwargs):
		if self.dateCreated is None:
			self.dateCreated = datetime.today()
		self.lastModified = datetime.today()
		super(DateAware, self).save(*args, **kwargs)
	
	class Meta:
		abstract = True;