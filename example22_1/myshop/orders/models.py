from django.db import models
from shop.models import Product



class Order(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.EmailField( blank= True)
    address = models.CharField(max_length=250)
    contact = models.CharField(max_length=11)
    note = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=10 , decimal_places=3 , null=True)
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return 'Order {}'.format(self.id)
    def get_total_cost(self):
        return sum( item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    def __str__(self):
        return '{}'.format(self.id)
    def get_cost(self):
        return self.price * self.quantity




