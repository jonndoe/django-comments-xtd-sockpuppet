from sockpuppet.reflex import Reflex
# for debugging
from urllib.parse import urlparse

class RendersinglepostReflex(Reflex):
    def increment(self, step=1):
        self.count = int(self.element.dataset['count']) + step

    def render(self):
        print('render method of SinglePost Reflex invoked!!!')
        self.pageurl = self.element.dataset['pageurl']
        print('self.url is:', self.url)
        print('self.pageurl is:', self.pageurl)
        parsed_url = urlparse(self.url)
        current_view_path = str(self.pageurl)
        new_url = parsed_url.scheme + '://' + parsed_url.netloc + current_view_path + parsed_url.params + parsed_url.fragment
        print('new_url is: ', new_url)
        self.url = new_url

