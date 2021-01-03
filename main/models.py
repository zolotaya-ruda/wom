from django.db import models
from django.contrib.auth.models import User

class new_sg(models.Model):
	song = models.CharField(max_length = 50,verbose_name = "Название трека:")
	opis = models.ForeignKey('opisan', on_delete = models.DO_NOTHING, default='')
	text = models.TextField(verbose_name='Описание к песни, Ваши соцести и прочее...', default='')
	artist = models.ForeignKey(User,on_delete = models.DO_NOTHING,verbose_name = 'Артист',null = False,blank = False,default = '',related_name = 'author')
	published = models.DateTimeField(auto_now_add = True,db_index = True,verbose_name = 'Дата публикации')
	add_mus = models.FileField(upload_to = 'arch/for_main',verbose_name = 'Файл', null = False,blank = False,default = '')
	genre = models.ForeignKey('rub', null = False,on_delete = models.PROTECT,verbose_name = 'Жанр',default = '')
	views = models.IntegerField(default = 0)
	potr = models.ManyToManyField(User,through = 'UserSongRalation',related_name = 'potr')
	
	def __str__(self):
		return self.song

	class Meta(object):
		ordering = ['published']
		

class rub(models.Model):
	name = models.CharField(max_length = 20,db_index = True,)

	def __str__(self):
		return self.name
# Create your models here.
class UserSongRalation(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE,default = '')
	track = models.ForeignKey(new_sg,on_delete = models.CASCADE,default = '')
	like = models.BooleanField(default = False,null = True)
	media = models.BooleanField(default = False,null = True)
class opisan(models.Model):
	img = models.ImageField(upload_to = 'img',default = '',verbose_name = 'Изображение для профиля:',)
	artist = models.ForeignKey(User,on_delete = models.CASCADE,default = '')
	text = models.TextField(verbose_name = 'О себе:')
	city = models.ForeignKey('city', null = False,on_delete = models.DO_NOTHING,verbose_name = 'Город',default = '')
	boo = models.BooleanField(default = False)

class city(models.Model):
	city = models.CharField(max_length = 50,db_index = True)
	def __str__(self):
		return self.city
			

		