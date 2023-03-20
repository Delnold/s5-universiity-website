from main_website.models import Champions, ChampionsSkills, ChampionsPresentations, ChallVideos, Items, Runes, UserExtended
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
class UserProfileInline(admin.StackedInline):
    model = UserExtended
    can_delete = False
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

admin.site.register(Champions)
admin.site.register(ChampionsSkills)
admin.site.register(ChampionsPresentations)
admin.site.register(Items)
admin.site.register(Runes)
admin.site.register(ChallVideos)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# Register your models here.
