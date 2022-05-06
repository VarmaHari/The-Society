from django.contrib import admin
from Member.models import *

# Register your models here.

admin.site.register(House) 
admin.site.register(Member)
admin.site.register(Notice)
admin.site.register(NoticeView)
admin.site.register(Complain)
admin.site.register(ComplainView)
admin.site.register(Event)
admin.site.register(EventView)