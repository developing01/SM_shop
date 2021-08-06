from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Product, Category, Rating
from .forms import RatingForm


class HeadViews(ListView):

    model = Category
    queryset = Category.objects.all()
    template_name = 'shop/first_page.html'



class ByCategoryView(View):

    def get(self, request, category_id):
        products = Product.objects.filter(category=category_id)
        categories = Category.objects.all()
        current_category = Category.objects.get(pk=category_id)
        context = {'categories': categories, 'products': products, 'current_category': current_category}
        return render(request, 'shop/by_category.html', context)


class ProductDetailView(DetailView):

    model = Product
    slug_field = "url"
    template_name = 'shop/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['star_form'] = RatingForm()
        return context


class AddStarRating(View):

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                product_id=int(request.POST.get("product")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)


class Search(ListView):

    def get_queryset(self):
        return Product.objects.filter(product_name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        return context
