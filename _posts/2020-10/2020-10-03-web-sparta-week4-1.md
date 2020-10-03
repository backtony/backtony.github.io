---
layout: post
title:  Flask
subtitle:   Flask
categories: web
tags: web webprogramming spartacodingclub
comments: true
# header-img:
---
+ __목차__
  - [1. 로컬 개발환경](#1-로컬-개발환경)
  - [2. flask 기초](#2-flask-기초)
  - [3. API 만들기](#3-api-만들기)
  

## 1. 로컬 개발환경
---
우리는 보통 컴퓨터가 1대이다. 그래서 같은 컴퓨터에다 서버를 만들고, 요청도 할 것이다. 즉, 클라이언트 = 서버가 되는 것이다. 이것을 로컬 개발환경이라고 한다. 그림으로 보면 대략 이렇다.

![그림1](https://backtony.github.io/assets/img/post/web/sparta/web-sparta-week4-1.PNG)

<br>

## 2. Flask 기초
---
### 기초 실행
Flask 프레임워크는 서버를 구동시켜주는 편한 코드 모음이다. 서버를 구동하려면 필요한 복잡한 일들을 쉽게 가져다 쓸 수 있게 하는 것이다. Flask 기본 시작 코드는 아래와 같다.

```python
from flask import Flask # flask를 쓸 것이다.

app = Flask(__name__) # Flask라는 것을 뭔가 만들어서 app에 담았다.


# 타입이 다르면 '/'뒤에 오는 것이 같아도 된다.
# 함수의 이름은 같으면 안된다.
@app.route('/') # URL 분리
def home():
    return 'This is Home!'

@app.route('/mypage') # URL 분리
def mypage():
    return 'This is mypage!'


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True) # 서버 돌리기

# 이 아래다가 작성시 정상 동작되지 않음.
```
코드를 실행하고 localhost:5000 을 주소창에 입력시 내가 만든 서버를 확인할 수 있다.
<br>

### 기본 폴더 구조
프레임워크라고 하는 것은 기본적으로 남이 만들어 놓은 틀 안에서 내가 하는 것이기 때문에 편한 것이다. 그래서 남이 만들어 놓은 규칙들을 지켜줘야 한다.

__기본 폴더 구조로 아래 3개가 필수__  
+ static 폴더 : 이미지나 css파일과 같은 파일을 담아두는 역할
+ templates 폴더 : html 파일을 담아두고, 불러오는 역할
    - 보통 메인 페이지를 index.html 로 만들어 둔다.
    - html은 프론트엔드 app.py는 서버를 생각하면 이해가 쉽다.
+ app.py 파일



#### html 파일 불러오기
flask 내장함수 render_template를 이용해서 templates 폴더에 있는 index.html파일을 불러온다.
```python
# app.py
from flask import Flask, render_template 

app = Flask(__name__) 

@app.route('/') # URL 분리
def home():
    return render_template('index.html') # html파일 불러오기

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True) # 서버 돌리기
```

#### 이미지 파일 불러오기
html 파일은 flask에서 읽어주기 때문에 flask에 미리 정의된 방법으로 경고를 입력해줘야한다. 서버를 만들었다 아래에 이미지를 불러와보자.
```html
<!--index.html-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <title>Document</title>
</head>
<body>
    <h1>서버를 만들었다!</h1>
    {% raw %}<img src="{{ url_for('static', filename='파일명.jpg') }}"/> {% endraw %}
</body>
</html>
```
여기까지는 html을 주는 flask의 역할을 본 것이다. 하지만 사실 서버의 역할은 데이터를 받고 주는 역할이 더 크다. 아래서는 이것을 다루겠다.  
<br>

## 3. API 만들기
---
API는 은행의 창구와 같다고 했었다. 같은 예금 창구에서도 개인 고객이냐 기업 고객이냐에 따라 처리하는 것이 다른 것처럼, 클라이언트가 요청할 때에도 '방식'이 존재한다. 클라이언트는 요청할 때 HTTP request method(요청 메소드)를 통해, 어떤 요청 종류인지 응답하는 서버 쪽에 정보를 알려줘야 한다.  
+ .GET : 통상적으로 데이터 조회(Read)를 요청할 때 사용한다.
    - 데이터 전달 : URL 뒤에 물음표를 붙여 key=value 의 형태로 전달 ex)google.com?q=북극곰
+ POST : 통상적으로 데이터 생성, 변경, 삭제 요청할 때 사용한다.
    - 데이터 전달 : 바로 보이지 않는 HTML body에 key:value 형태로 전달


예를 들어, 클라이언트에서 서버에 title_give란 키 값으로 데이터를 들고왔다고 생각해보자. (주민등록번호 라는 키 값으로 850120- .. 을 가져온 것과 같은 의미)  
받은 값을 개발자가 볼 수 있게 print 로 찍어볼 수 있게 했다. 실전에선 print로 찍어주는 것 외에, 여러가지 작업을 할 수 있다.  

__GET, POST 방식의 API 사용법__  
```python
from flask import Flask, render_template, request, jsonify

app = Flask(__name__) # Flask라는 것을 뭔가 만들어서 app에 담았다.

@app.route('/') # URL 분리
def home():
    return render_template('index.html')

@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give') # title_give라는 키로 가지고 온 데이터가 있나 찾아보고 receive에 대입
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'}) # 해당 딕셔너리를 json형식으로 반환해라 그럼 해당 내용이 response로 들어감

@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True) # 서버 돌리기
```
위의 코드는 서버에 해당하는 코드이고 아래는 클라이언트에 해당하는 코드이다. 아래는 크롬 검사탭에서 수행해보자.  

```python
$.ajax({
    type: "GET",
    url: "/test?title_give=봄날은간다", # 여기서 ajax는 title_give라는 키에 봄날은 간다라는 value를 준것
    data: {},
    success: function(response){
       console.log(response)
    }
  })


$.ajax({
    type: "POST",
    url: "/test",
    data: { title_give:'봄날은간다' }, # 가져갈땐 title, 즉 key에 따옴표가 없다.
    success: function(response){
       console.log(response)
    }
  })
```
위의 코드를 풀어서 설명하면 다음과 같다.  
+ GET : 클라이언트에서 ajax를 통해 서버로 요청하는데 key를 title_give value를 봄날은 간다라고 줬다. 서버에서는 request.args.get('title_give')을 통해 데이터를 찾아보고 title_recieve에 대입하고 찍어본다. 그리고 해당 딕셔너리를 json형식으로 반환한다. 그럼 그것은 클라이언트의 response에 들어가고 console.log로 찍어낸다. 
+ POST : GET과 다른 점은 url로 데이터 전달이 아니라 data로 데이터 전달을 하며 키에 따옴표가 없다는 점을 기억하고 다른 과정은 같다.

