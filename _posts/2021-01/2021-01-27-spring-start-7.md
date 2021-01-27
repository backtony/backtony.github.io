---
layout: post
title:  Spring 입문 - AOP
subtitle:   Spring 입문 - AOP
categories: spring
tags: start
comments: true
# header-img:
---

+ __목차__
  - [1. AOP가 필요한 상황](#1-aop가-필요한-상황)    
  - [2. AOP 적용](#2-aop-적용)    
    


## 1. AOP가 필요한 상황
---
만약 모든 메소드의 호출시간을 측정하고 싶다고 한다면 각각의 메서드마다 시간 측정에 관한 코드를 해야한다. try finally로 모든 메서드마다 시간 측정 코드를 넣게 되면 핵심 비즈니스와 시간을 측정하는 로직이 섞여서 유지보수가 매우 어렵게 된다. 시간을 측정하는 로직을 별도의 공통 로직으로 만들기 매우 어려울 뿐만아니라 로직을 변경할 경우, 직접 모두 찾아가며 변경해야 한다. 이럴 때 해결책으로 AOP를 사용한다.


<br>

## 2. AOP 적용
---
hello.spring 패키지 아래 aop라는 패키지를 만들어주고 TimeTraceAop 클래스를 만들어서 코딩을 시작하자.
```java
package hello.hellospring.aop;


import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;

@Aspect // Aspect를 적어줘야 aop로 사용가능
// @Component 으로 스프링빈으로 등록해줘도 되는데, aop같은 경우는 스프링 빈에 직접 등록해주는게 좋다
// 평범하지 않은 것이므로 직접 등록해서 이런게 있다고 인지해주는게 좋다.
public class TimeTraceAop {
    // 그냥 메뉴얼 보고 따라하면 된다.
    // Around는 어디에 붙여줄 껀지 타겟을 정하는 것이다.
    // 다음과 같이 작성하면 hello.hellospring 패키지 전체에 붙음
    // hello.hellospring.service..*(..) 하면 service 하위에 있는 것에 붙음
    @Around("execution(* hello.hellospring..*(..))")
    public Object execute(ProceedingJoinPoint joinPoint) throws Throwable{
        long start = System.currentTimeMillis();

        System.out.println("start: " + joinPoint.toString()); // 메소드이름 문자열로 반환해서 찍기
        try {
            // 다음 메소드로 진행
            return joinPoint.proceed();
        } finally {
            long end = System.currentTimeMillis();
            long timeMs = end - start;
            System.out.println("end "+ joinPoint.toString()+ " "+ timeMs + "ms" );
        }


    }

}
```
<br>

Component 말고 직접 configuration에 등록하자.
```java
package hello.hellospring;
import hello.hellospring.aop.TimeTraceAop;
import hello.hellospring.repository.*;
import hello.hellospring.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import javax.persistence.EntityManager;
import javax.sql.DataSource;
@Configuration
public class SpringConfig {
    private final MemberRepository memberRepository;

    @Autowired
    public SpringConfig(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    @Bean
    public MemberService memberService() {
        return new MemberService(memberRepository);
    }

    @Bean
    public TimeTraceAop timeTraceAop(){
        return new TimeTraceAop();
    }

}
```

<Br>

### 동작과정
![그림1](https://backtony.github.io/assets/img/post/spring/start/7-1.PNG)

붙이기 전에는 위와 같이 동작한다.

<br>

![그림2](https://backtony.github.io/assets/img/post/spring/start/7-2.PNG)

aop를 적용하면 프록시라는 가짜 memberSErvice를 만들어내서 스프링 빈을 등록할 때 진짜 스프링 빈 앞에 가짜 스프링 빈을 세워둔다. 가짜 스프링 빈에서 joinpoint.proceed()를 타서 진짜를 호출해준다. 결과적으로 컨트롤러가 호출하는 것은 진짜가 아닌 프록시라는 가짜 멤버서비스를 호출하는 것이다. 이런 기술 자체의 기반은 DI를 사용했기에 가능한 것이다. 컨트롤러에서는 그냥 DI로 받아 쓰는데 여기서 진짜가 아닌 프록시가 들어오게 되면서 가능하게 되는 것이다. 






<br>

---
__본 포스팅은 인프런 김영한님의 '스프링 입문 - 코드로 배우는 스프링 부트, 웹MVC, DB접근 기술' 강의를 듣고 정리한 내용을 바탕으로 작성하였습니다. [[강의 링크](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%EC%9E%85%EB%AC%B8-%EC%8A%A4%ED%94%84%EB%A7%81%EB%B6%80%ED%8A%B8){:target="_blank"}]__