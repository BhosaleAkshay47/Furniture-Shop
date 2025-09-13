from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('buynow/',views.buy_now, name='buynow'),
    path('chairs/', views.chairs, name='chairs'),
    path('product_details<int:pk>/',views.ProductDetailView.as_view(), name='product-detail'),
    path('chair/',views.chair, name='chair'),
    path('chair/<slug:data>', views.chair, name='chair_data'),
    path('sofa/', views.sofa, name='sofa'),
    path('sofa/<slug:data>', views.sofa, name='sofa_data'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cart/', views.cart_view, name='cart'),
    path('profile/', views.Profile_view, name='profile'),
    path('address/', views.address, name='address'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

