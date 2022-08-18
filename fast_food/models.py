from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class Client(models.Model):
    name = models.CharField(max_length=50)
    card_number = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return  f'{self.name} {self.card_number}'


class Worker(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} на позиции {self.position}'


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    extra_price = models.IntegerField()

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)
    start_price = models.IntegerField()
    ingredient = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name


class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    order_date_time = models.DateTimeField()

    def __str__(self):
        return self.food
