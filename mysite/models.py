from django.db import models

# Create your models here.
class Maker(models.Model):
	name = models.CharField(max_length=10)
	country = models.CharField(max_length=10)
	def __str__(self):
		return self.name
	
class PModel(models.Model):
	maker = models.ForeignKey(Maker,on_delete=models.CASCADE)
	name = models.CharField(max_length=20)
	url = models.URLField(default='http://www.7k7k.com')
	def __str__(self):
		return self.name
class Product(models.Model):
	pmodel = models.ForeignKey(PModel,on_delete=models.CASCADE,
verbose_name='型号')
	nickname = models.CharField(max_length=15,default='超值二手机',
verbose_name='摘要')
	description = models.TextField(default='暂无说明')
	year = models.PositiveIntegerField(default=2016,verbose_name='出厂年份')
	price = models.PositiveIntegerField(default=0,verbose_name='价格')
	def __str__(self):
		return self.nickname
class PPhoto(models.Model):
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	description = models.CharField(max_length=20,default='产品照片')
	url = models.URLField(default='http://www.7k7k.com')
	def __str__(self):
		return self.description
	