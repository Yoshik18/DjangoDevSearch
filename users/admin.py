from django.contrib import admin

# Register your models here.
from .models import Profile
from .models import Skill
from .models import Messages

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Messages)
