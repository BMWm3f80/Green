from django.contrib import admin
from django.urls import path
import Garage.views as globalviews
from django.contrib.auth import views as authview

app_name = 'authapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', globalviews.home, name='home'),
    path('login/', globalviews.signin, name='login'),
    path('register/', globalviews.signup, name='register'),
    path('logout/', authview.LogoutView.as_view(template_name='logout.html'), name='logout')

]
