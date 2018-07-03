from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .form import AddForm,RegisterForm,LoginForm
from .models import User,Ftest,Department,Stu_detail,Student,Course,BlogModel,UserModel

def add_user(request):
    # 方法一：
    # tizi = User(name='tizi',age=18)
    # tizi.save()
    # 方法二：
    # xm = User()
    # xm.name = 'xiaoming'
    # xm.age = 19
    # xm.save()
    # 方法三：
    # User.objects.create(name='xiaohong',age=20,)
    # 方法四：
    # User.objects.get_or_create(name='xiaohua',age=21)
    return HttpResponse('插入数据成功！！！')


def search_user(request):
    # 查询所有记录对象
    # rs = User.objects.all()
    # 查询一个记录对象
    # rs = User.objects.get(id=1)
    # 获取满足条件的对象
    rs = User.objects.filter(name='xiaoming')
    print(rs)
    return HttpResponse('查询数据成功！！！')


def update_user(request):
    #方法一
    # rs = User.objects.get(name='xiaoming')
    # rs.name = 'Xiaoming'
    # rs.save()

    #方法二
    # User.objects.filter(name='Xiaoming').update(name='XM')

    #方法三
    User.objects.all().update(country='changsha')
    # 这里的country需要再models.py文件中的User类中新增的一个字段
    return HttpResponse('更新数据成功！！！')





def delete_user(request):
    User.objects.get(id=4).delete()
    return HttpResponse('删除数据成功！！！')







#常用查询
def find_Ftest(request):
    # 获取所有记录：
    rs = User.objects.all()
    print(rs)
    #取具体的字段值
    # >>> s2 = Student.objects.all()
    # >>> s2
    #     <QuerySet[ < Student: Student < s_id = 1, s_name = xiaoming >>, < Student: Student < s_id = 2, s_name = xiaohong >>] >
    # >>> s2[1].s_name
    #     'xiaohong'
    # 获取第一条数据：
    # rs = User.objects.first()
    # 获取最后一条数据：
    # rs = User.objects.last()
    # 根据参数提供的条件获取过滤后的记录：
    # rs = User.objects.filter(name='xiaoming')
    # 注意：filter(**kwargs)
    # 方法：根据参数提供的提取条件，获取一个过滤后的QuerySet。
    # 排除name等于xiaoming的记录：
    # rs = User.objects.exclude(name='xiaoming')
    # 获取一个记录对象：
    # rs = User.objects.get(name='xiaoming')
    # 注意：get返回的对象具有唯一性质，如果符合条件的对象有多个，则get报错！
    #通过get字段取值
    # >>> r1 = Student.objects.get(s_name='xiaoming')
    # >>> r1
    #     < Student: Student < s_id = 1, s_name = xiaoming >>
    # >>> r1.s_name
    #     'xiaoming'
    # 对结果排序order_by：
    # rs = User.objects.order_by('age')
    # 多项排序：
    # rs = User.objects.order_by('age', 'id')
    # 逆向排序：
    # rs = User.objects.order_by('-age')
    # 将返回来的QuerySet中的Model转换为字典
    # rs = User.objects.all().values()
    # 获取当前查询到的数据的总数：
    # rs = User.objects.count()
    #
    # # 查询对象的条件
    # 查找对象的条件的意思是传给以上方法的一些参数。相当于是SQL语句中的where语句后面的条件，语法为字段名__规则，以下将对这些规则进行说明：
    # exact
    # 相当于等于号：
    # rs = User.objects.filter(name__exact='xiaoming')
    # iexact：跟exact，只是忽略大小写的匹配。
    # contains
    # 包含：
    # rs = User.objects.filter(name__contains='xiao')
    # icontains
    # 跟contains，唯一不同是忽略大小写。
    # startwith
    # 以什么开始：
    # rs = User.objects.filter(name__startswith='xiao')
    # istartswith：同startswith，忽略大小写。
    # endswith：同startswith，以什么结尾。
    # iendswith：同istartswith，以什么结尾，忽略大小写。
    # in 成员所属：
    # rs = User.objects.filter(age__in=[18, 19, 20])
    # gt
    # 大于：
    # rs = User.objects.filter(age__gt=20)
    # gte
    # 大于等于：
    # rs = User.objects.filter(age__gte=20)
    # lt
    # 小于：
    # rs = User.objects.filter(age__lt=20)
    # lte
    # 小于等于：
    # rs = User.objects.filter(age__lte=20)
    # range
    # 区间：
    # rs = User.objects.filter(age__range=(18, 20))
    # isnull
    # 判断是否为空：
    # rs = User.objects.filter(country__isnull=True)
    # 切片：
    # rs = User.objects.all()[:2]
    # 注意: 不能使用负数作为切片。
    return render(request, 'blog/find.html',
                      context={'rs': rs
                               }
                      )


