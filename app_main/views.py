from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from .models import *
from django.contrib import messages
import pyupbit
import time

@csrf_exempt
def main(request):
    return render(request, "main.html")

@csrf_exempt
def try_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        #user = UserList.objects.filter(user_id__exact=username, user_pw__exact=password)
        if user is not None:
            auth.login(request, user)
            #loginList.append(user[0].user_id)
            return render(request, 'trade')
        else:
            return HttpResponse("<script>alert('아이디 또는 패스워드가 일치하지 않습니다.');location.href='/';</script>")
    else:
        return redirect('/')

def get_value(request):
    coins = CoinList.objects.all()
    nowPrice = pyupbit.get_current_price(list(map(lambda x:x.coin_id, coins)))
    
    result = {}
    for i in coins:
        result[i.coin_id+"-LAST"] = str(round((nowPrice[i.coin_id] - i.coin_last_value/10000)/nowPrice[i.coin_id]*100,2))+"%"
        result[i.coin_id] = nowPrice[i.coin_id]
        tradeAmnt = TradeList.objects.filter(tlog_order_time__gt=1, coin_pk__exact=i.coin_pk)
        if len(tradeAmnt) > 0:
            result[i.coin_id+"-TRADE"] = sum(list(map(lambda x:x.tlog_coin_amnt, tradeAmnt)))/2
        else:
            result[i.coin_id+"-TRADE"] = 0

    # return the value as JSON
    return JsonResponse(result)
    # get the value from wherever you store it (e.g. database, cache, etc.)
    
# @csrf_exempt
# def coinlist(request):
#     #return redirect(url)
#     coins = CoinList.objects.all()
#     return render(request, "signup.html", {"coins":coins})

# @csrf_exempt
# def coinlist1(request):
#     coins = CoinList.objects.all()
#     print(request.POST)
#     return render(request, "trade.html", {"coins":coins})


# Create your views here.

# topics = [
#     {'id':1, 'title':'routing', 'body':'Routing is ..'},
#     {'id':2, 'title':'view', 'body':'View is ..'},
#     {'id':3, 'title':'Model', 'body':'Model is ..'},]


# def HTMLTemplate(articleTag, id=None):
#     global topics
#     contextUI = ''
#     if id != None:
#         contextUI += f'''
#             <li>
#                 <form action="/delete/" method="post">
#                     <input type="hidden" name="id" value={id}>
#                     <input type="submit" value="delete">
#                 </form>
#             </li>
#             <li><a href="/update/{id}">update</a></li>
#         '''
#     ol = ''
#     for topic in topics:
#         ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
#     return f'''
#     <html>
#     <body>
#         <h1><a href="/">Django</a></h1>
#         <ul>
#             {ol}
#         </ul>
#         {articleTag}
#         <ul>
#             <li><a href="/create/">create</a></li>
#             {contextUI}
#             <li><a href="/coinlist/">coinlist</a></li>
#         </ul>
#     </body>
#     </html>
#     '''
    
# def index(requset):
#     article ='''
#         <h2>Welcome</h2>
#         Hello, Django
#     '''
#     return HttpResponse(HTMLTemplate(article))

# def read(request,id):   
#     global topics
#     article =''
#     for topic in topics :
#         if topic['id']==int(id) :
#             article=f'<h2>{topic["title"]}</h2>{topic["body"]}' 
#     return HttpResponse(HTMLTemplate(article, id))

# @csrf_exempt
# def create(request):
#     global nextId
#     if request.method == 'GET':
#         article = '''
#             <form action="/create/" method="post">
#                 <p><input type="text" name="title" placeholder="title"></p>
#                 <p><textarea name="body" placeholder="body"></textarea></p>
#                 <p><input type="submit"></p>
#             </form>
#         '''
#         return HttpResponse(HTMLTemplate(article))
#     elif request.method == 'POST':
#         title = request.POST['title']
#         body = request.POST['body']
#         newTopic = {"id":nextId, "title":title, "body":body}
#         topics.append(newTopic)
#         url = '/read/'+str(nextId)
#         nextId = nextId + 1
#         return redirect(url)

# @csrf_exempt
# def delete(request):
#     global topics
#     if request.method == 'POST':
#         id = request.POST['id']
#         newTopics = []
#         for topic in topics:
#             if topic['id'] != int(id):
#                 newTopics.append(topic)
#         topics = newTopics
#     return redirect('/')

# @csrf_exempt
# def update(request,id):
#     global topics
#     if request.method == 'GET':
#         for topic in topics:
#             if topic['id'] == int(id):
#                 selectedTopic = {
#                     "title":topic['title'],
#                     "body":topic['body']
#                 }
#         article = f'''
#             <form action="/update/{id}/" method="post">
#                 <p><input type="text" name="title" placeholder="title" value={selectedTopic["title"]}></p>
#                 <p><textarea name="body" placeholder="body">{selectedTopic['body']}</textarea></p>
#                 <p><input type="submit"></p>
#             </form>
#         '''
#         return HttpResponse(HTMLTemplate(article, id))
#     elif request.method == 'POST':
#         title = request.POST['title']
#         body = request.POST['body']
#         for topic in topics:
#             if topic['id'] == int(id):
#                 topic['title'] = title
#                 topic['body'] = body
#         return redirect(f'/read/{id}')
