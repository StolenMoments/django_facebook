from django.shortcuts import render, redirect
from facebook.models import Article, Page, Comment
# Create your views here.


count = 0


def new_page(request):
    if request.method == "POST":
        if request.POST['master'] != '' and request.POST['name'] != '' and request.POST['category'] != '' and request.POST['text'] != '':
            new_page = Page.objects.create(
                master=request.POST['master'],
                name=request.POST['name'],
                category=request.POST['category'],
                text=request.POST['text']
            )
            return redirect('/pages/')

    return render(request, 'new_page.html')


def play(request):
    return render(request, 'play.html')


def newsfeed(request):
    articles = Article.objects.all()
    return render(request, 'newsfeed.html', {'articles' : articles})


def play2(request):
    leejonghwa = '이종화'
    age = 20
    global count
    count += 1
    diary = ['a', 'b', 'c']
    if age > 19:
        status = '성인'
    else:
        status = '청소년'

    if count == 7:
        message = '축하합니다 당첨입니다.'
    else:
        message = '꽝 입니다 ㅎ_ㅎ..'
    return render(request, 'play2.html', {'name': leejonghwa,  'cnt': count, 'age': status, 'diary': diary, 'message': message})


def profile(request):
    name = '이종화'
    age = 29
    phone = '01099117465'

    return render(request, 'profile.html', {'name': name, 'age': age, 'phone': phone})


def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':  # new comment
        Comment.objects.create(
            article=article,
            author=request.POST.get('author'),
            text=request.POST.get('text'),
            password=request.POST.get('password')
        )

        return redirect(f'/feed/{ article.pk }')

    return render(request, 'detail_feed.html', {'feed': article})


def pages(request):
    return render(request, 'pages.html')


def new_feed(request):
    # POST 안에서 내용을 하나 하나 꺼내오는 작업
    if request.method == "POST":
        if request.POST['author'] != '' and request.POST['title'] != '' and request.POST['content'] != '' and request.POST['password'] != '':
            new_article = Article.objects.create(
                author=request.POST['author'],
                title=request.POST['title'],
                text=request.POST['content'] + "추신: 감사합니다 ㅎㅎ",
                password=request.POST['password']
            )
            return redirect(f'/feed/{new_article.pk}')

    return render(request, 'new_feed.html')


def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.delete()
            return redirect('/') # 첫페이지로 이동하기

        else:
            return redirect('/fail/')  # 비밀번호 오류 페이지 이동하기

    return render(request, 'remove_feed.html', {'feed': article})

def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.author = request.POST['author']
            article.title = request.POST['title']
            article.text = request.POST['content']
            article.save()
            return redirect(f'/feed/{ article.pk }')
        else:
            return redirect('/fail/')  # 비밀번호 오류 페이지 이동하기

    return render(request, 'edit_feed.html', {'feed': article})


def fail(request):
    return render(request, 'fail.html')