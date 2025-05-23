# myapp/urls.py
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', login_View.as_view()),
    path('logout/', logoutView.as_view()),
    path('pro/', ProductAPIView.as_view(),name='role'),
    path('pro/<int:id>/', ProductAPIView.as_view(),name='role'),
    path('cat/',CategoryAPIView.as_view(),name='Category'),
    path('cat/<int:id>/',CategoryAPIView.as_view(),name='Category'),
    path('loc/',LocationAPIView.as_view(),name='Location'),
    path('loc/<int:id>/',LocationAPIView.as_view(),name='Location'),
    path('sto/',StockAPIView.as_view(),name="stock"),
    path('sto/<int:id>/',StockAPIView.as_view(),name="stock"),
    path('sup/',SupplierAPIView.as_view(),name="Supplier"),
    path('sup/<int:id>/',SupplierAPIView.as_view(),name="Supplier"),
    path('pur/',PurchaseOrderAPIView.as_view(),name="purchaseorder"),
    path('pur/<int:id>/',PurchaseOrderAPIView.as_view(),name="purchaseorder"),
    path('stot/',StockTransactionAPIView.as_view(),name="stocktransaction"),
    path('stot/<int:id>/',StockTransactionAPIView.as_view(),name="stocktraction"),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
]
