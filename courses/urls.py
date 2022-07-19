from django.contrib import admin
from django.urls import path ,re_path ,include
from . import views
from .admin import admin_site
from rest_framework.routers import DefaultRouter 

app_name ='course'

router = DefaultRouter()
router.register('courses',views.CourseViewSet)
router.register('lesson',views.LessonViewSet)
router.register('users',views.UserViewSet)

urlpatterns = [
    path('a/',views.course.as_view()),
    path('user',admin_site.urls),
    re_path(r'^wel/(?P<year>[0-9]{4})/$',views.welcome), # biểu thức chính quy 
    path('welcome/<int:year>/',views.welcome,name='welcome'),
    path('',include(router.urls))
]
