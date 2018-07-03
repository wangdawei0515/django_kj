import datetime
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

#编写自定义模板过滤器
@register.filter
def mycut(value, arg):
    return value.replace(arg, '')


@register.filter
@stringfilter    #注释掉此句传递int类型会报错
def mylower(value):
    return value.lower()
#register.filter('mylower', mylower) #这句的作用和上面的装饰器作用一样的




#自定义模板标签
@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


#如果你的自定义模板标签需要访问当前上下文，你可以在注册标签时使用takes_context 参数
@register.simple_tag(takes_context=True)
def current_time_2(context):
    tm = context['format_string']
    return datetime.datetime.now().strftime(tm)
# 这里的tm是从视图函数context中传进来的。


#包含标签
#另一种常见类型的模板标签是通过渲染另外一个模板来显示一些数据。这些类型的标签被称为"Inclusion 标签"。
@register.inclusion_tag('music/xxx.html')  #就是会把music/xxx.html这个文件的内容会在music/static.html文件中显示
def show_results():
    li = ['python','java','c++']
    return {'choices':li}

#分配标签
#为了简单化设置上下文中变量的标签的创建，Django 提供一个辅助函数assignment_tag。 除了将标签的结果存储在指定的上下文变量中，而不是直接输出，该函数的工作方式与simple_tag()相同
@register.assignment_tag
def current_time_3(format_string):
    return datetime.datetime.now().strftime(format_string)

