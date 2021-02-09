---
layout: post
title:  Spring 입문 - 스프링 웹 개발 기초
subtitle:   Spring 입문 - 스프링 웹 개발 기초
categories: spring
tags: start
comments: true
# header-img:
---

+ __목차__
  - [1. 정적 컨텐츠](#1-정적-컨텐츠)    
  - [2. MVC와 템플릿 엔진](#2-mvc와-템플릿-엔진)    
  - [3. API](#3-api)
  



## 1. 정적 컨텐츠
---
정적 컨텐츠는 welcome page처럼 서버에서 뭐 하는 것 없이 파일을 웹 브라우저에 내려주는 것이다. [메뉴얼 링크](https://docs.spring.io/spring-boot/docs/current/reference/html/spring-boot-features.html#boot-features-spring-mvc-static-content)에서 확인해보면 스프링 부트에서는 정적 컨텐츠를 /static 에서 가져온다고 되어 있다.  
![그림1](https://backtony.github.io/assets/img/post/spring/start/2-1.PNG)

위와 같이 코딩을 해서 static 폴더에 넣어놓으면 작성한 코드 그대로 화면에 출력한다. 대신 static은 어떤 프로그램은 할 수 없다. 그냥 코드 그대로 나가는 것이다.

<br>

![그림2](https://backtony.github.io/assets/img/post/spring/start/2-2.PNG)

어떻게 동작하는지 확인해보자. url을 입력하면 내장 톰켓 서버가 요청을 받고 스프링에 넘긴다. 스프링은 컨트롤러에서 먼저 hello-static이 있는지 확인해본다. 즉, 컨트롤러가 우선순위를 가진다는 뜻이다. 그 후에 없다면 resources의 static에서 찾는다. 그리고 반환해준다.

<br>

## 2. MVC와 템플릿 엔진
---
과거에 jps, php가 템플릿 엔진이다. html을 그냥 주는게 아니라 서버에서 프로그래밍 해서, html을 동적으로 바꿔서 내리는 것이 템플릿 엔진이다. 그것을 하기 위해서 필요한 컨트롤러, 모델, 템플릿 엔진 화면 이 세 가지를 MVC(model, view, controller)라고 한다. Controller와 View를 쪼개는게 기본이다. view는 화면에 관련된 일만, 비지니스 로직과 서버에 관련된 것은 Controller에서 처리를 하고 Model에 화면에 필요한 것들을 담아서 화면쪽에 넘겨주는 패턴을 주로 사용한다.  
<br>

### 파라미터 외부에서 받기
앞선 포스트에서는 model.addAttribute로 직접 값을 주어 사용했었는데 이번에는 외부에서 받아서 사용해보자.

![그림3](https://backtony.github.io/assets/img/post/spring/start/2-3.PNG)

외부에서 받을 때 @RequestParam를 사용했다. 사실 String code만으로도 받을 수 있는데 시스템에 따라 컴파일러 최적화 옵션 적용시 문제가 생긴다.  이 경우 컴파일 시점에 code이라는 변수가 다른 간단한 이름으로 바뀔 수가 있다. 예를 들면 String code 였던 변수가 String x01이 되고, 바로 아래 model. 코드에서도 code가 x01이 바뀌어 컴파일 될 수 있다는 뜻이다. 그럼 변수명이 바뀐 상태에서 code=hello라고 url에 값을 주면 전혀 엉뚱한 곳에 값을 주게 되는 상황이 발생한다. 이러한 상황을 방지하기 위해 @RequestParam을 사용하는 것이다.  
예를 들어 @RequestParam("country") String temp 이렇게 코딩하고, url에서 country=spring으로 값을 줬다고 해보자. 이 의미는 country라는 key에 담긴 value는 spring이고, value값인 spring을 temp에 복사한다는 의미이다.

<br>

![그림4](https://backtony.github.io/assets/img/post/spring/start/2-4.PNG)

url에서 get방식으로 ?문자=값 으로 검색하면 위와 같이 출력된다. 여기서 문자는 @RequestParam("문자")에서 문자이다.  
hello! empty는 화면에 출력되지 않는데 왜 그럴까? thymeleaf의 장점은 html을 그대로 쓰고 파일을 서버없이 바로 열어봐도 껍떼기를 볼 수 있다는 점이다. 템플릿 엔진이 동작하면 text ="'hello' +${name}" 값이 hello! empty를 대체하게 된다. 저렇게 hello empty를 넣어두는 이유는 서버없이 html을 만들어서 볼 때 뭔가 적어놓고 볼 수 있으려고 하는 것이라고 보면 된다. 껍떼기를 보려면 copy path -> absolute path를 클릭하고 url에 치면 확인할 수 있다.
<br>

### 동작 과정
![그림5](https://backtony.github.io/assets/img/post/spring/start/2-5.PNG)

웹 브라우저에서 url을 넘기면 먼저 내장 톰켓 서버가 받는다. 내장 톰켓 서버는 스프링한테 던지고 스프링은 컨트롤러에서 확인해서 있다면 메소드를 호출한다. 메소드는 모델에는 키값과 벨류값을 담고 리턴한 파일명을 스프링한테 넘긴다. 스프링에서 viewresolver가 동작하고 templates에 리턴값과 똑같은 파일명을 찾아서 랜더링하고 변환한 html 웹 브라우저에 넘긴다. 여기서 정적과 차이가 있다. 정적에서는 변환이 없었다. 이런 템플릿 엔진에서는 변환을 해서 넘겨준다.


<br>

## 3. API
---
정적 컨텐츠 방식을 제외하면 MVC방식에서 뷰를 찾아서 템플릿 엔진을 통해 화면을 랜더링해서 html을 웹 브라우저에 넘겨주는 방식이 있고, API을 사용하는 방식이 있다. 사실 정적 컨텐츠를 제외하면 이것을 html로 내리냐 API 방식으로 데이터를 바로 내리는가로 2가지 방식만 기억하면 된다. 안드로이드나 아이폰 클라이언트랑 개발을 해야한다면 요즘에는 JSON이라는 데이터 구조 포멧으로 클라이언트한테 데이터를 전달하는 것이 요즘의 API 방식이다.  

```java
// controller에 HelloController.java

package hello.hellospring.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;


@Controller // @Controller가 있어야 스프링이 스프링 컨트롤러로 인식한다.
public class HelloController {


    @GetMapping("hello-string")
    @ResponseBody // http에서 헤더부와 바디부가 있는데 바디부에 이 데이터를 직접 넣어주겠다.
    // @RequestParam에 의해서 ?p=spring으로 받으면
    // key:p, value:spring, -> value값을 code에 복사
    public String helloString(@RequestParam("p") String code) {
        return "hello " + code; // name에 spring으로 넣으면 "hello spring"
        // 템플릿 엔진과 차이는 뷰 이런게 없고 그냥 이 문자가 그대로 내려간다.
        // 페이지에서 소스코드를 보면 html이 없고 그냥 hello + code 그대로만 있다.
    }


    // 사실 위에서 문자열 넘긴거는 거의 안쓰고 아래가 주된 사용 목적    
    @GetMapping("hello-api")
    @ResponseBody    
    public Hello helloApi(@RequestParam("p") String code) {
        // 객체 생성하고 받은 인자로 set해주고 이 객체를 반환하는 작업

        Hello hello = new Hello(); // (까지 쓰고 ctrl+shft+enter 치면 자동 완성
        hello.setName(code);
        return hello; // 키 , 벨류 값으로 반환된다. {"key":"value"} 형식
        
        // {"abc":"spring"}이 나온다.
        // 이유는 JSON을 생성할 때 자바빈 프로퍼티 규약이라는 것 때문이다.
        // getXXX, setXXX 규칙의 메소드를 사용하는 것인데 여기서
        // get,set을 제거하고 첫글자를 소문자로 바꾸면 그것이 
        // setXXX의 XXX가 프로퍼티(키값)이 되고, getXXX의 리턴값이 value값이된다.        

        // 예전에는 XML 방식과 json방식이 있었는데 요즘에는 json방식이 거의 표준화되어서
        // 스프링도 객체를 반환하고 responsebody로 해놓으면 json으로 반환하는게 기본이다.
    }
    // 정적 클래스 생성
    static class Hello {
        // private이니까 외부에서 못 꺼내니까 게터, 세터사용해서 접근해야한다.
        // 이게 자바빔 표준방식, property 접근방식이라고도함
        private String abc;
        // alt+insert 후 getter and setter 찾으면 자동 완성된다.
        public String getAbc() {
            return abc;
        }

        public void setAbc(String abc) {
            this.abc = abc;
        }
    }

}
```
![그림6](https://backtony.github.io/assets/img/post/spring/start/2-6.PNG)

위에가 get방식으로 값 준것이고 아래것은 페이지 소스 보기를 한 것이다. 템플릿사용과 다르게 html 없이 반환값 그대로만 소스가 있는 것을 확인할 수 있다. 코드주석에도 작성했지만, @ResponseBody 어노테이션은 HTTP의 body에 문자 내용을 직접 반환한다.

<br>

![그림7](https://backtony.github.io/assets/img/post/spring/start/2-7.PNG)

동작과정을 살펴보자. 내장 톰켓서버가 먼저 받고 스프링으로 던진다. 스프링은 컨트롤러에서 hello-api가 있는 것을 확인했으나 @ResponseBody 어노테이션이 붙어있는 것을 확인했다. 이게 없었을 때는 스프링은 뷰 리졸버한테 던졌었는데, 이것은 http에 응답에 이 데이터를 그대로 넘겨야겠다고 동작한다. 즉, 류 리졸버가 아니라 HttpMessageConverter가 동작한다. 단순 문자의 경우는 StringConverter가 동작해서 문자를 http 응답에 바디부에 넣어서 그냥 줘버리고 끝난다. 하지만 객체일 경우에는 JsonConverter가 동작하여 json방식으로 데이터를 만들어서 http 응답에 반환하는 것이다.

<br>

---
__본 포스팅은 인프런 김영한님의 '스프링 입문 - 코드로 배우는 스프링 부트, 웹MVC, DB접근 기술' 강의를 듣고 정리한 내용을 바탕으로 작성하였습니다. [[강의 링크](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%EC%9E%85%EB%AC%B8-%EC%8A%A4%ED%94%84%EB%A7%81%EB%B6%80%ED%8A%B8){:target="_blank"}]__