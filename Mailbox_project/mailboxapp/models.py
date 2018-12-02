from django.db import models

# Create your models here.





class Person(models.Model):
    name = models.CharField(max_length=64, blank=False)
    surname  = models.CharField(max_length=250, blank=False)
    description = models.TextField()

    def __str__(self):
        return f"[Imię = {self.name},Nazwisko = {self.surname}, Opis = {self.description}]"


class Address(models.Model):
    city = models.CharField(max_length=64, blank=False)
    street = models.CharField(max_length=128, blank=False)
    house_number = models.CharField(max_length=5, blank=False)
    flat_number = models.CharField(max_length=7,blank=True)

    person_address = models.ForeignKey(Person, on_delete=models.CASCADE)





class Phone(models.Model):

    PHONES = (
        (1,"domowy"),
        (2,"służbowy"),
        (3,"prywatny"),
    )

    phone_number = models.IntegerField()
    phone_type = models.SmallIntegerField(choices=PHONES)

    person_phone = models.ForeignKey(Person, on_delete=models.CASCADE)


class Email(models.Model):


    TYPES = (
        (1,"prywatny"),
        (2,"służbowy"),
    )

    email_address = models.EmailField(max_length=254)
    email_type = models.SmallIntegerField(choices=TYPES)

    person_email = models.ForeignKey(Person, on_delete=models.CASCADE)


class Groups(models.Model):
    group_name = models.CharField(max_length=250, null=True)
    group_person = models.ManyToManyField(Person)


