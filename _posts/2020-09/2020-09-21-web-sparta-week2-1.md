---
layout: post
title:  JQuery
subtitle:   JQuery
categories: web
tags: web webprogramming spartacodingclub
comments: true
# header-img:
---
+ __목차__
  - [1.변수](#1-변수)
  - [2. 리스트](#2-리스트)
  - [3. 딕셔너리](#3-딕셔너리) 
  - [4. 함수](#4-함수) 
  - [5. 조건문](#5-조건문) 
  - [6. 반복문](#6-반복문) 


## 1. JQuery
---
JQuery는 HTML 요소들을 조작하는 Javascript 라이브러리이다. HTML에 글자를 바꾼다든지, 박스를 없앤다든지 이런 것들은 javascript로 모두 할 수 있다. 하지만 브라우저 호환성 문제, 코드 자체의 길이 때문에 JQuery 라이브러리가 등장하게 되었다. 따라서 JQuery를 남이 만들어 놓은 것을 import 해야한다.
<Br>

## 2. import
---
[링크](https://www.w3schools.com/jquery/jquery_get_started.asp){: target="_blank"}를 클릭해서 Google CDN을 head에 임포트하면 된다. 아래처럼 말이다.  
```html
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
</head>
```
<Br>

## 3. 선택자(id)
---
CSS와 마찬가지로, JQuery를 사용할 때에도 "가리켜야" 조작할 수 있다. 예를 들어 특정 인풋박스의 값을 가져와라, 특정 div를 안보이게 해라 같이 말이다. CSS에서는 선택자로 class를 사용했다. JQuery에서는 id값을 통해 특정 버튼/인풋박스/div 등을 가리킨다.  
아래 페이지를 통해 연습해보자.
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

    <link href="https://fonts.googleapis.com/css2?family=Jua&display=swap" rel="stylesheet">

    <style>
        * {
            font-family: 'Jua', sans-serif;
        }

        .wrap {
            width: 900px;
            margin: auto;
        }

        .comment {
            color: blue;
            font-weight: bold;
        }

        .posting-box {
            width: 500px;
            margin: 0px auto 20px auto;

            border: 2px solid black;
            padding: 30px;

            border-radius: 10px;
        }
    </style>
    <script>
        function hey(){
            alert('안녕!!!');
        }
    </script>
</head>

<body>

<div class="wrap">
    <div class="jumbotron">
        <h1 class="display-4">나홀로 링크 메모장!</h1>
        <p class="lead">중요한 링크를 저장해두고, 나중에 볼 수 있는 공간입니다</p>
        <hr class="my-4">
        <p class="lead">
            <a id="btn-postingbox" onclick="hey()" class="btn btn-primary btn-lg" href="#" role="button">포스팅박스 열기</a>
        </p>
    </div>
    <div id="postb" class="posting-box">
        <div class="form-group">
            <label for="exampleInputEmail1">아티클 URL</label>
            <input id="article_url" type="email" class="form-control"  aria-describedby="emailHelp"
                   placeholder="">
        </div>
        <div class="form-group">
            <label for="exampleFormControlTextarea1">간단 코멘트</label>
            <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
        </div>
        <button type="submit" class="btn btn-primary">기사저장</button>
    </div>
    <div id="cardbox" class="card-columns">
        <div class="card">
            <img class="card-img-top"
                 src="https://d1blyo8czty997.cloudfront.net/tour-photos/n/4708/1200x600/5791761964.jpg"
                 alt="Card image cap">
            <div class="card-body">
                <a href="https://naver.com" class="card-title">여기 기사 제목이 들어가죠</a>
                <p class="card-text">기사의 요약 내용이 들어갑니다. 동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라만세 무궁화 삼천리 화려강산...</p>
                <p class="comment">여기에 코멘트가 들어갑니다.</p>
            </div>
        </div>
        <div class="card">
            <img class="card-img-top"
                 src="https://d1blyo8czty997.cloudfront.net/tour-photos/n/4708/1200x600/5791761964.jpg"
                 alt="Card image cap">
            <div class="card-body">
                <a href="https://naver.com" class="card-title">여기 기사 제목이 들어가죠</a>
                <p class="card-text">기사의 요약 내용이 들어갑니다. 동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라만세 무궁화 삼천리 화려강산...</p>
                <p class="comment">여기에 코멘트가 들어갑니다.</p>
            </div>
        </div>
        <div class="card">
            <img class="card-img-top"
                 src="https://d1blyo8czty997.cloudfront.net/tour-photos/n/4708/1200x600/5791761964.jpg"
                 alt="Card image cap">
            <div class="card-body">
                <a href="https://naver.com" class="card-title">여기 기사 제목이 들어가죠</a>
                <p class="card-text">기사의 요약 내용이 들어갑니다. 동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라만세 무궁화 삼천리 화려강산...</p>
                <p class="comment">여기에 코멘트가 들어갑니다.</p>
            </div>
        </div>
        <div class="card">
            <img class="card-img-top"
                 src="https://d1blyo8czty997.cloudfront.net/tour-photos/n/4708/1200x600/5791761964.jpg"
                 alt="Card image cap">
            <div class="card-body">
                <a href="https://naver.com" class="card-title">여기 기사 제목이 들어가죠</a>
                <p class="card-text">기사의 요약 내용이 들어갑니다. 동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라만세 무궁화 삼천리 화려강산...</p>
                <p class="comment">여기에 코멘트가 들어갑니다.</p>
            </div>
        </div>
        <div class="card">
            <img class="card-img-top"
                 src="https://d1blyo8czty997.cloudfront.net/tour-photos/n/4708/1200x600/5791761964.jpg"
                 alt="Card image cap">
            <div class="card-body">
                <a href="https://naver.com" class="card-title">여기 기사 제목이 들어가죠</a>
                <p class="card-text">기사의 요약 내용이 들어갑니다. 동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라만세 무궁화 삼천리 화려강산...</p>
                <p class="comment">여기에 코멘트가 들어갑니다.</p>
            </div>
        </div>
        <div class="card">
            <img class="card-img-top"
                 src="https://d1blyo8czty997.cloudfront.net/tour-photos/n/4708/1200x600/5791761964.jpg"
                 alt="Card image cap">
            <div class="card-body">
                <a href="https://naver.com" class="card-title">여기 기사 제목이 들어가죠</a>
                <p class="card-text">기사의 요약 내용이 들어갑니다. 동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라만세 무궁화 삼천리 화려강산...</p>
                <p class="comment">여기에 코멘트가 들어갑니다.</p>
            </div>
        </div>
    </div>
</div>
</body>

</html>
```
파이참에 해당 코드를 입력하고 크롬 개발자도구 콘솔창에서 연습해보자.

### val
```javascript
기본
$('#id값').val();

사용법
$('#article_url').val(); // ""
$('#article_url').val('hello'); // hello
```
id값이 article_url인 곳을 가리키고, val()로 값을 가져오거나, ()안에 입력을 통해 페이지에 값을 입력할 수 있다. 단, input박스에만 입력이 가능하고 버튼 같은 내용을 수정할 수는 없다.
<br>

### hide, show
```javascript
기본
$('#id값').hide();
$('#id값').show();

사용법
$('#postb').hide(); // 포스트박스가 사라짐
$('#postb').show(); // 포스트박스가 다시 보여짐
```

### CSS 속성 가져오기
```javascript
기본
$('#postb').css('속성')

사용 예시
$('#postb').css('width')
$('#postb').css('padding')
$('#postb').css('display')

여기서 hide후에 display값을 물으면 none이라고 나오는데
사라진게 아니고 display값만 none으로 바뀐 것이다.
```
<br>

### text
```javascript
기본
$('#id값').text('내용')

// 버튼의 내용 바꾸기
$('#btn-postingbox').text('포스팅박스')
```

### append
카드를 더 붙이는 작업을 해보자. temp_html을 만들 때는 `(백틱)을 사용하자. 숫자1 왼쪽에 있다.
```javascript
기본
$('#id값').append()

예시
let temp_html= `<div class="card">
            <img class="card-img-top"
                 src="https://d1blyo8czty997.cloudfront.net/tour-photos/n/4708/1200x600/5791761964.jpg"
                 alt="Card image cap">
            <div class="card-body">
                <a href="https://naver.com" class="card-title">여기 기사 제목이 들어가죠</a>
                <p class="card-text">기사의 요약 내용이 들어갑니다. 동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라만세 무궁화 삼천리 화려강산...</p>
                <p class="comment">여기에 코멘트가 들어갑니다.</p>
            </div>
        </div>`

$('#cardbox').append(temp_html)
```
예시처럼 하면 카드가 아래에 하나씩 생성된다.

__cf) 백틱의 추가 기능__  
백틱 안에서 내용 중 어떤 부분을 내가 가지고 있는 변수값을 넣고 싶다면 그 부분에 ${변수명} 입력시 그 부분에 삽입된다.
```javascript
let title = '아무거나 제목'

let temp_html= `<div class="card">
            <img class="card-img-top"
                 src="https://d1blyo8czty997.cloudfront.net/tour-photos/n/4708/1200x600/5791761964.jpg"
                 alt="Card image cap">
            <div class="card-body">
                <a href="https://naver.com" class="card-title">${title}</a>
                <p class="card-text">기사의 요약 내용이 들어갑니다. 동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라만세 무궁화 삼천리 화려강산...</p>
                <p class="comment">여기에 코멘트가 들어갑니다.</p>
            </div>
        </div>`
```
<br>

## 4. 활용하기
---
위에서 사용한 나홀로메모장을 크롬에서 확인하면 포스팅박스 열기버튼이 있다. 페이지에 들어갔을 때 포스팅 박스는 닫혀있고, 포스팅박스 열기 버튼을 누르면 포스팅 박스가 열리고 닫기를 누르면 닫히게 만들어보자.  
다음의 내용을 추가하면 된다.
```javascript
.posting-box {
           
            display: none;
        }

<script>
        function closeopen(){
            let status=$('#postb').css('display');
            if (status == 'none'){
                $('#btn-postingbox').text('포스트박스 닫기');
                $('#postb').show();
            } else{
                $('#btn-postingbox').text('포스트박스 열기');
                $('#postb').hide();
            }

        }
</script>

<a id="btn-postingbox" onclick="closeopen()" class="btn btn-primary btn-lg" href="#" role="button">포스팅박스 열기</a>
```
<br>

## 5. 퀴즈
---
[클릭](https://s3.ap-northeast-2.amazonaws.com/materials.spartacodingclub.kr/web101/week02/06.+Jquery+%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C+%EC%99%84%EC%84%B1%EB%B3%B8.html){: target="_blank"} 의 화면과 같이 만들기

```javascript
<!doctype html>
<html lang="ko">

<head>
    <meta charset="UTF-8">
    <title>jQuery 연습하고 가기!</title>

    <!-- JQuery를 import 합니다 -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

    <style type="text/css">
        div.question-box {
            margin: 10px 0 20px 0;
        }
    </style>

    <script>
        function q1() {
            let input_q1 = $('#input-q1').val();
            if (input_q1==''){
                alert("입력하세요!")
            } else{
                alert(input_q1)
            }
        }

        function q2() {
            let input_q2 = $('#input-q2').val();
            if (input_q2.includes('@')){
                alert(input_q2.split('@')[1].split('.')[0])
            } else{
                alert("이메일이 아닙니다.")
            }

        }

        function q3() {
            let input_q3 = $('#input-q3').val();
            let temp_html = `<li>${input_q3}</li>`
            $('#names-q3').append(temp_html)
        }

        function q3_remove() {
            $('#names-q3').empty()

        }

    </script>

</head>

<body>
    <h1>jQuery + Javascript의 조합을 연습하자!</h1>

    <div class="question-box">
        <h2>1. 빈칸 체크 함수 만들기</h2>
        <h5>1-1. 버튼을 눌렀을 때 입력한 글자로 얼럿 띄우기</h5>
        <h5>[완성본]1-2. 버튼을 눌렀을 때 칸에 아무것도 없으면 "입력하세요!" 얼럿 띄우기</h5>
        <input id="input-q1" type="text" /> <button onclick="q1()">클릭</button>
    </div>
    <hr />
    <div class="question-box">
        <h2>2. 이메일 판별 함수 만들기</h2>
        <h5>2-1. 버튼을 눌렀을 때 입력받은 이메일로 얼럿 띄우기</h5>
        <h5>2-2. 이메일이 아니면(@가 없으면) '이메일이 아닙니다'라는 얼럿 띄우기</h5>
        <h5>[완성본]2-3. 이메일 도메인만 얼럿 띄우기</h5>
        <input id="input-q2" type="text" /> <button onclick="q2()">클릭</button>
    </div>
    <hr />
    <div class="question-box">
        <h2>3. HTML 붙이기/지우기 연습</h2>
        <h5>3-1. 이름을 입력하면 아래 나오게 하기</h5>
        <h5>[완성본]3-2. 다지우기 버튼을 만들기</h5>
        <input id="input-q3" type="text" placeholder="여기에 이름을 입력" />
        <button onclick="q3()">이름 붙이기</button>
        <button onclick="q3_remove()">다지우기</button>
        <ul id="names-q3">
            <li>세종대왕</li>
            <li>임꺽정</li>
        </ul>
    </div>
</body>

</html>
```