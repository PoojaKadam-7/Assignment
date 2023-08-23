from django.urls import path
from api.views import *
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import Sitemap
# from api.sitemaps import *

app_name = "api"
# sitemaps = {
#     'static': Static_Sitemap,
# }

urlpatterns = [
    path('', Home.as_view(),name="home"),
    # path('personal_details/', Personal_details.as_view({'get': 'list','post':'create'}),name="personal_details"),
    # path('personal_details/<int:id>', Personal_details.as_view({'get':'retrieve', 'put':'update','delete':'destroy'}),name="personal_details"),
    # path('bank_interest_rate/', Bank_interest_rate.as_view({'get':'list'}),name="bank_interest_rate"),
    path('personal_loan/', Personal_Loan.as_view(),name="personal_loan"),
    path('home_loan/', Home_Loan.as_view(),name="home_loan"),
    path('business_loan/', Business_Loan.as_view(),name="business_loan"),
    path('life_insurance/', Life_Insurance.as_view(),name="life_insurance"),
    path('general_insurance_plans/', General_Insurance_Plans.as_view(),name="general_insurance_plans"),
    path('idfc_credit_card/', IDFC_Credit_Card.as_view(),name="idfc_credit_card"),
    path('yes_bank_credit_card/', Yes_Bank_Credit_Card.as_view(),name="yes_bank_credit_card"),
    path('standard_chartered_credit_card/', Standard_Chartered_Credit_Card.as_view(),name="standard_chartered_credit_card"),
    path('axis_bank_credit_card/', Axis_Bank_Credit_Card.as_view(),name="axis_bank_credit_card"),
    path('playstore/', Play_store.as_view(),name="playstore"),
    path('about_us/', About_us.as_view(),name="about_us"),
    path('terms_and_condition/', Terms_and_Condition.as_view(),name="terms_and_condition"),
    path('privacy-policy/', Privacy_policy.as_view(),name="privacy-policy"),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]
