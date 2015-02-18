from django.contrib import admin
from contributors.models import Contributor, Article, Email, Contact, ThisMonthInEvolution, HaveYouSeen

admin.site.register(Article)
admin.site.register(Contributor)
admin.site.register(Email)
admin.site.register(Contact)
admin.site.register(ThisMonthInEvolution)
admin.site.register(HaveYouSeen)