####################关系表中的数据库操作#################

def add_info(request):
    # d1 = Department(d_name='CC')
    # d1.save()
    # # 一对多关系加内容
    # s1 = Student(s_name='xiaoming')
    # s1.department = d1
    # s1.save()
    # # 多对多关系添加内容
    # c1 = Course(c_name='python')
    # s1 = Student.objects.first()
    # c1.save()
    # s1.course.add(c1)    #中间表中添加数据
    return HttpResponse('添加数据成功')


def search_info(request):
    # rs = Student.objects.all()
    # print(rs)

    # 一对多的查询
    rs1 = Student.objects.all()[0]
    print(rs1.department)
    # 反向查询
    rs2 = Department.objects.get(d_id=1)
    print(rs2.student_set.all())
    # # 多对多的正向查询
    rs3 = Student.objects.all()[0]
    print(rs3.course.all())
    # # 多对多反向查询
    cs = Course.objects.first()
    print(cs.student_set.all())

    return HttpResponse('查询数据成功')



########小案例########


def blog_index(request):
    return  render(request,"blog/demo_index.html")

def blog_add(requset):
    if requset.method == "GET":
        return render(requset,"blog/demo_add.html")
    elif requset.method == "POST":
        yy = requset.POST.get("title")
        xx = requset.POST.get("content")
        blog = BlogModel(title=yy,content=xx)
        blog.save()
        return HttpResponse("获取数据")
    else:
        return  HttpResponse("这是不能处理的操作")

def blog_list(request):
    blog = BlogModel.objects.all()
    return render(request,"blog/demo_list.html",
                  context={"blogs":blog})


def blog_detail(request,blog_id):
    blog = BlogModel.objects.get(id=blog_id)
    return  render(request,"blog/demo_detail.html",
                   context={"blog":blog})


def blog_delete(request,blog_id):
    blog = BlogModel.objects.get(id = blog_id)
    if blog:
        blog.delete()
        return redirect(reverse("blog_list"))
    else:
        return HttpResponse("没有这个博客")

def blog_edit(request,blog_id):
    if request.method == "GET": #a 标签的href 的默认提交方式就是GET
        print("********",request.method)
        blog = BlogModel.objects.get(id = blog_id)
        print("#############",blog.title)
        print("#############",blog.content)
        return  render(request,'blog/demo_edit.html',
                       context={"blog":blog})
    elif request.method == "POST":
        blog =  BlogModel.objects.get(id=blog_id)
        if blog:
            title = request.POST.get("title")
            content = request.POST.get("content")
            blog.title = title
            blog.content = content
            blog.save()
            return HttpResponse("修改成功")
        else:
            return HttpResponse("没有这篇博客")
    else:
        return HttpResponse("不能被处理的操作")





######form表单基础，使用get方法的表单例子###########
def get_index(request):
    return render(request,'blog/add1.html')


def get_add(request):
    a = request.GET['a']
    # a = request.GET.get("a") #这种方式也可以取值和上面的方式是等价的
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))


