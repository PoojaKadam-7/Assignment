from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import *
# from .serializers import *
# from api.serializers import *
from django.shortcuts import redirect, render
from django.contrib import messages

from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class Home(TemplateView):
  template_name = 'index.html'

class About_us(TemplateView):
  template_name = 'about_us.html'

class Terms_and_Condition(TemplateView):
  template_name = 'Term_and_Condition.html'

class Privacy_policy(TemplateView):
  template_name = 'privacy-policy.html'

class Personal_Loan(TemplateView):
  template_name = 'personal_loan.html'

  def get_context_data(self,**kwargs):
    context = super().get_context_data(**kwargs)
    interest_rate = Interest_rate.objects.all
    context['interest_rate'] = interest_rate
    return context
  
  def post(self, request, *args, **kwargs):
    context = self.get_context_data(**kwargs)
    if request.method == 'POST':
      name = request.POST.get('name', None)
      contact = request.POST.get('contact', None)
      city = request.POST.get('city', None)
      occupation = request.POST.get('occupation', None)
      required_loan_amt = request.POST.get('required_loan_amt', None)
      net_salary = request.POST.get('net_salary', None)
      current_monthly_emi = request.POST.get('current_monthly_emi', None)
      tenure = request.POST.get('tenure', None)
      dob = request.POST.get('dob', None)
      agree = request.POST.get('agree', None)
      type = request.POST.get('type', None)
      if request.POST.get('agree')=='on':
        agree = True
      else:
        agree = False
        messages.error(request, 'Need to check I agree to the Credit DSA Terms Of Use and Privacy Policy.')
        return redirect('api:personal_loan')
    visitor = Personal_info(name=name, contact=contact, occupation=occupation, required_loan_amt=required_loan_amt, net_salary=net_salary,current_monthly_emi=current_monthly_emi, tenure=tenure, city=city, dob=dob, type=type,agree=agree)
    visitor.save()
    messages.success(request, 'Your Details Sent Successfully..!')
    return redirect('api:personal_loan') 

class Home_Loan(TemplateView):
  template_name = 'home_loan.html'

  def get_context_data(self,**kwargs):
    context = super().get_context_data(**kwargs)
    interest_rate = Interest_rate.objects.all
    context['interest_rate'] = interest_rate
    return context

  def post(self, request, *args, **kwargs):
    context = self.get_context_data(**kwargs)
    if request.method == 'POST':
      name = request.POST.get('name', None)
      contact = request.POST.get('contact', None)
      city = request.POST.get('city', None)
      occupation = request.POST.get('occupation', None)
      required_loan_amt = request.POST.get('required_loan_amt', None)
      net_salary = request.POST.get('net_salary', None)
      current_monthly_emi = request.POST.get('current_monthly_emi', None)
      tenure = request.POST.get('tenure', None)
      dob = request.POST.get('dob', None)
      agree = request.POST.get('agree', None)
      type = request.POST.get('type', None)
      if request.POST.get('agree')=='on':
        agree = True
      else:
        agree = False
        messages.error(request, 'Need to check I agree to the Credit DSA Terms Of Use and Privacy Policy.')
        return redirect('api:home_loan')
    visitor = Personal_info(name=name, contact=contact, occupation=occupation, required_loan_amt=required_loan_amt, net_salary=net_salary,current_monthly_emi=current_monthly_emi, tenure=tenure, city=city, dob=dob, type=type,agree=agree)
    visitor.save()
    messages.success(request, 'Your Details Sent Successfully..!')
    return redirect('api:home_loan')

