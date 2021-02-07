---
layout: post
title:  Spring 핵심 - 빈 생명주기 콜백
subtitle:   Spring 핵심 - 빈 생명주기 콜백
categories: spring
tags: basic
comments: true
# header-img:
---

+ __목차__
  - [1. 빈 생명주기 콜백](#1-빈-생명주기-콜백)    
  - [2. 빈 등록 초기화, 소멸 메서드](#2-빈-등록-초기화-소멸-메서드)    

## 1. 빈 생명주기 콜백
---
데이터베이스 커넥션 풀이나, 네트워크 소켓처럼 애플리케이션 시작 시점에 필요한 연결을 미리 해두고, 애들리케이션 종료 시점에 연결을 모두 종료하는 작업을 진행하려면, 객체의 초기화와 종료 작업이 필요하다.  
### 스프링 빈의 이벤트 라이프사이클
스프링 컨테이너 생성 -> 스프링 빈 생성 -> 의존관계 주입 -> 초기화 콜백 -> 사용 -> 소멸전 콜백 -> 스프링 종료  
+ 초기화 콜백 : 빈이 생성되고 빈의 의존관계 주입이 완료된 후 호출
+ 소면전 콜백 : 빈이 소멸되기 직전에 호출

__cf) 객체의 생성과 초기화를 분리하는 이유__  
생성자는 필수 정보(파라미터)를 받고, 메모리를 할당해서 객체를 생성하는 책임을 가지는 반면에 초기화는 생성된 값들을 바탕으로 외부 커넥션을 연결하는 등의 무거운 동작을 수행한다. 따라서 명확하게 나누는 것이 유지보수 관점에서 좋다.  
<br>

__cf) 콜백 함수__  
+ 다른 함수의 인자로써 이용되는 함수
+ 어떤 이벤트에 의해 호출되어지는 함수
<br>

## 2. 빈 등록 초기화, 소멸 메서드
---
### @PostConstruct, @PreDestory
스프링 빈으로 등록하는 클래스에서 초기화할 메서드와 소멸전 콜백할 소멸 메소드를 만들어두고 애노테이션으로 지정해두면 된다.
```java
// NetworkClient가 스프링 빈으로 등록되어있다고 가정
public class NetworkClient {
 
 // 객체 생성과 의존관계가 주입된 이후 초기화를 위해 실행되는 메소드
 @PostConstruct
 public void init() {
    System.out.println("NetworkClient.init");
    connect();
    call("초기화 연결 메시지");
 }
 // 빈이 소멸하기 전에 호출되는 소멸 메소드
 @PreDestroy
 public void close() {
    System.out.println("NetworkClient.close");
    disConnect();
 }
}
```
해당 애노테이션은 자바 표준이므로 스프링이 아닌 다른 컨테이너에서도 동작한다. 유일한 단점은 외부 라이브러리에는 적용하지 못한다는 점이다.
<br>

### initMethod, destroyMethod
외부 라이브러리에 초기화, 소멸 메서드를 지정하기 위해서는 initMethod과 destroyMethod를 사용한다.
```java
@Configuration
static class LifeCycleConfig {
    @Bean(initMethod = "init", destroyMethod = "close")
    public NetworkClient networkClient() {
        NetworkClient networkClient = new NetworkClient();
        networkClient.setUrl("http://hello-spring.dev");
        return networkClient;
    }
}
```
빈을 수동으로 등록하는 과정에서 @Bean(initMethod = "메서드명", destroyMethod = "메서드명")으로 등록해주면 된다. 초기화할 때는 initMethod값으로 들어온 메서드가, 소멸 전에는 destroyMethod로 들어온 메서드가 실행된다.  
@Bean의 destroyMethod 속성의 기본값은 (inferred)으로 등록되어 있다. 대부분의 라이브러리는 close, shutdown이라는 이름으로 종료 메서드를 사용하는데 (inferred)는 말그대로 추론기능으로 close, shutdown이라는 이름의 메서드를 자동으로 호출해준다. 따라서 종료 메서드는 따로 적어주지 않아도 된다.




<br>

---
__본 포스팅은 인프런 김영한님의 '스프링 핵심 원리 - 기본편' 강의를 듣고 정리한 내용을 바탕으로 복습을 위해 작성하였습니다. [[강의 링크](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%ED%95%B5%EC%8B%AC-%EC%9B%90%EB%A6%AC-%EA%B8%B0%EB%B3%B8%ED%8E%B8){:target="_blank"}]__