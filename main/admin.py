from django.contrib import admin
from .models import *


admin.site.register(rub)
class new_postsAdmin(admin.ModelAdmin):
	list_display = ('song','published','add_mus',)
	list_display_links = ('song','add_mus',)
	search_fields = ('song','add_mus',)
admin.site.register(new_sg,new_postsAdmin)
admin.site.register(UserSongRalation)
admin.site.register(opisan)
class UserSongRalation(admin.ModelAdmin):
	pass
class lk(admin.ModelAdmin):
	list_display = ('text','artist')
	list_display_links = ('text','artist')
	search_fields = ('text','artist')
admin.site.register(city)
class city(admin.ModelAdmin):
	pass
		
	