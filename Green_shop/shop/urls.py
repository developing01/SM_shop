from django.urls import path

from .views import HeadViews, ByCategoryView, ProductDetailView, AddStarRating, Search

urlpatterns = [
    path('', HeadViews.as_view(), name='head'),
    path('<int:category_id>/', ByCategoryView.as_view(), name='by_category'),
    path('search/', Search.as_view(), name='search'),
    path('add-rating/', AddStarRating.as_view(), name='add_rating'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]
