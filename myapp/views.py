from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth import authenticate
from .models import *
from .serializers import *
# Create your views here.

class login_View(APIView):
  def post(self,request):
    data_obj = request.data
    username = data_obj.get("username")
    password = data_obj.get("password")

    user = authenticate(username = username , password = password)
    

    if not user :
      return Response('user not found')
    
    else:
      refresh =  RefreshToken.for_user(user)
      access_token = refresh.access_token

      return Response ({
        'refresh' : str(refresh),
        'access_token' : str(access_token)
      })
    
class logoutView(APIView):
  def post(self,request):

    try:
      refersh_token = request.data.get('refresh')

      if not refersh_token:
        return Response({'error':'error refresh token is required'})
    
    
      token = RefreshToken(refersh_token)
      token.blacklist()
      return Response('logout successfull')
    
    except:
      return Response('error ouccured while logging out')

class ProductAPIView(APIView):
    def get(self, request, id=None):
        if id:
            try:
                obj=Product.objects.get(pk=id)
                serializers=ProductSerializer(obj)
                return Response(serializers.data)
            
            except:
                return Response("not found")
            
        else:
            obj=Product.objects.all()
            serializers=ProductSerializer(obj,many=True)
            return Response(serializers.data)    

    def post(self,request):
        value=request.data
        cat=Category.objects.get(category_id=value.get('product_category'))
        product=Product.objects.create(
            product_name=value.get('product_name'),
            product_img=value.get('product_img'),
            product_price=value.get('product_price'),
            product_category=cat
            
        )
        product.save()
        return Response("created successfully")
    
    def delete(self, request, id=None):
        obj=Product.objects.get(pk=id)
        obj.delete()
        return Response("deleted successfully")
    
    def put(self,request,id=None):
        obj=Product.objects.get(pk=id)
        serializers=ProductSerializer(obj,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response("successfully updated")


class CategoryAPIView(APIView):
    def get(self, request, id=None):
        if id:
            try:
                obj=Category.objects.get(pk=id)
                serializers=CategorySerializer(obj)
                return Response(serializers.data)
            except:
                return Response("data not found")
            
        else:
            obj=Category.objects.all()
            serializers=CategorySerializer(obj,many=True)
            return Response(serializers.data)  

    def post(self, request):
        value=request.data
        loc=Location.objects.get(location_id=value.get('location'))
        Category_instance=Category.objects.create(
            cate_name=value.get('cate_name'),
            location=loc
        )     
        Category_instance.save()
        return Response("created successfully") 
    
    def put(self, request,id=None):
        obj=Category.objects.get(pk=id)
        value=request.data
        serializers=CategorySerializer(obj,value)
        serializers.save()
        return Response("updated successfully")
    
    def delete(self, request, id=None):
        obj=Category.objects.get(pk=id)
        obj.delete()
        return Response("updated successfully")
    

class LocationAPIView(APIView):
    def get(self, request,id=None):
        if id:
            try:
                obj=Location.objects.get(pk=id)
                serializers=LocationSerializer(obj)
                return Response(serializers.data) 
            except:
                return Response("not found")   

        else:
            obj=Location.objects.all()
            serializers=LocationSerializer(obj,many=True)
            return Response(serializers.data)

    def post(self, request):
        value=request.data
        Location_instance=Location.objects.create(
            location_address=value.get("location_address")
        )   
        Location_instance.save()
        return Response("created successfuly")

    def put(self, request,id=None):
        obj=Location.objects.get(pk=id)
        value=request.data
        serializers=LocationSerializer(obj,value)
        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data)

    def delete(self, request,id=None):
        obj=Location.objects.get(pk=id)
        obj.delete()
        return Response("deleted successfully")     


