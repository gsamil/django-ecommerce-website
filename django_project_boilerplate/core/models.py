from django.conf import settings
from django.db import models


CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport Wear'),
    ('OW', 'Outwear')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)


class Item(models.Model):
    """ 
    Item will be displayed in a list of items that you can purchase.
    As soon as you add it to the cart, it becomes an OrderItem.
    """
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)

    def ___str___(self):
        return self.title


class OrderItem(models.Model):
    """
    OrderItem is just a way of linking between Order and Item.
    """
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def ___str___(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)  # So that we can add OrderItems into the Order
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def ___str___(self):
        return self.user.username