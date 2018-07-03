from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    country = models.CharField(max_length=30,null=True)  #这个字段是后来加上的，所以必须要设置允许为空（null=True），否则这个新增的字段添加不成功

    def __str__(self):
        return 'User表中的：id=%s,name=%s,age=%s,country=%s' % (
            self.id, self.name, self.age,self.country)


class Ftest(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    note = models.TextField()
    gender = models.BooleanField(default=True)
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)



#学院信息表  一
class Department(models.Model):
    d_id = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=30)
    def __str__(self):
        return 'Department: d_id=%s,d_name=%s'%(
            self.d_id,self.d_name
        )
#学生信息表  多
class Student(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=30)
    department = models.ForeignKey('Department')    #这句就是形成一对多关系
    course = models.ManyToManyField('Course')       #这句他会自动生成多对多的第三张表
    def __str__(self):
        return 'Student<s_id=%s,s_name=%s>'%(
            self.s_id,self.s_name
        )

#课程信息表
class Course(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=30)
    def __str__(self):
        return 'Course<c_id=%s,c_name=%s>'%(
            self.c_id,self.c_name
        )
#学生详细信息表
class Stu_detail(models.Model):
    s_id = models.OneToOneField('Student')  #这句形成了一对一
    age = models.IntegerField()
    gender = models.BooleanField(default=1)
    country = models.CharField(max_length=30,null=True)
    def __str__(self):
        return 'Stu_detail<s_id=%s,age=%s,gender=%s,country=%s>'%(
            self.s_id,self.age,self.gender,self.country
        )



########小案例#########
class BlogModel(models.Model):
    title = models.CharField(max_length=100,blank=True)
    content = models.TextField()

#####用户注册##########
class UserModel(models.Model):
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.username