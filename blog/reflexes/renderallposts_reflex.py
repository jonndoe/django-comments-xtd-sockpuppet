from sockpuppet.reflex import Reflex
from blog.models import Post

# for debugging
from urllib.parse import urlparse
from django.urls import resolve

class RenderallpostsReflex(Reflex):
    def increment(self, step=1):
        print('increment method of Reflex invoked!!!')
        #self.count = int(self.element.dataset['count']) + step

    def render(self):
        print('render method of Reflex invoked!!!')

        # here we need to implement the logic to create the self.url
        # based on the name of the reflex, and also knowledge of the
        # line in urls.py which reffers to the corresponding view.
        # i.e. whatever reflex.url is now, it should be 'http://localhost:8000/blog/renderallposts/'
        # i.e

        #print('self.url is: ', self.url)
        parsed_url = urlparse(self.url)
        #print('parsed url is: ', parsed_url)
        #print('parsed url path is: ', parsed_url.path)

        # hardcoded for now, but we should get this path programmatically
        current_view_path = '/blog/renderallposts/'

        if parsed_url.path != '/blog/renderallposts/':
            #print('parsed_url.path is wrong!!!!! :', parsed_url.path)
            #parsed_url.path = '/blog/renderallposts/'
            # todo: create new self.url taking into account parsed_url.path
            if parsed_url.query != '':
                query = '?'
            else:
                query = ''
            new_url = parsed_url.scheme + '://' + parsed_url.netloc + current_view_path + parsed_url.params + query + parsed_url.query + parsed_url.fragment
            #print('new_url is : ', new_url)
            self.url = new_url
            parsed_url = urlparse(self.url)

        #resolved = resolve(parsed_url.path)
        #print('resolved url is: ', resolved)

        #print(self)
        #view = resolved.func.view_class()
        #print('view is :', view)
        #view.request = self.request
        #print('view request is :', view.request)

        # Here we will not take any posts objects since
        # ListView will do it automatically for us. But we can if we need to,
        # for example:
        #posts = Post.objects.all()
        #self.posts = posts