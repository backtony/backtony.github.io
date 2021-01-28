---
layout: post
title:  파이썬 패키지
subtitle:   파이썬 패키지
categories: web
tags: sparta web webprogramming spartacodingclub
comments: true
# header-img:
---
+ __목차__
  - [1. 패키지](#1-패키지)
  - [2. 설치](#2-설치)
  - [3. 가상환경](#3-가상환경) 
  - [4. 사용하기](#4-사용하기) 

## 1. 패키지
---
python에서 패키지는 모듈(일종의 기능들 묶음)을 모아 놓은 단위이다. 이런 패키지의 묶음을 라이브러리라고 볼 수 있다. 외부 라이브러리를 사용하기 위해서는 패키지를 설치해야 한다.

## 2. 설치
파이참 -> 설정 -> 프로젝트: 열고있는폴더이름 -> 오른쪽 톱니바퀴 아래 + 클릭 -> 원하는 패키지 검색후 설치  

## 3. 가상환경
가상환경은 같은 시스템에서 실행되는 다른 파이썬 응용 프로그램들의 동작에 영향을 주지 않기 위해, 파이썬 배포 패키지들을 설치하거나 업그레이드하는 것을 가능하게 하는 격리된 실행 환경이다.  
예를 들어, 회사에서는 패키지 A, B, C를 설치해서 쓰고 개인 프로젝트에서는 패키지 B, C, D, E를 설치해서 쓰고 있다. 그런데 팀장님이 B를 이전 버전인 B-로 쓰자고 한다. 그렇게 되면, 같은 컴퓨터에 깔려 있는 개인 프로젝트에서는 B-로 쓰면 코드를 다 바꿔야 한다. 이러한 해결책으로 공구함 2개를 만들어서 공구함 1에는 A, B-, C를 담아두고, 공구함 2에는 B, C, D, E를 담아두고 쓰면 되는 것이다. 그래서 가상환경이라는 개념이 등장했다.

## 4. 사용하기
```python
import requests # requests 라이브러리 설치 필요 # request 라이브러리 가지고 와라

# requests.get('url')하면 그 결과를 받아온다.
r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
# r.json() 결과를 json형식으로 한 후 rjson에 대입
rjson = r.json()

print(rjson['RealtimeCityAir']['row'][0]['NO2'])
```