class StockAPIView(APIView):
    def get(self, request, id=None):
        if id:
            try:
                obj=Stock.objects.get(pk=id)
                serializers=StockSerializer(obj)
                return Response(serializers.data)
            
            except:
                return Response("Data not found")
            
        else:
            obj=Stock.objects.all()
            serializers=StockSerializer(obj,many=True) 
            return Response(serializers.data)   
        
    def post(self, request):
        value=request.data
        product=Product.objects.get(product_id=value.get('pro_name'))
        category1=Category.objects.get(category_id=value.get("category"))
        locations=Location.objects.get(location_id=value.get("loc"))
        stock_instance=Stock.objects.create(
            pro_name=product,
            category=category1,
            loc=locations,
            quantity=value.get("quantity"),
            updated_at=value.get("updated_at")
        )   
        stock_instance.save()
        return Response("created successfully")

    def put(self, request, id=None):
        value=request.data
        obj=Stock.objects.get(pk=id)
        serializers=StockSerializer(obj,value)
        if serializers.is_valid:
            serializers.save()
        return Response("updated successfully") 

    def delete(self, request,id=None):
        obj=Stock.objects.get(pk=id)
        obj.delete()
        return Response("deleted successfully")  

class SupplierAPIView(APIView):
    def get(self, request, id=None):
        if id:
            try:
                obj=Supplier.objects.get(pk=id)
                serializers=SupplierSerializer(obj)
                return Response(serializers.data)
            
            except:
                return Response("data not found")
            
        else:
            obj=Supplier.objects.all()
            serializers=SupplierSerializer(obj,many=True)
            return Response(serializers.data)    

    def post(self, request):
        value=request.data
        supplier=Supplier.objects.create(
            name=value.get("name"),
            email=value.get("email"),
            address=value.get("address")
        )
        supplier.save()
        return Response("created successfully")
    
    def put(self, request,id=None):
        value=request.data
        obj=Supplier.objects.get(pk=id)
        serializers=SupplierSerializer(obj,value)
        if serializers.is_valid():
            serializers.save()
        return Response("updated successfully")

    def delete(self, request, id=None):
        obj=Supplier.objects.get(pk=id)
        obj.delete()
        return Response("deleted successfully") 

class PurchaseOrderAPIView(APIView):
    def get(self,request, id=None):
        if id:
            try:
                obj=PurchaseOrder.objects.get(pk=id)
                serializers=PurchaseOrderSerializer(obj)
                return Response(serializers.data)
            except:
             return Response("data not found")
            
        else:
            obj=PurchaseOrder.objects.all()
            serializers=PurchaseOrderSerializer(obj,many=True)
            return Response(serializers.data)       
    
    def post(self, request):
        value=request.data
        supplier_instance=Supplier.objects.get(supplier_id=value.get("supplier"))
        purchase_instance=PurchaseOrder.objects.create(
            supplier=supplier_instance,
            order_date=value.get("order_date"),
            expected_arrival=value.get("expected_arrival"),
            status=value.get("status")
        )
        purchase_instance.save()
        return Response("created successfully")       

    def put(self, request, id=None):
        value=request.data
        obj=PurchaseOrder.objects.get(pk=id)
        serializers=PurchaseOrderSerializer(value,obj)
        if serializers.is_valid():
            serializers.save()
        return Response("updated successfully")

    def delete(self, request, id=None):
        obj=PurchaseOrder.objects.get()
        obj.delete()
        return Response("deleted successfully") 

class StockTransactionAPIView(APIView):
    def get(self, request, id=None):
        if id:
            try:
                obj=StockTransaction.objects.get(pk=id)
                serializers=StockSerializer(obj)
                return Response(serializers.data)

            except:
                return Response("not found")
        else:
            obj=StockTransaction.objects.all()
            serializers = StockTransactionSerializer(obj, many=True)
            return Response(serializers.data)   

    def post(self, request):
        value=request.data
        item1=Product.objects.get(product_id=value.get("item"))
        warehouse_instance=Location.objects.get(location_id=value.get("warehouse"))
        stocktransaction=StockTransaction.objects.create(
            item=item1,
            quantity=value.get("quantity"),
            transaction_type=value.get("transaction_type"),
            warehouse=warehouse_instance,
            timestamp=value.get("timestamp"),
            note=value.get("note")
        )  
        stocktransaction.save()
        return Response("created successfully")

    def put(self, request,id=None):
        value=request.data
        obj=StockTransaction.objects.get(pk=id)
        serializers=StockTransactionSerializer(value,obj)
        if serializers.is_valid():
            serializers.save()         

        return Response("updated successfully")    

    def delete(self, request,id=None):
        obj=StockTransaction.objects.get(pk=id)
        obj.delete()
        return Response("deleted successfully")    
    