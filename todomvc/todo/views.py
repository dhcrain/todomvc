from django.shortcuts import render
from rest_framework import generics
from todo.models import Todo
# Create your views here.

class TodosListCreateAPIView(generics.ListCreateAPIView):
    # queryset = Todo.Objects.all()
    pass
