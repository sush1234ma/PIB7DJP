from django.contrib import admin

# Register your models here.
from .models import students                                             # 8
admin.site.register(students)                                  # 8.1
