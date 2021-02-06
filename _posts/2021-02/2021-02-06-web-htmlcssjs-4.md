---
layout: post
title:  JavaScript - Ajax
subtitle:   JavaScript - Ajax
categories: web
tags: htmlcssjs
comments: true
# header-img:
---

+ __목차__
  - [1. Ajax](#1-ajax)    
  - [2. fetch API](#2-fetch-api)    
  - [3. url 만들기](#3-url-만들기)    



## 1. Ajax
---
HTML만으로 어려운 다양한 작업을 웹페이지에서 구현해 이용자가 웹페이지와 자유롭게 상호 작용할 수 있도록 하는 기술이다. 별도 프로그램을 설치하거나 웹페이지를 다시 로딩하지 않고도 메뉴 등 화면상의 객체를 자유롭게 움직이고 다룰 수 있다. 
<br>

## 2. fetch API
---
Ajax를 구현하는 여러가지 기술이 있는데 fetch API를 사용해보자.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <input type="button" value="fetch" onclick="
    fetch('css').then(function(response){
        response.text().then(function(text){
            alert(text);
        })
    })
    ">
</body>
</html>
```
확장자없이 css라는 파일에 hello world라고 저장해두면 fetch를 이용해서 hello world를 alert에 띄울 수 있다. 
![그림1](https://backtony.github.io/assets/img/post/web/htmlcssjs/4-1.PNG)  
<br>

문법을 하나씩 살펴보자.
```js
fetch('css') // 서버에 css라는 파일을 요청
then(함수) // 서버가 응답할 때까지 다른 일을 하고, 응답이 끝나면 정의한 함수를 실행시킨다.
// 안에서 함수를 정의(익명 함수)해도 되고 밖에서 정의한 함수 이름을 넣어도 된다.

// fetch api가 함수를 실행시킬 때 함수의 첫 파라미터의 값으로
// 자동으로 response 객체가 들어간다라고 사용 설명서에 적혀있다.
// fetch를 통해 요청을 했을 때 웹서버가 응답한 결과를 담고 있는 객체 = response

// 위에 문법을 이해했으면 아래는 응용이다.
// 서버에 css파일 요청하고 응답이 끝나면 받은 response 객체를 함수의 파라미터로 넣고 실행
// response의 text를 요청하고 받은 것을 함수 파라미터 text에 넣고 함수 실행
// article이라는 태그를 찾아서 (innerHTML -> 태그 안에 html 넣는다는 뜻) text값을 태그 안에 넣어준다.
<input type="button" value="fetch" onclick="
    fetch('css').then(function(response){
        response.text().then(function(text){
            document.querySelector('article').innerHTML = text;
        })
    })
    ">
```
<br>

위를 바탕으로 전에 만들었던 실습내용을 ajax를 이용해서 한 페이지에서 구현해보자.

```html
<!doctype html>
<html>
<head>
  <title>WEB1 - HTML</title>
  <meta charset="utf-8">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="colors.js"></script>
  <script>
    function fetchPage(name){
      fetch(name).then(function(response){
          response.text().then(function(text){
            document.querySelector('article').innerHTML=text
          })
        })
    }
  </script>
</head>
<body>
  <h1><a href="index.html">WEB</a></h1>
  <input id="night_day" type="button" value="night" onclick="
    nightDayHandler(this);
  ">
  <ol>
    <li><a  onclick="fetchPage('html')">HTML</a></li>
    <li><a onclick="fetchPage('css')">CSS</a></li>
    <li><a onclick="fetchPage('JavaScript')">JavaScript</a></li>
  </ol>  
  <article style="margin-top:45px;">
  </article>
</body>
</html>
```
<Br>

## 3. url 만들기
---
한 페이지에서 동작하게 만들었기에 url이 계속 같은데 남들에게 특정 위치를 링크보내기 위해서 해시를 이용해 url을 만들어보자. 해당 페이지에 링크를 만들기 위해서는 #는 북마크 기능이기에 구분하기 위해 관습적으로 #!을 붙인다.
```html
<!doctype html>
<html>
<head>
  <title>WEB1 - HTML</title>
  <meta charset="utf-8">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="colors.js"></script>
  <script>
    function fetchPage(name){
      fetch(name).then(function(response){
          response.text().then(function(text){
            document.querySelector('article').innerHTML=text
          })
        })
    }
    if (location.hash){
      fetchPage(location.hash.substr(2));
    } else{
      fetchPage('welcome');
    }
  </script>
</head>
<body>
  <h1><a href="index.html">WEB</a></h1>
  <input id="night_day" type="button" value="night" onclick="
    nightDayHandler(this);
  ">
  <ol>
    <li><a href="#!html" onclick="fetchPage('html')">HTML</a></li>
    <li><a href="#!css" onclick="fetchPage('css')">CSS</a></li>
    <li><a href="#!javascript" onclick="fetchPage('JavaScript')">JavaScript</a></li>
  </ol>
  
  <article style="margin-top:45px;">
  </article>
</body>
</html>

<!-- javascript 파일-->
<h2>js</h2>  
<p id="#!JavaScript">additional features beyond ECMA.</p>
```
링크들에 #!를 붙여주고 해당 파일에는 태그에 id값을 부여한다. location.hash로 현재 url에 hash값이 들어오면 #!을 빼고 fetchPage의 인자로 넣어줬다.









<br>

---
__본 포스팅은 생활코딩 egoing님의 강의를 듣고 정리한 내용을 바탕으로 복습을 위해 작성하였습니다. [[강의 링크](https://opentutorials.org/course/1){:target="_blank"}]__