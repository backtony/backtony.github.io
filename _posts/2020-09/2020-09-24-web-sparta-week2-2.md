---
layout: post
title:  Ajax
subtitle:   Ajax
categories: web
tags: web webprogramming spartacodingclub
comments: true
# header-img:
---
+ __목차__
  - [1. API](#1-api)
  - [2. ajax](#2-ajax)
  - [3. 연습하기](#3-연습하기) 
  - [4. 정리](#4-정리) 
  

## 1. API
---
은행은 정해진 기능에 대해서 정해진 방식으로만 커뮤니케이션 하겠습니다 라고 창구를 따로 놓는다. 예를 들면, 입출금하고 싶다면 입출금 창구로 가야하는 것이다. 이런 창구가 바로 API이다. 서버도 똑같다. 서버도 클라이언트가 해달라는 대로 일을 해줄 수가 없기 때문에 서버도 나는 정해진 대로만, 정해진 방식으로만, 정해진 기능으로만 창구를 놓고 커뮤니케이션 할거야 라고 하는 이 창구를 API라고 하는 것이다.  
아무나 가져갈 수 있게 만들어 놓은 것을 OpenAPI라고 한다. OpenAPI를 이용해서 클라이언트에서 서버로 Ajax라는 통신 방법을 이용해 데이터를 가지고 특정 url로 요청을 가고 받아온 정보를 가지고 가공해서 사용할 수 있다.  
딕셔너리와 리스트가 조합되어 있는 형태를 JSON이라고 부르는데 서버에서 받아오는 데이터는 대부분 JSON 형식이다.  
API는 은행 창구와 같다고 했다. 같은 예금 창구에서도 개인 고객이냐, 기업 고객이냐에 따라 가져와야 하는 것, 처리해주는 것이 다른 것처럼 클아이언트가 요청 할 때에도, 타입이라는 것이 존재한다.
+ GET : 통상적으로 데이터 조회(READ)를 요청할 때
+ POST : 통상적으로 데이터 생성, 변경, 삭제를 요청할 때

### GET
POST는 나중에 알아보고 GET만 우선 알아보자.  
```
https://movie.naver.com/movie/bi/mi/basic.nhn?code=161967
```
위 주소는 크게 두 부분으로 쪼개진다. '?'가 바로 쪼개지는 지점이다. '?' 기준으로 앞부분이 서버 주소, 뒷부분이 영화 번호이다.
+ ? : 여기부터 전달할 데이터가 작성된다는 의미
+ & : 전달할 데이터가 더 있다는 의미

여기서 code라는 이름으로 영화번호를 주자는 것은 프론트엔트 개발자와 백엔드 개발자가 미리 정해둔 약속이다.  

```
예시
google.com/search?q=아이폰&sourceid=chrome&ie=UTF-8
```
+  q=아이폰             (검색어)
+ sourceid=chrome      (브라우저 정보)
+ ie=UTF-8             (인코딩 정보)

<br>

## 2. Ajax
---
Ajax는 JQuery를 임포트한 페이지에서만 동작 가능하다. Ajax의 기본 골격은 다음과 같다.  
```html
$.ajax({
  type: "GET",
  url: "여기에URL을입력",
  data: {},
  success: function(response){
    console.log(response)
  }
})
```
+ type: "GET" → GET 방식으로 요청한다.
+ url : 요청할 url
+ data : 요청하면서 함께 줄 데이터(GET 요청시엔 비워둔다)
    - GET요청은 url뒤에 다음과 같이 붙여서 데이터를 가져간다. http://naver.com?param=value&param2=value2 
    - POST 요청은, data:{}에 넣어서 데이터를 가져간다. data: { param: 'value', param2: 'value2' },
+ success : 성공하면, response 값에 서버의 결과 값을 담아서 함수를 실행한다.

<br>

### Ajax 통신의 결과값 이용해보기
__미세먼지 OpenAPI__  
```
http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99
```

__OpeAPI를 통해 모든 구의 미세먼지 값 찍어보기__  
```html
$.ajax({
  type: "GET",
  url: "http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99",
  data: {},
  success: function (response) {
    let mise_list = response["RealtimeCityAir"]["row"];
    for (let i = 0; i < mise_list.length; i++) {
      let mise = mise_list[i];
      let gu_name = mise["MSRSTE_NM"];
      let gu_mise = mise["IDEX_MVL"];
      console.log(gu_name, gu_mise);
    }
  },
});
```
<br>

## 3. 연습하기
__연습 1__  
미세먼지 OpenAPI를 활용하여 아래 코드의 크롬창에서 업데이트를 누르면 구이름 : 미세먼지 의 형태가 업데이트되게 만들기. 단, 미세먼지 농도가 30보다 큰 경우는 빨간 글씨로 나타내기.
```html
<!doctype html>
<html lang="ko">

<head>
    <meta charset="UTF-8">
    <title>jQuery 연습하고 가기!</title>

    <!-- jQuery를 import 합니다 -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

    <style type="text/css">
        div.question-box {
            margin: 10px 0 20px 0;
        }
    </style>

    <script>
        function q1() {
            // 여기에 코드를 입력하세요
        }
    </script>

</head>

<body>
    <h1>jQuery+Ajax의 조합을 연습하자!</h1>

    <hr />

    <div class="question-box">
        <h2>1. 서울시 OpenAPI(실시간 미세먼지 상태)를 이용하기</h2>
        <p>모든 구의 미세먼지를 표기해주세요</p>
        <p>업데이트 버튼을 누를 때마다 지웠다 새로 씌여져야 합니다.</p>
        <button onclick="q1()">업데이트</button>
        <ul id="names-q1">
            <li>중구 : 82</li>
            <li>종로구 : 87</li>
            <li>용산구 : 84</li>
            <li>은평구 : 82</li>
        </ul>
    </div>
</body>

</html>
```

__연습 1 풀이__  
```html
<!doctype html>
<html lang="ko">

<head>
    <meta charset="UTF-8">
    <title>jQuery 연습하고 가기!</title>

    <!-- jQuery를 import 합니다 -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

    <style type="text/css">
        div.question-box {
            margin: 10px 0 20px 0;
        }
        .bad{
            color:red;
            font-weight: bold;
        }
    </style>

    <script>
        function q1() {
            $('#names-q1').empty()
            $.ajax({
                type: "GET",
                url: "http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99",
                data: {},
                success: function (response) {
                    let mise_list = response["RealtimeCityAir"]["row"];
                    for (let i = 0; i < mise_list.length; i++) {
                        let mise = mise_list[i];
                        let gu_name = mise["MSRSTE_NM"];
                        let gu_mise = mise["IDEX_MVL"];

                        let tmp_html =''
                        if (gu_mise>30){
                             tmp_html = `<li class="bad">${gu_name} : ${gu_mise}</li>`
                        } else{
                            tmp_html = `<li>${gu_name} : ${gu_mise}</li>`
                        }
                        $('#names-q1').append(tmp_html)
                    }
                },
            });

        }
    </script>

</head>

<body>
<h1>jQuery+Ajax의 조합을 연습하자!</h1>

<hr/>

<div class="question-box">
    <h2>1. 서울시 OpenAPI(실시간 미세먼지 상태)를 이용하기</h2>
    <p>모든 구의 미세먼지를 표기해주세요</p>
    <p>업데이트 버튼을 누를 때마다 지웠다 새로 씌여져야 합니다.</p>
    <button onclick="q1()">업데이트</button>
    <ul id="names-q1">
    </ul>
</div>
</body>

</html>
```
<br>

__연습 2__  
따릉이 OpenAPI를 활용하여 아래 코드의 크롬창에서 업데이트를 누르면 해당 내용의 형태가 업데이트되게 만들기. 단, 남은 자전거의 개수가 5개 미만이면 빨간 글씨로 나타내기.
```html
<!doctype html>
<html lang="ko">

<head>
    <meta charset="UTF-8">
    <title>JQuery 연습하고 가기!</title>
    <!-- JQuery를 import 합니다 -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

    <style type="text/css">
        div.question-box {
            margin: 10px 0 20px 0;
        }

        table {
            border: 1px solid;
            border-collapse: collapse;
        }

        td,
        th {
            padding: 10px;
            border: 1px solid;
        }
    </style>

    <script>
        function q1() {
            // 여기에 코드를 입력하세요
        }
    </script>

</head>

<body>
    <h1>jQuery + Ajax의 조합을 연습하자!</h1>

    <hr />

    <div class="question-box">
        <h2>2. 서울시 OpenAPI(실시간 따릉기 현황)를 이용하기</h2>
        <p>모든 위치의 따릉이 현황을 보여주세요</p>
        <p>업데이트 버튼을 누를 때마다 지웠다 새로 씌여져야 합니다.</p>
        <button onclick="q1()">업데이트</button>
        <table>
            <thead>
                <tr>
                    <td>거치대 위치</td>
                    <td>거치대 수</td>
                    <td>현재 거치된 따릉이 수</td>
                </tr>
            </thead>
            <tbody id="names-q1">
                <tr>
                    <td>102. 망원역 1번출구 앞</td>
                    <td>22</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>103. 망원역 2번출구 앞</td>
                    <td>16</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>104. 합정역 1번출구 앞</td>
                    <td>16</td>
                    <td>0</td>
                </tr>
            </tbody>
        </table>
    </div>
</body>

</html>
```
__연습 2 풀이__  
```html
<!doctype html>
<html lang="ko">

<head>
    <meta charset="UTF-8">
    <title>JQuery 연습하고 가기!</title>
    <!-- JQuery를 import 합니다 -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

    <style type="text/css">
        div.question-box {
            margin: 10px 0 20px 0;
        }

        table {
            border: 1px solid;
            border-collapse: collapse;
        }

        td,
        th {
            padding: 10px;
            border: 1px solid;
        }

        .bad {
            color: red;
            font-weight: bold;
        }
    </style>

    <script>
        function q1() {
            $('names-q1').empty()
            $.ajax({
                type: "GET",
                url: "http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/bikeList/1/99",
                data: {},
                success: function (response) {
                    let bike_list = response["rentBikeStatus"]["row"];
                    for (let i = 0; i < bike_list.length; i++) {
                        let bike_name = bike_list[i]["stationName"];
                        let bike_rack = bike_list[i]["rackTotCnt"];
                        let bike_cnt = bike_list[i]["parkingBikeTotCnt"];

                        let tmp_html = '';
                        if (bike_cnt < 5) {
                            tmp_html = `<tr class="bad">
                                            <td>${bike_name}</td>
                                            <td>${bike_rack}</td>
                                            <td>${bike_cnt}</td>
                                        </tr>`
                        } else {
                            tmp_html = `<tr>
                                            <td>${bike_name}</td>
                                            <td>${bike_rack}</td>
                                            <td>${bike_cnt}</td>
                                        </tr>`
                        }
                        $('#names-q1').append(tmp_html)
                    }
                },
            });
        }
    </script>

</head>

<body>
<h1>jQuery + Ajax의 조합을 연습하자!</h1>

<hr/>

<div class="question-box">
    <h2>2. 서울시 OpenAPI(실시간 따릉기 현황)를 이용하기</h2>
    <p>모든 위치의 따릉이 현황을 보여주세요</p>
    <p>업데이트 버튼을 누를 때마다 지웠다 새로 씌여져야 합니다.</p>
    <button onclick="q1()">업데이트</button>
    <table>
        <thead>
        <tr>
            <td>거치대 위치</td>
            <td>거치대 수</td>
            <td>현재 거치된 따릉이 수</td>
        </tr>
        </thead>
        <tbody id="names-q1">

        </tbody>
    </table>
</div>
</body>

</html>
```
<br>

__연습 3__  
랜덤 고양이 사진 API
```
https://api.thecatapi.com/v1/images/search
```
랜덤 고양이 사진 API와 아래 코드를 이용하여 업데이트 버튼을 누를 때마다 고양이 사진이 업데이트 되도록 만들기
```html
<!doctype html>
<html lang="ko">
  <head>
    <meta charset="UTF-8">
    <title>JQuery 연습하고 가기!</title>
    <!-- JQuery를 import 합니다 -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    
    <style type="text/css">
      div.question-box {
        margin: 10px 0 20px 0;
      }
      div.question-box > div {
        margin-top: 30px;
      }
      
    </style>

    <script>
      function q1() {
        // 여기에 코드를 입력하세요
      }
    </script>

  </head>
  <body>
    <h1>JQuery+Ajax의 조합을 연습하자!</h1>

    <hr/>

    <div class="question-box">
      <h2>3. 랜덤 고양이 사진 API를 이용하기</h2>
      <p>예쁜 고양이 사진을 보여주세요</p>
      <p>업데이트 버튼을 누를 때마다 지웠다 새로 씌여져야 합니다.</p>
      <button onclick="q1()">고양이를 보자</button>
      <div>
        <img id="img-cat" src="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"/>
      </div>
    </div>
  </body>
</html>
```

__연습 3 풀이__  
```html
<!doctype html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>JQuery 연습하고 가기!</title>
    <!-- JQuery를 import 합니다 -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

    <style type="text/css">
        div.question-box {
            margin: 10px 0 20px 0;
        }

        div.question-box > div {
            margin-top: 30px;
        }

    </style>

    <script>
        function q1() {
            $.ajax({
                type: "GET",
                url: "https://api.thecatapi.com/v1/images/search",
                data: {},
                success: function (response) {
                    $('#img-cat').empty()
                    let img_url = response[0]['url'];
                    $('#img-cat').attr("src",img_url);
                    // img태그 src 변경하는법 $('#id값').attr("src",url값)
                }
            })
        }
    </script>

</head>
<body>
<h1>JQuery+Ajax의 조합을 연습하자!</h1>

<hr/>

<div class="question-box">
    <h2>3. 랜덤 고양이 사진 API를 이용하기</h2>
    <p>예쁜 고양이 사진을 보여주세요</p>
    <p>업데이트 버튼을 누를 때마다 지웠다 새로 씌여져야 합니다.</p>
    <button onclick="q1()">고양이를 보자</button>
    <div>
        <img id="img-cat" src="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"/>
    </div>
</div>
</body>
</html>
```
<br>

위에서 작성한 코드들은 버튼을 누르면 onclick으로 함수가 호출되면서 업데이트가 되는 형식이었다. 그렇다면 버튼을 누르지 않고 페이지가 열리자마자 ajax로 해당 내용들을 받아오고 싶으면 어떻게 할까?
```html
<script>

$(document).ready(function(){	
  // 여기에 Ajax 요청을 하면 된다.
});

</script>
```

## 4. 정리
---
+ jQuery : javascript의 라이브러리 같은 것, 누가 만들어 놓은 javascript 같은 것인데 태그의 글씨도 바꾸고 뭘 붙이기도 하고 이미지도 바꾸고 할 때 쓰는것
+ ajax : 서버한테 통신할때 서버가 만들어 놓은 API로 통신해서 그 결과를 받아서 사용할 수 있게 하는 것