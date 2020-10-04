---
layout: post
title:  API 실습3 - 나홀로쇼핑몰
subtitle:   API 실습3 - 나홀로쇼핑몰
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
주어진 app.py와 index.html을 이용하여 해당 페이지에서 주문하기 버튼을 클릭하면 DB에 저장하고 이를 페이지에 붙여넣는 동작을 하게 만드시오.  
```python
# app.py
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기 
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
```
```html
<!doctype html>
<html lang="ko">

<head>
    <!-- Required meta tags -->
    <meta charset="UTF-8">
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

    <title>원페이지쇼핑몰</title>

    <link href="https://fonts.googleapis.com/css2?family=Do+Hyeon&display=swap" rel="stylesheet">

    <style>
        * {
            font-family: 'Do Hyeon', sans-serif;
        }

        .myitem {
            width: 500px;
            height: 300px;

            background-image: url("https://t1.daumcdn.net/liveboard/nts/5bcccfbd33da4865817b9c606b6b852e.JPG");
            background-position: center;
            background-size: cover;
        }

        .price {
            font-size: 16px;
        }

        .desc {
            width: 500px;
            margin-top: 20px;
            margin-bottom: 20px;
        }

        .order-box {
            width: 500px;
            margin-bottom: 40px;
        }

        .mybtn {
            width: 100px;
            margin: auto;
            display: block;
        }

        .wrap {
            margin: auto;
            width: 500px;
        }

        .rate {
            color: blue;
        }
    </style>
    <script>

        $(document).ready(function () {
            $.ajax({
                type: "GET",
                url: "https://api.manana.kr/exchange/rate.json",
                data: {},
                success: function (response) {
                    let nowRate = response[1]['rate'];
                    $('#rate-box').text(nowRate);
                }
            })
            order_listing();
        });

        function order_listing() {
            // 여기에 ajax 요청을 넣으세요 (주문목록 보기 API 연결)
        }

        function order() {
            let name = $('#order-name').val();
            let count = $('#order-count').val();
            let address = $('#order-address').val();
            let phone = $('#order-phone').val();

            if (name == '') {
                alert('이름을 입력하세요');
            } else if (count == '-- 수량을 선택하세요 --') {
                alert('수량을 입력하세요');
            } else if (address == '') {
                alert('주소를 입력하세요');
            } else if (phone == '') {
                alert('전화번호를 입력하세요');
            } else {
                // 여기에 ajax 요청을 넣으세요 (주문하기 API 연결)
            }
        }
    </script>
</head>

<body>
<div class="wrap">
    <div class="myitem"></div>
    <div class="desc">
        <h1>양초를 팝니다 <span class="price">가격:3,000원/개</span></h1>
        <p>이 양초는 특별한 힘을 가지고 있습니다. 하나 두 개 켜 놓으면 또 다른 촛불을 찾을 수 있죠!</p>

        <p class="rate">달러-원 환율: <span id="rate-box">1,000</span></p>
    </div>
    <div class="order-box">
        <div class="input-group mb-3">
            <div class="input-group-prepend">
                <span class="input-group-text" id="inputGroup-sizing-default">주문자이름</span>
            </div>
            <input id="order-name" type="text" class="form-control" aria-label="Default"
                   aria-describedby="inputGroup-sizing-default">
        </div>
        <div class="input-group mb-3">
            <div class="input-group-prepend">
                <label class="input-group-text" for="inputGroupSelect01">수량</label>
            </div>
            <select id="order-count" class="custom-select">
                <option selected>-- 수량을 선택하세요 --</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
            </select>
        </div>
        <div class="input-group mb-3">
            <div class="input-group-prepend">
                <span class="input-group-text" id="inputGroup-sizing-default">주소</span>
            </div>
            <input id="order-address" type="text" class="form-control" aria-label="Default"
                   aria-describedby="inputGroup-sizing-default">
        </div>
        <div class="input-group mb-3">
            <div class="input-group-prepend">
                <span class="input-group-text" id="inputGroup-sizing-default">전화번호</span>
            </div>
            <input id="order-phone" type="text" class="form-control" aria-label="Default"
                   aria-describedby="inputGroup-sizing-default">
        </div>
        <button onclick="order()" type="button" class="btn btn-primary mybtn">주문하기</button>
    </div>
</div>
</body>

</html>
```
<br>

