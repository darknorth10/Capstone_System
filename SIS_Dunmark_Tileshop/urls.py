"""SIS_Dunmark_Tileshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('/', include('VisitorsPage.urls')),
    path('Login/', include('LoginAuthentication.urls')),
    path('Dashboard/', include('Dashboard.urls')),
    path('UserManagement/', include('UserManagement.urls')),
    path('POS/', include('PointOfSale.urls')),
    path('Sales_transaction/', include('SalesTransaction.urls')),
    path('Product_management/', include('ProductManagement.urls')),
    path('Return_product/', include('ReturnProduct.urls')),
    path('Settings/', include('Settings.urls')),
    path('Audit_trail/', include('AuditTrail.urls')),
    path('Reports/', include('Reports.urls')),
    path('About_system/', include('AboutSystem.urls')),
    
    #PATH('SALESTRANSACTION/', INCLUDE('SALESTRANSACTION.URLS')),
    #PATH('PRODUCTMANAGEMENT/', INCLUDE('PRODUCTMANAGEMENT.URLS')),
    #PATH('RETURNPRODUCT/', INCLUDE('RETURNPRODUCT.URLS')),
    #PATH('SETTINGS/', INCLUDE('SETTINGS.URLS')),
    #PATH('AUDITTRAIL/', INCLUDE('AUDITTRAIL.URLS')),
    #PATH('REPORTS/', INCLUDE('REPORTS.URLS')),
    #PATH('ABOUTSYSTEM/', INCLUDE('ABOUTSYSTEM.URLS')),
]
