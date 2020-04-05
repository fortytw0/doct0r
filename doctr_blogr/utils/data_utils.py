import django
django.setup()

from rango.models import Category , Page , Author
from django.utils.text import slugify

def reduce_slug_to_50_char(old_slug) :

    if len(old_slug) < 50 : 
        return old_slug
    
    new_slug = old_slug[:50]

    for cnt , c in enumerate(reversed(new_slug)) : 
        if c == "-" : 
            return new_slug[:-cnt-1]

    

# all_pages = Page.objects.all()

# for cnt , page in enumerate(all_pages) : 

#     old_slug = page.slug
#     page.slug = reduce_slug_to_50_char(old_slug)
#     page.save()



all_categories = Category.objects.all()

for cnt , category in enumerate(all_categories) : 

    category.slug = slugify(category.name)
    category.save() 

all_authors = Author.objects.all()

for cnt , author in enumerate(all_authors) : 

    author.slug = slugify(author.author_name)
    author.save()