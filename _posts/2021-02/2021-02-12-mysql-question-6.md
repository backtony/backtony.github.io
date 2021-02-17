---
layout: post
title:  MySQL HackerRank - Intermediate
subtitle:   MySQL HackerRank - Intermediate
categories: mysql
tags: mysqlquestion
comments: true
# header-img:
---

__목차를 클릭하면 문제로 바로 이동__  

+ __목차__
  - [Weather Observation Station 5](#weather-observation-station-5)    
  - [Binary Tree Nodes](#binary_tree_nodes)    
  - [Symmetric Pairs](#symmetric-pairs)    
  - [Weather Observation Station 20](#weather-observation-station-20)    
  - [SQL Project Planning](#sql-project-planning)    
  - [Placements](#placements)    
  - [The Report](#the-report)    
  - [Top Competitors](#top-competitors)    
  - [Ollivander's Inventory](#ollivanders-inventory)    
  - [Challenges](#challenges)    
  - [Contest Leaderboard](#contest-leaderboard)    
  - [Interviews](#interviews)    



<br>

[문제링크](https://www.hackerrank.com/domains/sql?filters%5Bskills%5D%5B%5D=SQL%20%28Intermediate%29){:target="_blank"}  

## Weather Observation Station 5
---
```sql
-- 방법 1
select city,char_length(city) 
  from station 
  order by char_length(city), city 
  limit 1;
select city,char_length(city) 
  from station 
  order by char_length(city) desc, city
  limit 1;

-- 방법 2
(select city,char_length(city) 
from station 
order by char_length(city), city 
limit 1)
union
(select city,char_length(city) 
from station
order by char_length(city) desc, city
limit 1);
```
union은 결과를 합쳐서 중복을 제거하고 출력해주고 열이름은 1번째 것을 따른다. union all은 중복을 포함해서 출력해준다.
<Br>


## Binary Tree Nodes
---
```sql
select n,case
    when p is null then 'Root'
    when n in (select distinct p from bst) then 'Inner'
    else 'Leaf'
    End
    from bst
    order by n;
```
<br>

## New Companies
---
```sql
select c.company_code,c.founder,
    count(distinct l.lead_manager_code),
    count(distinct s.senior_manager_code), 
    count(distinct m.manager_code),
    count(distinct e.employee_code)
    from company c, lead_manager l,senior_manager s,manager m,employee e
    where c.company_code=l.company_code and 
    l.company_code=s.company_code and 
    s.company_code=m.company_code and 
    m.company_code=e.company_code
    group by c.company_code,c.founder
    order by c.company_code    
```
+ c.founder을 group by에 포함시키지 않으니 오류가 뜬다. company_code로만 group by시키면 만약 c.founder에 여러 인물이 있을 수 있으니 선택하지 못해 오류가 뜨는 것 같다. 따라서 group by를 사용하고 열을 select할 때는 열에 특별한 작업(함수)을 하지 않았다면 group by에서 사용한 열만 select 할 수 있다.
+ inner join은 각각 join하지 않고 from으로 한 번에 작성해서 on 대신 where로 사용하면 된다.
<br>

## Symmetric Pairs
---
```sql
select a.x,a.y
    from functions a
    inner join functions b
    on a.x = b.y and b.x=a.y    -- on 에서 이어진 조건은 ,가 아니라 and 사용
    group by a.x,a.y
    having count(*)>1 or a.x<a.y
    order by a.x
```
+ on 조건에 맞도록 테이블이 조회되고 a.x,a.y로 묶으면 where 조건으로 a.x<=a.y 넣어주면 끝날 줄 알았다. 하지만 중복에서 문제가 있다. 만약 20,20이 한 번만 있다면 문제 상 이것이 2개가 있어야 symmetric이다. where조건만으로 끝내버리면 20,20이 한번만 있어도 출력된다. 따라서 다른 조건이 필요하다. x<=y 형식으로 출력해야하므로 x < y 조건과 x = y인 조건을 따로 만드는 것이 해결책이다. x = y인 경우는 a.x,a.y로 그룹핑된 열 카운트가 1개보다 많으면 같은 x = y가 2개 이상 있다는 의미로 1개만 있는 경우를 제외시킬 수 있다. 이외에는 on과 group의 조건으로 잘 만들어진 상태이므로 x < y로 처리하면 된다.
<br>

## Weather Observation Station 20

---
```sql
select round(lat_n,4)
from station s
where (select count(lat_n) from station where s.lat_n<lat_n)
=
(select count(lat_n) from station where s.lat_n>lat_n);
```
<br>

## SQL Project Planning
---
```sql
select start_Date, min(end_date)
from
(select start_date from projects where start_date not in (select end_date from projects)) as a
 inner join 
(select end_Date from projects where end_Date not in (select start_date from projects)) as b
 on start_Date < end_Date
 group by start_Date
 order by datediff(min(end_Date),start_Date), start_Date;
```
프로젝트 단위에서 시작일과 종료일만 뽑아서 join한 뒤 start < end 로 쌍을 만들어서 start로 그루핑해준다. 그러면 그루핑되어 딸려온 end는 전부 프로젝트의 종료일인데 여기서 제일 빠른 종료일이 해당 프로젝트의 종료일이 된다.
<br>

## Placements
---
```sql
select s.name
    from students s
    join packages p1 on s.id = p1.id
    join friends f on p1.id = f.id
    join packages p2 on f.friend_id = p2.id
    where p2.salary - p1.salary>0
    order by p2.salary;
```
<br>

## The Report
---
```sql
select if(g.grade>=8,s.name,null), g.grade, s.marks
    from students s
    join grades g
    on s.marks between g.min_mark and g.max_mark    
    order by g.grade desc, s.name, s.marks;
```
+ on의 조건으로 between and를 사용할 수 있다.
+ 살짝 의문이 든게 s.name을 기준으로 정렬하고 후에 같으면 marks로 정렬인데 8보다 작은 경우에서는 이름 정렬이 아니라 marks정렬을 해야한다. 그런데 합격점을 받은 것을 보면 null로 찍었으니 null로 인식하는 것 같다.

<br>

## Top Competitors
---
```sql
-- 방법1
select h.hacker_id, h.name
    from hackers h
    join submissions s on h.hacker_id = s.hacker_id
    join challenges c on s.challenge_id = c.challenge_id
    join difficulty d on c.difficulty_level = d.difficulty_level     
    where d.score = s.score
    group by h.hacker_id,h.name
    having count(*)>1
    order by count(*) desc,h.hacker_id;        

-- 방법2
select h.hacker_id, h.name
    from hackers h, difficulty d, challenges c, submissions s
    where h.hacker_id = s.hacker_id
    and s.challenge_id = c.challenge_id
    and c.difficulty_level = d.difficulty_level
    and d.score = s.score
    group by h.hacker_id,h.name
    having count(*)>1
    order by count(*) desc,h.hacker_id;        
```
<br>

## Ollivander's Inventory
---
```sql
select t.id,p.age,w.coins_needed,w.power
    from (select code, min(coins_needed) as coins_needed,power from wands group by power,code) w
    join wands_property p
    on w.code = p.code
    join wands t
    on w.code = t.code and w.coins_needed = t.coins_needed and w.power = t.power
    where p.is_evil =0
    order by w.power desc, p.age desc
```
code가 같아도 비용과 power가 다르므로 code와 power로 묶어서 최소비용을 뽑아내고 진행해야 한다.code, power로 묶으면서 min으로 가장 최소비용을 뽑아내고 property와 code를 기준으로 join한다. 현재 id에 관한 값이 없으므로 id값을 찾기 위해 다시 wands와 join해서 id값을 찾는다.

<br>

## Challenges
---
```sql
select h.hacker_id, h.name, count(h.hacker_id) cnt
    from hackers h
    join challenges c
    on h.hacker_id = c.hacker_id
    group by h.hacker_id,h.name
    having cnt = (select max(t.cnt) from 
        (select count(*) cnt from challenges group by hacker_id) t)
    or
        cnt in (select p.cnt from
        (select count(*) cnt from challenges group by hacker_id) p
        group by p.cnt
        having count(p.cnt)=1)
    
    order by cnt desc, h.hacker_id;
```
+ 처음에는 이중 서브쿼리로 안짜고 max(count(*)) 이렇게 했는데 오류가 떴다. 생각해보면 count( * )는 결국 열의 개수를 세는거라 1개의 수만 나오는데 max를 한것도 잘못 된 것 같다. 그래서 count( * )로만 한 뒤에 다시 거기서 서브쿼리로 max를 찍어줬다.
+ count가 max인 사람은 중복이 상관없으나 max가 아닌 사람이 중복이 있다면 제거해야하므로 cnt는 max인 경우와 중복이 없는 경우만을 나타내도록 having 절에서 이를 해결했다.
+ where을 안쓰고 having을 쓴 이유는 group 한 상태에서 필터링해주기 위해서 group 뒤에 나오는 having을 사용

<br>

## Contest Leaderboard
---
```sql
select h.hacker_id, h.name, sum(s.score) score
    from hackers h
    join 
    (select hacker_id, challenge_id, max(score) score 
            from submissions 
            group by hacker_id, challenge_id
     ) s   
    on h.hacker_id = s.hacker_id
    group by h.hacker_id,h.name
    having score>0
    order by score desc, h.hacker_id;
```
서브 쿼리로 사람마다 각 문제에 대해 최고점수를 뽑아내고 그것을 id 기준으로 조인하고 group하면 각 문제에 대한 최고 점수를 가지고 있으니 그것을 sum하면 된다.


<br>


## Interviews
---
```sql
select con.contest_id,
        con.hacker_id, 
        con.name, 
        sum(total_submissions), 
        sum(total_accepted_submissions), 
        sum(total_views),
        sum(total_unique_views)
from contests con 
join colleges col on con.contest_id = col.contest_id 
join challenges cha on  col.college_id = cha.college_id 
left join
(select challenge_id, sum(total_views) as total_views, sum(total_unique_views) as total_unique_views
from view_stats group by challenge_id) vs on cha.challenge_id = vs.challenge_id 
left join
(select challenge_id, sum(total_submissions) as total_submissions, sum(total_accepted_submissions) as total_accepted_submissions from submission_stats group by challenge_id) ss on cha.challenge_id = ss.challenge_id
    group by con.contest_id, con.hacker_id, con.name
        having sum(total_submissions)!=0 or 
                sum(total_accepted_submissions)!=0 or
                sum(total_views)!=0 or
                sum(total_unique_views)!=0
            order by contest_id;
```
위에는 무난한 join이고 아래서 left join을 하는 이유는 college에서 선택된 challenge만 필요하기 때문이다. 그리고 하나라도 0이 아니면 총 합이 0이 아니므로 having의 조건으로 사용했다.

<br>

