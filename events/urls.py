from django.urls import path
from .views import (
    EventListView,
    EventDetailView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
    RSVPEventView,
    DashboardView,   # নতুন যোগ
)

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),          
    path('dashboard/', DashboardView.as_view(), name='dashboard'), 
    path('create/', EventCreateView.as_view(), name='event_create'),
    path('<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('update/<int:pk>/', EventUpdateView.as_view(), name='event_update'),
    path('delete/<int:pk>/', EventDeleteView.as_view(), name='event_delete'),
    path('rsvp/<int:event_id>/', RSVPEventView.as_view(), name='event_rsvp'),
]
