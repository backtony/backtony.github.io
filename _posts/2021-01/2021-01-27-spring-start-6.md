---
layout: post
title:  Spring 입문 - 스프링 DB 접근 기술
subtitle:   Spring 입문 - 스프링 DB 접근 기술
categories: spring
tags: start
comments: true
# header-img:
---

+ __목차__
  - [1. 스프링 JdbcTemplate](#1-스프링-jdbctemplate)    
  - [2. JPA](#2-jpa)    
  - [3. 스프링 데이터 JPA](#3-스프링-데이터-jpa)
    



## 1. 스프링 JdbcTemplate
---
![그림1](https://backtony.github.io/assets/img/post/spring/start/6-1.PNG)

H2 데이터베이스를 사용하기 위해서 bundle.gradle에 라이브러리를 추가해줘야 한다. 자바는 db와 붙기 위해서 드라이버가 필요하고 db랑 붙을 때 db가 제공하는 클라이언트에 관해서 라이브러리로 추가해준다.  
<br>

![그림2](https://backtony.github.io/assets/img/post/spring/start/6-2.PNG)
![그림3](https://backtony.github.io/assets/img/post/spring/start/6-3.PNG)

db에 붙으려면 접속 정보 같은 것을 넣어줘야한다. 경로만 넣으면 스프링 부트가 다 알아서 해준다. url은 접속할 때 url, driver은 h2 db로 접근 할 것이므로 h2 driver을 넣어준다. 처음 h2.Driver 입력하면 빨간불이 뜨는데 import가 안되었기 때문이다. bundle.gradle에 가서 화면 우측 상단에 코끼리 모양 표시를 누르면 자동으로 처리된다.  
DB에 붙으려면 DataSource 라는 것이 필요하다. 위에서 datasource를 세팅해 두었다. 스프링 부트는 설정파일을 보고 스프링 자체적으로 그에 대한 스프링 빈을 생성해준다. 즉, 위처럼 설정 정보만 넣어주면 db랑 연결할 수 있는 datasource 스프링 빈으로 자동 등록해준다는 것이다.
<br>

이제 db와 연결되는 새로운 MemberRepository의 구현 클래스를 작성해보자.
```java
public class JdbcTemplateMemberRepository implements  MemberRepository{

    // JdbcTemplate을 사용하기 위해 먼저 선언
    // 생성자에서는 datasource 인젝션이 필요하다
    private final JdbcTemplate jdbcTemplate;

    // 스프링 부트가 자동으로 처리해서 빈으로 만들어준 datasource주입
    @Autowired // 참고) 스프링 빈에 등록되어 있을 경우, 생성자가 딱 1개라면 autowired 생략가능
    public JdbcTemplateMemberRepository(DataSource dataSource) {
        this.jdbcTemplate = new JdbcTemplate(dataSource);
    }

    @Override
    public Member save(Member member) {
        // SimpleJdbcInsert는 jdbcTmplate을 넘겨서 만드는데
        // 알아서 sql문을 짜준다.
        SimpleJdbcInsert jdbcInsert = new SimpleJdbcInsert(jdbcTemplate);
        jdbcInsert.withTableName("member").usingGeneratedKeyColumns("id");
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("name", member.getName());

        // 키를 리턴 받아서 id저장
        Number key = jdbcInsert.executeAndReturnKey(new MapSqlParameterSource(parameters));
        member.setId(key.longValue());
        return member;
    }

    @Override
    public Optional<Member> findById(Long id) {
        // jdbcTemplate.query(db에 보내는 보낼쿼리문, 나오는 결과를 RowMapper로 매핑, ? 값)
        // RowMapper를 사용하면, 원하는 형태의 결과값을 반환할 수 있다.       
        // 결과 값은 List로 반환된다.
        List<Member> result = jdbcTemplate.query("select* from member where id = ?", memberRowMapper(),id);
        return result.stream().findAny(); // 반복자로 만들고 먼저 찾는 객체 반환
    }

    @Override
    public Optional<Member> findByName(String name) {
        List<Member> result = jdbcTemplate.query("select* from member where name = ?", memberRowMapper(),name);
        return result.stream().findAny(); // 반복자로 만들고 먼저 찾는 객체 반환
    }

    @Override
    public List<Member> findAll() {
        return jdbcTemplate.query("select * from member", memberRowMapper());
    }

    @Override
    public void clearStore() {

    }

    private RowMapper<Member> memberRowMapper () {
        return new RowMapper<Member>() { // 코드 다 작성하고 alt + enter로 람다식으로 변환 가능
            @Override
            // rs에 값을 받아오고  rownum만큼 반복
            public Member mapRow(ResultSet rs, int rowNum) throws SQLException {
                // rs값을 가공해서 Member 객체에 저장하고 member 객체 반환
                Member member = new Member();
                // rs에 있는 값중 id열을 int타입으로 가져와서 setid
                member.setId(rs.getInt("id"));
                // rs에 있는 값중 name열을 string타입으로 가져와서 setname
                member.setName(rs.getString("name"));
                return member;
            }
        };
    }
}

```
RowMapper는 template객체의 query메서드를 통해 결과값을 가져올 때 sql문에 따라 추출된 결과를 리턴받을 객체의 멤버변수에 적절하게 할당하기 위한 매핑수단이다. sql문의 반환값을 내가 원하는대로 가공할 수 있는 방법이라고 생각하면 된다.  
<br>

새로운 구현 클래스를 만들었으니 Configuration에서 연결작업을 해줘야한다.
```java
// 스프링이 뜰 때 Configuration을 읽는다
@Configuration
public class SpringConfig {

    // 지금 여기 안에서 파라미터로 dataSource가 필요하므로
    // 선언해서 스프링 빈에 있는 것을 받아서 넣어준다.
    private DataSource dataSource;
    
    @Autowired
    public SpringConfig(DataSource dataSource) {
        this.dataSource = dataSource;
    }    


    @Bean // 스프링 빈을 등록한다는 의미
    public MemberService memberService(){
        // MemberService는 생성자 인자가 필요함
        // Bean에 등록한 MemberRepository를 엮어줘야 한다.
        // 스프링 빈에 등록된 memberRepository()를 넣어준다.
        return new MemberService(memberRepository());
    }

    @Bean
    public MemberRepository memberRepository(){
        return new JdbcTemplateMemberRepository(dataSource);
    }
}
```
기존에서 추가된 것은 datasource와 memberRepository 생성자의 리턴값이 바뀐 것이다. datasource는 세팅해줬으니 스프링 빈으로 자동 등록이 되어있는 상태이다. 그런데 JdbcTemplateMemberRepository생성자의 파라미터로 DatasSource가 필요하므로 dataSource 프로퍼티에 인젝션으로 값을 넣어주고 사용한다.

<br>

지금 연결한 리포지토리는 db에 연결되어있으므로 전체를 확인하는 통합테스트를 진행해보자. 전에 진행했던 테스트는 순수 자바코드만 가지고 했던 테스트이다. 이제는 스프링과 엮어서 해야한다. 전에 했던 테스트와 다른 점은 @SpringBootTest, @Transactional, 프로퍼티 스프링 빈에서 받기이다. 
```java
@SpringBootTest // 스프링을 통한 테스트
@Transactional // 테스트마다 실행시 transactional 먼저 실행하고 db작업을 다 하고 자동으로 롤백해준다.
    // 전처럼 지워주는 작업을 안해도 된다는 것
class MemberServiceIntegrationTest {

    // 이제는 컨테이너에서 꺼내써야한다.
    // constructor로 인젠셕해서 사용하면 되는데
    // 사실 테스트는 제일 끝단에 있기에 테스트만 할것이기 때문에
    // 필드기반으로 autowired 받아서 하는게 편하다.
    @Autowired MemberService memberService;
    @Autowired MemberRepository memberRepository;

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
}
```
<Br>

__Cf) Autowired가 아닌 직접 꺼내기__  
스프링은 모든게 ApplicationCentext로 시작한다. 이걸 스프링 컨테이너라고 생각하면 된다. AnnotationConfigApplicationContext의 파라미터로 Configuration 어노테이션 있는 클래스를 넣어준다. 이때 파라미터로 들어온 클래스는 자동으로 빈으로 등록된다. @Bean이 붙은 것들을 객체생성해서 스프링 컨테이너에 넣어서 관리해준다. 그럼 거기서 이제 getBrean으로 꺼내서 사용하면 된다. getBean의 파라미터는 메소드이름, 반환타입이다. 파라미터로 반환타입만으로도 사용 가능하다.
```java
public class MemberApp {


    public static void main(String[] args) {

        ApplicationContext applicationContext = new AnnotationConfigApplicationContext(AppConfig.class);
        MemberService memberService = applicationContext.getBean("memberService",MemberService.class);

        Member member = new Member(1L, "memberA", Grade.VIP);
        memberService.join(member);

        Member findMember = memberService.findMember(1L);
        System.out.println("newMember = " + member.getName());
        System.out.println("findMember = " + findMember.getName());
    }
}
```

## 2. JPA
---
JPA는 기존의 반복 코드, SQL을 직접 만들어서 실행해주기 때문에 생산성을 크게 높일 수 있고, 사용시 SQL과 데이터 중심의 설계에서 객체 중심의 설계로 패러다임을 전환할 수 있다. JPA는 인터페이스만 제공되는 것이고, 이에 대한 구현체로 hiberante 등등 여러 가지가 있다. JPA는 객체랑 ORM이라는 기술이다. (O:Ojbect, R:Relational, M:Mapping )  
JPA 사용을 위해 라이브러리에 추가해주자. 위에 했던 방식과 똑같이 build.gradle에서 다음을 추가해준다. 이것이 jdbc도 포함하기에 전에 넣어줬던 jdbc는 지워줘도 된다.
```java
implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
```
<br>

이제는 설정을 해줄 차례이다. application.properties에서 다음과 같이 작성해준다. 전에 datasource를 설정해줬던 위치이다.
```java
spring.jpa.show-sql=true  // jpa가 날리는 sql 확인 가능하게 하기 
spring.jpa.hibernate.ddl-auto=none //  jpa사용하면 객체를 보고 테이블을 다 만드는데 이미 만들어놓았기에 기능 끄기
spring.datasource.username=sa // wrong user name or password관련한 오류는 스프링부트2.4부터 application.properties에 spring.datasource.username=sa를 추가
```
<br>

JPA를 사용하기 위해서는 Entity라는 매핑을 해야한다. domain에 작성해두었던 Member 클래스를 수정하자. Entity 어노테이션을 붙여서 이제부터 jpa가 관리하는 것으로 인식하게 한다. 이제 jpa로 Member 관련 쿼리를 사용 가능하다.
```java
@Entity // 이제부터 jpa가 관리하는 것
public class Member {
    // @Id : pk값 설정
    // db에 넣으면 자동으로 생성되게 해주는 것을 identity라고 함(auto_increment)
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id; // 고객이 정하는 아이디가 아니라 시스템이 저장하는 아이디

    // 만약 db에 컬럼명이 name이 아닌 username이라고 한다면
    // @Column(name = "username") 이렇게 해주면 매핑이 된다
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

이제 Repository를 Jpa로 만든 것으로 교체해보자. repository에 JpaMemberRepository를 만들어서 작성하자. JPA는 EntityManager이라는 것으로 모든 것이 동작한다. 라이브러리에 JPA등록 시 스프링 부트가 자동으로 application.properties에서 세팅값을 확인하고 EntityManager을 생성해준다. datasource처럼 이것도 그대로 인젝션 받아서 사용하면 된다. 즉, __JPA를 사용하려면 EntityManager을 인젝션받아서 사용해야한다.__
```java
public class JpaMemberRepository implements MemberRepository{

    // jpa는 EntitryManager라는 것으로 모든 것이 동작한다
    // 라이브러리에 jpa 등록시 스프링 부트가 자동으로 EntityManager라는 것을 생성해주는데
    // 그걸 인젝션 받아서 사용하면 된다.
    // 결론은 jpa 사용하려면 EntityManager을 인젝션받아서 사용해야한다
    private final EntityManager em;

    public JpaMemberRepository(EntityManager em) {
        this.em = em;
    }

    @Override
    public Member save(Member member) {
        // persist 저장한다. 리턴값 없음
        em.persist(member);
        return member;
    }

    @Override
    public Optional<Member> findById(Long id) {
        // pk값을 이용한 찾기 -> find(조회타입,식별자)
        Member member = em.find(Member.class, id);
        return Optional.ofNullable(member);
    }

    // pk기반이 아닌 것들의 조회는 jpql을 작성해야함

    @Override
    public Optional<Member> findByName(String name) {
        List<Member> result = em.createQuery("select Member from Member m where m.name =:name", Member.class)
                .setParameter("name", name) // sql문에서 name에 인자 name넣기
                .getResultList(); // 리스트로 받기
        return result.stream().findAny();
    }

    @Override
    public List<Member> findAll() {
        // 보통 테이블 대상으로 쿼리를 날리는데
        // jpql 쿼리 언어는 객체를 대상으로 쿼리를 날린다. 그럼 sql로 번역이된다.
        // 정확히는 Entity를 대상으로 쿼리를 날리는데
        // from Member m 은 Member entity를 조회하라는 뜻
        // 뒤에 m은 as가 생략된것 별칭이 m이라고 보면 된다
        // 열자리에 열이름이 아니라 m 즉 Member entity 자체를 조회, 객체 자체를 조회한다.
        // 뒤에 class 적은 것은 결과값 클래스
        return em.createQuery("select m from Member m",Member.class).getResultList();
    }

    @Override
    public void clearStore() {

    }
}
```
<br>

Configuration에 연결해주기전에 한 가지 작업이 더 필요하다. __JPA를 통한 모든 데이터 변경은 항상 transcational 어노테이션이 필요하다.__  앞선 테스트에서는 @Transactional은 데이터베이스에 커밋하는게 아니라 롤백을 해서 데이터베이스에 전달된 데이터를 모두 삭제한다고 했다. 이건 테스트의 경우에서 @Transactional이 사용될 경우에 해당하는 사항이고, @Transactional은 기본적으로 해당 메소드가 실행될 때 트랜잭션을 시작하고 해당 메소드가 끝날 때 커밋을 해서 데이터베이스에 전달된 내용을 확정한다. 따라서 MemberService 클래스에서 join 메소드에 @transactional을 붙여준다.  
Configuration 다음과 같이 작업해준다.
```java
@Configuration
public class SpringConfig {
    private final EntityManager em;

    @Autowired
    public SpringConfig(EntityManager em) {
        this.em = em;
    }

    @Bean
    public MemberService memberService() {
        return new MemberService(memberRepository());
    }
    @Bean
    public MemberRepository memberRepository() {
        return new JpaMemberRepository(em);
    }
}
```



<Br>

## 3. 스프링 데이터 JPA
---
스프링 부트와 JPA만 사용해도 개발 생산성이 많이 증가하고, 개발해야할 코드도 확연히 줄어든다. 여기에 스프링 데이터 JPA를 사용하면, 리포지토리에 구현 클래스 없이 인터페이스 만으로 개발을 완료할 수 있다.  
Repository 패키지에 SpringDataJpaMemberRepository라는 인터페이스를 하나 만들자.
```java
// JpaRepository<사용될 Entity 클래스, PK타입>
// 인터페이스가 인터페이스를 다중 상속
// jpaRepository를 상속받는 경우, 스프링 데이터 jpa가
// 구현체를 자동으로 만들어주고 스프링 빈에 자동으로 등록해준다. 우리는 그걸 가져다 쓰면 된다.
public interface SpringDataJpaMemberRepository extends JpaRepository<Member,Long>,MemberRepository {
    // jparepository에서는 대부분의 기본적인 것들이 다 설계되어있다.
    // 기본적인 CRUD 단순조회들이 다 들어있다.
    // 기본적인 것은 다 가져다 쓰면 되고,
    // 모든 코드에서 다 통용되지 않는 경우,
    // name으로 찾고싶어, 다른 곳에서는 username으로 찾을수도 있고 해서 공통으로 작성이 불가능
    // 그래서 findByName 처럼 규칙이있다. findByXXX
    // JPQL select m from Member m where m.name =? 이렇게 알아서 짜준다.
    // 규칙만 알면 이제 기본적인 것 외에도 간단하게 작성할 수 있는 것이다.
    @Override
    Optional<Member> findByName(String name);
}
```
인터페이스가 JpaRepository를 상속받는 경우, 스프링 데이터 JPA가 해당 구현 클래스를 자동으로 생성해주고 스프링 빈에 자동으로 등록해준다. 그럼 사용자는 이제 그걸 가져다가 쓰기만 하면 된다. JpaRepository에는 대부분의 기본적인 것들이 다 설계되어 있다. 하지만 모두에 통용되지 않는 것들은 따로 작성해줘야한다. 가령, 내 프로젝트에서는 name인데 타인의 프로젝트에서는 username일 수도 있듯이 이런 부분은 따로 코딩해줘야한다는 뜻이다. 하지만 이 경우에도 전부 코딩해야 하는 것이 아니고 단순한 규칙들로 쉽게 코딩할 수 있다. Name으로 찾고 싶다면 findByXXX -> findByName을 코딩하면 JPQL로 select m from Member m where m.name:=? 이렇게 만들어준다. 즉, 규칙만 알고 있으면 이제 인터페이스만으로도 쉽게 구현체를 만들 수 있는 것이다.
<br>

이제 Configuration에 연결시키자.
```java
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

}
```
앞서 말했듯이, JpaRepository을 상속받은 인터페이스JpaRepository의 구현체는 이미 자동으로 만들어져 스프링 빈에 있으므로 따로 등록할 필요가 없다. memberService의 파라미터에 memberRepository을 넣어줘야 하므로 memberService 를 빈에서 주입받아서 사용하면 된다.





<br>

---
__본 포스팅은 인프런 김영한님의 '스프링 입문 - 코드로 배우는 스프링 부트, 웹MVC, DB접근 기술' 강의를 듣고 정리한 내용을 바탕으로 작성하였습니다. [[강의 링크](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%EC%9E%85%EB%AC%B8-%EC%8A%A4%ED%94%84%EB%A7%81%EB%B6%80%ED%8A%B8){:target="_blank"}]__