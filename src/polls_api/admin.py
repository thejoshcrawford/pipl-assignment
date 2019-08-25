from django.contrib import admin

# Register your models here.
from .models import Poll
from .models import PollOption
from .models import PollResponse

admin.site.register(Poll)
admin.site.register(PollOption)
admin.site.register(PollResponse)