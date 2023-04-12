from django.shortcuts import render
from.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User, company
from user.serializers import UserSerializers,AdminSerialzers, companySerializers
from django.views.generic import DeleteView
from django.db.models import Q

# Create your views here.

class adminlog(APIView):
    def post(self,request):
        print(request.data)
        user_name = request.data['user_name']
        password = request.data['password']
        print('username',user_name)
        print('password',password)
        
        log = adminlogin.objects.filter(user_name=user_name)
        print('log',log)
        if log is not None:
            ad = True
        else:
            ad=False
            
        return Response(ad)

class users(APIView):
    def get(self,request):
        user=User.objects.filter(is_active=True)
        serializer = UserSerializers(user,many=True)
       
        return Response(serializer.data)
    
class delete(APIView):
    def post(self,request,id):
        user1 = User.objects.filter(id=id)
        print('user',user1)
        user1.delete()
        
        user=User.objects.filter(is_active=True)
        serializer = UserSerializers(user,many=True)
        print('deleted',user1)
        
        
        return Response(serializer.data)
    
class Update(APIView):
   def post(self,request,id):
        data = request.data
        try:
            users=User.objects.get(pk=id)
            data['password']=users.password
        except:
            return Response("Not found in DataBase")
        serializeobj=UserSerializers(users,data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            
            user=User.objects.filter(is_active=True)
            serializerobj = UserSerializers(user,many=True)    
            return Response (serializerobj.data)
        return Response(serializeobj.errors)
   

class company_list(APIView):
    def get(self,request):
        comp = company.objects.filter(processing=False,Accept=False,Decline=False)
        print('company',comp)
        serializer = companySerializers(comp,many=True)   
        return Response(serializer.data)

class company_detail(APIView):
    def get(self,request,id):
        comps = company.objects.get(id=id)
        serializer = companySerializers(comps)
        return Response(serializer.data)
        # order__order_number=order_id

class pend_list(APIView):
    def get(self,request,id):
        com = company.objects.filter(processing=False,Accept=False,Decline=False,id=id)
        com.update(processing=True)
        
        coms = company.objects.filter(processing=False)
        print('coms',coms)
        serializer = companySerializers(coms,many=True)
 
        return Response(serializer.data)
    
class pend_list1(APIView):
    def get(self,request):
         com = company.objects.filter(processing=True,Accept=False,Decline=False)
         serializer = companySerializers(com,many=True) 
         return Response(serializer.data)
     
class accept(APIView):
    def get(self,reuest,id):
        com = company.objects.filter(processing=True,Accept=False,Decline=False,id=id)
        com.update(Accept=True)
        coms = company.objects.filter(processing=True,Accept = True)
        serializer = companySerializers(coms,many=True)
        return Response(serializer.data)
    
class accept1(APIView):
    def get(self,request):
         com = company.objects.filter(processing=True,Accept=True,Decline=False)
         serializer = companySerializers(com,many=True) 
         return Response(serializer.data)

class Decline(APIView):
    def post(self,request,id):
        com =  company.objects.get(id=id)
        print('com',com)
        com.delete()
        print('deleted',com.id)
        comp=company.objects.all()
        serializer = companySerializers(comp,many=True)
        print('deleted',comp)
        
        
        return Response(serializer.data)

class application(APIView):
    def get(self,request):
        comp = company.objects.all()
        print('company',comp)
        serializer = companySerializers(comp,many=True)   
        return Response(serializer.data)

class get_approved(APIView):
    def get(self,request):
        com = company.objects.filter(Accept=True)
        serializer = companySerializers(com,many=True)
        return Response(serializer.data)

class booking(APIView):
    def post(self,request):
        slot = request.data['select_value']
        print('slot',slot)
        
        data1 = {key:value for key,value in request.data.items() if key!='select_value'}
        print('data1',data1)
        comp = company.objects.get(company_name=slot)
        print('comp',comp)
      
        serializer = companySerializers(comp,data=data1,partial=True)
        print('serializer',serializer)
       
        if serializer.is_valid():
            print('valid',serializer.is_valid())
            serializer.save()
            return Response(serializer.data)
        return Response('falileds')
        
            
class get_all(APIView):
    def get(slef,request):
        slot = request.data['select_value']
        com = company.objects.get(company_name=slot)       
        serializer = companySerializers(com,partial=True)
        return Response(serializer.data)