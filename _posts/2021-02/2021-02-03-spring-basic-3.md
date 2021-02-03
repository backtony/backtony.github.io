---
layout: post
title:  Spring 핵심 - 싱글톤
subtitle:   Spring 핵심 - 싱글톤
categories: spring
tags: basic
comments: true
# header-img:
---

+ __목차__
  - [1. 싱글톤](#1-싱글톤)    
  - [2. 싱글톤 주의점](#2-싱글톤-주의점)    
  - [3. Configuration과 싱글톤](#3-configuration과-싱글톤)    


## 1. 싱글톤
---
[싱글톤](https://backtony.github.io/java/2020/11/21/java-13/#5-%EC%8B%B1%EA%B8%80%ED%86%A4)에 관해서는 자바 기초문법을 공부할 때 나왔던 개념이다. 스프링 컨테이너는 알아서 코드를 다 짜주면서 자동으로 싱글톤 방식으로 데이터를 저장한다.(예외가 있긴 한데 대부분 실무에서도 자동으로 되는 싱글톤 방식 사용) 따라서 스프링 컨테이너에서 꺼내서 쓰는 데이터는 필요할 때마다 새로운 인스턴스를 만들어서 서로 다른 인스턴스를 가져오는게 아니라 하나의 인스턴스를 참조하는 것이다. 아래 그림을 보면 이해하기 쉬울 것이다.
![그림1](https://backtony.github.io/assets/img/post/spring/start/4-4.PNG)

<br>

## 2. 싱글톤 주의점
---
싱글톤 패턴은 여러 클라이언트가 하나의 같은 객체를 공유하기 때문에 싱글톤 객체는 상태를 유지(statefule)하게 설계하면 안된다.  
__무상태(stateless) 설계__
+ 특정 클라이언트에 의존적인 필드가 있으면 안된다.
+ 값을 변경할 수 있는 필드가 있으면 안된다. 
+ 필드 대신 공유되지 않는 지역변수, 파라미터, ThreadLocal 등을 사용해야 한다.

간단한 예시로 멀티스레드를 생각해볼 수 있다. 사용자1이 싱글톤 객체 필드에 값을 1로 저장해두고 10분 뒤에 값을 불러왔다고 하자. 그런데 10분 사이에 사용자2가 싱글톤 객체의 필드값을 0으로 수정했다면, 사용자1은 불러올 값을 1로 예상했지만 실제로는 0을 가져오게 되는 것이다. 싱글톤 패턴 즉, 객체를 공유하고 있기 때문에 이런 문제가 발생하는 것이다. 따라서 싱글톤 패턴의 경우, 싱글톤 객체의 필드는 작성하지 않는게 좋다. 해결방법 은 위에서 설명한 방법들이 있고 지역변수의 예를 들면 싱글톤 객체의 메소드로 필드값을 저장하고 나중에 불러오는 방식이 아니라 필드값을 선언하지 않고 바로 메소드의 리턴값으로 값을 반환해서 사용하는 곳에서 지역변수로 받아서 사용하는 방법이 있다.



<br>

## 3. Configuration과 싱글톤
---
```java
@Configuration
public class AppConfig {
 @Bean
 public MemberService memberService() {
 return new MemberServiceImpl(memberRepository());
 }
 @Bean
 public OrderService orderService() {
 return new OrderServiceImpl(
 memberRepository(),
 discountPolicy());
 }
 @Bean
 public MemberRepository memberRepository() {
 return new MemoryMemberRepository();
 }
}
```
위와 같이 설정정보가 등록된 상황에서 memberService를 호출한다면 memberService -> memberRepository -> MemoryMemberRepository가 될 것이고, orderService를 호출하면 orderService -> memberRepository -> MemoryMemberRepository 로 결국 MemoryMemberRepository가 2번 만들어지는 것을 확인할 수 있다. 그럼 결국 다른 인스턴스가 들어가니 싱글톤이 깨진 것이 아닌가 라고 생각할 수 있다. 하지만 실제로 테스트해보면 같은 MemoryMemberRepository를 참조하고 있는 것을 확인할 수 있다. 이런 것을 가능하게 해주는 것은 @Configuration이다.  
<br>


```java
// AppConfig도 자동으로 스프링 빈으로 등록된다.
ApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);

// AppConfig를 빈에서 꺼내서 출력
AppConfig bean = ac.getBean(AppConfig.class);
System.out.println("bean = " + bean.getClass());
// 출력: bean = class hello.core.AppConfig$$EnhancerBySpringCGLIB$$bd479d70
```
AnnotationConfigApplicationContext의 파라미터로 AppConfig.class을 넘기면서 AppConfig는 자동으로 스프링 빈에 등록이 된다. 이것을 꺼내서 출력해보면 순수한  class hello.core.AppConfig가 아니라 뒤에 뭐가 더 붙어서 나온다. 이것은 실제로 내가 등록한 AppConfig가 아니라는 의미인데, 스프링이 CGLIB라는 바이트 코드 조작 라이브러리를 사용해서 AppConfig 클래스를 상속받아 override한 임의의 다른 클래스를 만들고 그 클래스를 스프링 빈으로 등록한 것이다. 이 다른 클래스의 부모는 AppConfig이므로 부모클래스로 꺼냈으니 자식도 확인할 수 있으므로 자식 클래스가 딸려나와 출력된 것이다.  
앞서 내가 만든 AppConfig가 스프링 빈으로 등록되는 것이 아니라 이것을 상속하여 override한 다른 클래스가 스프링 빈에 등록된다고 했다. 이때 Override되는 형식을 간단히 나타내면 다음과 같다.
```java
@Bean
public MemberRepository memberRepository() {

 if (memoryMemberRepository가 이미 스프링 컨테이너에 등록되어 있으면?) {
 return 스프링 컨테이너에서 찾아서 반환;
 } else { //스프링 컨테이너에 없으면
 기존 로직을 호출해서 MemoryMemberRepository를 생성하고 스프링 컨테이너에 등록
 return 반환
 }
}
```
내가 작성한 로직에서 위와 같은 형식으로 override된 코드로 등록이 되는 것이다. 즉, memberRepository가 처음 호출되었다면 내가 실제로 작성한 로직을 타고 MemoryMemberRepository를 생성하고 스프링 컨테이너에 등록한다. 이후부터는 memberRepository가 호출되어도 내가 작성한 로직을 타는게 아니라 스프링 컨테이너에서 찾아서 반환하는 것이다. 이런 방식으로 싱글톤이 보장되는 것이다. @Configuration이 가능하게 해주는 것이기에 Configuration이 없다면 스프링 빈으로 등록은 되나 싱글톤이 보장되지 않는다. 따라서 스프링 설정정보는 @Configuration은 항상 적어준다고 보면 된다.









<br>

---
__본 포스팅은 인프런 김영한님의 '스프링 핵심 원리 - 기본편' 강의를 듣고 정리한 내용을 바탕으로 복습을 위해 작성하였습니다. [[강의 링크](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%ED%95%B5%EC%8B%AC-%EC%9B%90%EB%A6%AC-%EA%B8%B0%EB%B3%B8%ED%8E%B8){:target="_blank"}]__