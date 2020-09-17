---
layout: post
title:  HTML
subtitle:   HTML
categories: web
tags: web webprogramming spartacodingclub
comments: true
# header-img:
---
+ __목차__
  - [1. 브라우저의 역할](#1-브라우저의-역할)
  - [2. HTML](#2-html)
  - [3. 곱하기 혹은 더하기](#3-곱하기-혹은-더하기) 
  - [4. 문자열 뒤집기](#4-문자열-뒤집기)
  - [5. 만들 수 없는 금액](#5-만들-수-없는-금액)
  - [6. 볼링공 고르기](#6-볼링공-고르기)
  - [7. 무지의 먹방 라이브](#7-무지의-먹방-라이브)


## 1. 브라우저의 역할
---
간략하게 서버에 자신이 나타낼 것이 무엇인지 요청 -> 서버에서 응답 -> 그대로 받아서 나타낸다. 따라서 검사를 통해 페이지를 수정하면 인터넷과 관계없이 내 맘대로 바꿀 수 있다. 이미 받은 것이기 때문이다. 하지만 새고로침을 하게 되면 수정사항이 원래대로 돌아가게 된다. 새로고침으로 인해 서버로부터 다시 받아오기 때문이다.  
그럼 서버에서 전달해 주는 것을 무엇일까? 네이버를 예시로 보자.
+ HTML : 뼈대와 같다. NAVER 옆에 는 초록색 박스가 있다. 초록박스 아래는 사전, 뉴스, 부동산이 있다.
+ CSS : 꾸미기는 역할을 한다. naver는 초록색으로 이다. 부동산은 굵은 글씨로 한다.
+ 자바스크립트 : 움직이는 것들을 제어한다. 실시간 검색어가 돌아간다. 클릭 했을 때 페이지로 이동한다.

<br>

## 2. HTML
---
html은 크게보면 <html> 이라는 태그 안에 <head>, <body> 태그가 있다. head태크는 눈에 안 보이는 것들이 다 들어간다고 생각하면 된다. 예를 들어 구글 검색 엔진이 해당 사이트를 퍼가고 싶을 때 이런 것들이 head에 들어가는 것이다. 나머지 내 눈에 보이는 것을이 body에 들어간다고 생각하면 된다.  
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
