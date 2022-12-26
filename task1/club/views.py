from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import status


class CompetitionList(APIView):
    def get(self, request, format=None):
        queryset = Competition.objects.all()
        serializer = CompetitionSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe = False)
        
    def post(self, request, format=None):
        serializer = CompetitionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

class FootballclubList(APIView):
    def get(self, request, format=None):
        queryset = Footballclub.objects.all()
        serializer = FootballclubSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe = False)
        
    def post(self, request, format=None):
        serializer = FootballclubSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

class MatchList(APIView):
    def get(self, request, format=None):
        queryset = Match.objects.all()
        serializer = MatchSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe = False)
        
    def post(self, request, format=None):
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

class PlayerList(APIView):
    def get(self, request, format=None):
        queryset = Player.objects.all()
        serializer = PlayerSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe = False)
        
    def post(self, request, format=None):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)