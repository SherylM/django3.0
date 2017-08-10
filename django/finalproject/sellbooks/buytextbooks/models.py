from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Textbook(models.Model):
    """
        the class textbook creates textbook objects
        attributes: title
                    author
                    publisher
                    location
                    image
        methods: get_absolute_url
    """
    textbooktitle = models.CharField(max_length=250)
    textbookauthor = models.CharField(max_length=250)
    textbookpublisher = models.CharField(max_length=250)
    textbooklocation = models.CharField(max_length=400)
    textbookimage = models.FileField()

    def get_absolute_url(self):
        """
        this function gets the the pk of the newest book added and redirects
        it to books:detailtextbook
        """
        return reverse('books:detailtextbook', kwargs = {'pk' : self.pk})
    
    def __str__(self):
        """
        redefines the print function
        so that when you print the object,
        the actual string gets printed out and not something
        weird
        """
        return self.textbooktitle + ' - ' + self.textbookauthor

class Prepbook(models.Model):
    """
    the class Prepbook creates Prepbook objects
    attributes: title
                author
                publisher
                location
                image
    methods: get_absolute_url()
    """
    prepbooktitle = models.CharField(max_length=250)
    prepbookauthor = models.CharField(max_length=250)
    prepbookpublisher = models.CharField(max_length=250)
    prepbooklocation = models.CharField(max_length=400)
    prepbookimage = models.FileField()

    def get_absolute_url(self):
        """
        this function gets the the pk of the newest book added and redirects
        it to books:detailprepbook
        """
        return reverse('books:detailprepbook', kwargs = {'pk' : self.pk})

    def __str__(self):
        """
        redefines the print function
        so that when you print the object,
        the actual string gets printed out and not something
        weird
        """
        return self.prepbooktitle + ' - ' + self.prepbookauthor
    
