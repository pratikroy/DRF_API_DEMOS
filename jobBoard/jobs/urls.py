from django.urls import path

from jobs.views import JobListCreateApiView, JobDetailApiView

urlpatterns = [
    path('jobs/', JobListCreateApiView.as_view(), name='job-list'),
    path('jobs/<int:pk>/', JobDetailApiView.as_view(), name='job-detail')
]
