from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render,reverse,redirect
from datetime import datetime

def hello_python(request):
    return HttpResponse('Hello python!')

def hello_php(request):
    return HttpResponse('Hello php!')

def hello_course(request, course):
    return HttpResponse('Hello %s' % course)

def add(request,a,b): #url中获取到的参数是字符串类型
    c = int(a)+int(b)
    return HttpResponse(str(c))

def hello_django(request, name, num):
    return HttpResponse('Hello %s %s' % (name, num))

def index(request,*arg):
    if arg.get('switch') == 'true':
        print(datetime.datetime.now())
    return HttpResponse('<h1>这是首页</h1>')

#页面跳转
def article(request,**kwargs):
    if kwargs.get('switch') == 'true':
                return redirect(reverse('books_article_new'))
    return HttpResponse('这是文章首页')

def article_new(request,**kwargs):
    return HttpResponse('这是新的文章首页')

def index_1(request):
    return HttpResponse('<h1>Hello Django World!</h1>')

def index_2(request):
    t = get_template('books/index.html')
    html = t.render()
    return HttpResponse(html)


def index_3(request):
    return render(request, 'books/index.html')


def index_4(request,urlcc):
    return render(request, 'books/index.html',
                  context={'zheli':urlcc
                           }
                  )

#页面跳转时带参数,并且还是不定长参数
def old(request,*args,**kwargs):
    return redirect(reverse('books_new',args=args))       #只能使用一种方式接收，不能同时使用字典和元组
    # return redirect(reverse('books_new',kwargs=kwargs)) #只能使用一种方式接收，不能同时使用字典和元组

def new(request,*args,**kwargs):
    print(args,kwargs)
    return HttpResponse("这是新的页面")


#################03模板变量及模板过滤器#####################
def hello():
    return 'django'

class Fruits:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def say(self):
        return 'HAHAHAHA'

ap = Fruits('apple', 'red')
ls = ['x', 'y', 'z']
dc = {'a': 1, 'b': 2}


def index_5(request):
    return render(request,'books/index.html',
                  context={'books_name':'python',#字符串
                           'hello':hello,        # 函数
                           'fruits_say':ap.say,  # 方法
                           'fruits':ap,          # 类对象
                           'list':ls,            # 列表
                           'dict':dc,            # 字典
                           })

##############过滤器###################
ls = ['x','y','z']
def hello(request):
    test = 'THIS IS A LIST!'
    return render(request,'books/index2.html',
                  context={'test':test,
                           'xx':'',
                           'num1':1,
                           'num2':2,
                           'list':ls,
                           'now':datetime.now,
                           'html':'<h1>hello django!!!</h1>',
                           'float':3.1415926,
                           })





##############模板标签#################
def index33(request,name):
    return render(request, 'books/index33.html',
                  context={'test_name':name,
                           'list':ls,
                           'dict':dc,
                           'html': '<h1>hello django</h1>',
                           })

def test(request):
    return HttpResponse('test page!!!!!!!')

def index6(request):
    return render(request, 'music/index.html')

def index7(request):
    ss = "THIS IS A LIST"
    return render(request,'music/static.html',
                  context={"ss":ss,
                           "format_string":'%Y-%m-%d %H:%M:%P'})