## 2. 실습
---
```python
# app.py
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name = request.form['name']
    count = request.form['count']
    address = request.form['address']
    phone = request.form['phone']
    info = {
        'name': name,
        'count': count,
        'address': address,
        'phone':phone
    }
    db.info.insert_one(info)
    return jsonify({'result': 'success', 'msg': '주문 완료!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    info = list(db.info.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'info': info})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
```
```html
<!-- index.html -->
<!doctype html>
<html lang="ko">

<head>
    <!-- Required meta tags -->
    <meta charset="UTF-8">
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

    <title>원페이지쇼핑몰</title>

    <link href="https://fonts.googleapis.com/css2?family=Do+Hyeon&display=swap" rel="stylesheet">

    <style>
        * {
            font-family: 'Do Hyeon', sans-serif;
        }

        .myitem {
            width: 500px;
            height: 300px;

            background-image: url("https://t1.daumcdn.net/liveboard/nts/5bcccfbd33da4865817b9c606b6b852e.JPG");
            background-position: center;
            background-size: cover;
        }

        .price {
            font-size: 16px;
        }

        .desc {
            width: 500px;
            margin-top: 20px;
            margin-bottom: 20px;
        }

        .order-box {
            width: 500px;
            margin-bottom: 40px;
        }

        .mybtn {
            width: 100px;
            margin: auto;
            display: block;
        }

        .wrap {
            margin: auto;
            width: 500px;
        }

        .rate {
            color: blue;
        }

    </style>
    <script>

        $(document).ready(function () {
            $.ajax({
                type: "GET",
                url: "https://api.manana.kr/exchange/rate.json",
                data: {},
                success: function (response) {
                    let nowRate = response[1]['rate'];
                    $('#rate-box').text(nowRate);
                }
            })
            order_listing();
        });

        function order_listing() {
            $.ajax({
                type: "GET",
                url: "/order",
                data: {},
                success: function (response) {
                    if (response["result"] == "success") {
                        let info = response['info']

                        for (let i = 0; i < info.length; i++) {
                            let name = info[i]['name'];
                            let count = info[i]['count'];
                            let address = info[i]['address'];
                            let phone = info[i]['phone'];
                            let temp_html =`<tr>
                                                <th scope="row">${name}</th>
                                                <td>${count}</td>
                                                <td>${address}</td>
                                                <td>${phone}</td>
                                            </tr>`

                                $('#orders-box').append(temp_html)
                        }
                    } else {
                        alert("주문자가 없습니다.");
                    }
                }
            })
        }

        function order() {
            let name = $('#order-name').val();
            let count = $('#order-count').val();
            let address = $('#order-address').val();
            let phone = $('#order-phone').val();

            if (name == '') {
                alert('이름을 입력하세요');
            } else if (count == '-- 수량을 선택하세요 --') {
                alert('수량을 입력하세요');
            } else if (address == '') {
                alert('주소를 입력하세요');
            } else if (phone == '') {
                alert('전화번호를 입력하세요');
            } else {
                $.ajax({
                    type: "POST",
                    url: "/order",
                    data: {'name': name, 'count': count, 'address': address, 'phone': phone},
                    success: function (response) {
                        if (response["result"] == "success") {
                            alert(response["msg"]);
                            window.location.reload();
                        }
                    }
                })
            }
        }
    </script>
</head>

<body>
<div class="wrap">
    <div class="myitem"></div>
    <div class="desc">
        <h1>양초를 팝니다 <span class="price">가격:3,000원/개</span></h1>
        <p>이 양초는 특별한 힘을 가지고 있습니다. 하나 두 개 켜 놓으면 또 다른 촛불을 찾을 수 있죠!</p>

        <p class="rate">달러-원 환율: <span id="rate-box">1,000</span></p>
    </div>
    <div class="order-box">
        <div class="input-group mb-3">
            <div class="input-group-prepend">
                <span class="input-group-text" id="inputGroup-sizing-default">주문자이름</span>
            </div>
            <input id="order-name" type="text" class="form-control" aria-label="Default"
                   aria-describedby="inputGroup-sizing-default">
        </div>
        <div class="input-group mb-3">
            <div class="input-group-prepend">
                <label class="input-group-text" for="inputGroupSelect01">수량</label>
            </div>
            <select id="order-count" class="custom-select">
                <option selected>-- 수량을 선택하세요 --</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
            </select>
        </div>
        <div class="input-group mb-3">
            <div class="input-group-prepend">
                <span class="input-group-text" id="inputGroup-sizing-default">주소</span>
            </div>
            <input id="order-address" type="text" class="form-control" aria-label="Default"
                   aria-describedby="inputGroup-sizing-default">
        </div>
        <div class="input-group mb-3">
            <div class="input-group-prepend">
                <span class="input-group-text" id="inputGroup-sizing-default">전화번호</span>
            </div>
            <input id="order-phone" type="text" class="form-control" aria-label="Default"
                   aria-describedby="inputGroup-sizing-default">
        </div>
        <button onclick="order()" type="button" class="btn btn-primary mybtn">주문하기</button>
        <div class="orders">
            <table class="table">
                <thead>
                <tr>
                    <th scope="col">이름</th>
                    <th scope="col">수량</th>
                    <th scope="col">주소</th>
                    <th scope="col">전화번호</th>
                </tr>
                </thead>
                <tbody id="orders-box">

                </tbody>
            </table>

        </div>
    </div>
</div>
</body>

</html>
```