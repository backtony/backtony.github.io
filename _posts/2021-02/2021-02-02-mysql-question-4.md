---
layout: post
title:  MySQL 프로그래머스 - Level 4
subtitle:   MySQL 프로그래머스 - Level 4
categories: mysql
tags: mysqlquestion
comments: true
# header-img:
---

+ __목차__
  - [1. 우유와 요거트가 담긴 장바구니](#1-우유와-요거트가-담긴-장바구니)    
  - [2. 입양 시각 구하기2](#2-입양-시각-구하기2)    
  - [3. 보호소에서 중성화한 동물](#3-보호소에서-중성화한-동물)    
   

<br>

[문제 링크](https://programmers.co.kr/learn/challenges){:target="_blank"}

## 1. 우유와 요거트가 담긴 장바구니
---
```sql
SELECT a.cart_id 
    from (select cart_id from cart_products where name = 'Milk') a
    inner join
    (select cart_id from cart_products where name = 'Yogurt') b
    on a.cart_id = b.cart_id;
```
<br>

## 2. 입양 시각 구하기2
---
```sql
set @hour =-1;
select 
    (@hour := @hour+1) hour,
    (select count(*) from animal_outs where hour(datetime)=@hour) count
from animal_outs
where @hour<23;
```
변수의 증가를 이용해서 where 조건을 만족하면 계속 select한다. 마치 for문과 비슷하다.  
hour<23 으로 설정해야 22가 들어가서 23이 만들어지고 종료된다.  
전에 풀었던 입양 시각 구하기1 문제처럼 코딩한다면 있는 시간만 조회하므로 0~23까지 중에서 시간 중에서 카운트가 0인 경우가 있다면 0으로 표시하지 않고 다음으로 넘어가기 때문에 위처럼 코딩해야한다.
<br>

## 3. 보호소에서 중성화한 동물
---
```sql
SELECT ins.animal_id,ins.animal_type,ins.name
    from animal_ins ins
    inner join animal_outs outs
    on ins.animal_id = outs.animal_id
    where ins.SEX_UPON_INTAKE like "Intact%" and outs.SEX_UPON_OUTCOME not like "Intact%";
```
