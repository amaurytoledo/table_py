from django.shortcuts import render
from django.views.generic import TemplateView

class MyTableListView(TemplateView):
    template_name = "table_py/mytable_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mytable_list'] = MyTable.objects.all()
        return context
