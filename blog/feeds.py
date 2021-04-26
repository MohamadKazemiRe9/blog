from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from .models import Post
from django.template.defaultfilters import truncatewords , safe


class LatestPostsFeed(Feed):
    title = 'My Blog'
    link = reverse_lazy('blog:post_list')
    description = "This is my post description"

    def items(self):
        return Post.published.all()[:5]
    
    def item_title(self,item):
        return item.title
    
    def item_description(self,item):
        return safe(truncatewords(item.body,30))

# {{ items.body|truncatewords:20 }}