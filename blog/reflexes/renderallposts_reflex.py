from sockpuppet.reflex import Reflex


# for debugging
from urllib.parse import urlparse


# As far as I get the idea, One reflex should be connected with One View.
class RenderallpostsReflex(Reflex):

    def renderfrompaginator(self):
        print('renderfrompaginator method of Reflex invoked!!!')
        self.pagetogo = self.element.dataset['pagetogo']

        parsed_url = urlparse(self.url)
        current_view_path = '/blog/renderallposts/'
        if parsed_url.path != '/blog/renderallposts/':
            new_url = parsed_url.scheme + '://' + parsed_url.netloc + current_view_path + parsed_url.params + self.pagetogo + parsed_url.fragment
            self.url = new_url

    def render(self):
        print('render method of Reflex invoked!!!')

        # here we need to implement the logic to create the self.url
        # based on the name of the reflex, and also knowledge of the
        # line in urls.py which reffers to the corresponding view.
        # i.e. whatever reflex.url is now, it should be 'http://localhost:8000/blog/renderallposts/'

        parsed_url = urlparse(self.url)

        # This method has to trigger the view which can be riched with the following path:
        # hardcoded for now, but we should get this path programmatically
        current_view_path = '/blog/renderallposts/'

        if parsed_url.path != '/blog/renderallposts/':
            # todo: create new self.url taking into account parsed_url.path
            if parsed_url.query != '':
                query = '?'
            else:
                query = ''
            new_url = parsed_url.scheme + '://' + parsed_url.netloc + current_view_path + parsed_url.params + query + parsed_url.query + parsed_url.fragment
            self.url = new_url

        # Here we will not take any posts objects from db since
        # ListView will do it automatically for us. But we can if we need to,
        # for example:
        # from blog.models import Post
        # posts = Post.objects.all()
        # self.posts = posts