class Business_Loan(TemplateView):
  template_name = 'business_loan.html'

  def get_context_data(self,**kwargs):
    context = super().get_context_data(**kwargs)
    interest_rate = Interest_rate.objects.all
    context['interest_rate'] = interest_rate
    return context

  def post(self, request, *args, **kwargs):
    context = self.get_context_data(**kwargs)
    if request.method == 'POST':
      name = request.POST.get('name', None)
      contact = request.POST.get('contact', None)
      city = request.POST.get('city', None)
      occupation = request.POST.get('occupation', None)
      required_loan_amt = request.POST.get('required_loan_amt', None)
      net_salary = request.POST.get('net_salary', None)
      current_monthly_emi = request.POST.get('current_monthly_emi', None)
      tenure = request.POST.get('tenure', None)
      dob = request.POST.get('dob', None)
      agree = request.POST.get('agree', None)
      type = request.POST.get('type', None)
      if request.POST.get('agree')=='on':
        agree = True
      else:
        agree = False
        messages.error(request, 'Need to check I agree to the Credit DSA Terms Of Use and Privacy Policy.')
        return redirect('api:business_loan')
    visitor = Personal_info(name=name, contact=contact, occupation=occupation, required_loan_amt=required_loan_amt, net_salary=net_salary,current_monthly_emi=current_monthly_emi, tenure=tenure, city=city, dob=dob, type=type,agree=agree)
    visitor.save()
    messages.success(request, 'Your Details Sent Successfully..!')
    return redirect('api:business_loan')

class Life_Insurance(TemplateView):
  template_name = 'life_insurance.html'

  def post(self, request, *args, **kwargs):
    context = self.get_context_data(**kwargs)
    if request.method == 'POST':
      name = request.POST.get('name', None)
      contact = request.POST.get('contact', None)
      city = request.POST.get('city', None)
      occupation = request.POST.get('occupation', None)
      required_loan_amt = request.POST.get('required_loan_amt', None)
      net_salary = request.POST.get('net_salary', None)
      current_monthly_emi = request.POST.get('current_monthly_emi', None)
      tenure = request.POST.get('tenure', None)
      dob = request.POST.get('dob', None)
      agree = request.POST.get('agree', None)
      type = request.POST.get('type', None)
      if request.POST.get('agree')=='on':
        agree = True
      else:
        agree = False
        messages.error(request, 'Need to check I agree to the Credit DSA Terms Of Use and Privacy Policy.')
        return redirect('api:life_insurance')
    visitor = Personal_info(name=name, contact=contact, occupation=occupation, required_loan_amt=required_loan_amt, net_salary=net_salary,current_monthly_emi=current_monthly_emi, tenure=tenure, city=city, dob=dob, type=type,agree=agree)
    visitor.save()
    messages.success(request, 'Your Details Sent Successfully..!')
    return redirect('api:life_insurance')  

class General_Insurance_Plans(TemplateView):
  template_name = 'genral_insurance_plan.html'

  def post(self, request, *args, **kwargs):
    context = self.get_context_data(**kwargs)
    if request.method == 'POST':
      name = request.POST.get('name', None)
      contact = request.POST.get('contact', None)
      city = request.POST.get('city', None)
      occupation = request.POST.get('occupation', None)
      required_loan_amt = request.POST.get('required_loan_amt', None)
      net_salary = request.POST.get('net_salary', None)
      current_monthly_emi = request.POST.get('current_monthly_emi', None)
      tenure = request.POST.get('tenure', None)
      dob = request.POST.get('dob', None)
      agree = request.POST.get('agree', None)
      type = request.POST.get('type', None)
      if request.POST.get('agree')=='on':
        agree = True
      else:
        agree = False
        messages.error(request, 'Need to check I agree to the Credit DSA Terms Of Use and Privacy Policy.')
        return redirect('api:general_insurance_plans')
    visitor = Personal_info(name=name, contact=contact, occupation=occupation, required_loan_amt=required_loan_amt, net_salary=net_salary,current_monthly_emi=current_monthly_emi, tenure=tenure, city=city, dob=dob, type=type,agree=agree)
    visitor.save()
    messages.success(request, 'Your Details Sent Successfully..!')
    return redirect('api:general_insurance_plans')

