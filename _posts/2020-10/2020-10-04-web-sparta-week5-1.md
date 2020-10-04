---
layout: post
title:  API 실습4 - 무비스타
subtitle:   API 실습4 - 무비스타
categories: web
tags: web webprogramming spartacodingclub
comments: true
# header-img:
---
+ __목차__
  - [1. 문제](#1-문제)  
  - [2. 실습](#2-실습)

## 1. 문제
---
[완성 예시 클릭](http://spartacodingclub.shop/homework){: target="_blank"}  
주어진 뼈대를 가지고 예시처럼 페이지를 만들고 위로, 삭제 기능까지 만들어보자.  
무비스타가 사실은 거의 주제만 바꿔서 모든 프로젝트의 뼈대가 된다고 생각해도 좋다. 왜냐하면 대부분 뭔가를 클릭하거나 로딩을 할 때마다 크롤링을 하지는 않는다. 대부분은 크롤링을 먼저 해놓고 DB에 저장을 해놓은 뒤 보여주기도, 추가, 수정, 삭제하기도 한다. 그런식으로 웹 서비스가 굴러가는 것이다.  
### 뼈대
```python
# init_db.py  
# db에 무비스타들 저장하는 코드로 활용하기 위해 먼저 주어짐
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


# DB에 저장할 영화인들의 출처 url을 가져옵니다.
def get_urls():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://movie.naver.com/movie/sdb/rank/rpeople.nhn', headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    trs = soup.select('#old_content > table > tbody > tr')

    urls = []
    for tr in trs:
        a = tr.select_one('td.title > a')
        if a is not None:
            base_url = 'https://movie.naver.com/'
            url = base_url + a['href']
            urls.append(url)

    return urls


# 출처 url로부터 영화인들의 사진, 이름, 최근작 정보를 가져오고 mystar 콜렉션에 저장합니다.
def insert_star(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    name = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info.character > h3 > a').text
    img_url = soup.select_one('#content > div.article > div.mv_info_area > div.poster > img')['src']
    recent_work = soup.select_one(
        '#content > div.article > div.mv_info_area > div.mv_info.character > dl > dd > a:nth-child(1)').text

    doc = {
        'name': name,
        'img_url': img_url,
        'recent': recent_work,
        'url': url,
        'like': 0
    }

    db.mystar.insert_one(doc)
    print('완료!', name)


# 기존 mystar 콜렉션을 삭제하고, 출처 url들을 가져온 후, 크롤링하여 DB에 저장합니다.
def insert_all():
    db.mystar.drop()  # mystar 콜렉션을 모두 지워줍니다.
    urls = get_urls()
    for url in urls:
        insert_star(url)


### 실행하기
insert_all()
```
```python
# app.py
from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 화면 보여주기 
@app.route('/')
def home():
    return render_template('index.html')


# API 역할을 하는 부분
@app.route('/api/list', methods=['GET'])
def show_stars():
    # 1. db에서 mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
    # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
    # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
    return jsonify({'result': 'success', 'msg': 'list 연결되었습니다!'})


@app.route('/api/like', methods=['POST'])
def like_star():
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    # 2. mystar 목록에서 find_one으로 name이 name_receive와 일치하는 star를 찾습니다.
    # 3. star의 like 에 1을 더해준 new_like 변수를 만듭니다.
    # 4. mystar 목록에서 name이 name_receive인 문서의 like 를 new_like로 변경합니다.
    # 참고: '$set' 활용하기!
    # 5. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success', 'msg': 'like 연결되었습니다!'})


@app.route('/api/delete', methods=['POST'])
def delete_star():
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    # 2. mystar 목록에서 delete_one으로 name이 name_receive와 일치하는 star를 제거합니다.
    # 3. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success', 'msg': 'delete 연결되었습니다!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
```
```html
<!-- index.html-->
<!DOCTYPE html>
<html lang="ko">
    <head>
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <title>마이 페이보릿 무비스타 | 프론트-백엔드 연결 마지막 예제!</title>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.8.0/css/bulma.min.css"/>
        <script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>
        <style>
            .center {
                text-align: center;
            }

            .star-list {
                width: 500px;
                margin: 20px auto 0 auto;
            }

            .star-name {
                display: inline-block;
            }

            .star-name:hover {
                text-decoration: underline;
            }

            .card {
                margin-bottom: 15px;
            }
        </style>
        <script>
            $(document).ready(function () {
                // index.html 로드가 완료되면 자동으로 showStar() 함수를 호출합니다.
                showStar();
            });

            function showStar() {
                $.ajax({
                    type: 'GET',
                    url: '/api/list',
                    data: {},
                    success: function (response) {
                        if (response['result'] == 'success') {
                            let msg = response['msg'];
                            alert(msg);
                        }
                    }
                });
            }

            function likeStar(name) {
                $.ajax({
                    type: 'POST',
                    url: '/api/like',
                    data: {},
                    success: function (response) {
                        if (response['result'] == 'success') {
                            let msg = response['msg'];
                            alert(msg);
                        }
                    }
                });
            }

            function deleteStar(name) {
                $.ajax({
                    type: 'POST',
                    url: '/api/delete',
                    data: {},
                    success: function (response) {
                        if (response['result'] == 'success') {
                            let msg = response['msg'];
                            alert(msg);
                        }
                    }
                });
            }

        </script>
    </head>
    <body>
        <section class="hero is-warning">
            <div class="hero-body">
                <div class="container center">
                    <h1 class="title">
                        마이 페이보릿 무비스타😆
                    </h1>
                    <h2 class="subtitle">
                        순위를 매겨봅시다
                    </h2>
                </div>
            </div>
        </section>
        <div class="star-list" id="star-box">
            <div class="card">
                <div class="card-content">
                    <div class="media">
                        <div class="media-left">
                            <figure class="image is-48x48">
                                <img
                                        src="https://search.pstatic.net/common/?src=https%3A%2F%2Fssl.pstatic.net%2Fsstatic%2Fpeople%2Fportrait%2F201807%2F20180731143610623-6213324.jpg&type=u120_150&quality=95"
                                        alt="Placeholder image"
                                />
                            </figure>
                        </div>
                        <div class="media-content">
                            <a href="#" target="_blank" class="star-name title is-4">김다미 (좋아요: 3)</a>
                            <p class="subtitle is-6">안녕, 나의 소울메이트(가제)</p>
                        </div>
                    </div>
                </div>
                <footer class="card-footer">
                    <a href="#" onclick="likeStar('김다미')" class="card-footer-item has-text-info">
                        위로!
                        <span class="icon">
              <i class="fas fa-thumbs-up"></i>
            </span>
                    </a>
                    <a href="#" onclick="deleteStar('김다미')" class="card-footer-item has-text-danger">
                        삭제
                        <span class="icon">
              <i class="fas fa-ban"></i>
            </span>
                    </a>
                </footer>
            </div>
        </div>
    </body>
</html>
```
<Br>

## 2. 실습
---
```python
# app.py
from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')


# API 역할을 하는 부분
@app.route('/api/list', methods=['GET'])
def show_stars():
    # 1. db에서 mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
    # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
    stars = list(db.mystar.find({}, {'_id': False}).sort('like', -1))
    # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
    return jsonify({'result': 'success', 'stars_list': stars})


@app.route('/api/like', methods=['POST'])
def like_star():
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    name_receive = request.form['name_give']

    # 2. mystar 목록에서 find_one으로 name이 name_receive와 일치하는 star를 찾습니다.
    star = db.mystar.find_one({'name': name_receive})
    # 3. star의 like 에 1을 더해준 new_like 변수를 만듭니다.
    new_like = star['like'] + 1

    # 4. mystar 목록에서 name이 name_receive인 문서의 like 를 new_like로 변경합니다.
    # 참고: '$set' 활용하기!
    db.mystar.update_one({'name': name_receive}, {'$set': {'like': new_like}})

    # 5. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success'})


@app.route('/api/delete', methods=['POST'])
def delete_star():
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    name_receive = request.form['name_give']
    # 2. mystar 목록에서 delete_one으로 name이 name_receive와 일치하는 star를 제거합니다.
    db.mystar.delete_one({'name': name_receive})
    # 3. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
```
```html
<!-- index.html-->
<!DOCTYPE html>
<html lang="ko">
    <head>
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <title>마이 페이보릿 무비스타 | 프론트-백엔드 연결 마지막 예제!</title>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.8.0/css/bulma.min.css"/>
        <script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>
        <style>
            .center {
                text-align: center;
            }

            .star-list {
                width: 500px;
                margin: 20px auto 0 auto;
            }

            .star-name {
                display: inline-block;
            }

            .star-name:hover {
                text-decoration: underline;
            }

            .card {
                margin-bottom: 15px;
            }
        </style>
        <script>
            $(document).ready(function () {
                // index.html 로드가 완료되면 자동으로 showStar() 함수를 호출합니다.
                showStar();
            });

            function showStar() {
                // 1. #star_box의 내부 html 태그를 모두 삭제합니다.
                $('#star-box').empty()

                // 2. 서버에 1) GET 방식으로, 2) /api/list 라는 주소로 star_list를 요청합니다.
                $.ajax({
                    type: "GET",
                    url: "/api/list",
                    data: {},
                    success: function (response) {
                        // 3. 서버가 돌려준 star_list를 star라는 변수에 저장합니다.
                        let stars = response['stars_list']
                        // 4. for 문을 활용하여 star 배열의 요소를 차례대로 조회합니다.
                        for (let i = 0; i < stars.length; i++) {
                            let star = stars[i]
                            // 5. star[i] 요소의 name, url, img_url, recent, like 키 값을 활용하여 값을 조회합니다.
                            let name = star['name']
                            let url = star['url']
                            let imgUrl = star['img_url']
                            let recentWork = star['recent']
                            let like = star['like']

                            // 6. 영화인 카드를 만듭니다.
                            let tempHtml = `<div class="card">
                                <div class="card-content">
                                  <div class="media">
                                    <div class="media-left">
                                      <figure class="image is-48x48">
                                        <img
                                          src="${imgUrl}"
                                          alt="Placeholder image"
                                        />
                                      </figure>
                                    </div>
                                    <div class="media-content">
                                      <a href="${url}" target="_blank" class="star-name title is-4">${name} (좋아요: ${like})</a>
                                      <p class="subtitle is-6">${recentWork}</p>
                                    </div>
                                  </div>
                                </div>
                                <footer class="card-footer">
                                  <a href="#" onclick="likeStar('${name}')" class="card-footer-item has-text-info">
                                    위로!
                                    <span class="icon">
                                      <i class="fas fa-thumbs-up"></i>
                                    </span>
                                  </a>
                                  <a href="#" onclick="deleteStar('${name}')" class="card-footer-item has-text-danger">
                                    삭제
                                    <span class="icon">
                                      <i class="fas fa-ban"></i>
                                    </span>
                                  </a>
                                </footer>
                              </div>`

                            // 7. #star-box에 temp_html을 붙입니다.
                            $('#star-box').append(tempHtml)
                        }
                    }
                });
            }

            function likeStar(name) {
                $.ajax({
                    type: "POST",
                    url: "/api/like",
                    data: {'name_give': name},
                    success: function (response) {
                        if (response['result'] == 'success') {
                            // 2. '좋아요 완료!' 얼럿을 띄웁니다.
                            alert('좋아요 완료!')
                            // 3. 변경된 정보를 반영하기 위해 새로고침합니다.
                            window.location.reload()
                        }
                    }
                });
            }

            function deleteStar(name) {
                // 1. 서버에 1) POST 방식으로, 2) /api/delete 라는 url에, 3) name_give라는 이름으로 name을 전달합니다.
                // 참고) POST 방식이므로 data: {'name_give': name} 과 같은 양식이 되어야합니다!
                $.ajax({
                    type: "POST",
                    url: "/api/delete",
                    data: {'name_give': name},
                    success: function (response) {
                        if (response['result'] == 'success') {
                            // 2. '삭제 완료! 안녕!' 얼럿을 띄웁니다.
                            alert('삭제 완료! 안녕!')
                            // 3. 변경된 정보를 반영하기 위해 새로고침합니다.
                            window.location.reload()
                        }
                    }
                });
            }

        </script>
    </head>
    <body>
        <section class="hero is-warning">
            <div class="hero-body">
                <div class="container center">
                    <h1 class="title">
                        마이 페이보릿 무비스타😆
                    </h1>
                    <h2 class="subtitle">
                        순위를 매겨봅시다
                    </h2>
                </div>
            </div>
        </section>
        <div class="star-list" id="star-box">
            <div class="card">
                <div class="card-content">
                    <div class="media">
                        <div class="media-left">
                            <figure class="image is-48x48">
                                <img
                                        src="https://search.pstatic.net/common/?src=https%3A%2F%2Fssl.pstatic.net%2Fsstatic%2Fpeople%2Fportrait%2F201807%2F20180731143610623-6213324.jpg&type=u120_150&quality=95"
                                        alt="Placeholder image"
                                />
                            </figure>
                        </div>
                        <div class="media-content">
                            <a href="#" target="_blank" class="star-name title is-4">김다미 (좋아요: 3)</a>
                            <p class="subtitle is-6">안녕, 나의 소울메이트(가제)</p>
                        </div>
                    </div>
                </div>
                <footer class="card-footer">
                    <a href="#" onclick="likeStar('김다미')" class="card-footer-item has-text-info">
                        위로!
                        <span class="icon">
              <i class="fas fa-thumbs-up"></i>
            </span>
                    </a>
                    <a href="#" onclick="deleteStar('김다미')" class="card-footer-item has-text-danger">
                        삭제
                        <span class="icon">
              <i class="fas fa-ban"></i>
            </span>
                    </a>
                </footer>
            </div>
        </div>
    </body>
</html>
```