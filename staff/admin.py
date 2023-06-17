from django.contrib import admin

from staff.models import Department, Post, Staff


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'director')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('photo', 'fullname', 'department', 'post', 'birth_date')
    list_display_links = ('photo', 'fullname')
    list_filter = ('department', 'post')
    search_fields = ('_fullname',)
