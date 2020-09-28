from django.shortcuts import render
from django.views import View
from django.http import Http404, HttpResponse

from .models import SupplierRegistration


class IndexView(View):

    def get(self, request):
        """Return the registration form."""

        response = render(request, 'registration/index.html', {})
        return response

class RegistrationView(View):

    def get(self, request):
        """Return the registration form."""

        return render(request, "registration/registration.html", {})

    def post(self, request):
        b_name = request.POST.get('p_s_b_name')
        f_name = request.POST.get('p_s_f_name')
        p_email = request.POST.get('p_s_email')
        p_phone = request.POST.get('p_s_phone')
        match = SupplierRegistration.objects.filter(p_sup_email=p_email)
        if not match:
            try:
                obj = SupplierRegistration.objects.create(
                    p_sup_bus_name = b_name,
                    p_sup_full_name = f_name,
                    p_sup_email = p_email,
                    p_sup_phone = p_phone
                )
                return render(request, 'registration/reg_success.html', {})
            except Exception as e:
                return render(request, 'registration/registration.html', {
                    'error': str(e)
                })
        else:
            return render(request, 'registration/registration.html', {
                'error': 'Supplier with below email already exists in system. Try with another Email',
                'p_email': p_email
            })

class GetProfileView(View):

    def get(self, request):
        """
            Return the get profile form.
        """

        response = render(request, 'registration/get_profile.html', {})
        return response

    def post(self, request):
        """
            Return the profile form.
        """

        if 'get_profile_btn' in request.POST:
            email = request.POST.get('email')
            try:
                match = SupplierRegistration.objects.filter(p_sup_email=email)
                if len(match) == 1:
                    match = match[0]
                    return render(request, 'registration/profile.html', {
                        'obj': match
                    })
                else:
                    return render(request, 'registration/get_profile.html', {
                        'error': 'Supplier does not exist in system',
                        'email': email ,
                    })
            except:
                return render(request, 'registration/get_profile.html', {})
        elif 'profile_btn' in request.POST:
            p_b_name = request.POST.get('p_s_b_name')
            p_f_name = request.POST.get('p_s_f_name')
            p_p_email = request.POST.get('p_s_email')
            p_p_phone = request.POST.get('p_s_phone')
            s_b_name = request.POST.get('s_s_b_name')
            s_f_name = request.POST.get('s_s_f_name')
            s_s_email = request.POST.get('s_s_email')
            s_s_phone = request.POST.get('s_s_phone')
            address = request.POST.get('address')
            city = request.POST.get('city')
            postal_code = request.POST.get('postal_code')
            country = request.POST.get('country')
            try:
                match = SupplierRegistration.objects.filter(p_sup_email=p_p_email)
                if len(match) == 1:
                    match = match[0]
                    match.s_sup_bus_name = s_b_name
                    match.s_sup_full_name = s_f_name
                    match.s_sup_email = s_s_email
                    match.s_sup_phone = s_s_phone
                    match.address = address
                    match.city = city
                    match.postal_code = postal_code
                    match.country = country
                    match.save()
                    return render(request, 'registration/profile_success.html', {})
            except Exception as e:
                return render(request, 'registration/profile.html', {
                    'error': e,
                    'obj': match
                })
