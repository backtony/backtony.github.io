---
layout: post
title:  HTML와 CSS 간단 정리
subtitle:   HTML와 CSS 간단 정리
categories: web
tags: htmlcssjs
comments: true
# header-img:
---

+ __목차__
  - [1. 태그](#1-태그)    
  - [2. 간단한 페이지 만들기](#2-간단한-페이지-만들기)    
  - [3. CSS](#3-css)    

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

## 3. CSS
---
웹페이지 안에 CSS를 삽입하는 방법은 style 태그 사용과 style 속성 사용이라는 2가지 방법이 있다.  
style 태그는 html의 문법임과 동시에 style 안쪽에 있는 내용은 CSS니까 CSS언어 문법에 맞게 처리하라라는 뜻으로 보면 된다. style 태그는 head태그 안에 작성되며, 여러 개를 한 번에 처리할 수 있다.  
style 속성은 원하는 부분에 개별적으로 처리할 때 쓰인다. style="" 안에 원하는 내용을 ;로 구분해서 적어주면 된다. 아래 예시를 보면 쉽게 이해할 수 있을 것이다.

```html
<!DOCTYPE html>
<head>
  <title>web-html</title>
  <meta charset="utf-8">
  <style>
    #power{
      color:purple;
    }
    .saw {
      color:darkcyan;
    }
    .active{
      color:blue;
    }
    a { 
      color:black;
      text-decoration: none;      
    }
    h1 {
      font-size:40px;
      text-align:center;      
    }    
  </style>
</head>
<body>
  <h1><a href="index.html">WEB</a></h1>
  <ol>
    <li> <a href="1.html" class="saw">HTML</a></li>
    <li> <a href="2.html" class="saw active" id="power">CSS</a></li>
    <li> <a href="3.html" style="color:red;text-decoration:underline">JavaScript</a></li>
  </ol>

  <h2>HTML</h2>

  <p>
    HTML 페이지에 해당하고 이에 대한 설명
  </p>

</body>
```
style 태그에서 a {} 는 모든 a태그에 대한 적용이다. 만약 어떤 2개의 태그에 동일하게 적용하고 싶으면 ,를 사용한다. 예를 들면 a,h1 {} 이렇게 말이다.  
+ text-decoration : 밑줄 속성
+ color : 색상 속성
+ font-size : 폰트 크기 속성
+ text-align : 정렬 속성
+ class : 그룹 묶기, 속성값은 여러 개 가능 -> 공백으로 구분
  - 태그가 class값을 style태그 안에서 수정할 때는 class 이름 앞에 .을 붙인다. 
+ id : class와 같은 그룹 묶기이나 우선 순위가 높다. style태그에서 # 사용


__cf) 선택자 우선순위__  
id 선택자 > class 선택자 > 태그 선택자  
선택자 우선순위에 따라 style이 적용되는데 같은 선택자끼리는 style코드 내에서 나중에 나온 설정이 덮어쓰게되어 나중에 작성한 것이 최종 적용이 된다.

<br>

### inline element, block level element
+ block level element(= 태그) : 화면 전체를 쓰는 태그
  - ex) h1 태그
+ inlint element(= 태그) : 자신의 부피만큼 쓰는 태그
  - ex) a 태그
+ display 속성으로 수정 가능  -> display:inline; display:block;

<br>

### 테두리
```html
<!DOCTYPE html>
<head>
  <title>web-html</title>
  <meta charset="utf-8">
  <style>
   h1 {
    border: 5px solid black;
    padding : 20px;
    margin: 20px;
    width : 100px;
   }
  </style>
</head>
<body>
  <h1>WEB</h1> 
  <h1>WEB</h1> 
</body>
```
+ border : 테두리 속성
  - border-color, border-width : ~~ 로 개별적으로 속성값을 줄 수도 있지만 border : 으로 순서관계없이 적어도 알아서 적용된다.
+ padding : content와 테두리 사이 여백
+ margin : 테두리와 테두리 사이 간격
+ width : block level element의 크기 변경
  - h1태그는 block level element로 화면 전체를 사용하는데 width로 수정 가능

![그림2](https://backtony.github.io/assets/img/post/web/htmlcssjs/1-2.PNG)

참고로 해당 페이지 -> 우클릭 -> 검사를 통해서 각각에 대한 속성을 style 탭에서 한 눈에 확인할 수 있다.


<br>

### 그리드
```html
<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8">
  <title></title>
  <style>
    #grid {
      border:5px solid pink;
      display: grid;
      grid-template-columns: 150px 1fr;
    }
    div {
      border: 5px solid gray;
    }
  </style>
</head>

<body>
  <div id="grid">
    <div>navigation</div>
    <div>article</div>
  </div>
</body>

</html>
```
![그림3](https://backtony.github.io/assets/img/post/web/htmlcssjs/1-3.PNG)

grid-template-columns: 150px 1fr; 에서 px은 첫번째로 묶인 navigation의 열크기를 150px로 고정시켜준 것이고 fr은 화면전체를 쓰게 자동으로 조정되는 단위로 나머지 전부 사용한다.  

아무런 의미없이 디자인의 용도로만 묶어주기 위해 사용하는 태그
+ div : block level element
+ span : inline element


<br>

### 반응형 디자인
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div{
            border:10px solid green;
            font-size: 50px;
        }
        @media(min-width: 800px){
            div{
                display: none;
            }
        }
    </style>
</head>
<body>
    <div>
        responsive
    </div>
</body>
</html>
```
+ @media(min-width: 800px) : 최소 800px부터 다음을 작동
+ @media(max-width: 800px) : 최대 800px까지 다음을 작동

<br>

### 코드의 재사용
모든 파일마다 style태그를 주면서 사용하면 수정할 때 매우 번거롭게 된다. 따라서 한 파일에 css파일을 정리해두고 link태그를 통해 css파일을 가져와서 사용한다. grid 실습 파일을 가지고 만들어보자.
```css
/* style.css */
#grid {
    border:5px solid pink;
    display: grid;
    grid-template-columns: 150px 1fr;
  }
  div {
    border: 5px solid gray;
  }
```
```html
<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8">
  <title></title>
  <link rel="stylesheet" href="style.css">  
</head>

<body>
  <div id="grid">
    <div>navigation</div>
    <div>article</div>
  </div>
</body>

</html>
```
이렇게 따로 css파일을 만들어주고 link로 가져와서 사용하면 된다.  
하나의 웹페이지에서 여러 개의 파일을 별도로 바깥에 두고 다운로드 받는 것과 웹페이지 안에 css코드를 내장하는 것 중에서 후자가 네트워크 측면에서는 효율적이다. 하지만 캐싱이라는 테크닉 때문에 그렇지 않다. 캐싱은 저장하다라는 뜻인데 한 번 style.css라는 파일을 받았다면 파일이 변경되기 전까지 웹브라우저는 이 파일을 컴퓨터에 저장해놨다가 style.css 파일을 요청하면 저장된 결과를 가져와서 사용하기에 네트워크를 안 쓰게 되어 속도를 높일 수 있다.


<br>

---
__본 포스팅은 생활코딩 egoing님의 강의를 듣고 정리한 내용을 바탕으로 복습을 위해 작성하였습니다. [[강의 링크](https://opentutorials.org/course/1){:target="_blank"}]__