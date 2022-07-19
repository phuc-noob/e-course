# from curses.ascii import alt
from dataclasses import field
import imp
from pyexpat import model
import site
from django.contrib import admin
from matplotlib.widgets import Widget
from .models import Category ,Lesson ,Course, Tag, User 
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.
class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta :
        model =Lesson
        fields = '__all__'

class LessonTagInline(admin.TabularInline):
    model = Lesson.tags.through

class LessonAdmin(admin.ModelAdmin):
    class Media :
        css = {
            'all' : ('/static/courses/css/style.css',)
        }
    form = LessonForm
    list_display = ["id","subject","created_at","active","course"]
    search_fields = ["subject","created_at","course"]
    list_filter = ["subject","created_at"]
    readonly_fields = ["avatar"]
    inlines = (LessonTagInline,)

    def avatar(self,Lesson):
        return mark_safe("<img src='/static/{img_url}' alt='{alt}' width = 200/>".format(img_url=Lesson.img_upload.name,alt=Lesson.subject))

# custom for admine site
class CourseAppAdminSite(admin.AdminSite):
    site_header = "Course Online something"

# create object admin_site
admin_site = CourseAppAdminSite(name= 'myadmin')

class LessonInline(admin.StackedInline):
    model =Lesson
    pk_name ='course'

class CourseAdmin(admin.ModelAdmin):
    inlines = (LessonInline,)
# admin_site.register(Tag)
# admin_site.register(Category)
# admin_site.register(Lesson,LessonAdmin)
# admin_site.register(Course,CourseAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Lesson,LessonAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(User)
# custom admin_header site
admin.site.site_header = "Coursera - Let's start learning"
admin.site.site_title  =  "Site title ... "
admin.site.index_title  =  "Index title"



# bản chất của open source là luôn luôn mở để cho mình cusom 