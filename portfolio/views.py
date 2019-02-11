from django.shortcuts import render
from .models import Portfolio
from django.utils import timezone

def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios':portfolios})

def new_portfolio(request):
    return render(request, 'new_portfolio.html')

def create_portfolio(request):#입력받은 내용을 데이터베이스에 넣어주는 함수
    portfolio = Portfolio()#Blog라는 클래스로부터 blog라는 객체를 하나 생성
    portfolio.title = request.GET['title']#블로그 객체안에 title을 넣어준다.
    portfolio.description = request.GET['description']
    portfolio.image = request.GET['file']
    # portfolio.pub_date = timezone.datetime.now()#이것을 쓰기 위해 위에 import해준다.
    portfolio.save()#지금까지 객체에 넣은 내용을 데이터베이스에 저장해라
    return redirect('/portfolio')#여기 다시 고치기-이미지 업로더 해야 가능.