---
layout: post
title:  Spring 핵심 - 스프링 빈 테스트
subtitle:   Spring 핵심 - 스프링 빈 테스트
categories: spring
tags: basic
comments: true
# header-img:
---

+ __목차__
  - [1. 전체 조회](#1-전체-조회)    
  - [2. 개별적 조회](#2-개별적-조회)    
  - [3. 스프링 빈 상속관계 조회](#3-스프링-빈-상속관계-조회)    

## 1. 전체 조회
---
AppConfig에 빈 코드를 작성해놓았다고 가정하고 시작한다.
```java
package hello.core.beanfind;

import hello.core.AppConfig;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.config.BeanDefinition;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;



public class ApplicationContextInfoTest {
    AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);

    @Test
    @DisplayName("모든 빈 출력하기") // 실행시 왼쪽 아래에 뜨는 이름 변경
    void findAllBean(){
        String[] beanDefinitionNames = ac.getBeanDefinitionNames();// 스프링에 등록된 모든 빈 이름 가져오기
        for (String beanDefinitionName : beanDefinitionNames) { // 하나씩 대입
            // 빈 이름으로 빈 객체(인스턴스) 가져오기
            // 예를 들면 beandefinitionname은 Memberrepository, value값은 memorymemberrepository
            Object bean = ac.getBean(beanDefinitionName);
            System.out.println("name = " + beanDefinitionName + "object = "+bean);
        }
    }
    @Test
    @DisplayName("애플리케이션 빈 출력하기") // 실행시 왼쪽 아래에 뜨는 이름 변경
    void findApplicationBean(){
        String[] beanDefinitionNames = ac.getBeanDefinitionNames();// 정의된 빈 이름을 전부 가져오기
        for (String beanDefinitionName : beanDefinitionNames) { // 하나씩 대입
            BeanDefinition beanDefinition = ac.getBeanDefinition(beanDefinitionName);// 빈 하나하나에 대한 메타데이터 정보

            // BeanDefinition.ROLE_APPLICATION 직접 등록한 애클리케이션 빈
            // BeanDefinition.ROLE_INFRASTRUCTURE 스프링 내부에서 사용하는 빈
            if (beanDefinition.getRole() == BeanDefinition.ROLE_APPLICATION){
                Object bean = ac.getBean(beanDefinitionName);
                System.out.println("name = " + beanDefinitionName + "object = "+bean);
            }
        }
    }
}
```
+ getBeanDefinitionNames : 스프링에 등록 된 모든 빈 이름 조회
+ getBean : 빈 이름으로 빈 객체(인스턴스) 조회
+ getBeanDefinition : 빈에 대한 메타데이터 정보


<Br>


## 2. 개별적 조회
---
```java
public class ApplicationContextBasicFindTest {
    AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);

    @Test
    @DisplayName("빈 이름으로 조회")
    void findBeanByName(){
        MemberService memberService = ac.getBean("memberService", MemberService.class);
        assertThat(memberService).isInstanceOf(MemberServiceImpl.class);
    }
    @Test
    @DisplayName("이름 없이 타입으로만 조회")
    void findBeanByType(){
        MemberService memberService = ac.getBean(MemberService.class);
        assertThat(memberService).isInstanceOf(MemberServiceImpl.class);
    }

    // 위에 둘은 인터페이스 타입으로 조회했고 아래는 구체화 타입으로 조회했다
    // 실제로 인스턴스 타입을 보고 결정하기 때문에 구체화 타입으로 조회해도 상관 없다.
    // 구체화 타입으로 확인은 좋은 코딩이 아니다.
    // 역할과 구현을 구분해야하고 역할에 의존해야하는 것이 좋기 때문

    @Test
    @DisplayName("구체화 타입으로 조회")
    void findBeanByType2(){
        MemberService memberService = ac.getBean(MemberServiceImpl.class);
        assertThat(memberService).isInstanceOf(MemberServiceImpl.class);
    }

    @Test
    @DisplayName("빈 이름으로 조회 X")
    void findBeanByNameX(){
        // junit assertions.asserThrow 사용
        // 원하는 예외가 터지는지 확인
        // 오른쪽 파라미터의 로직이 실행하면 왼쪽 예외가 터지면 성공
        assertThrows(NoSuchBeanDefinitionException.class,
            () -> ac.getBean("xxx", MemberService.class));
    }

     @Test
    @DisplayName("타입으로 조회시 2개 이상 -> 중복 오류 발생")
    void findBeanByType3(){
        // junit assertions.asserThrow 사용
        // 원하는 예외가 터지는지 확인
        // 오른쪽 파라미터의 로직이 실행하면 왼쪽 예외가 터지면 성공
        assertThrows(NoUniqueBeanDefinitionException.class,
                () -> ac.getBean(MemberService.class));
    }

    @Test
    @DisplayName("특정 타입 모두 조회")
    void findBeanByType4(){
        // 특정 타입의 빈 모두 꺼내기
        Map<String, MemberRepository> beansOfType = ac.getBeansOfType(MemberRepository.class);
        for (String key : beansOfType.keySet()) {
            System.out.println("key = " + key + "value = "+beansOfType.get(key));
        }
        assertThat(beansOfType.size()).isEqualTo(2); // 나온게 2개인지 확인

    }


}
```
+ junit의 assertThroew : 2번 파라미터의 실행 결과가 1번 파라미터와 같으면 성공, 실패시 오류
+ 이름 없이 타입으로만 조회할 경우, 같은 타입이 2개 있다면 오류 발생 -> 해결책 : 이름으로 조회
+ getBeansOfType : 특정 타입 빈 모두 꺼내기

<Br>

## 3. 스프링 빈 상속관계 조회
---
위에서 타입으로 조회했을 때 같은 타입이 2개 이상이면 오류가 발생했던 것이랑 비슷하다. 
```java
@Configuration
static class TestConfig {
@Bean
public DiscountPolicy rateDiscountPolicy() {
    return new RateDiscountPolicy();
    }
@Bean
public DiscountPolicy fixDiscountPolicy() {
    return new FixDiscountPolicy();
    }
}
```
이렇게 2개가 빈으로 등록되어 있을 때 DiscountPolicy.class로 조회하게 되면 2개가 나와서 오류가 발생한다. 해결방법은 빈 이름을 지정해서 조회하거나, 특정 하위 타입으로 조회하면 된다. 앞서 설명했듯이 하위 타입으로 조회하는 것은 구현에 의존하는 것이기에 좋지 않다.  
2번에서 설명했듯이 부모 타입을 모두 조회하려면 beansOfType을 사용하면 되고, java의 최고 부모는 Object이므로 Object.class로 꺼내면 전부 다 조회할 수 있다.  
<br>







<br>

---
__본 포스팅은 인프런 김영한님의 '스프링 핵심 원리 - 기본편' 강의를 듣고 정리한 내용을 바탕으로 복습을 위해 작성하였습니다. [[강의 링크](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%ED%95%B5%EC%8B%AC-%EC%9B%90%EB%A6%AC-%EA%B8%B0%EB%B3%B8%ED%8E%B8){:target="_blank"}]__