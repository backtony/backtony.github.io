---
layout: post
title:  API 실습2 - 나홀로메모장
subtitle:   API 실습2 - 나홀로메모장
categories: web
tags: web webprogramming spartacodingclub
comments: true
# header-img:
---
+ __목차__
  - [1. 문제](#1-문제)
  - [2. API 설계하기](#2-api-설계하기)
  - [3. 실습](#3-실습)

## 1. 문제
---
[완성 예시 클릭](http://spartacodingclub.shop/){: target="_blank"}  
url과 코멘트를 넣고 기사저장을 하면 자동으로 크롤링해와서 DB에 넣고 쭉쭉 카드를 형성하는 페이지를 만들어보자.  
```python
# app.py 준비된 뼈대
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/memo', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result':'success', 'msg':'GET 연결되었습니다!'})

## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
		# 1. 클라이언트로부터 데이터를 받기
		# 2. meta tag를 스크래핑하기
		# 3. mongoDB에 데이터 넣기
    return jsonify({'result': 'success', 'msg':'POST 연결되었습니다!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
```
```html
<!Doctype html>
<html lang="ko">

    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
              integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
              crossorigin="anonymous">

        <!-- JS -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
                integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
                crossorigin="anonymous"></script>

        <!-- 구글폰트 -->
        <link href="https://fonts.googleapis.com/css?family=Stylish&display=swap" rel="stylesheet">


        <title>스파르타코딩클럽 | 나홀로 메모장</title>

        <!-- style -->
        <style type="text/css">
            * {
                font-family: "Stylish", sans-serif;
            }

            .wrap {
                width: 900px;
                margin: auto;
            }

            .comment {
                color: blue;
                font-weight: bold;
            }

            #post-box {
                width: 500px;
                margin: 20px auto;
                padding: 50px;
                border: black solid;
                border-radius: 5px;
            }
        </style>
        <script>
            $(document).ready(function () {
                $("#cards-box").html("");
                showArticles();
            });
            
            function openClose() {
                // id 값 post-box의 display 값이 block 이면(= 눈에 보이면)
                if ($("#post-box").css("display") == "block") {
                    // post-box를 가리고
                    $("#post-box").hide();
                    // 다시 버튼을 클릭하면, 박스 열기를 할 수 있게 텍스트 바꿔두기
                    $("#btn-post-box").text("포스팅 박스 열기");
                } else {
                    // 아니면(눈에 보이지 않으면) post-box를 펴라
                    $("#post-box").show();
                    // 다시 버튼을 클릭하면, 박스 닫기를 할 수 있게 텍스트 바꿔두기
                    $("#btn-post-box").text("포스팅 박스 닫기");
                }
            }

            function postArticle() {
                $.ajax({
                    type: "POST",
                    url: "/memo",
                    data: {},
                    success: function (response) { // 성공하면
                        if (response["result"] == "success") {
                            alert(response["msg"]);
                        }
                    }
                })
            }

            function showArticles() {
                $.ajax({
                    type: "GET",
                    url: "/memo",
                    data: {},
                    success: function (response) {
                        if (response["result"] == "success") {
                            alert(response["msg"]);
                        }
                    }
                })
            }

            function makeCard(url, title, desc, comment, image) {

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
                    <button onclick="openClose()" id="btn-post-box" type="button" class="btn btn-primary">포스팅 박스 열기
                    </button>
                </p>
            </div>
            <div id="post-box" class="form-post" style="display:none">
                <div>
                    <div class="form-group">
                        <label for="post-url">아티클 URL</label>
                        <input id="post-url" class="form-control" placeholder="">
                    </div>
                    <div class="form-group">
                        <label for="post-comment">간단 코멘트</label>
                        <textarea id="post-comment" class="form-control" rows="2"></textarea>
                    </div>
                    <button type="button" class="btn btn-primary" onclick="postArticle()">기사저장</button>
                </div>
            </div>
            <div id="cards-box" class="card-columns">
                <div class="card">
                    <img class="card-img-top"
                         src="https://www.eurail.com/content/dam/images/eurail/Italy%20OCP%20Promo%20Block.adaptive.767.1535627244182.jpg"
                         alt="Card image cap">
                    <div class="card-body">
                        <a href="#" class="card-title">여기 기사 제목이 들어가죠</a>
                        <p class="card-text">기사의 요약 내용이 들어갑니다. 동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라만세 무궁화 삼천리 화려강산...</p>
                        <p class="card-text comment">여기에 코멘트가 들어갑니다.</p>
                    </div>
                </div>
                <div class="card">
                    <img class="card-img-top"
                         src="https://www.eurail.com/content/dam/images/eurail/Italy%20OCP%20Promo%20Block.adaptive.767.1535627244182.jpg"
                         alt="Card image cap">
                    <div class="card-body">
                        <a href="#" class="card-title">여기 기사 제목이 들어가죠</a>
                        <p class="card-text">기사의 요약 내용이 들어갑니다. 동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라만세 무궁화 삼천리 화려강산...</p>
                        <p class="card-text comment">여기에 코멘트가 들어갑니다.</p>
                    </div>
                </div>
                <div class="card">
                    <img class="card-img-top"
                         src="https://www.eurail.com/content/dam/images/eurail/Italy%20OCP%20Promo%20Block.adaptive.767.1535627244182.jpg"
                         alt="Card image cap">
                    <div class="card-body">
                        <a href="#" class="card-title">여기 기사 제목이 들어가죠</a>
                        <p class="card-text">기사의 요약 내용이 들어갑니다. 동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라만세 무궁화 삼천리 화려강산...</p>
                        <p class="card-text comment">여기에 코멘트가 들어갑니다.</p>
                    </div>
                </div>
                <div class="card">
                    <img class="card-img-top"
                         src="https://www.eurail.com/content/dam/images/eurail/Italy%20OCP%20Promo%20Block.adaptive.767.1535627244182.jpg"
                         alt="Card image cap">
                    <div class="card-body">
                        <a href="#" class="card-title">여기 기사 제목이 들어가죠</a>
                        <p class="card-text">기사의 요약 내용이 들어갑니다. 동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라만세 무궁화 삼천리 화려강산...</p>
                        <p class="card-text comment">여기에 코멘트가 들어갑니다.</p>
                    </div>
                </div>
                <div class="card">
                    <img class="card-img-top"
                         src="https://www.eurail.com/content/dam/images/eurail/Italy%20OCP%20Promo%20Block.adaptive.767.1535627244182.jpg"
                         alt="Card image cap">
                    <div class="card-body">
                        <a href="#" class="card-title">여기 기사 제목이 들어가죠</a>
                        <p class="card-text">기사의 요약 내용이 들어갑니다. 동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라만세 무궁화 삼천리 화려강산...</p>
                        <p class="card-text comment">여기에 코멘트가 들어갑니다.</p>
                    </div>
                </div>
                <div class="card">
                    <img class="card-img-top"
                         src="https://www.eurail.com/content/dam/images/eurail/Italy%20OCP%20Promo%20Block.adaptive.767.1535627244182.jpg"
                         alt="Card image cap">
                    <div class="card-body">
                        <a href="#" class="card-title">여기 기사 제목이 들어가죠</a>
                        <p class="card-text">기사의 요약 내용이 들어갑니다. 동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라만세 무궁화 삼천리 화려강산...</p>
                        <p class="card-text comment">여기에 코멘트가 들어갑니다.</p>
                    </div>
                </div>
            </div>
        </div>
    </body>

</html>
```
<br>

## 2. API 설계하기
---
### 포스팅 API - 카드 생성
+ 요청 정보
  - 요청 URL = /memo, 요청 방식 = POST
  - 요청 데이터 : url, 코멘트
+ 서버가 제공할 기능
  - URL의 META태그 정보를 바탕으로 제목, 설명, 이미지 url 스크래핑
  - 해당 정보를 모두 DB에 저장
+ 응답 데이터
  - API가 정상적으로 작동하는지 클라이언트에게 알려주기 위해서 성공 메시지 보내기
  - JSON 형식, 'result' = 'success'

### 리스팅 API - 저장된 카드 보여주기
+ 요청 정보
  - 요청 URL = /memo, 요청 방식 = GET
  - 요청 데이터 : 없음
+ 서버가 제공할 기능
  - DB에 저장돼있는 모든 정보를 가져오기
+ 응답 데이터
  - API 동작 잘했다는 성공 메시지, 기사들의 정보
  - JSON 형식, 'result' = 'success', 'articles':아티클 정보

### meta 태그 스크래핑
메타 태그는 <head></head> 부분에 들어가는, 눈으로 보이는 것(body) 외에 사이트 속성을 설명해주는 태그들이다. ex) 구글 검색 시 표시 될 설명문, 사이트 제목, 카톡 공유 시 표시 될 이미지 등  
__스크래핑__  
```python
# soup.select_one('태그이름[속성]')
og_image = soup.select_one('meta[property="og:image"]')
```
<br>

## 3. 실습
---
```python
# app.py
from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta_ninework  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/memo', methods=['POST'])
def post_article():
    # 1. 클라이언트로부터 데이터를 받기
    url_receive = request.form['url_give']  # 클라이언트로부터 url을 받는 부분
    comment_receive = request.form['comment_give']  # 클라이언트로부터 comment를 받는 부분

    # 2. meta tag를 스크래핑하기
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')
    og_description = soup.select_one('meta[property="og:description"]')

    url_title = og_title['content']
    url_description = og_description['content']
    url_image = og_image['content']

    article = {'url': url_receive, 'title': url_title, 'desc': url_description, 'image': url_image,
               'comment': comment_receive}

    # 3. mongoDB에 데이터를 넣기
    db.articles.insert_one(article)

    return jsonify({'result': 'success'})


@app.route('/memo', methods=['GET'])
def read_articles():
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기 (Read)
    result = list(db.articles.find({}, {'_id': 0}))
    # 2. articles라는 키 값으로 article 정보 보내주기
    return jsonify({'result': 'success', 'articles': result})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
```

```html
<!-- index.html -->
<!Doctype html>
<html lang="ko">

    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
              integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
              crossorigin="anonymous">

        <!-- JS -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
                integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
                crossorigin="anonymous"></script>

        <!-- 구글폰트 -->
        <link href="https://fonts.googleapis.com/css?family=Stylish&display=swap" rel="stylesheet">


        <title>스파르타코딩클럽 | 나홀로 메모장</title>

        <!-- style -->
        <style type="text/css">
            * {
                font-family: "Stylish", sans-serif;
            }

            .wrap {
                width: 900px;
                margin: auto;
            }

            .comment {
                color: blue;
                font-weight: bold;
            }

            #post-box {
                width: 500px;
                margin: 20px auto;
                padding: 50px;
                border: black solid;
                border-radius: 5px;
            }
        </style>
        <script>
            $(document).ready(function () {
                $("#cards-box").html("");
                showArticles();
            });

            function openClose() {
                // id 값 post-box의 display 값이 block 이면(= 눈에 보이면)
                if ($("#post-box").css("display") == "block") {
                    // post-box를 가리고
                    $("#post-box").hide();
                    // 다시 버튼을 클릭하면, 박스 열기를 할 수 있게 텍스트 바꿔두기
                    $("#btn-post-box").text("포스팅 박스 열기");
                } else {
                    // 아니면(눈에 보이지 않으면) post-box를 펴라
                    $("#post-box").show();
                    // 다시 버튼을 클릭하면, 박스 닫기를 할 수 있게 텍스트 바꿔두기
                    $("#btn-post-box").text("포스팅 박스 닫기");
                }
            }

            function postArticle() {
                let url = $("#post-url").val();
                let comment = $("#post-comment").val();

                // 2. memo에 POST 방식으로 메모 생성 요청하기
                $.ajax({
                    type: "POST", // POST 방식으로 요청하겠다.
                    url: "/memo", // /memo라는 url에 요청하겠다.
                    data: {url_give: url, comment_give: comment}, // 데이터를 주는 방법
                    success: function (response) { // 성공하면
                        if (response["result"] == "success") {
                            alert("포스팅 성공!");
                            // 3. 성공 시 페이지 새로고침하기
                            window.location.reload();
                        } else {
                            alert("서버 오류!")
                        }
                    }
                })
            }

            function showArticles() {
                $.ajax({
                    type: "GET",
                    url: "/memo",
                    data: {},
                    success: function (response) {
                        let articles = response["articles"];
                        console.log(articles);
                        for (let i = 0; i < articles.length; i++) {
                            makeCard(articles[i]["image"], articles[i]["url"], articles[i]["title"], articles[i]["desc"], articles[i]["comment"]);
                        }
                    }
                })
            }

            function makeCard(image, url, title, desc, comment) {
                let tempHtml = `<div class="card">
                        <img class="card-img-top" src="${image}" alt="Card image cap">
                        <div class="card-body">
                        <a href="${url}" target="_blank" class="card-title">${title}</a>
                        <p class="card-text">${desc}</p>
                        <p class="card-text comment">${comment}</p>
                        </div>
                    </div>`;
                $("#cards-box").append(tempHtml);

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
                    <button onclick="openClose()" id="btn-post-box" type="button" class="btn btn-primary">포스팅 박스 열기
                    </button>
                </p>
            </div>
            <div id="post-box" class="form-post" style="display:none">
                <div>
                    <div class="form-group">
                        <label for="post-url">아티클 URL</label>
                        <input id="post-url" class="form-control" placeholder="">
                    </div>
                    <div class="form-group">
                        <label for="post-comment">간단 코멘트</label>
                        <textarea id="post-comment" class="form-control" rows="2"></textarea>
                    </div>
                    <button type="button" class="btn btn-primary" onclick="postArticle()">기사저장</button>
                </div>
            </div>
            <div id="cards-box" class="card-columns">
                <div class="card">
                    <img class="card-img-top"
                         src="https://www.eurail.com/content/dam/images/eurail/Italy%20OCP%20Promo%20Block.adaptive.767.1535627244182.jpg"
                         alt="Card image cap">
                    <div class="card-body">
                        <a href="#" class="card-title">여기 기사 제목이 들어가죠</a>
                        <p class="card-text">기사의 요약 내용이 들어갑니다. 동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라만세 무궁화 삼천리 화려강산...</p>
                        <p class="card-text comment">여기에 코멘트가 들어갑니다.</p>
                    </div>
                </div>
                <div class="card">
                    <img class="card-img-top"
                         src="https://www.eurail.com/content/dam/images/eurail/Italy%20OCP%20Promo%20Block.adaptive.767.1535627244182.jpg"
                         alt="Card image cap">
                    <div class="card-body">
                        <a href="#" class="card-title">여기 기사 제목이 들어가죠</a>
                        <p class="card-text">기사의 요약 내용이 들어갑니다. 동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라만세 무궁화 삼천리 화려강산...</p>
                        <p class="card-text comment">여기에 코멘트가 들어갑니다.</p>
                    </div>
                </div>
                <div class="card">
                    <img class="card-img-top"
                         src="https://www.eurail.com/content/dam/images/eurail/Italy%20OCP%20Promo%20Block.adaptive.767.1535627244182.jpg"
                         alt="Card image cap">
                    <div class="card-body">
                        <a href="#" class="card-title">여기 기사 제목이 들어가죠</a>
                        <p class="card-text">기사의 요약 내용이 들어갑니다. 동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라만세 무궁화 삼천리 화려강산...</p>
                        <p class="card-text comment">여기에 코멘트가 들어갑니다.</p>
                    </div>
                </div>
                <div class="card">
                    <img class="card-img-top"
                         src="https://www.eurail.com/content/dam/images/eurail/Italy%20OCP%20Promo%20Block.adaptive.767.1535627244182.jpg"
                         alt="Card image cap">
                    <div class="card-body">
                        <a href="#" class="card-title">여기 기사 제목이 들어가죠</a>
                        <p class="card-text">기사의 요약 내용이 들어갑니다. 동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라만세 무궁화 삼천리 화려강산...</p>
                        <p class="card-text comment">여기에 코멘트가 들어갑니다.</p>
                    </div>
                </div>
                <div class="card">
                    <img class="card-img-top"
                         src="https://www.eurail.com/content/dam/images/eurail/Italy%20OCP%20Promo%20Block.adaptive.767.1535627244182.jpg"
                         alt="Card image cap">
                    <div class="card-body">
                        <a href="#" class="card-title">여기 기사 제목이 들어가죠</a>
                        <p class="card-text">기사의 요약 내용이 들어갑니다. 동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라만세 무궁화 삼천리 화려강산...</p>
                        <p class="card-text comment">여기에 코멘트가 들어갑니다.</p>
                    </div>
                </div>
                <div class="card">
                    <img class="card-img-top"
                         src="https://www.eurail.com/content/dam/images/eurail/Italy%20OCP%20Promo%20Block.adaptive.767.1535627244182.jpg"
                         alt="Card image cap">
                    <div class="card-body">
                        <a href="#" class="card-title">여기 기사 제목이 들어가죠</a>
                        <p class="card-text">기사의 요약 내용이 들어갑니다. 동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라만세 무궁화 삼천리 화려강산...</p>
                        <p class="card-text comment">여기에 코멘트가 들어갑니다.</p>
                    </div>
                </div>
            </div>
        </div>
    </body>

</html>
```

