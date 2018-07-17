from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginuser, name='login'),
    path('logoutuser/', views.logoutuser,name='logoutuser'),
    path('', views.index, name='home'),
    path('aboutus/', views.aboutus, name='about-us'),
    path('faq/', views.faq, name='faq'),
    path('terms-and-conditions', views.terms, name='terms'),
    path('privacy-policy', views.privacy, name='privacy'),
    path('signup', views.signup, name='signup'),
    path('become-a-tutor', views.becometutor, name='become-a-tutor'),
    path('pricing', views.pricing, name='pricing'),
    path('Blogs', views.Blogs, name='Blogs'),
    path('blog-detail/<int:id>' , views.blogid , name='blogid'),
    path('tutor', views.tutor, name='tutor'),
    path('tutorprofile/<int:id>', views.tutorprofile, name='tutorprofile'),
    path('studenthistory/', views.studenthistory, name='studenthistory'),
    path('admin/admin/', admin.site.urls),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('addblog', views.add_blog, name='addblog'),
    path('tutorformadmin', views.tutorformadmin, name='tutorformadmin')
]