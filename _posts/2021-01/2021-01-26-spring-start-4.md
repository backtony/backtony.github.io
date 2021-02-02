---
layout: post
title:  Spring 입문 - 스프링 빈과 의존관계
subtitle:   Spring 입문 - 스프링 빈과 의존관계
categories: spring
tags: start
comments: true
# header-img:
---

+ __목차__
  - [1. 컴포넌트 스캔과 자동 의존관계 설정](#1-컴포넌트-스캔과-자동-의존관계-설정)    
  - [2. 자바 코드로 직접 스프링 빈 등록하기](#2-자바-코드로-직접-스프링-빈-등록하기)    
  - [3. 장단점](#3-장단점)
    



## 1. 컴포넌트 스캔과 자동 의존관계 설정
---
지금까지 멤버, 서비스, 리포지토리를 만들었다. 이제부터는 화면에 붙이는 작업을 해야한다. 그러기 위해서는 컨트럴러와 뷰 템플릿을 이용해서 결과들을 html로 뿌려줘야 한다. 그럼 이제 컨트롤러를 만들 차례이다. 회원 컨트롤러가 회원서비스와 회원 리포지토리를 사용할 수 있게 의존관계를 만들어보자.  
컨트롤러 패키지에 MemberController를 만들자.
```java
// MemberController 클래스
@Controller
public class MemberController{
  private final MemberService memberService = new MemberService();
}
```
스프링은 처음에 시작할 때 스프링 컨테이너라는 스프링 통을 생성한다. 그리고 Controller 어노테이션이 있으면 해당하는 클래스의 인스턴스를 만들어서 스프링 컨테이너에 넣어두고 관린한다. 이런 관계를 스프링 컨테이너에 스프링 빈이 관리된다고 표현한다. 이렇게 스프링 컨테이너에 넣어두고 스프링이 관리하게 되는 순간부터는 스프링 컨테이너로부터 받아서 사용하도록 코드를 수정해야 한다.  
위 코드에서 MemberService 인스턴스를 만들었다. MemberService는 단순한 기능들만 있다. MemberService는 멤버서비스말고도 주문서비스에서도 사용하고 다른 컨트롤러에서도 사용할 수 있다. 그럼 그때마다 간단한 기능인 MemberService를 새로 만들어서 사용해야할까? 비효율적이다. 기능은 어쩌피 다 똑같기 때문에 하나의 인스턴스만 만들어서 공유하면 된다. 그럼 스프링 컨테이너에 등록해놓고 MemberService는 스프링 컨테이너에서 가져와서 사용하면 된다.  
<br>

```java
@Controller
public class MemberController {   
    private final MemberService memberService;

    @Autowired
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }
}
```
컨트롤러 어노테이션이 있으면 스프링이 시작할 때 인스턴스를 만들어서 스프링 컨테이너에 등록시킨다고 했다. 즉, 스프링이 시작하면 컨트롤러 어노테이션이 붙은 것은 생성자가 호출된다. 생성자에 Autowired 어노테이션이 있으면 생성자의 매개인자는 스프링이 스프링 컨테이너에서 연관된 객체를 찾아서 넣어준다. 이렇게 객체 의존관계를 외부에서 넣어주는 것을 DI(Dependency Injection), 의존성 주입이라고 한다. 하지만 현재 MemberService 클래스를 확인해보면 MemberService는 아무런 어노테이션이 없는 그냥 순수 자바 파일이다. 아직 스프링 빈에 등록되어 있지 않기 때문에 스프링이 자동으로 인자에 넣어줄 수 없다는 뜻이다. 스프링이 인식할 수 있도록 MemberService를 스프링 컨테이너에 넣을 수 있도록 처리를 해줘야 한다. 이 처리를 하기 위해서는 컴포넌트 스캔 원리를 알아야 한다.  
<br>

__컴포넌트 스캔 원리__  
@Component 어노테이션이 있으면 자동으로 스프링 빈으로 등록된다. @Controller 가 스프링 빈으로 자동 등록되는 이유도 @Controller 어노테이션 안에 컴포넌트 스캔이 있기 때문이다. @Service, @Repository도 @Component를 포함하고 있기 때문에 스프링 빈으로 자동 등록된다.  
컨트롤러를 통해서 외부 요청을 받고 서비스에서 비즈니스 로직을 만들고 리포지토리에 데이터를 저장하는 것이 정형화된 패턴이다. 따라서 각각의 해당 클래스에 @Service, @Repository, @Controller 어노테이션을 붙여주면 스프링 컨테이너에 스프링 빈으로 등록이 되고 앞으로 사용하게 된다면 모두 같은 인스턴스에서 가져다가 쓰게 된다.
<br>

```java
@Controller
public class MemberController {   
    private final MemberService memberService;

    @Autowired
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }
}

@Service
public class MemberService {
   private final MemberRepository memberRepository;
    
    @Autowired
    public MemberService(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }
}

@Repository
public class MemoryMemberRepository implements MemberRepository{

}
```
이렇게 각각 어노테이션을 붙여주면 스프링이 시작할 때 @Controller, @Service, @Repository를 가지고 스프링 컨테이너에 스프링 빈으로 자동등록시키고, Autowired가 붙은 생성자가 호출되면 생성자 인자로 필요한 객체를 등록되어 있는 스프링 빈에서 찾아서 전달해주게 되는 것이다.  
![그림1](https://backtony.github.io/assets/img/post/spring/start/4-1.PNG)
<br>

아무 곳에서나 @Controller, @Service, @Repository를 사용해도 스프링이 자도 등록시켜주는 것은 아니다.
![그림2](https://backtony.github.io/assets/img/post/spring/start/4-2.PNG)

현재 HelloSpringApplication을 실행시키는 것인데 이 파일의 패키지를 보면 hello.hellospring이다. 이 패키지 안에 있는 것만 끌어다가 자동 등록해주는 것이다.

<Br>

cf) 스프링 컨테이너에 스프링 빈을 등록할 때, 유일하게 하나만 등록해서 공유하는 싱글톤으로 등록된다. 따라서 만약에 memberService와 orderService 모두 Autowired로 memberRepository로 연결되어 있다면 memberRepository 하나의 인스턴스로 연결되어 있는 것이다. 즉, 같은 인스턴스라는 뜻이다.
![그림4](https://backtony.github.io/assets/img/post/spring/start/4-4.PNG)



<br>


## 2. 자바 코드로 직접 스프링 빈 등록하기
---
컴포넌트 스캔으로 자동으로 인식하는 방법말고 직접 스프링 빈을 등록해보자.
![그림3](https://backtony.github.io/assets/img/post/spring/start/4-3.PNG)

hello.hellospring에서 SpringCongfig 클래스를 만든다.
```java
// 스프링이 뜰 때 Configuration을 읽는다
// Configuration한 것도 스프링 빈으로 관리 된다.
@Configuration
public class SpringConfig {

    @Bean // 스프링 빈을 등록한다는 의미
    public MemberService memberService(){
        // MemberService는 생성자 인자가 필요함
        // Bean에 등록한 MemberRepository를 엮어줘야 한다.
        // 스프링 빈에 등록된 memberRepository()를 넣어준다.
        return new MemberService(memberRepository());
    }

    @Bean
    public MemberRepository memberRepository(){
        return new MemoryMemberRepository();
    }
}
```
Configuration어노테이션으로 인해 스프링이 뜰 때 Configuration을 읽게 되고, @Bean은 스프링 빈으로 등록한다는 뜻으로 보면 된다. 간단하게 해당 Service와 Repository의 인스턴스를 만들어서 반환해주는 식으로 코딩하면 된다. 그럼 그 내용이 스프링 빈으로 저장되는 것이다. 그럼 나중에 사용 시에는 스프링 빈에서 만든 하나의 인스턴스를 공유해서 사용한다고 보면 된다. 직접 등록할 때의 연결 표현(Autowired)는 위 코드처럼 스프링 빈에 등록된 것을 코드에서 바로 사용하면 된다.  
Service와 Repository는 직접 스프링 빈에 등록했지만, Controller은 직접할 수 없다. 컨트롤러는 스프링이 어쩌피 관리하는 것이기 때문에 컴포넌트 스캔으로 올라가고 컴포넌트 스캔이기 때문에 Autowired로 연결시켜줘야 한다.
<br>



## 3. 장단점
---
실무에서는 주로 정형화된 컨트롤러, 서비스, 리포지토리 같은 코드는 컴포넌트 스캔을 사용한다. 하지만 정형화되지 않거나, 상황에 따라 구현 클래스를 변경해야 하면 설정을 통해 스프링 빈을 등록해야한다. 정형화 되지 않는 상황의 예시로, 앞서 포스팅했듯이 아직 데이터 저장소가 선정되지 않았다는 가상의 시나리오에서 나중에 MemoryMemberRepository를 다른 메모리로 바꿔치기하는 상황이 있다. 이런 경우에는 직접 등록한 스프링 빈에서 return new MemoryMemberRepository();를 return new dbRepository(); 처럼 간단하게 바꾸기만 하면 한 번에 처리가 가능하다. 컴포넌트 스캔에서는 여러 코드를 바꿔야한다.


<br>

---
__본 포스팅은 인프런 김영한님의 '스프링 입문 - 코드로 배우는 스프링 부트, 웹MVC, DB접근 기술' 강의를 듣고 정리한 내용을 바탕으로 작성하였습니다. [[강의 링크](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%EC%9E%85%EB%AC%B8-%EC%8A%A4%ED%94%84%EB%A7%81%EB%B6%80%ED%8A%B8){:target="_blank"}]__