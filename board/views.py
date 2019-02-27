from django.shortcuts import render,redirect
from .models import BoardMessage
from .forms import BoardForm
from django.contrib.auth import authenticate
from django.contrib import  auth
import math

page = 0
def home(request,pageindex=None):
    global page  # 重複開啟本網頁時需保留 page1 的值
    pagesize = 5  # 每頁顯示的資料筆數
    Posts = BoardMessage.objects.all().order_by('-date')  # 讀取資料表,依時間遞減排序
    datasize = len(Posts)  # 資料筆數
    totpage = math.ceil(datasize / pagesize)  # 總頁數
    if pageindex == None:  # 無參數
        page = 0
        Posts = BoardMessage.objects.order_by('-date')[:pagesize]
    elif pageindex == 'prev':  # 上一頁
        start = (page - 1) * pagesize  # 該頁第1筆資料
        if start >= 0:  # 有前頁資料就顯示
            Posts = BoardMessage.objects.order_by('-date')[start:(start + pagesize)]
            page -= 1
    elif pageindex == 'next':  # 下一頁
        start = (page + 1) * pagesize  # 該頁第1筆資料
        if start < datasize:  # 有下頁資料就顯示
            Posts = BoardMessage.objects.order_by('-date')[start:(start + pagesize)]
            page += 1
    currentpage = page + 1  # 將目頁前頁面以區域變數傳回html
    return render(request, "home.html", locals())

def post(request):
    if request.method =="POST":
        postform = BoardForm(request.POST)
        if postform.is_valid():
            title = postform.cleaned_data['title']
            author = request.user.email
            content =postform.cleaned_data['content']
            unit = BoardMessage.objects.create(author=author,title=title,content=content)
            unit.save()
            message = 'stored'
            postform = BoardForm()
            return redirect('/')
        else:
            message = postform.errors
    else:
        message ='欄位需輸入完成'
        postform = BoardForm()
    return render(request,"post.html",locals())

def edit(request,postid=None,edittype=None):
    unit = BoardMessage.objects.get(id=postid)
    if edittype==None:
        id = postid
        title = unit.title
        content = unit.content
    elif edittype=='1':
        title = request.POST.get('title','')
        content = request.POST.get('content','')
        unit.title = title
        unit.content = content
        unit.save()
        return redirect('/')
    return render(request,'edit.html',locals())