---
layout: post
title:  HTML
subtitle:   HTML
categories: web
tags: htmlcssjs
comments: true
# header-img:
---

+ __목차__
  - [1. 태그](#1-태그)    
  - [2. 간단한 페이지 만들기](#2-간단한-페이지-만들기)    


## 1. 태그
---

### 굵게 strong
```html
<strong>hello web</strong>
```
<br>

### 밑줄 u
```html
<u>hello web</u>
```
<br>

### 제목 h1~h6
```html
<h1> 제목 </h1>
<h6> 제목 </h6>
```
1에서 6으로 갈수록 크기가 작아진다.
<br>

### 줄바꿈 br
```html
이 줄 다음에 줄바꿈 한다. <br>
```
<br>

### 단락구분 p
```html
<p>이 것은 한 단락으로 구분한다</p>
```
자동으로 마지막줄 공백 나눈다.
<br>

### 이미지 img
```html
<img src="url입력">
```
<Br>

### 목차 li
+ 부모태그 ul : unordered list
+ 부모태그 ol : ordered list

부모태그끼리 구분되어 실제 출력시 공백으로 목차끼리 구분된다. ol의 경우는 자동으로 순번이 붙는다.
```html
<ul>
  <li>1. html</li>
  <li>2. css</li>
  <li>3. javascript</li>
</ul>

<ul>
  <li>1. html</li>
  <li>2. css</li>
  <li>3. javascript</li>
</ul>

<ol>
  <li>html</li>
  <li>css</li>
  <li>javascript</li>
</ol>
```
<br>

### 타이틀 title
```html
<title>web1 - html</title>
```
브라우저 맨 위에 탭 이름에 해당하는 것
<br>

### 링크 a
```html
<a href="url입력"> 링크 걸어줄 내용 </a>
<a href="url입력" traget="_blank"> 링크내용 새창으로 열기 </a>
<a href="url입력" title ="네이버로 이동"> 마우스 올리면 설명뜨게 하기 </a>
```
<br>

### utf-8로 문서 읽기
```html
<meta charset="UTF-8">
```
head 태그 안에 작성해야 하고 문서를 읽을 때 utf-8로 읽도록 지정

<Br>

### html파일 표시하기
문서 맨 위에 작성하고 파일이 html로 작성되었음을 알림
```html
<!doctype html>
```

<br>

### 동영상 삽입 iframe
```html
<iframe src="url">

<!-- 유튜브에서 복사한 코드 -->
<iframe width="560" height="315" src="https://www.youtube.com/embed/7T7r_oSp0SE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```


## 2. 간단한 페이지 만들기
---
![그림1](https://backtony.github.io/assets/img/post/web/htmlcssjs/1-1.PNG)
```html
<!-- 메인 페이지, index.html-->
<!DOCTYPE html>
<head>
  <title>web-welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.html">WEB</a></h1>
  <ol>
    <li> <a href="1.html">HTML</a></li>
    <li> <a href="2.html">CSS</a></li>
    <li> <a href="3.html">JavaScript</a></li>
  </ol>

  <h2>WEB</h2>

  <p>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/7T7r_oSp0SE" frameborder="0" allow="accelerometer;
   autoplay; clipboard-write; encrypted-media; gyroscope; 
   picture-in-picture" allowfullscreen></iframe>
  </p>
  <p>
    welcome 페이지에 해당하고 web에 관련된 내용에 대한 설명이 들어갑니다.
  </p>

</body>

<!-- 1.html-->
<!DOCTYPE html>
<head>
  <title>web-html</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.html">WEB</a></h1>
  <ol>
    <li> <a href="1.html">HTML</a></li>
    <li> <a href="2.html">CSS</a></li>
    <li> <a href="3.html">JavaScript</a></li>
  </ol>

  <h2>HTML</h2>

  <p>
    HTML 페이지에 해당하고 이에 대한 설명
  </p>

</body>

<!-- 2.html-->

<!DOCTYPE html>
<head>
  <title>web-css</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.html">WEB</a></h1>
  <ol>
    <li> <a href="1.html">HTML</a></li>
    <li> <a href="2.html">CSS</a></li>
    <li> <a href="3.html">JavaScript</a></li>
  </ol>

  <h2>CSS</h2>

  <p>
    CSS 페이지에 해당하고 이에 대한 설명
  </p>

</body>

<!-- 3.html-->
<!DOCTYPE html>
<head>
  <title>web-js</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.html">WEB</a></h1>
  <ol>
    <li> <a href="1.html">HTML</a></li>
    <li> <a href="2.html">CSS</a></li>
    <li> <a href="3.html">JavaScript</a></li>
  </ol>

  <h2>JavaScript</h2>

  <p>
    js 에 대한 페이지로 이에 대한 설명
  </p>

</body>
```




<br>

---
__본 포스팅은 생활코딩 egoing님의 강의를 듣고 정리한 내용을 바탕으로 복습을 위해 작성하였습니다. [[강의 링크](https://opentutorials.org/course/3084){:target="_blank"}]__