from django.views.generic.base import TemplateView
from django.views.generic import ListView
from blog.models import Post


class RenderallpostsView(ListView):
    model = Post
    template_name = 'renderallposts.html'
    paginate_by = 3
    context_object_name = 'posts'

'''
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        #context['posts'] = Post.objects.all()
        #print(context)

        if not context.get('stimulus_reflex'):
            print('NOT from reflex!!!')
            #context['posts_from_url'] = Post.objects.all()
            #return context

        elif context.get('stimulus_reflex'):
            print('YES from reflex!!!')
            return context
'''


'''
class RenderallpostsView(TemplateView):
    template_name = 'renderallposts.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['posts'] = Post.objects.all()

        if not context.get('stimulus_reflex'):
            print('NOT from reflex!!!')
            context['posts_from_url'] = Post.objects.all()
            return context
        else:
            print('YES from reflex!!!')
            return context
'''