from django.shortcuts import render, HttpResponse, redirect


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