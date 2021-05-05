from django.db import models

# Create your models here.

#we use this model for defining the category and setting for pizza like we create size as one feild and regular&sqare for its value
class pizzaDropdown(models.Model):
    sno = models.AutoField(db_column='sno',primary_key=True)
    pid = models.IntegerField(db_column='pid')
    feild= models.CharField(db_column='feild', max_length=500)
    value= models.CharField(db_column='value', max_length=550)
    is_delete=models.IntegerField(db_column='is_delete',default=0)# 0 for not deleted 1 for deleted
    is_edit= models.IntegerField(db_column='is_edit',default=0)#same as above
    #using this model we can crete as much as parameter and values for creating & editing pizza
    class Meta:
        db_table='Pizzadropdown'
        managed=True

class pizzaCreated(models.Model):
    type=models.ForeignKey(pizzaDropdown,related_name='pizzatype',on_delete=models.SET_NULL,null=True)
    size= models.ForeignKey(pizzaDropdown,related_name='pizzasize',on_delete=models.SET_NULL,null=True)
    toppings= models.ForeignKey(pizzaDropdown,related_name='pizzatoppings',on_delete=models.SET_NULL,null=True)
    is_edit= models.IntegerField(db_column='is_edit',default=0)# 0 for not deleted 1 for deleted
    class Meta:
        db_table='Pizzacreated'
        managed=True