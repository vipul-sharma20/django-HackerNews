from django.contrib import admin
from contacts.models import Contact, News, UserProfile, Articles, Like, \
                            ContactUs, Comment
class ChoiceInline(admin.TabularInline):
    pass
class contact_admin(admin.ModelAdmin):
    pass

admin.site.register(Contact, contact_admin)
admin.site.register(UserProfile, contact_admin)
admin.site.register(Articles, contact_admin)
admin.site.register(Like, contact_admin)
admin.site.register(Comment, contact_admin)
admin.site.register(News, contact_admin)
admin.site.register(ContactUs, contact_admin)
