---
layout: post
title:  HTML, CSS
subtitle:   HTML, CSS
categories: web
tags: web webprogramming spartacodingclub
comments: true
# header-img:
---
+ __목차__
  - [1. 브라우저의 역할](#1-브라우저의-역할)
  - [2. HTML](#2-html)
  - [3. CSS](#3-css) 



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
__부트스트랩 컴포넌트 [클릭](https://getbootstrap.com/docs/4.0/components/alerts/)__  
템플릿을 붙여넣고 위의 클릭으로 링크를 타고 들어가 원하는 CSS를 복사해서 붙여넣으면 된다. 예시는 다음과 같다.  
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
    <style>
        .wrap {
            width: 900px;
            margin: auto;
        }
    </style>
</head>

<body>
<div class="wrap">
    <div class="jumbotron">
        <h1 class="display-4">Hello, world!</h1>
        <p class="lead">This is a simple hero unit, a simple jumbotron-style component for calling extra attention to
            featured content or information.</p>
        <hr class="my-4">
        <p>It uses utility classes for typography and spacing to space content out within the larger container.</p>
        <p class="lead">
            <a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a>
        </p>
    </div>
    <div class="card-columns">
        <div class="card">
            <img class="card-img-top"
                 src="data:image/jpeg;base64,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"
                 alt="Card image cap">
            <div class="card-body">
                <h5 class="card-title">Card title that wraps to a new line</h5>
                <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
                    content. This content is a little bit longer.</p>
            </div>
        </div>
        <div class="card">
            <img class="card-img-top"
                 src="data:image/jpeg;base64,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"
                 alt="Card image cap">
            <div class="card-body">
                <h5 class="card-title">Card title that wraps to a new line</h5>
                <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
                    content. This content is a little bit longer.</p>
            </div>
        </div>
    </div>
</div>
</body>

</html>
```
<Br>

