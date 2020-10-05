from django.db import models

from django.contrib.auth.models import User

from django.db import models



class Field(models.Model):
    ID1 = models.AutoField(primary_key=True)
    subject= models.CharField(default=True,max_length=200)

    def __str__(self):
        return self.subject


class Difficulty_level(models.Model):
    ID = models.AutoField(primary_key=True)
    diff_levels= models.CharField(default=True,max_length=200)
    marks= models.IntegerField(default=True)
    def __str__(self):
        return str(self.marks)



class Questionaries(models.Model):
     field_id = models.ForeignKey(Field,default=True,on_delete=models.CASCADE)
     diff_id =  models.ForeignKey(Difficulty_level,default=True,on_delete=models.CASCADE)
     questions= models.CharField(default=True,max_length=200)
     op_1= models.CharField(default=True,max_length=100)
     op_2= models.CharField(default=True,max_length=100)
     op_3= models.CharField(default=True,max_length=100)
     op_4= models.CharField(default=True,max_length=100)
     answer= models.CharField(default=True,max_length=100)

     def __str__(self):
        return self.questions


class User_Marks(models.Model):
    users = models.ForeignKey(User,default=True,on_delete=models.CASCADE)
    ENGLISH = models.IntegerField(default='0')
    COMPUTER = models.IntegerField(default='0')
    PHYSICS = models.IntegerField(default='0')
    BIOLOGY = models.IntegerField(default='0')
    CHEMISTRY = models.IntegerField(default='0')
    ACCOUNTING = models.IntegerField(default='0')
    BUSINESS_ADMINISTRATION = models.IntegerField(default='0')
    


    def __str__(self):
        return (str(self.users))
      





