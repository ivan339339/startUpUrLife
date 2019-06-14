from django.contrib import admin
from app.models import *

# Register your models here.
@admin.register(User)
@admin.register(CVID)
@admin.register(Appointement)
@admin.register(Portfolio)
@admin.register(Goal)
@admin.register(QuestionTip)
@admin.register(Answer)

class PersonAdmin(admin.ModelAdmin):
        pass
