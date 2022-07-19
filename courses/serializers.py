# serializers sẽ chuyển những tập tin dữ liệu phức tạp
# về dạng Json hoặc đơn giản hơn để xử lý hoặc gửi ra bên ngoài .
from ast import mod
from dataclasses import field, fields
from pyexpat import model
from turtle import mode
from rest_framework.serializers import ModelSerializer
from .models import Course, Lesson, Tag, User 

class UserSerializers(ModelSerializer):
    class Meta :
        model = User
        fields = ['id','username','password','first_name','last_name','email']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])   # set_password : method bam password de luu vao database
        return user

    

class CourseSerializers(ModelSerializer):
    class Meta :
        model = Course 
        fields = ["id","subject","img_upload","description","created_at","category"]

class TagsSerializers(ModelSerializer):
    class Meta :
        model =Tag
        fields = ["id","name"]

class LessonSerializers(ModelSerializer):
    tags = TagsSerializers(many=True)
    class Meta : 
        model = Lesson
        fields = ['id','subject','created_at',"active",'content','img_upload','tags']