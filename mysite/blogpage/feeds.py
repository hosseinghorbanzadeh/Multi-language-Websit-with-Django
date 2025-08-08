from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogpage.models import Post
from django.utils import timezone

class LatestEntriesFeed(Feed):

    title = "Blog News Posts"
    link = "/rss/feed"
    description = "My Blog"

    def items(self):
        now=timezone.now()
        return Post.objects.filter(published_date__lte=now,status=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[0:100]

