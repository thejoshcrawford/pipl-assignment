from django.contrib import admin

# Register your models here.
from .models import Poll
from .models import PollOption
from .models import PollResponse
from .models import BrowserInstance

admin.site.register(Poll)
admin.site.register(PollOption)
admin.site.register(PollResponse)
admin.site.register(BrowserInstance)