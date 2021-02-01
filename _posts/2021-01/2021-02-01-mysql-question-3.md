---
layout: post
title:  MySQL 프로그래머스 - Level 3
subtitle:   MySQL 프로그래머스 - Level 3
categories: mysql
tags: mysqlquestion
comments: true
# header-img:
---

+ __목차__
  - [1. 없어진 기록 찾기](#1-없어진-기록-찾기)    
  - [2. 있는데요 없었습니다](#2-있는데요-없었습니다)    
  - [3. 오랜 기간 보호한 동물1](#3-오랜-기간-보호한-동물1)    
  - [4. 오랜 기간 보호한 동물2](#4-오랜-기간-보호한-동물2)    

<br>

[문제 링크](https://programmers.co.kr/learn/challenges){:target="_blank"}


## 1. 없어진 기록 찾기
---
```sql
SELECT outs.animal_id, outs.name 
    from animal_ins ins
    right join animal_outs outs
    on outs.animal_id = ins.animal_id
    where ins.animal_id is null;    
```
outer join으로 id가 같은 것 + outs의 모든 것이 조회된다. outs에만 있고 ins의 없는 경우 outs의 아이디만 적히고 ins의 아이디는 null로 표현되는데 이것을 조건으로 사용하면 된다.

<br>

## 2. 있는데요 없었습니다
---
```sql
SELECT ins.animal_id,ins.name
    from animal_ins ins
    inner join animal_outs outs
    on ins.animal_id = outs.animal_id
    where ins.datetime>outs.datetime
    order by ins.datetime;
```

<br>

## 3. 오랜 기간 보호한 동물1
```sql
SELECT ins.name,ins.datetime
    from animal_ins ins
    left join animal_outs outs
    on ins.animal_id = outs.animal_id
    where outs.animal_id is null
    order by ins.datetime
    limit 3;
```

<br>

## 4. 오랜 기간 보호한 동물2
```sql
-- 방법 1
SELECT outs.animal_id, outs.name
    from animal_ins ins
    inner join animal_outs outs
    on ins.animal_id = outs.animal_id
    order by outs.datetime - ins.datetime desc
    limit 2;

-- 방법 2
SELECT outs.animal_id, outs.name
    from animal_ins ins
    inner join animal_outs outs
    on ins.animal_id = outs.animal_id
    order by datediff(outs.datetime,ins.datetime) desc
    limit 2;
```
+ datediff(날짜1,날짜2) : 날짜1 - 날짜2의 일수를 결과로 반환
+ timediff(시간1,시간2) : 시간1 - 시간2의 시간차 결과를 반환