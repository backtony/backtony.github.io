---
layout: post
title:  Javascript 기초
subtitle:   Javascript 기초
categories: web
tags: web webprogramming spartacodingclub
comments: true
# header-img:
---
+ __목차__
  - [1.변수](#1-변수)
  - [2. 리스트](#2-리스트)
  - [3. 딕셔너리](#3-딕셔너리) 
  - [4. 함수](#4-함수) 
  - [5. 조건문](#5-조건문) 
  - [6. 반복문](#6-반복문) 

## 1. 변수
---
```javascript
let 변수명

let a =7
let b = 'hello'
a + b // 7hello

대문자로 바꾸기
let name = 'highlite'
name.toUpperCase() // HIGHLITE
```
문자열은 따옴표를 붙여주면 된다.  
<br>

## 2. 리스트
---
```javascript
선언
let a_list = ['수박','참외','배']
let b_list = ['영희','철수','영지']

추가
a_list.push('감') // ['수박','참외','배','감']
a_list.push(b_list) // ['수박','참외','배','감',['영희','철수','영지']]
a_list[4][1] // 철수

자르기
let myemail = 'sparta@gmail.com'
myemail.split('@') // ['sparta','gmail.com']
myemail.split('@')[1].split('.')[1] // 'com'

붙이기
myemail.split('@').join('_') // "sparta_gmail.com"
```
파이썬은 append이므로 주의할 것!
<br>

## 3. 딕셔너리
---
```javascript
let a_dict = {'name':'hong','age':21}
a_dict['name'] // 'hong'
a_dict['age'] // 21

추가
a_dict['height']=180 // {'name':'hong','age':21, 'height':180}
a_dict['friends']=['영희','철수'] // {'name':'hong','age':21, 'height':180,'friends':['영희','철수']}

변경
a_dict['age']=25 // // {'name':'hong','age':25, 'height':180,'friends':['영희','철수']}
```
<Br>

## 4. 함수
---
```javascript
function 함수명(인자){
  내용
}

function sum(num1,num2){
  return num1+num2
}
```
<br>

## 5. 조건문
---
```javascript
if (age> 20 && sex == 'man'){
  alert('adult and man')
} else if (age > 20 && sex == 'woman'){
  alert('adult and woman')
} else {
  alert('child')
}
```
<Br>

## 6. 반복문
---
cf) print같은 출력 => console.log(0) // 0
```javascript
for (let 1=0;i<100;i++>){
  console.log(i)
}

let mylist = ['부산','서울','제주','강화도']
for (let i=0;i<mylist.length;i++){
  console.log(mylist[i])
}
```