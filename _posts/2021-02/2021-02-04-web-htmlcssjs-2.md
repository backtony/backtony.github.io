---
layout: post
title:  JavaScript와 HTML
subtitle:   JavaScript와 HTML
categories: web
tags: htmlcssjs
comments: true
# header-img:
---

+ __목차__
  - [1. Script 태그](#1-script-태그)    
  - [2. 이벤트](#2-이벤트)    
  - [3. 콘솔](#3-콘솔)    


## 1. Script 태그
---
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>JavaScript</h1>
    <script>
        document.write('hello world');
    </script>  
</body>
</html>
```
html 문법 사이에 <script></script> 태그를 사용해주면 태그 안에서는 js코드를 사용할 수 있다.
<br>

## 2. 이벤트
---
웹브라우저 위에서 일어나는 일들을 사건, 이벤트라고 한다. 어떠한 이벤트가 일어났을 때 어떠한 js코드가 실행되도록 하는 속성들이 있다. 
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>JavaScript</h1>    
    <input type="button" value="hi" onclick="alert('hi')">
    <input type="text" onchange="alert('changed')">
    <input type="text" onkeydown="alert('keydown')">      
</body>
</html>
```
+ type값으로 button을 주면 버튼이 생성되고 value는 버튼 안에 들어가는 텍스트내용이다. onclick은 버튼을 누르는 이벤트가 발생하면 뒤에 적힌 js코드가 실행된다.
+ type값으로 text를 주면 텍스트입력창이 생성된다. onchange는 텍스트창에 입력하고 다른 페이지로 나가면 해당 js코드가 동작하고, onkeydown은 키를 입력하면 js코드가 동작한다.

웹브라우저 위에서 일어나는 여러가지 이벤트들을 onXXX를 이용해 사용자와 상호작용하는 코드를 만들 수 있다.
<br>

## 3. 콘솔
---
![그림1](https://backtony.github.io/assets/img/post/web/htmlcssjs/2-1.PNG)

웹브라우저에서 검사를 클릭하고 콘솔창에서 js코드를 작성하면 해당 페이지를 대상으로 js코드가 작동한다. 추가로 위 방향키를 누르면 전에 작성했던 코드를 바로 불러올 수 있다.






<br>

---
__본 포스팅은 생활코딩 egoing님의 강의를 듣고 정리한 내용을 바탕으로 복습을 위해 작성하였습니다. [[강의 링크](https://opentutorials.org/course/1){:target="_blank"}]__