import django
django.setup()


from faker import Faker
from blog.models import Tag , Article
import random

from django.utils.text import slugify

num_of_tags = 10
min_articles_per_tag = 10
max_articles_per_tag = 100


fake = Faker()

def create_tag(tag_details) :

    new_tag = Tag(name=tag_details["name"] , 
                  slug = tag_details["slug"],
                  description = tag_details["description"])
    new_tag.save()

def create_author(author_details) : 

    new_author = Tag(author_name=author_details["author_name"] , 
                        author_username=author_details["author_username"] , 
                        author_facebook=author_details["author_facebook"] , 
                        author_website=author_details["author_webiste"])

    new_author.save()

def create_article(article_details) : 

    new_article = Article( 
                    title=article_details["title"] , 
                    slug=article_details["url"] , 
                    content=article_details["content"])

    new_article.save()
    for tag in article_details["tags"] : 
        new_article.tags.add(tag)


def generate_fake_author_data() :

    author_details = {}

    for _ in range(num_of_authors) : 

        author_profile = fake.simple_profile()

        author_details["author_name"] = author_profile["name"]
        author_details["author_username"] = author_profile["username"]
        author_details["author_facebook"] = fake.domain_name()
        author_details["author_webiste"] = fake.domain_name()

        create_author(author_details)

def generate_fake_tag_data() : 

    tag_details = {}

    for _ in range(num_of_tags) : 

        tag_details["name"] = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        tag_details["slug"] = slugify(tag_details["name"])
        tag_details["description"] = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)

        create_tag(tag_details)

def generate_fake_articles_data() : 

       
    articles_for_random_tag = random.randint(min_articles_per_tag , max_articles_per_tag)
    article_details = {}

    for _ in range(articles_for_random_tag) : 

        random_tags = random.sample(list(Tag.objects.all()) , random.randint(1 , 5))
       
        article_details["tags"] = random_tags
        article_details["title"] = fake.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None)
        article_details["url"] = slugify(article_details["title"])
        print(article_details["url"])
        article_details["content"] = fake.text(max_nb_chars=5000)

        create_article(article_details)



generate_fake_tag_data()


generate_fake_articles_data()

        







# generate_fake_author_data()
# generate_fake_tag_data()

# print(type(tag.objects.all()))

# random_tag = random.sample(list(tag.objects.all()) , 1)[0]

# print(type(random_tag))

