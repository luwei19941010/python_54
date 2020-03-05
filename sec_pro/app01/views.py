from django.shortcuts import render,HttpResponse
# Create your views here.
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