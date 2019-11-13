from django.http import HttpResponse
from .forms import PizzaForm
from django.views.generic import ListView, FormView
from .models import Pizza


class PizzaView(ListView):
    model = Pizza
    template_name = 'base.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Pizza.objects.all()
        return context


class PizzaFormView(FormView):
    template_name = 'form_pizza_add.html'
    form_class = PizzaForm
    success_url = '/'

    def form_valid(self, form):
        form.create_objects()
        return super().form_valid(form)

    def form_invalid(self, form):
        print("ERROR")
        return super().form_invalid(form)
