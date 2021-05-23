from django.views.generic import ListView, TemplateView
from blog.models import Post


class HomePageView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        #context['posts'] = Post.objects.all()
        #print(context)
        print('HomePageView invoked!!!')
        return context
