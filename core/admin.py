from django.contrib import admin

from .models import Member, OKR


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(OKR)
class OKRAdmin(admin.ModelAdmin):
    list_display = ('member', 'objective', 'key_result_1', 'key_result_2', 'key_result_3', 'key_result_4',
                    'key_result_5')
