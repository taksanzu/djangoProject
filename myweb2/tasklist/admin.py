from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Course, Lesson, Tag
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'description', 'image', 'create_dates', 'update_dates', 'active', 'category']
    search_fields = ['subject', 'create_dates', 'category__name']
    readonly_fields = ['featured_image']
    def featured_image(self, course):
        return format_html('<img src="/static/{0}" width="240px"/>',course.image.name)

class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Lesson
        fields = '__all__'

class LessonAdmin(admin.ModelAdmin):
    form = LessonForm
    list_display = ['id', 'subject', 'content', 'image', 'create_dates', 'update_dates', 'active', 'course']
    search_fields = ['subject', 'create_dates', 'course__subject']
    readonly_fields = ['featured_image']
    def featured_image(self, lesson):
        return format_html('<img src="/static/{0}" width="240px"/>',lesson.image.name)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)

