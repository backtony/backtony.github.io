---
layout: post
title:  Spring 핵심 - 컴포넌트 스캔
subtitle:   Spring 핵심 - 컴포넌트 스캔
categories: spring
tags: basic
comments: true
# header-img:
---

+ __목차__
  - [1. 컴포넌트 스캔과 의존관계 자동 주입](#1-컴포넌트-스캔과-의존관계-자동-주입)    
  - [2. 탐색 위치](#2-탐색-위치)    
  - [3. 컴포넌트 스캔 기본 대상](#3-컴포넌트-스캔-기본-대상)    
  - [4. 필터](#4-필터)    
  - [5. 중복 등록과 충돌](#5-중복-등록과-충돌)    


## 1. 컴포넌트 스캔과 의존관계 자동 주입
---
이전까지는 클래스에 @Configuration과 @Bean을 붙여서 직접 스프링빈에 등록했다. 만약 스프링 빈에 넣어야 하는 것이 무수히 많아진다면 일일이 이렇게 작성하는 과정은 매우 번거로워질뿐만 아니라 실수를 유발할 수 있다. 따라서 자동으로 스프링 빈으로 등록해주고 의존관계를 주입해주는 컴포넌트라는 것이 있다.  
먼저 클래스를 만든다.
```java
@Configuration
@ComponentScan (    
    excludeFilters = @ComponentScan.Filter(type= FilterType.ANNOTATION,classes = Configuration.class)
)
public class AutoAppConfig {

}
```
전에는 Configuration을 붙여주고 클래스 안에 빈을 붙이고 작성했는데 이제는 @Configuration 아래 @ComponentScan만 붙여주면 끝이다. @ComponentScan이란 스프링이 뜰 때 @Component 어노테이션이 붙은 클래스를 찾아서 자동으로 스프링빈으로 등록해주는 기능이다. 이때, @Configuration이 붙은 클래스도 자동으로 등록되는데 이유는 @Configuration 안에 @Component 어노테이션이 들어있기 때문이다. excludeFilters는 자동으로 스프링 빈으로 등록되는 것들 중에서 제외하고 싶은 것을 설정하는 것이다. 실무에서는 보통 사용하지 않는데, 지금은 전에 Configuration으로 직접 스프링 빈으로 등록한 것과 지금 하는 것중 어느 것이 스프링 빈으로 등록한지 확인할 수 없어서 전에 만들었던 것을 자동으로 등록하지 않도록 한 것이다.  
이제 스프링 빈으로 자동 등록할 클래스를 찾아서 @Component를 붙여주면 된다. 사실 여기서 살짝 고민했다. 인터페이스에 붙여줘야 하는지, 구현 클래스에 붙여줘야 하는지 말이다. 이건 스프링 빈을 사용하는 이유를 생각해보면 쉽게 해결된다. 스프링 빈에 등록되면 싱글톤으로 하나의 객체를 공유한다. 실제 사용할 때는 인터페이스 = 구현 클래스로 사용한다. 그럼 여기에 들어오는 구현 클래스를 하나로 공유하려고 지금까지 이런 과정을 거쳐온 것이다. 그럼 당연히 구현 클래스를 스프링 빈에 등록해야 한다.
```java
@Component
public class MemberServiceImpl implements  MemberService{

    private final MemberRepository memberRepository;
   
    @Autowired
    public MemberServiceImpl(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    @Override
    public void join(Member member) {
        memberRepository.save(member);
    }

    @Override
    public Member findMember(Long memberId) {
        return memberRepository.findById(memberId);
    }
}
```
구현 클래스에 @Component를 붙여줬다. 전에는 @Configuration붙은 클래스에서 @Bean으로 직접 등록하는 과정에서 내가 직접 의존관계를 작성해줬다. 그런데 지금은 위에 작성했듯이 @Configuration이 붙은 클래스에는 아무런 정보도 적지 않았다. 이때 구현 클래스의 생성자에 @Autowired 어노테이션을 붙여주면 의존관계가 자동으로 주입된다. 스프링이 뜰 때, @Component가 붙은 클래스는 자동으로 객체가 만들어져 스프링 빈으로 등록되어 관리된다고 했다. 그럼 객체가 만들어질 때 생성자가 호출될텐데 (위 코드로 예시로) 생성자에 Autowired가 붙어있으면 생성자의 파라미터로 MemberRepository.class를 스프링 컨테이너에 찾아서 넣어준다. MemberRepository가 부모니까 구현체인 memorymemberrepository를 찾아서 넣어주는 것이다. Autowired 어노테이션을 통해 의존관계가 자동으로 주입되는 것이다.  
<br>


![그림1](https://backtony.github.io/assets/img/post/spring/basic/4-1.PNG)

@Component가 붙은 클래스는 자동으로 스프링 빈으로 등록된다고 했는데 스프링 컨테이너에는 위와 같이 등록된다. 빈 이름은 클래스의 이름에서 맨 앞글자만 소문자로 바뀐다. 만약 빈의 이름을 지정하고 싶다면 @Component("빈이름") 이렇게 어노테이션 옆에 붙여주면 된다. 하지만 보통 그대로 사용한다.


<br>

## 2. 탐색 위치
---
![그림2](https://backtony.github.io/assets/img/post/spring/basic/4-2.PNG)
```java
// 범위 default는 무엇인가
// @ComponentScan가 붙은 클래스의 패키지를 시작 위치로 지정

@Configuration
@ComponentScan (        
        basePackages = "hello.core",
        excludeFilters = @ComponentScan.Filter(type= FilterType.ANNOTATION,classes = Configuration.class)
)
public class AutoAppConfig {

}
```
@ComponentScan에서 자동 스프링 빈 등록 제외이외에도 스캔시작 위치를 지정할 수 있다. 
+ basePackages : 스캔 위치 지정, 위 그림을 확인하면 hello.core를 포함해서 하위 패키지를 모두 탐색해서 스캔한다.
    - basePackages ={"",""} 로 여러개의 시작 위치 지정 가능
+ basePackagesClasses : 지정한 클래스의 패키지를 시작 위치로 지정 
    - 해당 클래스를 확인하면 위에 패키지가 적혀있는데 그 패키지를 시작 위치로 한다는 의미

위와 같은 설정이 있지만 그래도 default값으로 사용하는게 좋다. default는 @ConponentScan이 붙은 클래스의 패키지를 시작 위치로 지정한다. 권장하는 방법은 패키지 위치를 지정하지 않는 default값으로 사용하고, 설정 정보 클래스의 위치를 프로젝트 최상단에 두는 것이 좋은 방법이다. 위 그림을 확인해보면 hello.core 패키지를 기점으로 안에 프로젝트가 생성되어 있다. 따라서 hello.core에 설정 정보 클래스를 만들어두면 클래스의 패키지는 hello.core이므로 default값으로 지정되어 hello.core을 포함한 하위는 모두 자동으로 컴포넌트 스캔 대상이 되는 것이다. 길게 설명했지만, __설정 정보 클래스는 프로젝트 최상단에 두고 범위는 default값으로 사용한다 정도로 알아두면 된다.__  
프로젝트를 만들 때 스프링 부트를 사용했는데 스프링 부트를 이용하면 XXXApplication이 만들어지는데 다음과 같다.
```java
package hello.core;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class CoreApplication {

	public static void main(String[] args) {
		SpringApplication.run(CoreApplication.class, args);
	}
}
```
스프링 부트의 대표 시작 정보인 @SpringBootApplication 어노테이션 안에는 @ComponentScan이 들어있다. 따라서 XXXApplication를 프로젝트 시작 루트 위치에 두면 된다. 이것이 관례이다. 그러므로 스프링 부트를 사용하면 사실 @ComponentScan을 따로 위에서 처럼 만들어줄 필요가 없다. 스프링 부트가 만들어준 XXXApplication에 이미 들어있기 때문이다.
<br>

## 3. 컴포넌트 스캔 기본 대상
---
@ComponentScan은 @Component뿐만 아니라 아래 내용도 대상으로 포함한다. 그런데 사실 아래 어노테이션 안에는 @Component가 붙어있다.
+ @Component : 컴포넌트 스캔에 사용
+ @Controller : 스프링 MVC 컨트롤러로 인식
+ @Service : 개발자들끼리 스프링 비즈니스 로직이 여기 있겠구나 하는 비지느스 계층 인식 용도(특별한 기능은 없음)
+ @Repository : 스프링 데이터 접근 계층으로 인식, 데이터 계층 예외를 스프링 예외로 변환
+ @Configuration : 스프링 설정 정보로 인식, 스프링 빈이 싱글톤을 유지하도록 처리

__cf) 앞서 계속 어노테이션 안에 어노테이션이 붙어있다고 했는데 어노테이션은 상속관계라는 것이 없다. 이런 관계는 스프링이 지원하는 기능이다.__

<br>

## 4. 필터
---
위에서 컴포넌트 스캔할 때 대상에서 추가, 제외했던 내용이다.
+ includeFilters : 컴포넌트 스캔 대상에 추가
+ excludeFilters : 컴포넌트 스캔 대상에 제외

어노테이션을 만들어서 BeanA 클래스에는 MyIncludeComponent 어노테이션을 붙이고, BeanB에는 MyExcludeComponent어노테이션을 붙였다는 가정하에 테스트 코드를 작성해보자.
```java
public class ComponentFilerAppConfigTest {
    @Test
    void filterScan() {
        ApplicationContext ac = new AnnotationConfigApplicationContext(ComponentFilterAppConfig.class);
        BeanA beanA = ac.getBean("beanA", BeanA.class);
        assertThat(beanA).isNotNull(); // BeanA는 자동 등록 대상에 추가됬으니 null이 아님
        Assertions.assertThrows(
                NoSuchBeanDefinitionException.class,
                () -> ac.getBean("beanB", BeanB.class)); // 람다식이 실행되면 스프링 빈에는 beanB가 없으니 예외 터짐
    }
    @Configuration
    @ComponentScan(
            // 스프링 빈 자동 등록 대상에서 추가, 제외
            // @ComponentScan.Filter 스태틱 임포트            
            includeFilters = @Filter(type = FilterType.ANNOTATION, classes = MyIncludeComponent.class),
            excludeFilters = @Filter(type = FilterType.ANNOTATION, classes = MyExcludeComponent.class)
    )
    static class ComponentFilterAppConfig {
    }
}
```
FilterType에는 5가지 옵션이 있는데 옵션중에서 ANNOTATION이 기본값으로, 어노테이션을 인식해서 동작한다. 기본값이므로 사실 type = FilterType.ANNOTATION은 지워도 정상적으로 동작한다.

<br>

## 5. 중복 등록과 충돌
---
+ 자동 빈 등록 vs 자동 빈 등록
    - @Component에 의해 자동으로 스프링 빈으로 등록되는데 빈 이름이 같은 경우의 충돌은 ConflictingBeanDefinitionException 예외가 발생한다.
+ 자동 빈 등록 vs 수동 빈 등록
    - 스프링 부트를 통하지 않고 그냥 실행시 수동 빈이 우선권을 가지고 수동 빈이 자동 빈을 오버라이딩 해버린다. 
    - 스프링 부트로 돌리면(XXXApplication을 돌리면) 오류가 발생한다. 

수동이 우선권을 가지게 의도해서 코딩하는 경우보다 사실상 의도치 않게 발생하는 경우가 더 많다. 따라서 스프링 부트는 이것을 막기 위해서 수동 빈과 자동 빈 등록이 충돌나면 오류가 발생하도록 기본값을 만든 것이다. 스프링 부트에서도 충돌 시 수동 빈으로 오버라이딩 하게 하려면 스프링 부트로 만들 때 resources에 생긴 properties에 다음과 같이 코딩하면 된다.

![그림2](https://backtony.github.io/assets/img/post/spring/basic/4-2.PNG)

```java
// 기본값이 false로 되어있음 -> true로 수정
spring.main.allow-bean-definition-overriding=true
```


<br>

---
__본 포스팅은 인프런 김영한님의 '스프링 핵심 원리 - 기본편' 강의를 듣고 정리한 내용을 바탕으로 복습을 위해 작성하였습니다. [[강의 링크](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%ED%95%B5%EC%8B%AC-%EC%9B%90%EB%A6%AC-%EA%B8%B0%EB%B3%B8%ED%8E%B8){:target="_blank"}]__