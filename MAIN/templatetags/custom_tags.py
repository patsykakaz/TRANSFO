from __future__ import unicode_literals

from mezzanine import template
from mezzanine.blog.models import BlogPost, BlogCategory
register = template.Library()

@register.filter(name='BlogCatFromBlog')
def BlogCategories_from_Blog(blog_id, *args):
    blog_id = int(blog_id)
    post = BlogPost.objects.get(id=blog_id)
    return post.categories.all()
