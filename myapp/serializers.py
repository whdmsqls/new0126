from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    #클라이언트에서입력하는 데이터만 나열
    #아래 나열한 데이터를 입력하면 Book클래스의 인스턴스를 자동 생성
    fields = ['bid', 'title', 'author', 'publisheddate']