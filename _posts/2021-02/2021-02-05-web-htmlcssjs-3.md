---
layout: post
title:  JavaScript - 객체
subtitle:   JavaScript - 객체
categories: web
tags: htmlcssjs
comments: true
# header-img:
---

+ __목차__
  - [1. 생성과 추가](#1-생성과-추가)    
  - [2. 반복문](#2-반복문)    
  - [3. 함수](#3-함수)    
  - [4. 객체 활용](#4-객체-활용)  
  - [5. js코드 파일로 쪼개서 관리하기](#5-js코드-파일로-쪼개서-관리하기)  
  - [6. 라이브러리와 프레임워크](#6-라이브러리와-프레임워크)  
  - [7. UI와 API](#7-UI와-API)  


## 1. 생성과 추가
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
  <script>
    let coworker={
      "programmer":"backtony",
      "designer":"backtony"
    };
    coworker.bookkeeper="backtony";
    coworker["data scientist"] = "backtony";
    document.write("programmer : "+ coworker.programmer+"<br>");
    document.write("designer : "+ coworker.designer+"<br>");
    document.write("bookkeeper : "+ coworker.bookkeeper+"<br>");
    document.write("programmer : "+ coworker["data scientist"]+"<br>");
  </script>
  
</body>
</html>
```
객체의 생성은 {}로 하고 추가는 .을 이용한다. 이름에 공백을 주고 싶다면 [""]를 사용하면 된다.


<br>

## 2. 반복문
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
  <script>
    let coworker={
      "programmer":"backtony",
      "designer":"backtony",
      "bookkeeper":"backtony",
      "data scientist" : "backtony"
    };
    
    for (let key in coworker){      
      document.write("key : " + key + " value : " + coworker[key] + "<br>");
    }
  </script>
  
</body>
</html>
```
파이썬의 for문처럼 받아서 사용하면 되고 value값은 배열처럼 []로 접근하면 된다.
<br>

## 3. 함수
---
객체에 함수를 넣어보자. 객체의 이름이 변경될 수 있으므로 coworker로 대신 this로 자신이 소속되어 있는 객체를 가리키게 한다.
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    let coworker={
      "programmer":"backtony",
      "designer":"backtony",
      "bookkeeper":"backtony",
      "data scientist" : "backtony"
    };
    
    coworker.showAll = function(){
      for (let key in this){      
        if (key != 'showAll'){
          document.write("key : " + key + " value : " + this[key] + "<br>");
        }
      }
    }
    coworker.showAll();   
  </script>
  
</body>
</html>
```
<br>

## 4. 객체 활용
---
앞선 포스팅에서 사용했던 코드이다. 함수를 살펴보면 링크의 색을 바꾸는 함수로 setColor이름을 사용했다. 그런데 dayNightHandler함수 코드를 보면 폰트 색상을 바꾸는 코드와 배경을 바꾸는 코드가 있다. 사실 이렇게 명확한 기능을 가지고 있는 것은 함수로 따로 만드는게 좋은데 이때 setColor이름을 또 다시 사용할 수는 없다. 따라서 링크객체와 바디객체를 만들어서 함수를 관리해보자.
```html
<!DOCTYPE html>

<head>
  <title>web-html</title>
  <meta charset="utf-8">
  <script>
    function setColor(color) {
      let alist = document.querySelectorAll('a')
      let i = 0;
      while (i < alist.length) {
        alist[i].style.color = color;
        i++;
      }

    }
    function dayNightHandler(self) {
      let target = document.querySelector('body');
      if (self.value === 'night') {
        target.style.backgroundColor = 'black';
        target.style.color = 'white';
        self.value = 'day'

        setColor('powderblue');

      } else {
        target.style.backgroundColor = 'white';
        target.style.color = 'black';
        self.value = 'night'

        setColor('blue');
      }
    }
  </script>
</head>

<body>
  <h1><a href="index.html">WEB</a></h1>
  <input type="button" value='night' onclick="      
    dayNightHandler(this);
  ">
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
```
<br>

객체를 이용한 코드, 코드가 길어졌다고 생각할 수 있지만 지금은 단순한 경우이고 복잡해진다면 이 코드가 유지보수하기 편하고 효율적인 코드이다.
```html
<!DOCTYPE html>

<head>
  <title>web-html</title>
  <meta charset="utf-8">
  <script>
    let Links = {
      setColor: function (color) {
        let alist = document.querySelectorAll('a');
        let i = 0;
        while (i < alist.length) {
          alist[i].style.color = color;
          i++;
        }
      }
    }
    let Body ={
      setColor:function(color){
        document.querySelector('body').style.color = color;
      },
      setBackGroundColor(color){
        document.querySelector('body').style.background = color;
      }
    }

    function dayNightHandler(self) {
      let target = document.querySelector('body');
      if (self.value === 'night') {
        Body.setBackGroundColor('black') ;
        Body.setColor('white');
        self.value = 'day'

        Links.setColor('powderblue');

      } else {
        Body.setBackGroundColor('white') ;
        Body.setColor('black');       
        self.value = 'night'

        Links.setColor('blue');
      }
    }
  </script>
</head>

<body>
  <h1><a href="index.html">WEB</a></h1>
  <input type="button" value='night' onclick="      
    dayNightHandler(this);
  ">
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
```
<br>

## 5. js코드 파일로 쪼개서 관리하기
---
CSS에서 style을 파일로 따로 관리해서 사용하는 곳에 link태그를 이용해서 불러온 것처럼 사용하는 이유와 동일한 이유로 js코드도 파일로 따로 관리하는 것이 유지보수에 좋다. 위에 실습한 코드에서 script태그 안에 있는 js코드를 script태그를 제외하고 복사해서 color에 관련된 코드이니 color.js 파일에 저장했다고 하자. 이제는 사용할 때 head태그 안에 script 태그에 src=""로 파일 경로를 알려주면 사용할 수 있다. (src는 source의 약자이다.)
```html
<script src="color.js"></script>
```
<br>

## 6. 라이브러리와 프레임워크
---
+ 라이브러리 : 내가 만들고자 하는 프로그램에 필요한 부품이 되는 소프트웨어를 재사용하기 쉽도록 정리해 놓은 소프트웨어, 내가 만들고 있는 프로그램에서 사용할 부품을 가져오는 느낌
+ 프레임워크 : 만들고자 하는 것이 있을 때 언제나 필요한 공통적인 것이 있고 기획의도에 따라 달라지는 부분이 있을 것인데 공통적인 부분은 프레임워크로 만들어 놓고 만들고자 하는 기능, 개성에 따라서 달라지는 부분만 살짝살짝 수정하는 것을 통해서 우리가 만들고자 하는 것을 처음부터 끝까지 만들지 않도록 해주는 반제품과 같은 것

라이브러리는 소프트웨어를 만드는데 땡겨와서 쓰는 느낌이라면 프레임워크는 우리가 프레임워크 안에 들어가서 작업하는 느낌이다. js에서 가장 유명한 라이브러리는 jquery라는 라이브러리다. 라이브러리를 직접 다운로드해서 프로젝트에 포함시키고 업로드하는 등의 작업은 매우 번거롭다. 그래서 많은 라이브러리들이 CDN이라는 것을 통해서 자기들의 서버에다가 보관해놓고 사용자는 script src를 통해서 가져다 쓸 수 있도록 해주고 있다.

```html
<!DOCTYPE html>

<head>
  <title>web-html</title>
  <meta charset="utf-8">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="color.js"></script>
</head>

<body>
  <h1><a href="index.html">WEB</a></h1>
  <input type="button" value='night' onclick="      
    dayNightHandler(this);
  ">
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
```
위 코드처럼 내가 만든 js코드를 가져오는 코드 위에 cdn을 붙여넣고, color.js 파일에서 jquery를 이용해서 코딩할 수 있다.
```js
// color.js
let Links = {
    setColor: function (color) {
        // let alist = document.querySelectorAll('a');
        // let i = 0;
        // while (i < alist.length) {
        //     alist[i].style.color = color;
        //     i++;
        // }

        // 모든 a태그의 css수정, 'color'값을 매개인자로 들어온 color값으로
        $('a').css('color',color);
    }
}
let Body = {
    setColor: function (color) {
        //document.querySelector('body').style.color = color;
        // 모든 body태그의 css 수정
        $('body').css('color',color);
    },
    setBackGroundColor(color) {
        //document.querySelector('body').style.background = color;
        // 모든 body태그의 css 수정
        $('body').css('background',color);
    }
}

function dayNightHandler(self) {
    let target = document.querySelector('body');
    if (self.value === 'night') {
        Body.setBackGroundColor('black');
        Body.setColor('white');
        self.value = 'day'

        Links.setColor('powderblue');

    } else {
        Body.setBackGroundColor('white');
        Body.setColor('black');
        self.value = 'night'

        Links.setColor('blue');
    }
}
```

<br>

## 7. UI와 API
---
+ UI : User Interface, 사용자가 시스템을 제어하기 위해서 사용하는 조작 장치, 사용자를 위한 조작 장치
+ API : application Programming Inerface, 프로그래밍을 위한 조작장치
  - web api -> 브라우저가 제공하는, 브라우저가 이해할 수 있는 함수들,, ex) alert



<br>

---
__본 포스팅은 생활코딩 egoing님의 강의를 듣고 정리한 내용을 바탕으로 복습을 위해 작성하였습니다. [[강의 링크](https://opentutorials.org/course/1){:target="_blank"}]__