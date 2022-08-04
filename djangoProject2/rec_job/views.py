from django.shortcuts import render
from .models import Sampleuser
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password

from django.http import HttpResponse, HttpRequest

def index(request):
  return render(request, "index.html")

def register(request):
  if request.method == 'GET':  # 주소를 치고 들어갔을때의 경우
    return render(request, 'register.html')
  elif request.method == 'POST':  # 등록을 눌렀을때의 액션
    username = request.POST.get('username', None)  # 초기값 None으로 설정
    password = request.POST.get('password', None)
    re_password = request.POST.get('re-password', None)

    res_data = {}  # 에러를 받을 딕셔너리 만들어줌
    if not (username and password and re_password):  # 값 3개가 다들어있지않는경우
      res_data['error'] = '모든 값을 가지지않았습니다'
    elif password != re_password:
      res_data['error'] = '비밀번호가 다릅니다'
    else:

      sampleuser = Sampleuser(
        username=username,
        password=make_password(password)  # 암호화 후 저장
      )
      sampleuser.save()
    # 데이터 포스트를 하고 다시 html페이지를반환

    return render(request, 'register.html', res_data)
      # res_data를 줘야 에러메시지 출력됨
    # 리퀘스트와 반환하고싶은 html파일 리턴


# Create your views here.
