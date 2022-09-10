from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signupUsers, name='signupusers'),
    path('home', views.home, name='ups-home'),
    path('profile', views.profile, name='ups-profile'),
    path('login', views.loginUsers, name='loginusers'),
    path('package', views.packageList, name='ups-package'),
    path('showpackage', views.onepackage, name='ups-onepackage'),
    path('searchpackage', views.searchPackage, name='search-package'),
    path('searchresult', views.searchResult, name='search-result'),
    path('feedback', views.feedback, name='ups-feedback'),
    path('submitfeedback', views.submitFeedback, name='ups-submitfeedback'),
    path('viewfeedback', views.viewFeedback, name='ups-viewfeedback'),
    path('update', views.update, name='ups-update'),
    path('', views.trackpackage, name = 'ups-track'),
    path('trackresult', views.trackResult, name = 'ups-trackresult'),
    path('calculate', views.calculate, name = 'ups-calculate'),
    path('cost', views.cost, name='ups-cost'),
]
