from django.views.generic import DateDetailView
from blog.models import Post

class RendersinglepostView(DateDetailView):
    template_name = 'rendersinglepost.html'
    date_field = "publish"
    model = Post


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        #context['count'] = 0
        print('RendersinglePostView entered!!!!!')
        return context
