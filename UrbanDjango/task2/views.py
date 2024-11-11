from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
# Create your views here.
# class index(TemplateView):
#     template_name = 'class_template.html'

def function_base_view(request):
    return render(request,'second_task/fubc_template.html')


class ClassBasedView(View):
    def get(self,request):
        return render(request, 'second_task/class_template.html')