from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
	path('',views.index,name='index'),
	path('',views.login_redirect,name='login_redirect'),
	path('login/', auth_views.LoginView.as_view(template_name='Form_base/login.html'), name="login"),
	path('Agent_register/', views.Agent_register,name='Agent_register'),
	path('user_create/', views.user_create,name='user_create'),
	path('apply_for_loan/',views.apply_for_loan,name='apply_for_loan'),
	path('apply_for_loan/smit/',views.smit,name='smit'),
	path('apply_for_loan/smit/smit/',views.smit,name='smit'),
	path('apply_for_loan/smit/smit/smit/',views.smit,name='smit'),
	path('apply_for_loan/smit/smit/smit/smit/',views.smit,name='smit'),
	path('apply_for_loan/smit/smit/smit/smit/smit/',views.smit,name='smit'),
	path('apply_for_loan/smit/smit/smit/smit/smit/smit/',views.smit,name='smit'),
	path('apply_for_loan/smit/smit/smit/smit/smit/smit/smit/',views.smit,name='smit'),
	path('apply_for_loan/smit/smit/smit/smit/smit/smit/smit/smit/',views.smit,name='smit'),
	path('apply_for_loan/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/',views.smit,name='smit'),
	path('apply_for_loan/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/',views.smit,name='smit'),
	path('apply_for_loan/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/',views.smit,name='smit'),
	path('apply_for_loan/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/',views.smit,name='smit'),
	path('apply_for_loan/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/',views.smit,name='smit'),
	path('apply_for_loan/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/',views.smit,name='smit'),
	path('apply_for_loan/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/smit/',views.smit,name='smit'),
	path('Applications/',views.Applications,name='Applications'),
	path('pending/',views.pending,name='pending'),
	path('pending/(?P <id>[\W-]+)',views.info,name='info'),
	path('pending/updatee',views.updatee,name='updatee'),
	path('logout/', auth_views.LogoutView.as_view(template_name='index.html'),name='logout'),
	path('accounts/profile/',views.index,name='index'),
	path('customer_list/',views.customer_list,name='customer_list'),
	path('customer_list/(?P <id>[\W-]+)',views.cust_edit,name='cust_edit'),
	path('customer_list/cust_update',views.cust_update,name='cust_update'),
	path('customer_list/cust_edit_re',views.cust_edit_re,name='cust_edit_re'),
	path('Applications/(?P <id>[\W-]+)',views.edit_application,name='edit_application'),
	path('Applications/application_update',views.application_update,name='application_update')
]