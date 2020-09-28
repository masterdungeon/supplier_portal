from django.db import models


class SupplierRegistration(models.Model):
    p_sup_bus_name = models.CharField(max_length=256, blank=False)
    p_sup_full_name = models.CharField(max_length=256, blank=False)
    p_sup_email = models.EmailField(blank=False)
    p_sup_phone = models.CharField(max_length=256, blank=True)
    address = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=256, blank=True)
    postal_code = models.CharField(max_length=256, blank=True)
    country = models.CharField(max_length=256, blank=True)
    s_sup_bus_name = models.CharField(max_length=256, blank=False)
    s_sup_full_name = models.CharField(max_length=256, blank=False)
    s_sup_email = models.EmailField(blank=False)
    s_sup_phone = models.CharField(max_length=256, blank=True)