class IDFC_Credit_Card(TemplateView):
  template_name = 'idfc_credit_card.html'

  def post(self, request, *args, **kwargs):
    context = self.get_context_data(**kwargs)
    if request.method == 'POST':
      name = request.POST.get('name', None)
      contact = request.POST.get('contact', None)
      city = request.POST.get('city', None)
      occupation = request.POST.get('occupation', None)
      required_loan_amt = request.POST.get('required_loan_amt', None)
      net_salary = request.POST.get('net_salary', None)
      current_monthly_emi = request.POST.get('current_monthly_emi', None)
      tenure = request.POST.get('tenure', None)
      dob = request.POST.get('dob', None)
      agree = request.POST.get('agree', None)
      type = request.POST.get('type', None)
      if request.POST.get('agree')=='on':
        agree = True
      else:
        agree = False
        messages.error(request, 'Need to check I agree to the Credit DSA Terms Of Use and Privacy Policy.')
        return redirect('api:idfc_credit_card')
    visitor = Personal_info(name=name, contact=contact, occupation=occupation, required_loan_amt=required_loan_amt, net_salary=net_salary,current_monthly_emi=current_monthly_emi, tenure=tenure, city=city, dob=dob, type=type,agree=agree)
    visitor.save()
    messages.success(request, 'Your Details Sent Successfully..!')
    return redirect('api:idfc_credit_card')

class Yes_Bank_Credit_Card(TemplateView):
  template_name = 'yes_bank_credit_card.html'

  def post(self, request, *args, **kwargs):
    context = self.get_context_data(**kwargs)
    if request.method == 'POST':
      name = request.POST.get('name', None)
      contact = request.POST.get('contact', None)
      city = request.POST.get('city', None)
      occupation = request.POST.get('occupation', None)
      required_loan_amt = request.POST.get('required_loan_amt', None)
      net_salary = request.POST.get('net_salary', None)
      current_monthly_emi = request.POST.get('current_monthly_emi', None)
      tenure = request.POST.get('tenure', None)
      dob = request.POST.get('dob', None)
      agree = request.POST.get('agree', None)
      type = request.POST.get('type', None)
      if request.POST.get('agree')=='on':
        agree = True
      else:
        agree = False
        messages.error(request, 'Need to check I agree to the Credit DSA Terms Of Use and Privacy Policy.')
        return redirect('api:yes_bank_credit_card')
    visitor = Personal_info(name=name, contact=contact, occupation=occupation, required_loan_amt=required_loan_amt, net_salary=net_salary,current_monthly_emi=current_monthly_emi, tenure=tenure, city=city, dob=dob, type=type,agree=agree)
    visitor.save()
    messages.success(request, 'Your Details Sent Successfully..!')
    return redirect('api:yes_bank_credit_card')

class Standard_Chartered_Credit_Card(TemplateView):
  template_name = 'standard_chartered_credit_card.html'

  def post(self, request, *args, **kwargs):
    context = self.get_context_data(**kwargs)
    if request.method == 'POST':
      name = request.POST.get('name', None)
      contact = request.POST.get('contact', None)
      city = request.POST.get('city', None)
      occupation = request.POST.get('occupation', None)
      required_loan_amt = request.POST.get('required_loan_amt', None)
      net_salary = request.POST.get('net_salary', None)
      current_monthly_emi = request.POST.get('current_monthly_emi', None)
      tenure = request.POST.get('tenure', None)
      dob = request.POST.get('dob', None)
      agree = request.POST.get('agree', None)
      type = request.POST.get('type', None)
      if request.POST.get('agree')=='on':
        agree = True
      else:
        agree = False
        messages.error(request, 'Need to check I agree to the Credit DSA Terms Of Use and Privacy Policy.')
        return redirect('api:standard_chartered_credit_card')
    visitor = Personal_info(name=name, contact=contact, occupation=occupation, required_loan_amt=required_loan_amt, net_salary=net_salary,current_monthly_emi=current_monthly_emi, tenure=tenure, city=city, dob=dob, type=type,agree=agree)
    visitor.save()
    messages.success(request, 'Your Details Sent Successfully..!')
    return redirect('api:standard_chartered_credit_card')

