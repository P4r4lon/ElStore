"""mySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='home'),
    path('clients', login_required(views.clients), name='clients'),
    path('cl_create', views.ClCreate, name='cl_create'),
    path('clients/<int:pk>', views.ClDetailView.as_view(), name='cl_view'),
    path('clients/<int:pk>/delete', views.ClDeleteView.as_view(), name='cl_delete'),
    path('clients/<int:pk>/update', views.ClUpdateView.as_view(), name='cl_update'),

    path('clients/<int:client_id>/comment/', views.comment_new, name='comment_new'),
    path('comment/<int:client_id>/edit/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('comment/<int:client_id>/remove/<int:comment_id>/', views.comment_remove, name='comment_remove'),


    path('suppliers', views.suppliers, name='suppliers'),
    path('sup_create', views.SupCreate, name='sup_create'),
    path('suppliers/<int:pk>', views.SupDetailView.as_view(), name='sup_view'),
    path('suppliers/<int:pk>/delete', views.SupDeleteView.as_view(), name='sup_delete'),
    path('suppliers/<int:pk>/update', views.SupUpdateView.as_view(), name='sup_update'),

    path('orders_search/<slug:filter>', login_required(views.orders), name='orders'),
    path('ord_create', views.OrdCreate, name='ord_create'),
    path('orders/<int:pk>', views.OrdDetailView.as_view(), name='ord_view'),
    path('orders/<int:pk>/delete', views.OrdDeleteView.as_view(), name='ord_delete'),
    path('orders/<int:pk>/update', views.OrdUpdateView.as_view(), name='ord_update'),


    path('managers', views.managers, name='managers'),
    path('man_create', views.ManCreate, name='man_create'),
    path('managers/<int:pk>', views.ManDetailView.as_view(), name='man_view'),
    path('managers/<int:pk>/delete', views.ManDeleteView.as_view(), name='man_delete'),
    path('managers/<int:pk>/update', views.ManUpdateView.as_view(), name='man_update'),

    path('documents', views.documents, name='documents')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
