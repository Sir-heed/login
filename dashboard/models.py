from django.db import models
from django.contrib.auth import settings
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class Post(models.Model):

    POST_STATUS = (
        ('draft', 'DRAFT'),
        ('published', 'PUBLISHED'),
    )


    CATEGORY = (
        ('sports', 'SPORTS'),
        ('politics', 'POLITICS'),
        ('entertainment', 'ENTERTAINMENT'),
        ('business', 'BUSINESS'),
        ('tech', 'TECH'),
        ('health', 'HEALTH'),
    )

    COUNTRIES = (
        ('AU','Australia'),
        ('NZ', 'New Zealand'),
        ('CN', 'Çhina'),
        ('IN', 'India'),
        ('ID', 'Indonesia'),
        ('PK', 'Pakistan'),
        ('BD', 'Bangladesh'),
        ('JP', 'Japan'),
        ('PH', 'Philippines'),
        ('VN', 'Vietnam'),
        ('IR', 'Iran'),
        ('TH', 'Thailand'),
        ('KR', 'South Korea'),
        ('AE', 'UAE'),
        ('NG', 'Nigeria'),
        ('ET', 'Ethopia'),
        ('EG', 'Egypt'),
        ('CG', 'Congo'),
        ('ZA', 'South Africa'),
        ('TZ', 'Tanzania'),
        ('KE', 'Kenya'),
        ('SD', 'Sudan'),
        ('DZ', 'Algeria'),
        ('UG', 'Uganda'),
        ('MA', 'Morocco'),
        ('MZ', 'Mozambique'),
        ('GH', 'Ghana'),
        ('AO', 'Angola'),
        ('CI', 'Ivory Coast'),
        ('RU', 'Russia'),
        ('DE', 'Germany'),
        ('TR', 'Turkey'),
        ('FR', 'France'),
        ('GB', 'United Kingdom'),
        ('IT', 'Italy'),
        ('ES', 'Spain'),
        ('UA', 'Ukraine'),
        ('PL', 'Poland'),
        ('RO', 'Romania'),
        ('NL', 'Netherlands'),
        ('BE', 'Belgium'),
        ('BR', 'Brazil'),
        ('CO', 'Colombia'),
        ('AR', 'Argentina'),
        ('PE', 'Peru'),
        ('VE', 'Venezuela'),
        ('US', 'United State'),
        ('MX', 'Mexico'),
        ('CA', 'Canada'),
        ('CU', 'Cuba'),
        ('HT', 'Haiti'),
    )
    


    #sources = models.TextField(blank=True)
    #named_entities = models.TextField(blank=True)
    #named_entities_type = models.TextField(blank=True)
    author = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField(blank=True)
    post_url = models.URLField(blank=True)
    image_url = models.URLField(blank=True)
    published_date = models.DateTimeField(blank=True)
    category = models.CharField(max_length=200, choices=CATEGORY, blank=True)
    country = models.CharField(max_length=200, choices=COUNTRIES, blank=True)
    summary = models.TextField(blank=True)
    

    class Meta:
        ordering = ('-published_date', )
        get_latest_by = "published_date"

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('dashboard:post_detail_edit',
                    args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Collection(models.Model):
    '''A collection is a selected number of sorted posts under a category that appears 
    on the feeds.'''

    posts = models.ManyToManyField(Post)
    title = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return str(self.title)
    

class Curator(models.Model):
    '''A curator is a user that collates a selected number of posts into a collection, 
    categorize them and adds them to feeds.'''

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    collections = models.ForeignKey(Collection, on_delete=models.CASCADE)
    #photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    

# Every curator has a collection. And every collection has a set of posts.


# every curator has many post.
# every collection.
# ever collec

    