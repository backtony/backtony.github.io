---
layout: post
title:  Spring 입문 - 회원 관리 예제 - 웹 MVC 개발
subtitle:   Spring 입문 - 회원 관리 예제 - 웹 MVC 개발
categories: spring
tags: start
comments: true
# header-img:
---

+ __목차__
  - [1. 회원 웹 기능 - 홈 화면 추가](#1-회원-웹-기능--홈-화면-추가)    
  - [2. 회원 웹 기능 - 등록](#2-회원-웹-기능--등록)    
  - [3. 회원 웹 기능 - 조회](#3-회원-웹-기능--조회)
    


## 1. 회원 웹 기능 - 홈 화면 추가
---
매우 간단하다. 앞서 공부했던 내용의 복습이다. 
![그림1](https://backtony.github.io/assets/img/post/spring/start/5-1.PNG)

Home 컨트롤러를 하나 만들어 주고, templates의 home을 찾아가게 만든다.
```html
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<body>
<div class="container">
    <div>
        <h1>Hello Spring</h1>
        <p>회원 기능</p>
        <p>
            <a href="/members/new">회원 가입</a>
            <a href="/members">회원 목록</a>
        </p>
    </div>
</div> <!-- /container -->
</body>
</html>
```
templates에 home.html을 만들어주고 다음과 같이 코딩하면 간단한 홈화면이 만들어진다. 앞서 welcomePage는 정적 컨텐츠로 static 폴더에 index.html을 찾아간다고 했는데 요청이 내장 톰켓 서버에서 먼저 스프링 컨테이너 -> 정적 순이다. 따라서 스프링 컨테이너에 있으면 여기서 끝나고 static을 찾아가지 않는다.

![그림2](https://backtony.github.io/assets/img/post/spring/start/5-2.PNG)
<br>

## 2. 회원 웹 기능 - 등록
---
![그림3](https://backtony.github.io/assets/img/post/spring/start/5-3.PNG)

회원 가입 화면을 먼저 만들자. 회원 관리 내용이니 MemberController에서 코딩한다.
홈 화면에서 링크 연결을 members/new로 했으므로 GetMapping으로 똑같이 받고 회원 가입이나 회원 목록이나 비슷하므로 templates에 members 폴더 하나 만들어서 관리하도록 하자. 
<br>

![그림4](https://backtony.github.io/assets/img/post/spring/start/5-4.PNG)
![그림5](https://backtony.github.io/assets/img/post/spring/start/5-5.PNG)

이렇게 껍데기 화면을 만들었다. 이제 기능들을 실제 동작하게 만들어줘야한다.
<br>

화면으로부터 입력받은 데이터를 바로 Member 클래스로 받는게 아니라 먼저 한 번 가공한 뒤에 Member에 넣어주는 것이 좋다. 지금은 간단하게 이름 정보만 넘어오지만 실무에서는 회원 정보뿐만 아니라 수 많은 정보들이 들어오기 때문에 한 번에 받기보다는 분리해서 받아주는 것이 좋다. 
![그림6](https://backtony.github.io/assets/img/post/spring/start/5-6.PNG)

controller 패키지에 입력받은 것을 가공해줄 클래스 MemberForm을 만든다.
```java
package hello.hellospring.controller;

public class MemberForm {
    private String name;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
```
지금은 이름만 받으므로 간단하다.
<br>

이제 MemberController에서 데이터를 받아서 처리해보자.
```java
@Controller
public class MemberController {

    private final MemberService memberService;

    @Autowired
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }

    @GetMapping("/members/new")
    public String createForm(){
        return "members/createMemberForm";
    }

    // 보통 조회할 때 Get, 등록할 때는 post 사용
    // GetMapping은 url 입력으로 데이터를 받아오는 것이었다면
    // PostMapping은 보통 form을 통해 데이터를 받아온다.    
    @PostMapping("/members/new")
    // 지금 post로 받아오는 값은 name이라는 키에 value값을 받아오고 있다
    // 값이 넘어오면서 create 메소드가 실행되고 스프링은 파라미터인 MemberForm Form을
    // 임의로 생성해서 넣어주는데 이때 만들어지는 객체는,
    // 넘어온 key값과 MemberForm의 setter메소드이름이 동일하므로
    // setName과 키값인 name 뒤에 name이 동일하므로 자동으로 세터를 호출해서 값을 세팅한 상태의 객체다.

    public String create(MemberForm Form){
        Member member = new Member();
        member.setName(Form.getName());
        memberService.join(member);

        return "redirect:/"; // '/'화면으로 돌려보내기
    }
```
보통 조회할 때 get방식, 등록할 때는 post방식을 사용한다. 이 부분에서 이해하는데 좀 오래걸렸다. 천천히 생각해보자. members/new 화면에서 회원 이름을 받았다. html form에서 키값을 name으로 주고 있으므로 name=입력값으로 넘어오게 된다. 그리고 create 메소드를 자동으로 실행하게 되는데 스프링에서는 create의 매개인자에 해당하는 객체를 임의로 만들어준다. 이때 만들어지는 MemberForm 클래스의 Setter의 이름과 넘어온 키값의 이름과 일치하면 만들어지는 객체는 setter로 값이 세팅된 객체가 들어온다. return redirect:url 는 url로 이동한다.


<br>


## 3. 회원 웹 기능 - 조회
---
이제 마지막으로 join한 회원들을 조회해보자. controller 패키지의 MemberController에서 조회이므로 GetMapping으로 코딩하면 된다.
```java
    // 이제 조회
    @GetMapping("/members")
    public String list(Model model){
        List<Member> members = memberService.findMembers(); // 회원을 다뽑아서
        model.addAttribute("members",members); // 모델링해주고
        return "members/memberList"; // 여기로 던진다.
    }
```
```html
<!-- members/memberList -->
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<body>
<div class="container">
    <div>
        <table>
            <thead>
            <tr>
                <th>#</th>
                <th>이름</th>
            </tr>
            </thead>
            <tbody>
            <!-- th: 타임리프 문법 each로 for문과 같이 돌리는것-->
            <tr th:each="member : ${members}">
                <td th:text="${member.id}"></td>
                <td th:text="${member.name}"></td>
            </tr>
            </tbody>
        </table>
    </div>
</div> <!-- /container -->
</body>
</html>
```
뷰 리졸버를 통해 랜더링해서 변환후 화면으로 보낸다.
![그림7](https://backtony.github.io/assets/img/post/spring/start/5-7.PNG)








<br>

---
__본 포스팅은 인프런 김영한님의 '스프링 입문 - 코드로 배우는 스프링 부트, 웹MVC, DB접근 기술' 강의를 듣고 정리한 내용을 바탕으로 작성하였습니다. [[강의 링크](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%EC%9E%85%EB%AC%B8-%EC%8A%A4%ED%94%84%EB%A7%81%EB%B6%80%ED%8A%B8){:target="_blank"}]__