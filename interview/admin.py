# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from interview.models import User, Interview, Author, Imagecount


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email',)
    list_filter = ('username', 'email',)
    search_fields = ('username', 'email',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'position',)
    list_filter = ('name', 'position',)
    search_fields = ('name', 'position',)


class InterviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'company',)
    list_filter = ('title', 'desc', 'company',)
    search_fields = ('title', 'desc', 'company',)


class ImagecountAdmin(admin.ModelAdmin):
    list_display = ('imageName',)
    list_filter = ('imageName',)
    search_fields = ('imageName',)


admin.site.register(User, UserAdmin),
admin.site.register(Author, AuthorAdmin),
admin.site.register(Interview, InterviewAdmin),
admin.site.register(Imagecount, ImagecountAdmin),
