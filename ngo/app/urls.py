from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('our-work/', views.our_work, name='our_work'),
    path('projects/', views.projects, name='projects'),
    path('media/', views.media, name='media'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('blogs/', views.blogs, name='blogs'),
    path('contact/', views.contact, name='contact'),
    path('donate/', views.donate, name='donate'),
    path('signin/',views.signin, name='signin'),
    path('signup/',views.signup, name='signup'),
    path('logout/', views.userlogout, name='userlogout'),
    path('request_password-reset/', views.request_password_reset, name='request_password_reset'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/employee/', views.employee_dashboard, name='employee_dashboard'),
    path('dashboard/volunteer/', views.volunteer_dashboard, name='volunteer_dashboard'),
    path('task/', views.task, name='task'),
    path('access-denied/', views.access_denied, name='access_denied'),
    path('add-task/', views.add_task, name='add_task'),
    path('add-blog/', views.add_blog, name='add_blog'),
    path('add-project/', views.add_project, name='add_project'),
    path('add-media/', views.add_media, name='add_media'),
    path('add-ourwork/', views.add_ourwork, name='add_ourwork'),
    path('payment-success/', views.payment_success, name='payment_success'),

]
