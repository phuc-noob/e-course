# base library 
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from matplotlib.style import context
from psutil import STATUS_RUNNING
from requests import Response 

# rest_frameword library 
from rest_framework.decorators import action
from rest_framework import viewsets ,permissions ,status ,generics
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

# model import
from .models import Course, Lesson, User
from .serializers import CourseSerializers, LessonSerializers ,UserSerializers

# swagger drf-yasg framework 
from drf_yasg.utils import swagger_auto_schema


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active = True)
    serializer_class = CourseSerializers 
    permission_classes = [permissions.IsAuthenticated]
    
    # def get_permissions(self):
    #     if self.action == 'list' : 
    #         return [permissions.AllowAny()]
    #     return [permissions.IsAuthenticated()]   
    # list (GET) --> xem danh sách khóa học 
    # list (POST) -> thêm khóa học 
    # detail      -> xem chi tiết khóa học 
    # PUT ()      -> cập nhật khóa học 
    # DELETE      -> xóa khóa học 

class UserViewSet(viewsets.ViewSet,generics.CreateAPIView,generics.RetrieveAPIView,generics.UpdateAPIView):
    queryset = User.objects.filter(is_active = True)
    serializer_class =UserSerializers
    parser_classes =[MultiPartParser,] 

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.filter(active = True)
    serializer_class = LessonSerializers
    print('lesson view set')
    
    @swagger_auto_schema(operation_description="This method do hide lesson by set False value to active", responses={
        status.HTTP_200_OK: LessonSerializers()
        }
    )


    @action(methods=['post'] ,detail=True,url_path='hide-lesson',url_name='hide-lesson')
    def hide_lesson(self,request,pk):
        print(pk)
        try :
            print(pk)
            l = Lesson.objects.get(pk=pk)
            l.active = False
            l.save()
        except Lesson.DoesNotExist:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        return Response(data=LessonSerializers(l).data,status=status.HTTP_200_OK)
    


class course(View):
    def get(self,request):
        return render(request,'courses/index.html')

def welcome(request,year):
    return HttpResponse("Welcome to Online Course " + str(year))


