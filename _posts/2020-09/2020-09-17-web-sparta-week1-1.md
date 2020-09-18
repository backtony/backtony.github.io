---
layout: post
title:  HTML, CSS 기초
subtitle:   HTML, CSS 기초
categories: web
tags: web webprogramming spartacodingclub
comments: true
# header-img:
---
+ __목차__
  - [1. 브라우저의 역할](#1-브라우저의-역할)
  - [2. HTML](#2-html)
  - [3. CSS](#3-css) 
  - [4. 부트스트랩](#4-부트스트랩) 

## 1. 브라우저의 역할
---
간략하게 서버에 자신이 나타낼 것이 무엇인지 요청 -> 서버에서 응답 -> 그대로 받아서 나타낸다. 따라서 검사를 통해 페이지를 수정하면 인터넷과 관계없이 내 맘대로 바꿀 수 있다. 이미 받은 것이기 때문이다. 하지만 새고로침을 하게 되면 수정사항이 원래대로 돌아가게 된다. 새로고침으로 인해 서버로부터 다시 받아오기 때문이다.  
그럼 서버에서 전달해 주는 것을 무엇일까? 네이버를 예시로 보자.
+ HTML : 구역과 텍스트를 나타내는 코드이다. NAVER 옆에는 초록색 박스가 있고, 초록박스 아래는 사전, 뉴스, 부동산이 있다.
+ CSS : 꾸미기는 역할을 한다. naver는 초록색으로 하고, 부동산은 굵은 글씨로 한다.
+ 자바스크립트 : 움직이는 것들을 제어한다. 실시간 검색어가 돌아간다. 클릭 했을 때 페이지로 이동한다.

<br>

## 2. HTML
---
html은 크게보면 <html> 이라는 태그 안에 <head>, <body> 태그가 있다. head태크 안에는 페이지의 속성 정보를, body안에는 페이지의 내용을 담는다. 즉, head에는 눈에 안보이는 필요한 것들을 담고, 나머지 눈에 보이는 것들이 body에 들어간다고 생각하면 된다.  
html에는 여러 가지 태그들이 있는데 대표적으로는 다음과 같다.  
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>스파르타코딩클럽 | HTML 기초</title>
</head>

<body>
    <!-- 구역을 나누는 태그들 -->
    <div>나는 구역을 나누죠</div>
    <p>나는 문단이에요</p>
    <ul>
        <li> bullet point!1 </li>
        <li> bullet point!2 </li>
    </ul>

    <!-- 구역 내 콘텐츠 태그들 -->
    <h1>h1은 제목을 나타내는 태그입니다. 페이지마다 하나씩 꼭 써주는 게 좋아요. 그래야 구글 검색이 잘 되거든요.</h1>
    <h2>h2는 소제목입니다.</h2>
    <h3>h3~h6도 각자의 역할이 있죠. 비중은 작지만..</h3>
    <hr>
    span 태그입니다: 특정 <span style="color:red">글자</span>를 꾸밀 때 써요
    <hr>
    a 태그입니다: <a href="http://naver.com/"> 하이퍼링크 </a>
    <hr>
    img 태그입니다: <img src="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png" />
    <hr>
    input 태그입니다: <input type="text" />
    <hr>
    button 태그입니다: <button> 버튼입니다</button>
    <hr>
    textarea 태그입니다: <textarea>나는 무엇일까요?</textarea>
</body>

</html>
```
<br>

### 로그인 페이지 만들기
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>스파르타코딩클럽 | 로그인페이지</title>
</head>

<body>
    <h1>로그인 페이지</h1>
    <div>
        <p>
            ID: <input type="text" />
        </p>
        <p>
            PW: <input type="password" />
        </p>
    </div>
    <button>로그인하기</button>
</body>

</html>
```
<br>

## 3. CSS
---
HTML 내 style 속성으로 꾸미기를 할 수 있지만, 긴 세월동안 이것을 한 데 모아 볼 수 있는 CSS파일이 탄생했다. HTML 코드 내에 CSS파일을 불러와서 적용한다.  
<br>

### HTML 부모 자식 구조
![그림1](https://backtony.github.io/assets/img/post/web/sparta/web-sparta-week1-1.PNG)

html 태그는 누가 누구 안에 있느냐를 이해하는 것이 가장 중요하다. 감싸고 있는 태그가 바뀌면, 그 안의 내용물도 모두 영향을 받기 때문이다. 예를 들면 위 그림처럼 빨간색 div 안에 초록색/파란색 div가 있다고 한다면 빨간색 div를 가운데로 옮기면 내용물인 초록/파란 div도 모두 이동하게 되는 것이다. 이렇게 어떤 것들을 묶어줄 때는 div를 사용한다는 것도 기억하자.  
<br>

### CSS 기초
CSS는 <head> ~ </head> 안에 <style> ~ </style>로 공간들 만들어 작성한다. 만약 mytitle라는 클래스를 가리킬 때, .mytitle {} 라고 써줘야 한다는 것을 꼭 기억하자. 아래는 간단한 CSS 내용이다.  
```
배경관련
background-color
background-image
background-size
background-position

사이즈
width
height

폰트
font-size
font-weight
font-famliy
color

간격
margin  바깥 여백
padding  안쪽 여백
```
<br>

__로그인 페이지 가운데로 가져오기__  
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>스파르타코딩클럽 | 로그인페이지</title>
    <link href="https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@700&display=swap" rel="stylesheet">

    <style>
        * {
            font-family: 'Nanum Myeongjo', serif;
        }

        .mytitle {
            color: white;
            background-image: url('https://www.ancient-origins.net/sites/default/files/field/image/Agesilaus-II-cover.jpg');
            background-position: center;
            background-size: cover;
            width: 300px;
            height: 200px;

            border-radius: 10px;
            text-align: center;
            padding-top: 50px;
        }

        .wrap {
            width: 300px;
            /*시계방향 순서 위 오른쪽 아래 왼쪽*/
            margin: 50px auto auto auto;            
            text-align: center;
        }


    </style>
</head>

<body>
<div class="wrap">
    <div class="mytitle">
        <h1>로그인 페이지</h1>
        <h5> 아이디, 비밀번호를 입력하세요</h5>
    </div>
    <div>
        <p>
            ID: <input type="text"/>
        </p>
        <p>
            PW: <input type="password"/>
        </p>


        <button>로그인하기</button>
    </div>
</div>
</body>

</html>
```
스타일에서 * 는 모든 태그에 적용시키겠다는 뜻이다. 폰트는 구글에서 구글 폰트 입력후 복사해서 title 아래정도에 복붙해주고 스타일에 *로 복붙해준다.  
<br>

## 4. 부트스트랩
---
부트스트랩이란 예쁜 CSS를 미리 모아둔 것이다. CSS를 다룰 줄 아는 것과 미적 감각을 발휘하여 예쁘게 만드는 것은 다른 영역이기 때문에 현업에서는 미리 완성도니 부트스트랩을 가져다 쓰는 경우가 많다. 남이 미리 작성한 CSS를 내 HTML 파일에 적용한다는 점에서 bootstrap 적용은 CSS파일 분리와 원리가 동일하다. 다만, CSS의 파일이 인터넷 어딘가에 있다는 점이 다를 뿐이다.  
<br>

### 부트스트랩 시작 템플릿
```html
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>

    <title>스파르타코딩클럽 | 부트스트랩 연습하기</title>
</head>

<body>
    <h1>이걸로 시작해보죠!</h1>
</body>

</html>
```
__부트스트랩 컴포넌트 [클릭](https://getbootstrap.com/docs/4.0/components/alerts/){: target="_blank"}__  
템플릿을 붙여넣고 위의 클릭으로 링크를 타고 들어가 원하는 CSS를 복사해서 붙여넣으면 된다. 부트스트랩을 이용해서 '나홀로 메모장'을 만들어 보자.  
<br>

__나홀로 메모장__  
```html
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
          integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>스파르타코딩클럽 | 부트스트랩 연습하기</title>
    <link href="https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&family=Sunflower:wght@500&display=swap"
          rel="stylesheet">

    <style>
        * {
            font-family: 'Nanum Pen Script', cursive;
            font-family: 'Sunflower', sans-serif;
        }

        .wrap {
            width: 900px;
            margin: 10px auto;
        }

        .box {
            width: 300px;
            margin: 30px auto;
            padding: 30px;
            border: 3px solid black;
            border-radius: 10px;
        }

        .butt {
            margin-top: 30px;
        }

        .comment {
            font-weight: bold;
            color: blue;
        }
    </style>
</head>

<body>

<div class="wrap">
    <div class="jumbotron">
        <h1 class="display-4">나홀로 링크 메모장!</h1>
        <p class="lead">중요한 링크를 저장해두고, 나중에 볼 수 있는 공간입니다</p>
        <hr class="my-4">
        <p class="lead">
            <a class="btn btn-primary btn-lg" href="#" role="button">포스트박스 열기</a>
        </p>
    </div>
    <div class="box">
        <div class="form-group">
            <label for="exampleFormControlInput1">이타클 URL</label>
            <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
        </div>
        <div class="form-group">
            <label for="exampleFormControlTextarea1">간단 코멘트</label>
            <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
            <button type="button" class="btn btn-primary butt">기사 저장</button>
        </div>
    </div>

    <div class="card-columns">
        <div class="card">
            <img class="card-img-top"
                 src="https://www.eurail.com/content/dam/images/eurail/Italy%20OCP%20Promo%20Block.adaptive.767.1535627244182.jpg"
                 alt="Card image cap">
            <div class="card-body">
                <h5 class="card-title"><a href="http://www.naver.com">여기에 제목이 들어간다.</a></h5>
                <p class="card-text">hello world. 여기가 본문</p>
                <p class="comment">코멘트 입력</p>
            </div>
        </div>
        <div class="card">
            <img class="card-img-top"
                 src="https://www.eurail.com/content/dam/images/eurail/Italy%20OCP%20Promo%20Block.adaptive.767.1535627244182.jpg"
                 alt="Card image cap">
            <div class="card-body">
                <h5 class="card-title"><a href="http://www.naver.com">여기에 제목이 들어간다.</a></h5>
                <p class="card-text">hello world. 여기가 본문</p>
                <p class="comment">코멘트 입력</p>
            </div>
        </div>
        <div class="card">
            <img class="card-img-top"
                 src="https://www.eurail.com/content/dam/images/eurail/Italy%20OCP%20Promo%20Block.adaptive.767.1535627244182.jpg"
                 alt="Card image cap">
            <div class="card-body">
                <h5 class="card-title"><a href="http://www.naver.com">여기에 제목이 들어간다.</a></h5>
                <p class="card-text">hello world. 여기가 본문</p>
                <p class="comment">코멘트 입력</p>
            </div>
        </div>
        <div class="card">
            <img class="card-img-top"
                 src="https://www.eurail.com/content/dam/images/eurail/Italy%20OCP%20Promo%20Block.adaptive.767.1535627244182.jpg"
                 alt="Card image cap">
            <div class="card-body">
                <h5 class="card-title"><a href="http://www.naver.com">여기에 제목이 들어간다.</a></h5>
                <p class="card-text">hello world. 여기가 본문</p>
                <p class="comment">코멘트 입력</p>
            </div>
        </div>
        <div class="card">
            <img class="card-img-top"
                 src="https://www.eurail.com/content/dam/images/eurail/Italy%20OCP%20Promo%20Block.adaptive.767.1535627244182.jpg"
                 alt="Card image cap">
            <div class="card-body">
                <h5 class="card-title"><a href="http://www.naver.com">여기에 제목이 들어간다.</a></h5>
                <p class="card-text">hello world. 여기가 본문</p>
                <p class="comment">코멘트 입력</p>
            </div>
        </div>
        <div class="card">
            <img class="card-img-top"
                 src="https://www.eurail.com/content/dam/images/eurail/Italy%20OCP%20Promo%20Block.adaptive.767.1535627244182.jpg"
                 alt="Card image cap">
            <div class="card-body">
                <h5 class="card-title"><a href="http://www.naver.com">여기에 제목이 들어간다.</a></h5>
                <p class="card-text">hello world. 여기가 본문</p>
                <p class="comment">코멘트 입력</p>
            </div>
        </div>
        <div class="card">
            <img class="card-img-top"
                 src="https://www.eurail.com/content/dam/images/eurail/Italy%20OCP%20Promo%20Block.adaptive.767.1535627244182.jpg"
                 alt="Card image cap">
            <div class="card-body">
                <h5 class="card-title"><a href="http://www.naver.com">여기에 제목이 들어간다.</a></h5>
                <p class="card-text">hello world. 여기가 본문</p>
                <p class="comment">코멘트 입력</p>
            </div>
        </div>
    </div>
</div>

<!-- Optional JavaScript -->
<!-- jQuery first, then Popper.js, then Bootstrap JS -->
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>
</body>

</html>
```
부트스트랩에서 form, button, card, jumbotron을 이용했다. 이외에 구글 폰트도 이용했다. 새로 사용한 태그는 a 태그인데 a태그는 링크를 걸어주는 태그이다. 또 style에서는 border을 새로 사용했는데 테두리를 나타내준다.
<Br>

