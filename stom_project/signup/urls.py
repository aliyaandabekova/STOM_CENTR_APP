from django.urls import path
from .views import *

urlpatterns = [
    path('',DayViewSet.as_view({
        'get':'list',
        'post':'create'
    }),name='day'),
    path('day/<int:day_id>/',DayViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    }),name='day_detail'),
    path('work_days/',DoctorDayView.as_view({
        'get':'list'
    })),
    path('work_days/<int:day_id>/',DoctorDayView.as_view({
        'post':'create'
    })),
    path('modify_wd/<int:doctor_day_id>/',DoctorDayView.as_view({
        'put':'update',
        'get':'retrieve'
    })),
    path('order/',OrderViewSet.as_view({
        'post':'create',
        'get':'list'
    }),name='order'),
    path('order/<int:order_id>/',OrderViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    }),name='order_detail'),
    path('doctors/',DoctorViewSet.as_view({
        'get':'list'
    })),
    path('doctor/<str:d_username>/',DoctorViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    }))
]
