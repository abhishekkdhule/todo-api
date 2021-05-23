from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from . models import CheckList,CheckListItem
from . serializers import CheckListSerializer,CheckListItemSerializer
from . permissions import IsOwner
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView)
# Create your views here.

@api_view(['GET'])
def testapi(request):
    return Response({"Name":"Abhi"})

class CheckListsAPI(ListCreateAPIView):
    """
    Listing, Creation
    """
    serializer_class=CheckListSerializer
    permission_classes=[IsAuthenticated,IsOwner]

    def get_queryset(self):
        qs=CheckList.objects.filter(user=self.request.user)
        return qs

# class CheckListsAPI(APIView):
#     serializer_class=CheckListSerializer
#     permission_classes=[IsAuthenticated]
#     def get(self,request,format=None):
#         print(request.user)
#         checklists=CheckList.objects.filter(user=request.user)
#         serializer=self.serializer_class(checklists,many=True)
#         serialized_data=serializer.data
#         return Response(serialized_data,status=status.HTTP_200_OK)

#     def post(self,request,format=None):
#         serializer=self.serializer_class(data=request.data,context={"request":request})
#         if(serializer.is_valid()):
#             serializer.save()
#             serialized_data=serializer.data
#             return Response(serialized_data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CheckListAPI(RetrieveUpdateDestroyAPIView):
    """
    Retrive, Update, Destroy
    """
    serializer_class=CheckListSerializer
    permission_classes=[IsAuthenticated,IsOwner]
    queryset=CheckList.objects.all()

# # class CheckListAPI(APIView):
# #     serializer_class=CheckListSerializer
# #     permission_classes=[IsAuthenticated,IsOwner]
# #     def get_object(self,pk):
# #         try:
# #             obj=CheckList.objects.get(id=pk)
# #             self.check_object_permissions(self.request,obj)
# #             return obj
# #         except CheckList.DoesNotExist:
# #             raise Http404

# #     def get(self,request,pk,format=None):
# #         checklist=self.get_object(pk)
# #         serializer=self.serializer_class(checklist)
# #         serialized_data=serializer.data
# #         return Response(serialized_data,status=status.HTTP_200_OK)

# #     def put(self,request,pk,format=None):
# #         checklist=self.get_object(pk)
# #         serializer=self.serializer_class(checklist,data=request.data,context={"request":request})
# #         if(serializer.is_valid()):
# #             serializer.save()
# #             serialized_data=serializer.data
# #             return Response(serialized_data,status=status.HTTP_202_ACCEPTED)
# #         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,pk,format=None):
#         checklist=self.get_object(pk)
#         checklist.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class checkListItemCreateAPI(CreateAPIView):
    """
    Creation
    """
    serializer_class=CheckListItemSerializer
    permission_classes=[IsAuthenticated]

# class checkListItemCreateAPI(APIView):
#     serializer_class=CheckListItemSerializer
#     permission_classes=[IsAuthenticated]
#     def post(self,request,format=None):
#         serializer=self.serializer_class(data=request.data,context={"request":request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class checkListItemAPI(RetrieveUpdateDestroyAPIView):
    serializer_class=CheckListItemSerializer
    permission_classes=[IsAuthenticated,IsOwner]
    queryset=CheckListItem.objects.all()
        
# class checkListItemAPI(APIView):
#     serializer_class=CheckListItemSerializer
#     permission_classes=[IsAuthenticated,IsOwner]
#     def get_object(self,pk):
#         try:
#             obj=CheckListItem.objects.get(id=pk)
#             self.check_object_permissions(self.request,obj)
#             return obj
#         except CheckListItem.DoesNotExist:
#             raise Http404
#     def get(self,request,pk,format=None):
#         checklistitem=self.get_object(pk)
#         serializer=self.serializer_class(checklistitem)
#         serialized_data=serializer.data
#         return Response(serialized_data,status=status.HTTP_200_OK)

#     def put(self,request,pk,foramt=None):
#         checklistitem=self.get_object(pk)
#         serializer=self.serializer_class(checklistitem,data=request.data,context={"request":request})
#         if serializer.is_valid():
#             serializer.save()
#             serialized_data=serializer.data
#             return Response(serialized_data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,pk,format=None):
#         checklistitem=self.get_object(pk)
#         checklistitem.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
