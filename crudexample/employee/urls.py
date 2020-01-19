from django.contrib import admin  
from django.urls import path,include
from employee import views  
from rest_framework import routers


router = routers.DefaultRouter()
router.register('api/employee',views.EmployeeView)

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('emp', views.emp,name='emp'),  
    path('show',views.show,name='show'),  
    path('edit/<int:id>', views.edit,name='edit'),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
    path('',include(router.urls)),
]  