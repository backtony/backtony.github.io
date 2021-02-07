---
layout: post
title:  Spring 핵심 - 의존관계 자동 주입
subtitle:   Spring 핵심 - 의존관계 자동 주입
categories: spring
tags: basic
comments: true
# header-img:
---

+ __목차__
  - [1. 의존관계 주입 방법](#1-의존관계-주입-방법)    
  - [2. 옵션 처리](#2-옵션-처리)    
  - [3. lombok 라이브러리](#3-lombok-라이브러리)    
  - [4. 조회 빈이 2개 이상일 때](#4-조회-빈이-2개-이상일-때)    
  - [5. 애노테이션 직접 만들기](#5-애노테이션-직접-만들기)    
  - [6. 조회한 빈이 모두 필요할 때](#6-조회한-빈이-모두-필요할-때)    
  - [7. 자동, 수동의 기준](#7-자동-수동의-기준)    


## 1. 의존관계 주입 방법
---
스프링 컨테이너는 두 가지 라이프 사이클이 있다. 
1. 스프링 빈 등록 
2. 연관관계 자동 주입  

스프링 빈을 등록할 때 어쩔수 없이 생성자를 호출해야하기 때문에 생성자에는 빈 등록과 동시에 의존관계가 자동 주입된다. 하지만 이외의 경우, 예를 들면 수정자 주입 같은 경우는 빈 등록 이후에 연관관계 주입단계에서 주입된다.  

+ 생성자 주입
    - 지금까지 계속 해왔던 방식이 생성자를 통한 의존관계 주입이다.
    - 생성자는 스프링이 뜰 때, 한 번만 호출되므로 불변, 필수(private final) 의존관계에 주로 사용
    - 생성자가 단 한개라면, @Autowired 생략 가능
+ 수정자 주입(setXXX 주입)
    - setter로 필드의 값을 변경하는 수정자 메소드를 통한 의존관계 주입
    - 선택, 변경 가능성이 있는 의존관계에 주로 사용
+ 필드 주입
    - 필드 자체에 @Autowired를 붙여 바로 의존관계 주입
    - 외부에서 변경하기 불가능해서 테스트하기 힘들다.
    - DI프레임워크가 없으면 아무것도 할 수 없다.
    - 실제 코드와 관계없는 테스트 코드(테스트 할 때만 쓸 것이므로), 스프링 설정 목적의 @Configuration 같은 곳(Configuration클래스는 스프링에서만 쓸 것이므로)에서만 사용 권장
+ 일반 메소드 주입
    - 메소드 위에 @Autowired 붙여서 사용하는 건데 사실 수정자주입이랑 다를게 없다.
    - 한번에 여러 필드 주입을 받을 수 있는데 거의 사용하지 않는다. 

의존관계는 대부분 시작부터 끝까지 변경할 일이 없다. 생성자 주입을 하면 final 키워드를 사용해서 주입 이후의 변화를 막을 수 있고 순수한 자바 코드로 테스트하는 경우에도 누락을 막을 수 있다. 따라서 대부분 __생성자 주입을 권장한다.__  

cf) 스프링 컨테이너가 관리하는 스프링 빈이어야만 @Autowired가 동작한다.

<br>

## 2. 옵션 처리
---
스프링 빈에 주입 대상이 없다면 오류가 터진다. 하지만 옵션으로 주입 대상이 없는 경우도 처리할 수있는 3가지 방법이 있다.
+ @Autowired(required=false)
    - 주입 대상이 없으면 메서드 자체가 호출이 안된다.
+ 파라미터 앞에 @Nullable을 붙이면 주입 대상이 없을 때 null이 주입된다.
    - ex) void setNoBean(@Nullable Member member)
+ Optional<>을 사용하면 주입 대상이 없을 때 Optional.empty가 주입된다.
    - ex) void setNoBean(Optional< Member > member)

<Br>

## 3. lombok 라이브러리
---
개발 단계에서는 대부분이 불변이기 때문에 생성자 주입을 하고 필드에 final 키워드를 사용하게 된다. 그런데 필드마다 생성자를 만드는 과정이 귀찮기 때문에 이 과정을 lombok 라이브러리를 이용해서 최적화할 수 있다.  
build.gradle에 다음 코드를 추가해줘야 한다. 애초에 프로젝트를 만들 때, spring.io에서 dependency에서 lombok을 추가해주면 되지만 지금은 안해줬기에 이렇게 추가해주고 코끼리모양 클릭으로 적용해준다. 그리고 Prefrences - plugin - lombok 설치, Prefrences - Annotation - Processors Enable annotation processing 체크를 해줘야 한다.
```java
// build.gradle
//lombok 라이브러리 추가 시작
 compileOnly 'org.projectlombok:lombok'
 annotationProcessor 'org.projectlombok:lombok'
 testCompileOnly 'org.projectlombok:lombok'
 testAnnotationProcessor 'org.projectlombok:lombok'
 //lombok 라이브러리 추가 끝
```
<Br>

lombok의 기능은 여러가지 있지만 대표적으로 다음과 같은 어노테이션이 있다.
+ @Setter : 필드의 setter을 만들어준다.
+ @Getter : 필드의 getter을 만들어준다.
+ @RequiredArgsConstructor : final이 붙은 필드들을 모아서 생성자를 만들어준다.

해당 애노테이션을 붙여주면 눈에 보이진 않지만, 컴파일 시점에서 자동으로 생성해준다. 생성자를 딱 한개두면 @Autowired를 생략할 수 있기 때문에 여기서 lombok을 활용하면 아래와 같이 코드를 상당히 줄일 수 있다.
```java
// lombok 미적용
@Component
public class OrderServiceImpl implements OrderService{

    private final MemberRepository memberRepository;
    private final DiscountPolicy discountPolicy;

    // @Autowired 생성자 한개이므로 생략해서 코드 줄이고
    public OrderServiceImpl(MemberRepository memberRepository, DiscountPolicy discountPolicy) {
        this.memberRepository = memberRepository;
        this.discountPolicy = discountPolicy;
    }
}

// lombok 라이브러리 추가
@Component
@RequiredArgsConstructor
public class OrderServiceImpl implements OrderService{

    private final MemberRepository memberRepository;
    private final DiscountPolicy discountPolicy;
}
```
<br>

## 4. 조회 빈이 2개 이상일 때
---
자동으로 의존관계가 주입될 때, 추상화에 의존하기 때문에 주어진 부모타입으로 스프링 빈에서 찾을 것이다. 그런데 만약 스프링 빈에 자식타입이 2개 이상이 있을 때, 무엇을 주입해줘야할지하는 문제가 생겨 오류가 뜬다. 이런 상황을 어노테이션으로 간단하게 해결하는 3가지 방법이 있다.
### @Autowired
Autowired는 타입 매칭을 우선적으로 한 뒤에 여러 개의 빈이 검색되면 파라미터 명, 필드 명이 빈의 이름과 일치하는 것을 주입한다. 
```java
// 기존 코드 -> 2개 발견 오류
 @Autowired
    public OrderServiceImpl(MemberRepository memberRepository, DiscountPolicy discountPolicy) {
        this.memberRepository = memberRepository;
        this.discountPolicy = discountPolicy;
    }
// 2개 발견했으나 파라미터 명을 빈 이름과 일치하는 것 주입
@Autowired
    public OrderServiceImpl(MemberRepository memberRepository, DiscountPolicy rateDiscountPolicy) {
        this.memberRepository = memberRepository;
        this.discountPolicy = rateDiscountPolicy;
    }
```
<br>

### @Qualifier
스프링 빈의 이름 외에 또 다른 구분자를 넣어주는 방법이다. @Component로 스프링 빈에 자동등록 할 때, @Qualifier('구분명')의 어노테이션을 붙여주고 주입되는 생성자 파라미터 앞에 @Qualifier('구분명')를 붙여주면 구분명이 같은 것으로 주입시켜주고 만약 없다면 구분명과 빈 이름이 일치하는 것을 찾고 없다면 NoSuchBeanDefinitionException예외를 발생시킨다.
```java
@Component
@Qualifier("rateDiscountPolicy")
~~~~ // 빈에 등록할 클래스에 @Qualifier로 구분자 넣어주고

// 생성자 파라미터 앞에 구분자 넣어준다.
public OrderServiceImpl(MemberRepository memberRepository, @Qualifier("rateDiscountPolicy") DiscountPolicy rateDiscountPolicy){}
```
<Br>

### @Primary
@Component로 스프링 빈에 자동등록 할 때, 우선순위를 지정해주는 방법이다. @Qualifier와 달리 주입되는 곳에 추가적으로 처리코드를 붙여주지 않아도 된다.
```java
@Component
@Primary // 여러 개의 빈이 검색되면 이것을 우선으로 주입
// 이외 코드 추가 없음
```
<br>

@Primary와 @Qualifier이 충돌한다면 당연히 수동적인 @Qualifier가 우선권을 가진다.  
__즉, 같은 부모타입의 2가지 이상 자식 타입이 스프링 빈에 들어가게 된다면 반드시 위와 같은 처리 중 한 가지를 사용해야 한다.__ 처리하지 않고 뒤에 실습을 진행했다가 오류를 한참 찾았다.
<br>

## 5. 애노테이션 직접 만들기
---
위에서 사용한 @Qualifier에서 구분자를 문자로 적으면 컴파일 시 타입 체크가 안된다.(구분자를 잘못 적어도 동작한다는 뜻) 따라서 애노테이션을 직접 만들어서 사용하는 것이 좋다.
```java
@Target({ElementType.FIELD, ElementType.METHOD, ElementType.PARAMETER, ElementType.TYPE, ElementType.ANNOTATION_TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Inherited
@Documented
@Qualifier("mainDiscountPolicy")
public @interface MainDiscountPolicy {
}
```
위의 어노테이션은 Qualifier가 가지고 있는 애노테이션을 다 복사해온 것이고, @Qualifier("mainDiscountPolicy")는 내가 구분자로 지정할 내용을 적어서 애노테이션을 붙여준 것이다. 따라서 이제부터는 @Qualifier("mainDiscountPolicy") 대신 @MainDiscountPolicy을 사용할 수 있다. 똑같이 동작한다.
<br>

## 6. 조회한 빈이 모두 필요할 때
---
조회한 빈이 여러 개 일때 모두 필요한 경우라면 Map, List로 빈을 받아서 사용하면 된다.
```java
public class AllBeanTest {

    @Test
    void findAllBean(){
        ApplicationContext ac = new AnnotationConfigApplicationContext(AutoAppConfig.class, DiscountService.class);        
        DiscountService discountService = ac.getBean(DiscountService.class);
        // Map에서 키값이 fixDiscountPolicy인 value를 꺼냄
        DiscountPolicy fixDiscountPolicy = discountService.policyMap.get("fixDiscountPolicy");
        // Map에서 키값이 rateDiscountPolicy value를 꺼냄
        DiscountPolicy rateDiscountPolicy = discountService.policyMap.get("rateDiscountPolicy"); 

    }
    @RequiredArgsConstructor // lombok 라이브러리 사용
    static class DiscountService{
        private final Map<String, DiscountPolicy> policyMap; // 주입될 때 key는 빈 이름, value는 스프링 빈
        private final List<DiscountPolicy> policies;
    }
}
```
의존관계 주입에 따라 DiscountPolicy가 스프링 빈에서 자식타입 fixDiscountPolicy와 rateDiscountPolicy 2개가 스프링 빈에 검색된다. 현재 ratediscountpolicy에 @primary를 주었기에 하나만 들어가는 보통의 경우라면 ratediscountpolicy가 들어가겠지만, Map이나 List로 받을 경우, 전부 다 조회된 전체가 들어오게 된다. 위 코드는 Map으로 전부 받아서 저장한 뒤에 getBean으로 키값을 주고 꺼내서 원하는 것을 사용할 수 있는 방법이다.

<br>

## 7. 자동, 수동의 기준
---
편리한 자동 기능을 기본적으로 사용하고, 기술 지원 객체는 수동으로 등록하는 것이 좋다. 다형성을 활용하는 비즈니스 로직은 수동으로 등록해서 한 눈에 확인할 수 있도록 하는 것을 고려해보도록 한다.

<br>

---
__본 포스팅은 인프런 김영한님의 '스프링 핵심 원리 - 기본편' 강의를 듣고 정리한 내용을 바탕으로 복습을 위해 작성하였습니다. [[강의 링크](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%ED%95%B5%EC%8B%AC-%EC%9B%90%EB%A6%AC-%EA%B8%B0%EB%B3%B8%ED%8E%B8){:target="_blank"}]__