from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import *
from core.serializers import *

# Create your views here.


class UserCreate(APIView):
    """
    Creates the user.
    """
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        prof_serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid() and prof_serializer.is_valid():
            user = serializer.save()
            if user:
                profile = Profile(
                    user=user,
                    phone=request.data.get("phone"),
                    national_id=request.data.get("national_id")
                    )
                profile.save()
                if profile:
                    token = Token.objects.create(user=user)
                    json = serializer.data
                    json['token'] = token.key
                    json['profile'] = prof_serializer.data

                    return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CustomerDetails(APIView):
    """
    Fetch customer debt status
    """
    def get(self, request, username, phone, format='json'):

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(dict(user="Customer not found. Please check details and submit again. "), status=status.HTTP_400_BAD_REQUEST)

        try:
            due_listing = DueListing.objects.get(customer=user)
        except DueListing.DoesNotExist:
            return Response(dict(due_listing="Customer selected has no due listings. "), status=status.HTTP_400_BAD_REQUEST)

        serializer = DueListingSerializer(due_listing)
        dict_data = dict(serializer.data);
        customer = User.objects.get(id=dict_data['customer'])
        debtor = User.objects.get(id=dict_data['debtor'])

        json = serializer.data
        json['customer'] = customer.username
        json['debtor'] = debtor.username

        return Response(json, status=status.HTTP_201_CREATED)



class DebtorsDetails(APIView):
    """
    Fetch customer debt status
    """
    def get(self, request, format='json'):

        if not DueListing.objects.filter().count() > 0:
            return Response(dict(due_listing="No customers with due listings "), status=status.HTTP_400_BAD_REQUEST)

        due_listing = DueListing.objects.all()
        serializer = DueListingSerializer(due_listing, many=True)
        output = []
        for listing in serializer.data:

            dict_data = dict(listing);
            customer = User.objects.get(id=dict_data['customer'])
            debtor = User.objects.get(id=dict_data['debtor'])

            json = listing
            json['customer'] = customer.username
            json['debtor'] = debtor.username
            output.append(json)

        return Response(output, status=status.HTTP_201_CREATED)





class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



def CreateDueListing(request):
    if request.method == 'POST':

        customer = User.objects.get(username="Dan")
        debtor = User.objects.get(username="DanielInvestors")

        due_listing = DueListing(
        customer=customer,
        debtor=debtor,
        amount=30000000,
        debt_status='none'
        )
        due_listing.save()
        return HttpResponse('OK!')

