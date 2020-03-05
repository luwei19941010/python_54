day54

#### MVC框架

```
web 服务器开发领域里著名的MVC模式，将web应用分为模型(M)，控制器(C)和视图(v)三层，他们之间以一种插件式的，松耦合的方式连接在一起，模型负责业务对象与数据库的映射(ORM)，视图负责与用户的交互(页面)，控制器接受用户的输入调用模型和视图完成用户的请求。
```

![image-20200304124220748](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20200304124220748.png)

#### MTV框架

Django的MTV模式本质上和MVC是一样的，也是各组件保持松耦合关系，只是定义有些不一样。Django的MTV分别是值：

- M 代表模型(Model)：负责业务对象和数据库的关系映射（ORM）
- T代表模版（Template）：负责如何把页面展示给用户（html）
- V代表视图（View）：负责业务逻辑，并在适当时候调用Model和Template



```
#创建一个django项目
django-amdin startproject first-project

#创建项目文件介绍
	manage.py-----Django项目里面的工具，通过他可以调用django shell和数据库，启动关闭项目与项目交互等，不管你将框架分了几个文件，必然有一个启动文件，其实他们本身就是一个文件
 	setting.py-----包含了项目的默认设置，包括数据库信息，调试标志以及其他一些工作的变量
 	urls.py-----负责吧UTL模式映射到应用程序
 	wsgi.py-----runserver 命令就是用wsgiref模块做简单的web server，后面会看到renserver命令，所有与socket相关的内容都在这个文件里面，目前不需要关注它

#mysite目录下创建应用
C:\Users\davidlu\PycharmProjects\luwei-Knightsplan\day54\first_project>python manage.py startapp app01
 
# 开启django
C:\Users\davidlu\PycharmProjects\luwei-Knightsplan\day54\first_project>python manage.py runserver 127.0.0.1:8001
```



 get请求获取数据

```
def index(request):
    # print(request.GET)	#<QueryDict: {'username': ['luwei'], 'password': ['Lw123123']}>
    username=request.get.get('username')
    password=request.get.get('password')
    if username=='luwei' and password=='Lw123123':
    	return HttpResponse('登录成功')
    else:
    	return HttpResponse('登录失败!')
```

post 请求提交数据时关掉一个认证csf机制，settings中

```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

post 请求获取数据

```
def index(request):
    # print(request.GET)
    if request.method=='GET':
        return render(request,'login.html')
    else:
        print(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username=='luwei' and password=='Lw123123':
            return HttpResponse('登录成功')
        else:
            return HttpResponse('登录失败!')
```



Django框架简单总结

```
1.urls

        from app01 import views

        urlpatterns = [
            url(r'^index/', views.index),
        ]
2.views
		def index(request):
            # print(request.GET)
            if request.method=='GET':
                return render(request,'login.html')
            else:
                print(request.POST)
                username=request.POST.get('username')
                password=request.POST.get('password')
                if username=='luwei' and password=='Lw123123':
                    return HttpResponse('登录成功')
                else:
                    return HttpResponse('登录失败!')
                    
3.html
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>login</title>
</head>
<body>
	<h1>luwei denglu</h1>
	<form action="/index/" method="post">
		用户名：<input type="username" name="username" id="" value="" placeholder="user"/>
		密码：<input type="password" name="password" id="" value="" placeholder="psw" />
		<input type="submit" id="" name="" />
	</form>
</body>
</html>
```

#### url配置

##### 无名分组

```
url(r'^books/(\d{4})/', views.books),
```

##### 位置参数

```
	url(r'^books/(\d{4})/', views.year_books), #匹配年份的
	url(r'^books/(\d{4})/(\d{1,2})/', views.year_month_books), #匹配年份和月份的
# http://127.0.0.1:8000/books/2001/
	视图:
		def year_month_books(request,year,month): #位置参数,第一个参数接收的就是无名分组路径中匹配到的第一个分组的数据,第二个参数接收的就是无名分组路径中匹配到的第二个分组的数据
		print(year,month)
		# return render(request,'books.html')
		return HttpResponse(year+month)
```

##### 有名分组

```
	url(r'^books/(?P<year>\d{4})/(?P<month>\d{1,2})/', views.year_month_books), #匹配年份和月份的
	def year_month_books(request,month,year): #形参名称要和url中的分组名对应好,参数位置就没有要求了
	print(year,month)
	# return render(request,'books.html')
	return HttpResponse(year+month)
```

 默认值

```
# urls.py中
from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^blog/$', views.page),
	url(r'^blog/page(?P<num>[0-9]+)/$', views.page),
]
#views.py中，可以为num指定默认值
def page(request, num="1"):
	pass
```

关于URL 访问最后是否带‘/’

```
默认情况下 django是对URL最后不带/，会向浏览器返回301 让浏览器重定向URL 在最后加上/。当然可以在django中把该重定向机制关闭，在django项目的setting配置文件中加上APPEND_SLASH=False即可
```

