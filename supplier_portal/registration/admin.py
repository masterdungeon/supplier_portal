from django.contrib import admin
from django.contrib.admin import AdminSite
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

from .models import SupplierRegistration


class MyAdminSite(AdminSite):

    def get_urls(self):
        urls = super().get_urls()
        urls += [
            path('custom_admin_view/', self.admin_view(self.custom_view))
        ]
        return urls

    def custom_view(self, request):
        """
            This method return all supplier records
            to custom admin template.
        """
        supplier_recs = SupplierRegistration.objects.all()
        return render(request, 'registration/admin.html', {
            'Suppliers': supplier_recs
        })

admin_site = MyAdminSite()
