from django.contrib import admin

from backend.models.post import Post
from backend.models.building import Building
from backend.models.jibun import Jibun

# Register your models here.
admin.site.register(Jibun)
admin.site.register(Building)
admin.site.register(Post)
