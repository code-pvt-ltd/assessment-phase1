from django.urls import path
from . import views
 
app_name="file"

urlpatterns = [


    path("", views.indexpage, name="indexpage"),
   # path('student_login/', views.student_login, name="student_login"),
    path("userlogin/",views.userlogin,name="userlogin"),
    path("schoolreg/", views.schoolreg, name="schoolreg"),
    path('Package1/', views.Package1, name='Package1'),
    path('Package2/', views.Package2, name='Package2'),
    path('Package3/', views.Package3, name='Package3'),
    path('Package4/', views.Package4, name='Package4'),
    path('school_details_atl_incharge/', views.school_details_atl_incharge, name='school_details_atl_incharge'),
    path('schoolatlinchargeweb/', views.schoolatlinchargeweb, name='schoolatlinchargeweb'),
    path('AESWeb/', views.AESWeb, name='AESWeb'),
    path('TNFA/', views.TNFA, name='TNFA'),
    path("atl_login/", views.atl_login, name="atl_login"),
    path("venregweb/", views.venregweb, name="venregweb"),
    path("mentorofchangeweb/", views.mentorofchangeweb, name="mentorofchangeweb"),
    path('question/', views.question, name="question"),
     path('data/',views.data,name="data"),
    
    
]