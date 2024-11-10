from django.contrib.sitemaps import Sitemap
from .models import Post
from taggit.models import Tag, TaggedItem
from django.contrib.contenttypes.models import ContentType

class TagSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return Post.tags.all()
    
    def location(self, obj):
        return f'/blog/tag/{obj.slug}/'
    

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()
    
    def lastmod(self, obj):
        return obj.updated