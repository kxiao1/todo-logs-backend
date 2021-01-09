from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo

from datetime import datetime, timedelta
# Create your views here.


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer

    def get_queryset(self):
        queryset = Todo.objects.all()
        date = self.request.query_params.get('date', None)
        mode = int(self.request.query_params.get('mode', '-1'))
        if date is not None:
            if mode == -1:
                raise TypeError("Insufficient arguments")
            if mode == 0:  # weekly
                queryset = queryset.filter(date_added=date)
            else:  # weekly
                dt = datetime.fromisoformat(date)
                start = dt - timedelta(days=dt.weekday())
                end = start + timedelta(days=6)
                queryset = queryset.filter(
                    date_added__gte=start).filter(date_added__lte=end)
        return queryset
