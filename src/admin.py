from django.contrib import admin

from .models import Question,Option,Answer,Total,Marks,StoreUserAns

admin.site.register(Question)

admin.site.register(Option)

admin.site.register(Answer)

admin.site.register(Total)

admin.site.register(Marks)

admin.site.register(StoreUserAns)