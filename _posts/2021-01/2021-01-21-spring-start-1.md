---
layout: post
title:  Spring 입문 - 프로젝트 환경설정
subtitle:   Spring 입문 - 프로젝트 환경설정
categories: spring
tags: start
comments: true
# header-img:
---

+ __목차__
  - [1. 프로젝트 생성](#1-프로젝트-생성)    
  - [2. 라이브러리 살펴보기](#2-라이브러리-살펴보기)    
  - [3. view 환경설정](#3-view-환경설정)
  - [4. 빌드하고 실행하기](#4-빌드하고-실행하기)
  


## 1. 프로젝트 생성
--- 
대부분 요즘에는 스프링 부트로 스프링 프로젝트를 만든다. [링크](https://start.spring.io/) 해당 링크는 스프링 부트 기반으로 스프링 관련 프로젝트를 만들어주는 사이트이다.  

![그림1](https://backtony.github.io/assets/img/post/spring/start/1-1.PNG)

+ Maven, gradle project : 필요한 라이브러리를 땡겨서오고 빌드한 라이프 사이클까지 관리해주는 툴, 요즘에는 gradle을 사용한다.
+ spring boot : 버전 선택, snapshot은 아직 만들고 있는 버전이고, m1은 아직 정식 release된 버전이 아니다.
+ project metadata
  - group : 보통 기업명, 기업도메인 명을 적는다.
  - artifact : 빌드되어 나온 결과물, 프로젝트명 같은 것
+ dependencies : 스프링 부트 기반으로 프로젝트를 시작할것인데 어떤 라이브러리를 땡겨쓸껀지 선택하는 곳

선택을 마치고 아래 generate를 클릭해서 다운받아 압축을 풀고 intellij에서 build.gradle을 열어준다.

![그림2](https://backtony.github.io/assets/img/post/spring/start/1-2.PNG)
생성된 프로젝트에 대해서 간단히 알아보자.


<br>

### build.gradle
설명은 그림 주석으로 적어놓았다. __여기서 부터 나오는 그림은 ctrl + 휠로 확대해서 보기를 바란다.__  
![그림3](https://backtony.github.io/assets/img/post/spring/start/1-3.PNG)

<br>

### main
설명은 그림 주석으로 적어놓았다.
![그림4](https://backtony.github.io/assets/img/post/spring/start/1-4.PNG)

<br>

### 추가 설정
![그림5](https://backtony.github.io/assets/img/post/spring/start/1-5.PNG)
setting에서 gradle을 검색해서 설정을 아래와 같이 바꿔준다. gradle을 통해서 실행하게 되면 느린 경우가 있기 때문이다. 다음과 같이 설정하면 바로 gradle을 통하지 않고 intellij에서 자바를 띄워서 돌려주기 때문에 빨라진다.

<br>

## 2. 라이브러리 살펴보기
---
![그림6](https://backtony.github.io/assets/img/post/spring/start/1-6.PNG)

external libraries는 땡겨온 라이브러리를 확인할 수 있다. 프로젝트를 만들 때 라이브러리 2개를 땡겨왔었는데 위와 같이 엄청나게 많은 라이브러리를 땡겨온 것을 볼 수 있다. 이유는 의존관계가 있기 때문이다. 라이브러리는 서로 의존관계를 갖고 있기 때문에 이것을 사용할 때 저것이 필요하다고 알아두면 된다.
+ 스프링 부트 라이브러리
  - spring-boot-starter-web (프로젝트 생성할 때 당겨왔던 라이브러리) -> 아래는 이 안에 들어있는 것
    - spring-boot-starter-tomcat : 톰캣(웹서버)
    - spring-webmvc : 스프링 웹 mvc
  - spring-boot-starter-thymeleaf : 타임리프 템플릿 엔진
  - spring-boot-starter(공통) : 스프링 부트 + 스프링 코어 + 로깅
    - spring-boot
      - spring-core
    - spring-boot-starter-logging
      - logback,slf4j
+ 테스트 라이브러리
  - spring-boot-starter-test
    - junit : 테스트 프레임워크
    - mockito : 목 라이브러리
    - assertj : 테스트 코드를 좀 더 편하게 작성하게 도와주는 라이브러리
    - spring-test : 스프링 통합 테스트 지원

설명을 들었지만 처음 배우는 내용이기에 사실 와닿지는 않지만, 일단 이런게 있다는 정도만 알아두면 될 것 같다.

<br>

## 3. view 환경설정
---
### 첫 화면 welcompage 만들기
resources/static/ 폴더에 index.html 파일 형태로 넣어두면 이 파일은 도메인으로 들어왔을 때의 첫 화면을 구성한다. 
```html
<!DOCTYPE HTML>
<html>
<head>
 <title>Hello</title>
 <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>
Hello
<a href="/hello">hello</a>
</body>
</html>
```
index.html 파일에 위와 같은 코드를 작성하고 실행해서 localhost:8080 에 접속하면 첫 화면을 확인할 수 있다. 위에서 작성했던 페이지는 정적 페이지이다. 내가 적어놓은 파일을 웹서버가 그냥 그대로 웹브라우저에 넘겨주는 것이다. 템블릿 엔진이라는 것을 사용하면 위 모양을 바꿀 수 있다.
<br>

### thymeleaf 템플릿 엔진
![그림7](https://backtony.github.io/assets/img/post/spring/start/1-7.PNG)
![그림8](https://backtony.github.io/assets/img/post/spring/start/1-8.PNG)

위와 같은 결과가 어떤 과정을 거치는지는 코드에 주석으로 달아놨지만 그림으로 한 번 확인해보자.  
<br>

![그림9](https://backtony.github.io/assets/img/post/spring/start/1-9.PNG)

웹 브라우저에서 localhost:8080/hello라고 던진다. 스프링 부트는 톰켓이라는 내장 서버가 있다. 톰켓 서버는 이것을 받아서 스프링 부트에 물어본다. 스프링은 이걸 받아서 @GetMapping("hello")에 hello가 url에 매칭이 되면서 해당 메소드를 실행한다. 스프링은 모델이란걸 만들어서 알아서 넣어주고 모델에 키값과 value값을 넣어주고 문자를 반환한다. 컨트롤러에서 리턴 값으로 문자를 반환하면 뷰 리졸버(viewResolver)가 resources:templates/ + 리턴한문자(ViewName) + .html 을 찾아가서 Thymeleaf 템플릿 엔진 처리를 해주고 다시 웹 브라우저로 던져준다.



<br>

## 4. 빌드하고 실행하기
---
![그림10](https://backtony.github.io/assets/img/post/spring/start/1-10.PNG)
cmd에서 폴더를 찾아가서 gradlew 파일을 build 한다.

<br>

![그림11](https://backtony.github.io/assets/img/post/spring/start/1-11.PNG)

build하고 build 폴더 -> libs 로 들어가면 파일이 만들어져 있다. 이제 이 파일을 실행시키면 된다. java는 'java -jar 파일명' 으로 실행시키면 된다. 서버 종료는 ctrl + c 누르면 된다.(윈도우 기준) 서버 배포핦 때는 이 파일만 복사해서 서버에 넣어주고 java -jar로 실행시키면 서버에서도 스프링이 동작한다.
<br>

__cf) 필요한 기능 찾기__  
spring에는 엄청나게 많은 양의 기능이 있기 때문에 필요한 내용을 찾는 것이 중요하다. [spring.io](https://spring.io/) 홈페이지에 들어가서 projects -> spring boot -> learn -> documentation 버전 확인 후 reference doc 클릭 -> 이제 여기서 부터 필요한 내용을 찾아서 사용하면 된다.

<br>

---
__본 포스팅은 인프런 김영한님의 '스프링 입문 - 코드로 배우는 스프링 부트, 웹MVC, DB접근 기술' 강의를 듣고 정리한 내용을 바탕으로 작성하였습니다. [[강의 링크](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%EC%9E%85%EB%AC%B8-%EC%8A%A4%ED%94%84%EB%A7%81%EB%B6%80%ED%8A%B8){:target="_blank"}]__