######form表单基础，使用POST方法的表单例子###########
def post_add(request):
    if request.method == "GET":
        form = AddForm()
        return  render(request,"blog/add2.html",
                       context={"form":form})
    elif request.method == "POST":
        form = AddForm(request.POST)   #拿到form提交的数据
        print("####",form)
        if form.is_valid():
            print(form.cleaned_data)
            #form.cleaned_data的作用是把拿到的数据进行特殊处理下变成字典的形式，以便查看和取值
            first = form.cleaned_data["first"]
            second = form.cleaned_data["second"]
            return HttpResponse(str(int(first)+int(second)))





########HTTPRequest对象###########
def get_test11(request):
    return render(request,"blog/get_test11.html")

def get_test22(request):
    a = request.GET.get("a",65) #获取a的值，如果没有获取到a的值，那么就默认给他一个值是65，也可以不写默认值
    b = request.GET.get("b")
    c = request.GET.getlist("c","没获取到值，我是默认参数")  #以列表方式获取某个变量中所有的元素
    return render(request,"blog/get_test22.html",
                  context={"a":a,
                           "b":b,
                           "c":c})





########HTTPResponse对象###########
from datetime import datetime
def ckTest(request):
    response = HttpResponse()
    # response.set_cookie('a','123',expires=datetime(2018,6,8)) #指定到某一天
    response.set_cookie('a','123',max_age=3600) #3600秒后cookie过期
    cookie = request.COOKIES
    a = cookie.get('a',2222) #如果获取不到，默认给你cook为2222
    response.write(a)
    return response

#临时测试用的，不同的页面跳转时带参数
def w1(request):
    return render(request,"blog/w1.html")

#临时测试用的，不同的页面跳转时带参数
def w2(request,w2_id,w2_name):
    return render (request,"blog/w2.html",
                   context={"a":w2_id,
                            "name":w2_name})




#************以下是注册、登陆、退出的一个小程序**************，再次看到*后为结束




#####通过取session实现保持登陆########
def home(request):    #这是配合session缓存用的
    username = request.session.get('username222','未登录')
    #request.session是一个可读可写的对象，这里是读取username222，如果没读到则显示默认值“未登录”
    return render(request,'blog/home.html',
                  {'username':username})

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'blog/register.html',
                      {'form': form})
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username', None)
            # form.cleaned_data的作用是把拿到的数据进行特殊处理下变成字典的形式，以便查看和取值
            password = form.cleaned_data.get('password', None)
            password_repeat = form.cleaned_data.get('password_repeat', None)
            email = form.cleaned_data.get('email', None)
            if password == password_repeat:
                user = UserModel()
                user.username = username
                user.password = password
                user.email = email
                user.save()
                return HttpResponse('注册成功')
        else:
            return HttpResponse('注册失败')


###这是以session的方式保持登陆，推荐用这个，安全级别高
def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'blog/login.html',
                      context={'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # username = request.POST.get('username111') #这里的username_111值从login.html的表单中获取,再从forms.py文件中的username111中获取到
            #username取值，用这种方式也可以
            username = form.cleaned_data.get("username111")
            password = form.cleaned_data.get('password')
            print("用户名：",username,"密码：",password)
            userModel = UserModel.objects.filter(username=username,
                                                 password=password)
            if userModel:
                request.session['username222'] = username
                # request.session是一个可读可写的对象，这里是取一个键名为username222，然后写入username的值
                request.session.set_expiry(30)  # 0表示关闭浏览器就过期，100表示100秒后过期
                return redirect(reverse('blog_home'))
            else:
                return redirect(reverse('blog_register'))
        else:
            return render(request,"blog/login.html",
                          context={"error":form.errors})

def logout(request):
    # response.set_cookie('username', username,max_age=0)
    # del request.session['username222'] #删除session方式一，当不会从数据库中删除
    # request.session.clear()   #删除session方式二，当不会从数据库中删除
    request.session.flush()   #删除session方式三，并且会从数据库中删除
    return redirect(reverse('blog_home'))


#***************结束********************