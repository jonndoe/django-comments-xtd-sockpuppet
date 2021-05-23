from sockpuppet.reflex import Reflex
from blog.models import Post

class RenderallpostsReflex(Reflex):
    def increment(self, step=1):
        print('increment method of Reflex invoked!!!')
        #self.count = int(self.element.dataset['count']) + step

    def render(self):
        print('render method of Reflex invoked!!!')
        posts = Post.objects.all()
        self.posts = posts