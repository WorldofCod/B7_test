from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100, null = True)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    ispublished = models.BooleanField(default=False)
    is_deleted= models.BooleanField(default=0)  # adhi chi entry nasli tar defualt value  =0, 1 asla t deleted, 0 not deleted
    
    def __str__(self):
        return self.title
    class Meta:
        db_table = "book"
    
    def save(self,*args,**kwargs):
        print(self.__dict__)
        if self.id:
            print("it is an update")
        else:
            print("New book is created")
        super(Book,self).save(*args,**kwargs)


    def company():
        print("Hello")    