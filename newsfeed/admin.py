from django.contrib import admin
from .models import LiveStream
from .models import LiveVideo
from .models import News
from .models import Post
from .models import Event
from .models import Like
from .models import Comment


# Register your models here



admin.site.register(LiveStream)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(News)
admin.site.register(Post)
admin.site.register(LiveVideo)
admin.site.register(Event)
