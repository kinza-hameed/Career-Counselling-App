from django.contrib import admin

from .models import Field,Difficulty_level,Questionaries,User_Marks

admin.site.register([Field,Difficulty_level,Questionaries,User_Marks])
