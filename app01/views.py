from django.shortcuts import render, HttpResponse, redirect

from app01.models import Department, UserInfo


# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")

def user_list(request):
    return render(request,"user_list.html")

def user_add(request):
    return render(request,"user_add.html")

def test(request):
    name = "huangyixi"
    role = ["CEO","Staff"]
    userInfo = {"name":"huangxiaoming","salary":100000,"role":"cto"}
    dataList =[
        {"name": "zhangsan", "salary": 100000, "role": "staff"},
        {"name": "lisi", "salary": 200000, "role": "staff"},
        {"name": "wangwu", "salary": 300000, "role": "staff"}
    ]
    return render(request,"test.html",{"name":name,"role":role,"userInfo":userInfo,"dataList":dataList})

def news(req):
    import requests
    res = requests.get("http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2025/7/news")
    data_llist = res.json()
    return render(req,"news.html",{"news_llist":data_llist})

def something(request):
    print("request.method : ",request.method)
    print("request.path : ",request.path)
    print("request.GET : ",request.GET)
    print("request.POST : ",request.POST)

    # return HttpResponse("返回内容")
    # return render(request,"something.html")
    return redirect("https://www.baidu.com")

def login(request):
    if request.method == "GET":
        return render(request,"login.html")

    username = request.POST.get("username")
    password = request.POST.get("pwd")

    if username == "root" and password == "123":
        # return HttpResponse("登录成功！")
        return redirect("https://www.baidu.com")
    return render(request,"login.html",{"error_msg":"用户名或密码错误"})

def orm(request):

    # create data
    # Department.objects.create(title="销售部")
    # Department.objects.create(title="运营部")
    # Department.objects.create(title="IT部")
    #
    # UserInfo.objects.create(name ="hyx",password="123",age=18)
    # UserInfo.objects.create(name ="lbc",password="456")

    # delete data
    # UserInfo.objects.filter(id=1).delete()
    # Department.objects.all().delete()

    # query data
    data_list = UserInfo.objects.all()
    for item in data_list:
        print(item.id , item.name,item.age,item.data)

    print('_'*30)
    data_first =UserInfo.objects.filter(id=2).first()
    print(data_first.id,data_first.name,data_first.age,data_first.data)

    # update
    print("-" * 30)
    UserInfo.objects.all().update(password=999)
    UserInfo.objects.filter(id=2).update(password=777)
    UserInfo.objects.filter(name='hyx').update(password=888)

    return HttpResponse("成功")


def info_list(request):
    # if request.method == "POST":
    #     username = request.POST.get("username")
    #     password = request.POST.get("password")
    #     age = request.POST.get("age")
    #     data = request.POST.get("data")
    #     # create data
    #     if username != None:
    #         UserInfo.objects.create(name=username, age=age, password=password, data=data)

    data_list = UserInfo.objects.all()
    return render(request, "info_list.html",{"data_list": data_list})


def info_add(request):
    if request.method == "GET":
        return render(request,"info_add.html")

    username = request.POST.get("username")
    password = request.POST.get("password")
    age = request.POST.get("age")
    data = request.POST.get("data")
    # create data
    if username != None:
        UserInfo.objects.create(name=username, age=age, password=password, data=data)
    return redirect("/info/list/")

def info_delete(request):
    nid = request.GET.get("nid")
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/info/list/")