class Axis_Bank_Credit_Card(TemplateView):
  template_name = 'axis_bank_credit_card.html'

  def post(self, request, *args, **kwargs):
    context = self.get_context_data(**kwargs)
    if request.method == 'POST':
      name = request.POST.get('name', None)
      contact = request.POST.get('contact', None)
      city = request.POST.get('city', None)
      occupation = request.POST.get('occupation', None)
      required_loan_amt = request.POST.get('required_loan_amt', None)
      net_salary = request.POST.get('net_salary', None)
      current_monthly_emi = request.POST.get('current_monthly_emi', None)
      tenure = request.POST.get('tenure', None)
      dob = request.POST.get('dob', None)
      agree = request.POST.get('agree', None)
      type = request.POST.get('type', None)
      if request.POST.get('agree')=='on':
        agree = True
      else:
        agree = False
        messages.error(request, 'Need to check I agree to the Credit DSA Terms Of Use and Privacy Policy.')
        return redirect('api:axis_bank_credit_card')
    visitor = Personal_info(name=name, contact=contact, occupation=occupation, required_loan_amt=required_loan_amt, net_salary=net_salary,current_monthly_emi=current_monthly_emi, tenure=tenure, city=city, dob=dob, type=type,agree=agree)
    visitor.save()
    messages.success(request, 'Your Details Sent Successfully..!')
    return redirect('api:axis_bank_credit_card')


class Play_store(TemplateView):
  template_name = 'index.html'

  def post(self, request, *args, **kwargs):
    context = self.get_context_data(**kwargs)
    if request.method == 'POST':
      contact = request.POST.get('contact', None)
      visitor = Playstore(contact=contact,)
      visitor.save()
      messages.success(request, 'Your Details Sent Successfully..! Our team will get back to you.')
      return redirect('api:home')
    else:
      messages.error(request,'somthing went wrong')
      return redirect('api:home')



# class Personal_details(viewsets.ModelViewSet):
#   serializer_class = Personal_infoSerializer
  
#   def create(self, request,*args, **kwargs):
#     if request.data["agree1"]=='on':
#       agree = True
#     else:
#       agree = False
#     details = Personal_info.objects.create(
#         name = request.data["name"],
#         contact= request.data["contact"],
#         city= request.data["city"],
#         occupation= request.data["occupation"],
#         required_loan_amt= request.data["required_loan_amt"],
#         net_salary= request.data["net_salary"],
#         current_monthly_emi= request.data["current_monthly_emi"],
#         tenure= request.data["tenure"],
#         dob= request.data["dob"],
#         agree=agree,
#         type = request.data["type"]
        
#         )
#     return Response({"message":"data created successfully"}, status=status.HTTP_201_CREATED)

#   def list(self, request,*args, **kwargs):
#     Personal_info_obj = Personal_info.objects.all()
#     serializer = Personal_infoSerializer(Personal_info_obj,many=True)
#     return Response(serializer.data,status=status.HTTP_200_OK)  
  
#   def update(self, request,*args, **kwargs):
#     if request.data["agree1"]=='on':
#       agree = True
#     else:
#       agree = False
#       details = Personal_info.objects.filter(id = kwargs['id']).update(
#           name = request.data["name"],
#           contact= request.data["contact"],
#           city= request.data["city"],
#           occupation= request.data["occupation"],
#           required_loan_amt= request.data["required_loan_amt"],
#           net_salary= request.data["net_salary"],
#           current_monthly_emi= request.data["current_monthly_emi"],
#           tenure= request.data["tenure"],
#           dob= request.data["dob"],
#           agree=agree,
#           type = request.data["type"]
#         )
#     return Response({"message":"data updated successfully"}, status=status.HTTP_200_OK)  
  
#   def destroy(self, request,*args, **kwargs):
#         try:
#             details = Personal_info.objects.get(id=self.kwargs['id']).delete()
#             return Response({"message":"data Deleted successfully"}, status=status.HTTP_200_OK)
#         except:
#             return Response({"message":"data not Found"}, status=status.HTTP_200_OK)
    

  

# class Bank_interest_rate(viewsets.ModelViewSet):
#   def list(self, request,*args, **kwargs):
#     Interest_rate_obj = Interest_rate.objects.all()
#     serializer = Interest_rateSerializer(Interest_rate_obj,many=True)
#     return Response(serializer.data,status=status.HTTP_200_OK)  

