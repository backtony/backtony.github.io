---
layout: post
title:  Spring 핵심 - 스프링 빈 테스트, 스프링 빈 상속관계, 메타 정보
subtitle:   Spring 핵심 - 스프링 빈 테스트, 스프링 빈 상속관계, 메타 정보
categories: spring
tags: basic
comments: true
# header-img:
---

+ __목차__
  - [1. 전체 조회](#1-전체-조회)    
  - [2. 개별적 조회](#2-개별적-조회)    
  - [3. 스프링 빈 상속관계 조회](#3-스프링-빈-상속관계-조회)    
  - [4. 스프링 빈 상속관계](#4-스프링-빈-상속관계)    
  - [5. 스프링 빈 설정 메타 정보](#5-스프링-빈-설정-메타-정보)    


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

AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class); 에서 ApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class); 를 사용하지 않은 이유는 ApplicationContext에는 getBeanDefinition이 없다. 왜냐하면 실제로 beanDefinition 정보를 뽑아쓸 필요가 없기 때문에 이런 복잡한 메소드들은 ApplicationContext에 구현되어있지 않다. 여기서는 저 메소드가 필요했기 때문에 AnnotationConfigApplicationContext로 받았다고 생각하면 된다. 보통은 ApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class); 이렇게 사용한다고 생각하면 된다.

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

## 4. 스프링 빈 상속 관계
---
![그림1](https://backtony.github.io/assets/img/post/spring/basic/2-1.PNG)

+ BeanFactory : 스프링 컨테이너의 최상위 인터페이스이고, 스프링 빈을 관리하고 조회하는 역할을 담당한다.
+ ApplicationContext : BeanFactory 기능을 모두 상속받아 제공하며, 위 그림과 같이 다른 인터페이스도 상속받아서 기능을 제공한다. 
    - 메시지소스 활용한 국제화 기능
    - 환경변수
    - 애플리케이션 이벤트
    - 편리한 리소스 조회

ApplicationContext나 BeanFactory를 스프링 컨테이너라고 한다.

<br>

## 5. 스프링 빈 설정 메타 정보
---
![그림2](https://backtony.github.io/assets/img/post/spring/basic/2-2.PNG)

@Configuration 으로 사용되었던 자바 파일을 다른 확장자의 파일로(xml) 코딩해서 제공해도 같은 기능을 수행할 수 있다. 이유는 이것 또한 BeanDefination이라는 추상화 때문이다. 결국 어떤 파일이 BeanDefination을 만드는지는 상관없고 스프링 컨테이너는 만들어진 BeanDefination에만 의존한다. @bean당 각각 하나씩 메타 정보가 생성되고, 이것들을 묶어서 BeanDefination로 빈 설정 메타정보가 만들어진다. 결론은 스프링은 BeanDefination으로 스프링 빈 설정 메타정보를 추상화한다 정도로 알아두면 된다.  
참고로 스프링 빈을 만들 때는 직접적으로 등록하는 방법과 factoryBean을 통해 등록하는 방법이 있고 일반적으로 지금까지 해왔던 @Configuration을 통해 등록하는 것이 factoryBean을 통한 방법이다. 직접등록하는 경우는 거의 없다.


<br>

---
__본 포스팅은 인프런 김영한님의 '스프링 핵심 원리 - 기본편' 강의를 듣고 정리한 내용을 바탕으로 복습을 위해 작성하였습니다. [[강의 링크](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%ED%95%B5%EC%8B%AC-%EC%9B%90%EB%A6%AC-%EA%B8%B0%EB%B3%B8%ED%8E%B8){:target="_blank"}]__