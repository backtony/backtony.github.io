---
layout: post
title:  Spring 입문 - 회원 관리 예제
subtitle:   Spring 입문 - 회원 관리 예제
categories: spring
tags: start
comments: true
# header-img:
---

+ __목차__
  - [1. 비즈니스 요구사항 정리](#1-비즈니스-요구사항-정리)    
  - [2. 회원 도메인과 리포지토리 만들기](#2-회원-도메인과-리포지토리-만들기)    
  - [3. 회원 리포지토리 테스트 케이스 작성](#3-회원-리포지토리-테스트-케이스-작성)
  - [4. 회원 서비스 개발](#4-회원-서비스-개발)
  - [5. 회원 서비스 테스트](#5-회원-서비스-테스트)




## 1. 비즈니스 요구사항 정리
---
+ 데이터 : 회원 id, 이름
+ 기능 : 회원 등록, 조회
+ 아직 데이터 저장소가 선정되지 않음(가상의 시나리오)

![그림1](https://backtony.github.io/assets/img/post/spring/start/3-1.PNG)

+ 컨트롤러 : 웹 MVC의 컨트롤러 역할
+ 서비스 : 핵심 비즈니스 로직 구현 ex) 회원은 중복 가입이 안된다.
+ 도메인 : 비즈니스 도메인 객체 ex) 회원, 주문 등등 주로 데이터베이스에 저장하고 관리되는 것
+ 리포지토리 : 데이터베이스에 접근, 도메인 객체를 db에 저장하고 관리하는 것

<br>

![그림2](https://backtony.github.io/assets/img/post/spring/start/3-2.PNG)

위에서 언급했듯이 아직 데이터 저장소가 선정되지 않아서, 우선 인터페이스로 구현 클래스를 변경할 수 있도록 설계하고, 개발을 진행하기 위해서 초기 개발 단계에서는 구현체로 가벼운 메모리 기반의 데이터 저장소를 사용

<br>

## 2. 회원 도메인과 리포지토리 만들기
---
![그림3](https://backtony.github.io/assets/img/post/spring/start/3-3.PNG)

패키지와 클래스,인터페이스 위치이니 참고하자.  

먼저 hello.hellospring 안에 domain이라는 패키지를 만들고 그 안에 Member 클래스를 만들자.
```java
package hello.hellospring.domain;

public class Member {
    private long id; // 고객이 정하는 아이디가 아니라 시스템이 저장하는 아이디
    private String name; // 가입시 고객이 적는 이름

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
```
<br>

회원들을 저장할 저장소를 만들자. hello.hellosprint에 repository라는 패키지를 만들고 repository의 기능을 선언한 MemberRepository 인터페이스부터 만든다.
```java
package hello.hellospring.repository;

import hello.hellospring.domain.Member;

import java.util.List;
import java.util.Optional;

// repository는 member저장소

public interface MemberRepository {
    Member save(Member member); // 회원 저장 메소드
    // optional은 findbyid,name으로 가져올 때 없으면 null일수도 있는 경우를 위한 자바8방식    
    // 널을 처리하는 방법에서 그대로 반환하는 방법 대신에 optional로 감싸서 반환하는것을 선호하는 추세
    // Member 클래스 객체를 Optional 방식으로 반환이라고 생각
    Optional<Member> findById(Long id); // id로 회원 찾는 메소드
    Optional<Member> findByName(String name); // 이름으로 회원 찾는 메소드
    List<Member> findAll(); // 저장된 모든 회원 리스트 반환 메소드
    void clearStore(); // 저장소 비우기
}
```
<br>

인터페이스 구현 클래스 만들자. implement MemberRepository 작성 후 alt + enter로 재정의 메소드 가져올 수 있다.
```java
package hello.hellospring.repository;

import hello.hellospring.domain.Member;

import java.sql.SQLTransactionRollbackException;
import java.util.*;

// 인터페이스 memberrepository 구현 클래스
public class MemoryMemberRepository implements MemberRepository { // alt + enter로 재정의 한번에 가져옴
    // 메모리니까 어딘가에 저장을 해야겠지 -> 저장 필드 생성
    // Map<키타입,벨류타입>
    private static Map<Long, Member> store = new HashMap<>(); // 객체 생성
    private static long sequence = 0L; // id값으로 넣을 변수


    @Override
    // save하기 전에 이름은 넘어온 상태라고 가정
    public Member save(Member member) {
        member.setId(++sequence); // id설정
        store.put(member.getId(), member); // 키값,value값 -> 저장
        return member;
    }

    @Override
    public Optional<Member> findById(Long id) {
        // get()으로 인해 key값에 맞는 Member 클래스의 value값이 반환
        return Optional.ofNullable(store.get(id));
        // 자바 8부터 반환값이 null일 가능성이 있는 경우 Optional 사용
        // Optional의 ofNullable로 감싸서 반환할 경우
        // NullPointerException 예외를 제공되는 메소드로 회피 가능        
    }

    @Override
    public Optional<Member> findByName(String name) {
        // values() : 저장된 모든 value값을 컬렉션에 담아서 리턴, []에 담겨서 나옴
        // 자바6에는 iterator을 이용해 반복자를 사용했지만
        // 자바 8부터는 stream을 이용해 반복자를 사용한다.
        // stream은 일회용이다.
        // stream.filter은 조건에 충족하는 요소만 stream 생성
        // filter의 조건으로 람다식을 사용했는데
        // 만약 stream으로 나온 반복자가 [a,b,c,d] 였다면 매개변수에 하나씩 들어가는 식으로 생각
        // 람다식이란 함수를 간단히 사용하도록 하는것
        // (매개변수,...) -> {실행문}
        // 매개변수는 오른쪽 실행문을 실행하기 위해 필요한 값을 제공하는 역할
        // 매개 변수는 인자 타입을 명시하지 않아도 된다.
        // stream.findAny 는 순서 관계없이 먼저 찾아지는 객체 반환
        return store.values().stream()
                .filter(member -> member.getName().equals(name))
                .findAny();
    }

    @Override
    public List<Member> findAll() {
        // store은 Map인데 반환은 List -> 자바 실무에서는 루프돌리기 편해서 List를 많이 씀
        return new ArrayList<>(store.values());
    }
     @Override
    public void clearStore() {
        store.clear(); // 스토어 비우기
    }
}
```

<br>

## 3. 회원 리포지토리 테스트 케이스 작성
---
![그림4](https://backtony.github.io/assets/img/post/spring/start/3-4.PNG)

Test할 때는 보통 패키지는 똑같은 이름으로 두고, 클래스는 이름 뒤에 Test라고 붙여준다.  
테스트 할 때는 반드시 @AfterEach를 이용해서 각 메소드가 끝날 때 마다 실행하는 메소드를 선언해주고 저장된 정보를 지워줘야 한다. 테스트 마다 저장하는 값에 충돌이 생길 수 있기 때문이다. 

```java
package hello.hellospring.repository;

import hello.hellospring.domain.Member;


import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;

import java.util.List;
import java.util.Optional;

public class MemoryMemberRepositoryTest {
    MemberRepository repository = new MemoryMemberRepository();

    @AfterEach // 각 메소드가 끝날 때마다 동작
    public void afterEach(){
        repository.clearStore(); // 저장된 것들 지우기
    }

    // save가 동작하는지 확인하고 싶으면 메소드 쓰고 위에 어노테이션 Test를 적는다.
    // @Test에 보면 org.junit.jupiter.api
    // 이제 save 메소드를 test해본다는 것이고 안에는 main 메소드처럼 쓰면 된다
    @Test
    public void save(){
        // 마치 main 메소드처럼 작성
        // 객체 만들고 저장까지
        Member member = new Member();
        member.setName("spring");
        repository.save(member);

        // 이제 저장이 잘 되었는가 확인
        // repository.findById(member.getId())까지만 작성하고
        // 반환 타입이 기억이 안나면 ctrl + alt + V 누르고 원하는 expression을 선택하면
        // 타입 변수 = reposi~~ 으로 자동 완성 시켜준다. -> 반환 타입 확인할 때 사용
        // optional에서 값을 꺼낼 때는 get으로 꺼낼 수 있다.
        Member result = repository.findById(member.getId()).get();

        // 검증: 꺼낸거랑 저장값이랑 똑같은지 확인
        // Assertions.assertThat 사용(org.assertj.core.api)
        // member가 result랑 똑같은가 확인
        Assertions.assertThat(member).isEqualTo(result);
        // Assertions.assertThat(member).isEqualTo(result);
        // Assertions에서 alt + enter로 add로 import해주면 앞으로 asserThat 바로 사용 가능
        // 맞은 경우에는 아무런 창 없음, 틀린 경우에만

        // isEqualTo : 내용물이 같은지
        // isNotSameAs() : 다른 주소값을 가지는지
        // SameAs() : 같은 주소값을 가지는지
    }

    @Test
    public void findByName(){
        Member member1 = new Member();
        member1.setName("spring1");
        repository.save(member1);
        // 복붙한 내용 한번에 수정 -> shft + F6
        Member member2 = new Member();
        member2.setName("spring2");
        repository.save(member2);

        Member result = repository.findByName("spring1").get();

        Assertions.assertThat(result).isEqualTo(member1);

    }

    @Test
    public void findAll(){
        Member member1 = new Member();
        member1.setName("spring1");
        repository.save(member1);
        // 복붙한 내용 한번에 수정 -> shft + F6
        Member member2 = new Member();
        member2.setName("spring2");
        repository.save(member2);

        // reposirotry.findAll() + ctrl+alt+V : 변수 만들어주고 대입식
        List<Member> result = repository.findAll();
        Assertions.assertThat(result.size()).isEqualTo(2);
    }
}
```
<br>

![그림5](https://backtony.github.io/assets/img/post/spring/start/3-5.PNG)
Assertions.asserThat에서 일치하지 않으면 다음과 같은 화면이 나온다. 기대했던 값(result.size)은 2인데 3이 들어왔다는 뜻이다.

<br>

![그림6](https://backtony.github.io/assets/img/post/spring/start/3-6.PNG)

하나의 메소드만 또는 클래스 전체를 테스트할 수 있다.  
또는 만든 전체 테스트 코드를 실행하고 싶다면 상위 패키지 우클릭으로 Run 시키면 된다.

![그림10](https://backtony.github.io/assets/img/post/spring/start/3-10.PNG)

<br>

![그림7](https://backtony.github.io/assets/img/post/spring/start/3-7.PNG)

클래스 전체를 한 번에 테스트해보면 알 수 있는데, 테스트는 순서대로 실행되지 않는다. 순서에 상관없이 실행되므로 항상 메소드마다 테스트 후 데이터가 지워지도록 해야 한다.



<br>

## 4. 회원 서비스 개발
---
![그림8](https://backtony.github.io/assets/img/post/spring/start/3-8.PNG)

회원 서비스는 회원 리포지토리랑 도메인을 활용해서 실제 비지니스 로직을 작성하는 쪽이다. service 패키지를 만들어 MemberService 클래스를 만들자.
```java
package hello.hellospring.service;

import hello.hellospring.domain.Member;
import hello.hellospring.repository.MemberRepository;
import hello.hellospring.repository.MemoryMemberRepository;

import java.util.List;
import java.util.Optional;

public class MemberService {

    // 회원 서비스를 만들려면 먼저 저장소(리포지토리)가 있어야겠지
    private final MemberRepository memberRepository = new MemoryMemberRepository();

    // 회원가입
    public Long join(Member member) {
        /* 같은 이름이 있는 중복 회원은 가입 안된다고 가정하자.
         ifPresent는 Optional을 위한 메소드, optional이 아니었다면 'if 널이 아니면' 조건을 사용했겠지.
         Optional로 감싼 덕분에 여러가지 메소드를 사용할 수 있다. Optional을 꺼내고 싶으면 그냥 .get으로 꺼내면 된다.         
        Optional<Member> result = memberRepository.findByName(member.getName());

        result가 null이 아니면 다음을 동작
        result.ifPresent(m -> {
            throw new IllegalStateException("이미 존재하는 회원입니다.");
        });
        사실 Optional을 반환해서 다시 대입하는 식은 좋지 않다. 코드가 더럽다.
        따라서 아래와 같이 바로 사용한다.
        memberRepository.findByName(member.getName())
                .ifPresent(m -> {
                    throw new IllegalStateException("이미 존재하는 회원입니다.")
                });

        그런데 뭔가 findByName을 통해 하나의 로직이 쭉 실행된다.
        이런 경우에는 따로 메소드로 뽑아주는 것이 좋다.
        드래그해서 ctrl + alt + shft + t -> extract method로 뽑아낼 수 있다.
        */
        // 이렇게 한 메소드로 뽑아서 중복회원 검증이라고 써두면 한 번에 이해 가능
        validateDuplicateMember(member); // 중복 회원 검증
        memberRepository.save(member);
        return member.getId();// 그냥 임의로 id리턴하게 해봤음
    }

    private void validateDuplicateMember(Member member) {
        memberRepository.findByName(member.getName())
                .ifPresent(m -> {
                    throw new IllegalStateException("이미 존재하는 회원입니다.");
                });
    }

    // 전체 회원 조회
    public List<Member> findMembers() {
        return memberRepository.findAll();
    }

    // 회원 조회
    public Optional<Member> findOne(Long memberId) {
        return memberRepository.findById(memberId);
    }

}
```

<br>

## 5. 회원 서비스 테스트
---
앞서 진행했던 테스트에서는 패키지를 직업 만들고 직접 선언해서 작성했다면 이번에는 쉽게 단축키로 만들어 보자. 테스트를 원하는 클래스에서 ctrl + shft + T -> create new test를 클릭한다.
![그림9](https://backtony.github.io/assets/img/post/spring/start/3-9.PNG)

아래 쪽에서 하고자 하는 테스트 멤버를 선택하고 만들어주면 간단하게 껍떼기를 만들어준다. 이렇게 빠르게 껍떼기를 만들 수 있고 이후에 코딩을 이어나가면 된다.

```java
package hello.hellospring.service;

import hello.hellospring.domain.Member;
import hello.hellospring.repository.MemberRepository;
import hello.hellospring.repository.MemoryMemberRepository;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.*;

class MemberServiceTest {
    
    MemberService memberService = new MemberService();
    MemberRepository memberRepository = new MemoryMemberRepository();
    
    @AfterEach // 각 메소드가 끝날 때마다 동작
    public void afterEach(){
        memberRepository.clearStore();
    }

    // 테스트는 영어권 사람들과 하는게 아니라면 그냥 한글로 써도 된다.
    // 테스트에서는 given(무엇이 주어졌을 때) when(어떤 것을 검증) then(결과) 주석패턴을 가지고 사용해라
    @Test
    void 회원가입() {
        //given 무엇이 주어졌을 때
        Member member = new Member();
        member.setName("hello");

        //when 무엇을 검증하는가
        Long saveId = memberService.join(member);
        Member result = memberService.findOne(saveId).get();

        //then 결과
        assertThat(member.getName()).isEqualTo(result.getName());
    }
    // 위의 회원가입 테스트는 단순 정상 과정, 테스트는 예외가 더 중요

    @Test
    void 중복회원예외(){
        // given
        Member member1 = new Member();
        member1.setName("spring");

        Member member2 = new Member();
        member2.setName("spring");

        // when
        /*  이것 때문에 try catch 넣는게 좀 애매하다 다른 문법 사용
        memberService.join(member1);
        try {
            memberService.join(member2);
            fail(); // catch로 안넘어가고 일로 오면 fail
        } catch (IllegalStateException e){
            assertThat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다.");
        }
        */

        memberService.join(member1);
        // 뒤 실행문이 동작했을 때 IllegalStateException이 나오면 성공하고 진행, 아니면 오류 발생
        // 성공 시 해당 예외에 대한 메시지를 반환한다.
        IllegalStateException e = assertThrows(IllegalStateException.class, () -> memberService.join(member2));

        assertThat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다.");


        // then
    }

    @Test
    void findMembers() {
    }

    @Test
    void findOne() {
    }
}
```
<Br>

여기서 맨 위 선언을 살펴볼 필요가 있다. 
```java
MemberService memberService = new MemberService();
MemberRepository memberRepository = new MemoryMemberRepository();
```
굳이 이렇게 2개로 나눌 필요가 있을까? 지금은 MemoryMemberRepository의 store 필드가 인스턴스 마다 다른게 아닌 클래스에 붙어있는 정적 필드이기 때문에 이렇게 2개를 만드는게 상관없었다. 하지만 static이 아닐 경우에는 위 코드는 전혀 다른 db를 보게 된다. MemberService 클래스를 보면 MemoryMemberRepository를 객체 생성하고 그곳에 데이터를 저장하고 있는데 여기서 또 다른 MemoryMemberRepository를 만들었다. 그럼 전혀 다른 db인데 이렇게 되면 afterEach에서 지우는 데이터는 전혀 다른 db를 지우고 있는 것이다.  
그럼 이제 store이 static이 아니라면 어떻게 처리해야 같은 db를 보게 할 수 있을까? 간단하다. memberService 클래스에서 MemoryMemberRepository를 새로 만드는게 아니라, memberService의 생성 인자로 MemoryMemberRepository를 받으면 된다.
```java
// MemberService 클래스
public class MemberService {

    // 회원 서비스를 만들려면 먼저 저장소(리포지토리)가 있어야겠지
    private final MemberRepository memberRepository;
    // alt + insert -> contructor 로 바로 생성가능
    public MemberService(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

}

// MemberServiceTest 클래스
class MemberServiceTest {

    MemberService memberService;
    MemberRepository memberRepository;

    @BeforeEach // 메소드 시작 전에 실행
    public void beforeEach(){
        memberRepository = new MemoryMemberRepository();
        memberService = new MemberService(memberRepository);
    }
```
MemberService 입장에서 외부에서 MemberRepository를 넣어주는데 이런 것을 DI(dependency injection)라고 한다.





<br>

---
__본 포스팅은 인프런 김영한님의 '스프링 입문 - 코드로 배우는 스프링 부트, 웹MVC, DB접근 기술' 강의를 듣고 정리한 내용을 바탕으로 작성하였습니다. [[강의 링크](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%EC%9E%85%EB%AC%B8-%EC%8A%A4%ED%94%84%EB%A7%81%EB%B6%80%ED%8A%B8){:target="_blank"}]__