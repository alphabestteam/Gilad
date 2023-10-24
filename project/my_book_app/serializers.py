from rest_framework import serializers
from .models import Book, Message, User
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ('publication_date',)


    def create(self, validated_data):
        """
        Create and return a new `book` instance, given the validated data.
        """
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `book` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.save()
        return instance
    
    def get_age(self, obj):
        # Calculate the age of the book based on the publication year and current year.
        current_year = datetime.now().year
        return current_year - obj.publication_date.year
    

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'