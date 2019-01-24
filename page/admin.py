# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
# Register your models here.
from. models import User, BankDetails

from django.core.exceptions import ValidationError


class AuthorAdmin(admin.ModelAdmin):
	search_fields = ['first_name', 'last_name', 'email']
  	list_display = ('first_name','last_name','email')
  	# change_list_template = 'admin/index.html'

admin.site.register(User, AuthorAdmin)
# admin.site.unregister(Group)
admin.site.register(BankDetails)