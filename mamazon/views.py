from django.views.generic import TemplateView, ListView
from .models import Product


class Home(TemplateView):
    template_name = 'mamazon/home.html'

class ProductListView(ListView):
    model = Product
    template_name = 'mamazon/list.html'

    def get_queryset(self):
        queryser = Product.objects.all()
        if 'query' in self.request.GET:
            qs = self.request.GET['query']
            queryset =queryser.filter(name_contains=qs)

