from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),   
	path('about.html', views.about, name='about'), 
	path('service.html', views.service, name='service'),
	path('pricing.html', views.pricing, name='pricing'),
	path('blog.html', views.blog, name='blog'),
	path('blog-details.html', views.blogDetails, name='blogDetails'),
	path('contact.html', views.contact, name="contact"),
]
