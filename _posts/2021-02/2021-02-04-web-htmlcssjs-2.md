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
  - [4. 제어할 태그 선택하기](#4-제어할-태그-선택하기) 
  - [5. 리팩토링](#5-리팩토링)



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

## 4. 제어할 태그 선택하기
---
```html
<!DOCTYPE html>
<head>
  <title>web-html</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.html">WEB</a></h1>
  <input type="button" value = 'night' onclick="
    document.querySelector('body').style.backgroundColor ='black';
    document.querySelector('body').style.color = 'white';    
  ">
  <input type="button" value = 'day' onclick="
     document.querySelector('body').style.backgroundColor ='white';
    document.querySelector('body').style.color = 'black';    
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
버튼을 클릭하는 이벤트가 발생하면 동적으로 화면에 변화를 주려고 하는 코드이다. onclick=""에는 js코드가 와야한다고 했다. js코드를 그대로 해석해보면 doucument 화면에서(문서에서) 태그를 선택한다 body라는, 스타일을 줄건데 backgroundcolor라는 배경색을 준다라고 해석하면 된다. querySelector에서 인자로 태그를 줬으니 그냥 body인 것이고 만약 class면 .을 붙이고 id면 #을 붙이면 된다. 위 코드의 화면은 아래와 같다.
![그림2](https://backtony.github.io/assets/img/post/web/htmlcssjs/2-2.PNG)


<br>

### if문으로 개선하기
![그림3](https://backtony.github.io/assets/img/post/web/htmlcssjs/2-3.PNG)

day,night를 버튼 하나로 만들어서 사용해보자.
```html
<!DOCTYPE html>

<head>
  <title>web-html</title>
  <meta charset="utf-8">
</head>

<body>
  <h1><a href="index.html">WEB</a></h1>
  <input id='day_night' type="button" value='night' onclick="
    if (document.querySelector('#day_night').value==='night') {
      document.querySelector('body').style.backgroundColor ='black';
      document.querySelector('body').style.color = 'white';    
      document.querySelector('#day_night').value ='day'
    } else {
      document.querySelector('body').style.backgroundColor ='white';
      document.querySelector('body').style.color = 'black';    
      document.querySelector('#day_night').value ='night'
    }
    
  "> 
  <ol>
    <li> <a href="1.html">HTML</a></li>
    <li> <a href="2.html">CSS</a></li>
    <li> <a href="3.html">JavaScript</a></li>
  </ol>

  <h2>HTML</h2>
  <script>
    document.write(1 == 1);
  </script>

  <p>
    HTML 페이지에 해당하고 이에 대한 설명
  </p>

</body>
```
if문을 활용하여 버튼 하나로 컨트롤 할 수 있도록 만들었다. input 태그에 id값을 주고 querySelector로 id값을 선택해서 value값을 가져와서 사용하고 수정했다.  
<br>

__cf) js에서 ==와 ===__  
js에는 다른 언어와 달리 === 연산자가 존재한다. == 연산자는 동등 연산자로, 피연산자가 서로 다른 타입이면 타입을 강제 형변환하여 비교한다. 하지만 === 연산자는 일치 연산자로, 두 피연산자를 더 정확하게 비교한다.
```javascript
0 == '' // true
0 == '0' // true
1 == true // true

0 === '' // false
0 === false // false
1 === true // false
```
<br>

## 5. 리팩토링
---
코드 자체를 효율적으로 만들어서 가독성을 높이고 유지보수가 편리하게 만들고 중복된 코드를 줄여 개선하는 작업을 말한다. 위의 실습을 리팩토링해보자.  
+ document.querySelector('body')가 중복되므로 변수로 받아서 사용
+ onclick의 이벤트가 발생했을 때 실행되는 js코드가 onclick이 있는 태그, 즉 현재 js가 포함되어있는 태그를 가리킬 때는 선택자를 사용하지 않고 this.를 사용하면 훨씬 더 효율적이다.

```html
<!DOCTYPE html>

<head>
  <title>web-html</title>
  <meta charset="utf-8">
</head>

<body>
  <h1><a href="index.html">WEB</a></h1>
  <input type="button" value='night' onclick="
    var target = document.querySelector('body');
    if (this.value==='night') { // document.querySelector('body')의 중복을 변수로 받아서 줄임
      target.style.backgroundColor ='black';
      target.style.color = 'white';    
      this.value ='day' 
      // querySelector로 id 선택자 day_night를 선택했었는데 해당 선택자는 현재 js코드가 포함된 태그를 가리키므로 this.로 변경
      // this로 교체한 상황에서 현재 굳이 id 선택자의 필요성이 사라졌으므로 id선택자 삭제
    } else {             
      target.style.backgroundColor ='white';
      target.style.color = 'black';    
      this.value ='night'
    }
    
  "> 
  <ol>
    <li> <a href="1.html">HTML</a></li>
    <li> <a href="2.html">CSS</a></li>
    <li> <a href="3.html">JavaScript</a></li>
  </ol>

  <h2>HTML</h2>
  <script>
    document.write(1 == 1);
  </script>

  <p>
    HTML 페이지에 해당하고 이에 대한 설명
  </p>

</body>
```
<Br>

## 6. 반복문과 배열 활용
---
![그림4](https://backtony.github.io/assets/img/post/web/htmlcssjs/2-4.PNG)

night 상황에서 a태그들의 폰트 색상이 어두워서 잘 보이지 않는다. 반복문과 배열을 통해 수정해보자.  
querySelector는 처음 나오는 것 하나를 가져오는 것이고, querySelectorAll은 전체 태그를 가져온다. 반환값을 배열처럼 사용하면 된다.

```html
<!DOCTYPE html>

<head>
  <title>web-html</title>
  <meta charset="utf-8">
</head>

<body>
  <h1><a href="index.html">WEB</a></h1>
  <input type="button" value='night' onclick="
    var target = document.querySelector('body');
    if (this.value==='night') { 
      target.style.backgroundColor ='black';
      target.style.color = 'white';    
      this.value ='day' 

      var alist = document.querySelectorAll('a') // querySelectorAll은 모든 a태그를 가져오는데 정확하게 배열은 아니지만 일단 배열로 가져온다고 생각
      var i=0;
      while(i<alist.length){
        alist[i].style.color = 'powderblue';
        i++;
      }
    } else {            
      target.style.backgroundColor ='white';
      target.style.color = 'black';    
      this.value ='night'
      
      var alist = document.querySelectorAll('a') 
      var i=0;
      while(i<alist.length){
        alist[i].style.color = 'blue';
        i++;
      }
    }
    
  "> 
  <ol>
    <li> <a href="1.html">HTML</a></li>
    <li> <a href="2.html">CSS</a></li>
    <li> <a href="3.html">JavaScript</a></li>
  </ol>

  <h2>HTML</h2>
  <script>
    var a=1;
    while (a<3){
      document.write(a +'<br>');
      a ++;
    }
  </script>

  <p>
    HTML 페이지에 해당하고 이에 대한 설명
  </p>

</body>
```
<br>

## 7. 함수 활용
---
함수는 리팩토링에서 중요한 수단이다. 위에서 만든 버튼이 만약 1억개일 때, 수정하려면 1억번을 수정해야하고, 같은 내용을 중복하는 비효율적 사태가 벌어진다. 이것을 함수로 해결할 수 있다.  
head 태그 안에 js코드를 사용하겠다고 script태그를 써주고 함수라는 의미의 function을 적어주고 나머지 동작방법은 다른 언어와 같다. 위 코드와 바뀐점이 하나 더 있는데 this를 self로 바꿨다. this는 onclick이 포함된 자신 태그를 가리켰는데 함수로 빼오면서 this를 사용할 수 없게된 것이다. 따라서 함수 인자로 this를 넘겨주고 코드를 this에서 인자로 수정해준 것이다.
```html
<!DOCTYPE html>

<head>
  <title>web-html</title>
  <meta charset="utf-8">
  <script>
    function setColor(color) {
      var alist = document.querySelectorAll('a')
      var i = 0;
      while (i < alist.length) {
        alist[i].style.color = color;
        i++;
      }

    }
    function dayNightHandler(self) {
      var target = document.querySelector('body');
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

---
__본 포스팅은 생활코딩 egoing님의 강의를 듣고 정리한 내용을 바탕으로 복습을 위해 작성하였습니다. [[강의 링크](https://opentutorials.org/course/1){:target="_blank"}]__