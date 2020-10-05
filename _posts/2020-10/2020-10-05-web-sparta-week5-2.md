---
layout: post
title:  내 프로젝트 서버에 올리기
subtitle:  내 프로젝트 서버에 올리기
categories: web
tags: web webprogramming spartacodingclub
comments: true
# header-img:
---
+ __목차__
  - [1. 웹서비스 런칭에 필요한 개념](#1-웹서비스-런칭에-필요한-개념)  
  - [2. AWS 서버](#2-aws-서버)
  - [3. flask 서버 실행해보기](#3-flask-서버-실행해보기)
  - [4. AWS에서 포트 열어주기](#4-aws에서-포트-열어주기)
  - [5. mongoDB 설치하기](#5-mongodb-설치하기)


## 1. 웹서비스 런칭에 필요한 개념
---
+ 웹 서비스 런칭을 하기 위해서는 클라이언트의 요청에 항상 응답해줄 수 있는 서버에 프로젝트를 실행시켜줘야 한다.
+ 언제나 요청에 응답하려면, 
    - 컴퓨터가 항상 켜져있고 프로그램이 실행되고 있어야 한다.
    - 모두가 접근할 수 있는 공개 주소인 공개 IP주소로 나의 웹 서비스에 접근할 수 있도록 해야 한다.
+ 서버는 역할이고 컴퓨터는 사람이라고 비유할 수 있다고 앞서 설명했었다. 외부 접속이 가능하게 설정한 다음에 내 컴퓨터를 서버로 사용할 수 있다.
+ AWS라는 클라우드 서비스에서 편하게 서버를 관리하기 위해서 항상 켜 놓을 수 있는 컴퓨터인 EC2 사용권을 구입해서 서버로 사용해보자.

### IP 주소와 포트
우리가 접속하는 컴퓨터는 숫자로 되어있는 주소(IP주소)가 붙어있다. 우리가 아는 URL은 우리가 알아보기 쉽게 하는 등의 이유로 IP주소를 알파벳으로 바꾼 것이다. 이렇게 변환해 주는 시스템을 DNS라고 한다.

![그림1](https://backtony.github.io/assets/img/post/web/sparta/web-sparta-week5-2-1.PNG)


+ IP 주소 : 컴퓨터가 통신할 수 있도록 컴퓨터마다 가지는 고유한 주소라고 생각하면 된다. 정확히는 네트워크가 가능한 모든 기기가 통신할 수 있도록 가지고 있는 특수한 번호이다. 서버는 하나의 주소를 가지고 있다.
+ 포트 : 하나의 IP에는 여러 포트가 있다. 하나의 포트에 하나의 프로그램을 실행시킬 수 있다.
    - 항구와 비유하면 쉽다. 한국에 들어갈 껀데 부산항, 인천항 등으로 들어갈 수 있다. 항구마다 어떤 일이 각각 매칭이 되어 있다. 어떤 항구는 flask 관련 일만, 어떤 항구는 mongodb와 관련된 일만 할 수 있는 것이다. 컴퓨터에서 하고 있는 일들이 많을 것이고 컴퓨터에서 외부와 뚫어놓은 일들이 많을 것인데 그 뚫어놓은 일들 하나하나가 다 다른 항구와 연결되어 있다고 보면 된다. 이 항구를 포트라고 하는 것이다.


## 2. AWS 서버
---
### 준비 상식
윈도우와 같이 OS는 여러개 존재한다. 리눅스도 그 중의 하나이며, 오픈소스로 발전되는 OS이다. AWS에서 서버를 구매하게 되면 리눅스 OS의 서버를 구매하게 된다.  

### AWS EC2에 접속하기
SSH는 다른 컴퓨터에 접속할 때 쓰는 프로그램이다. 서로 22번 포트가 열려있어야 접속이 가능하다. AWS EC2의 경우, 이미 22번 포트가 열려있다. 
+ Mac OS의 경우 : Mac은 ssh가 있어서, 명령어로 바로 접근이 가능하다.
+ Window OS의 경우 : ssh가 없으므로, git bash라는 프로그램을 이용
  - git bash를 실행하고 `ssh -i 받은키페어를끌어다놓기 ubuntu@AWS에적힌내아이피` 를 입력한다.
  - 대략 sh -i /path/my-key-pair.pem ubuntu@13.125.250.20 이러한 생김새이다.
  - key fingerprint 관련 메시지가 나올 경우 Yes를 입력한다.
  - 참고로 git bash를 종료할 때는 exit 명령어를 입력하여 ssh 접속을 먼저 끊어준다.

### 간단한 리눅스 명령어
+ 리눅스는 윈도우 같지 않아서, 쉘 명령어를 통해 OS를 조작한다.(일종의 마우스 역할)

__가장 많이 사용하는 몇 가지 명령어__
팁이 있다면 리눅스 커널에서 윗화살표를 누르면 바로 전에 썻던 명령어가 나온다.
```
ls: 내 위치의 모든 파일을 보여준다.

pwd: 내 위치(폴더의 경로)를 알려준다.

mkdir: 내 위치 아래에 폴더를 하나 만든다.

cd [갈 곳]: 나를 [갈 곳] 폴더로 이동시킨다.

cd .. : 나를 상위 폴더로 이동시킨다.

cd ~ : home 디렉토리로 이동

cp -r [복사할 것] [붙여넣기 할 것]: 복사 붙여넣기

rm -rf [지울 것]: 지우기

sudo [실행 할 명령어]: 명령어를 관리자 권한으로 실행한다.
sudo su: 관리가 권한으로 들어간다. (나올때는 exit으로 나옴)
```
<br>

## 3. flask 서버 실행해보기
---
filezilla를 이용할 건데 filezilla는 쉽게 컴퓨터간의 파일을 옮기는 역할을 한다고 보면 된다.  

파일질라 실행 후 다음과 같이 설정

![그림2](https://backtony.github.io/assets/img/post/web/sparta/web-sparta-week5-2-2.PNG)

정보들을 입력하고, ok 누르면 서버의 파일들을 볼 수 있음(Host: 내 EC2서버의 ip // User: ubuntu 로 입력)

![그림3](https://backtony.github.io/assets/img/post/web/sparta/web-sparta-week5-2-3.PNG)

마우스로 드래그 해서 파일을 업로드/다운로드 하면 완료
![그림4](https://backtony.github.io/assets/img/post/web/sparta/web-sparta-week5-2-4.PNG)

간단하게 print('hello world')가 저장된 test.py를 옮겨보고 콘솔창에서 python test.py를 실행해보면 콘솔창에 hello world가 뜨는 것을 확인 할 수 있다.   
기초적인 flask 서버 파일을 하나 만들어서 옮겨보자.
```python
# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return 'This is Home!'

if __name__ == '__main__':  
   app.run('0.0.0.0', port=5000, debug=True)
```
app.py 파일을 filezilla를 통해 EC2에 업로드 한 다음에 python app.py로 실행해보면 에러가 난다. flask 패키지가 없기 때문이다.  

### 리눅스에서 패키지 설치하기
파이참에서는 자동으로 pip이 설치되지만 AWS에는 pip을 따로 설치해줘야 한다. 아래 코드를 차례대로 콘솔창에 입력해주자.  
```
# pip 설치 1
sudo apt-get update

# pip 설치 2
sudo apt-get install -y python3-pip


# pip 설치 3
sudo apt-get update
sudo apt-get install -y python3-pip

# pip3 대신 pip 라고 입력하기 위한 명령어
sudo update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1
```
pip이 설치가 완료되었으면 이제 가상환경에 flask를 설치해보자.
```
pip install flask # 이제 다른 것들도 이것과 마찬가지로 pip install ~~ 으로 설치하면 된다.
```
이제 다시 콘솔창에서 python app.py 입력을 통해 서버가 실행 되면, 크롬에서 접속해보자.
```
크롬 브라우저 창에 아래와 같이 입력한다. EC2 IP는 퍼블릭IPv4 주소이다.
http://[내 EC2 IP]:5000/
```
하지만 페이지가 작동하지 않는다. -> AWS에서 약간의 설정이 더 필요하기 때문이다.
<br>

## 4. AWS에서 포트 열어주기
---
### AWS에서 5000포트 열어주기
EC2 서버(가상의 내 컴퓨터)에서 포트를 따로 설정하는 것 외에도, AWS EC2에서도 자체적으로 포트를 열고/닫을 수 있게 관리하고 있다. 그래서 AWS EC2 Security Group에서 인바운드 요청 포트를 열어줘야 한다.  
세 가지 포트를 추가해 보자.  
+ 80포트 : HTTP 접속을 위한 기본 포트
+ 5000포트 : flask 기본 포트
+ 27017포트 : 외부에서 mongoDB 접속을 하기 위한 포트

EC2 -> 보안 그룹 -> 해당 서버의 보안 그룹 ID 클릭 -> 인바운드 규칙 편집 -> 규칙 추가 -> 사용자 지정 TCP, 포트범위 : 5000, 위치무관으로 설정하고 나머지 포트범위만 다르고 동일하게 설정 후 저장하면 완료된다.
```
다시 아래와 같이 크롬 주소창에 입력시 정상 동작하는 것을 확인할 수 있다.
http://[내 EC2 IP]:5000/
```

## 5. mongoDB 설치하기
### mongoDB 설치 코드
무슨 뜻인지는 굳이 알 필요 없이 그냥 mongoDB를 설치하는 코드라고 생각하면 된다. 콘솔창에 다음과 같이 입력하자. 
```
# 설치 1
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -

# 설치 2
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list

# 설치 3
sudo apt-get update

# 설치 4
sudo apt-get install -y mongodb-org
```

### mongoDB 실행하기
```
sudo service mongod start
# 실행. 아무 반응이 없으면, 잘 실행된 것!
# 리눅스는 보통 잘 되면 아무것도 안나온다.
```

### mongoDB 접속 계정 생성하기
만든 mongoDB를 외부에 열어주기 전에, 접속에 필요한 아이디와 비밀번호를 세팅해보자. 설정 안하면 누구나 DB정보를 볼수 있기 때문이다. 마찬가지로 콘솔창에서 진행한다.  
```
mongo
# 좌측에 > 표시가 나오면 성공적으로 mongoDB에 접속한 것이다. 다음 명령어를 순차적으로 입력한다.

# admin 계정으로 바꾸기
use admine;

# 계정 생성하기 , 간단하게 user와 pwd를 test로 했다.
db.createUser({user: "test", pwd: "test", roles:["root"]}); 

# 나오기
exit

# mongoDB 재시작
sudo service mongod restart
```
<br>

mongoDB는 디폴트로 내부에서만 접속을 허용하고 있다. 이제 외부에서 접근이 가능하도록 잠금을 풀어주는 작업을 해보자.  
```
sudo vi /etc/mongod.conf
# sudo: 관리자(SuperUser) 권한으로 다음을 실행
# => "관리자 권한으로 /etc 폴더 아래 mongod.conf 파일을 Vim으로 켜줘!"라는 뜻
```
위 명령어를 실행한 후, 아래 방향 화살 키를 누르면 다음과 같은 내용이 보인다.  
![그림5](https://backtony.github.io/assets/img/post/web/sparta/web-sparta-week5-2-5.PNG)


위의 붉은 박스를 아래와 같이 수정한다. A키(입력모드로 전환)를 누르면 수정이 가능하다.
![그림6](https://backtony.github.io/assets/img/post/web/sparta/web-sparta-week5-2-6.PNG)

수정한 것을 저장하고 종료하기 위해서는 esc키를 누르고 :wq 입력 후 엔터키를 누르면 된다. 이후 sudo service mongod restart로 재시작을 해준다.  
<br> 

이제 진짜 내 컴퓨터에서 Robo3T를 이용해 서버에 있는 mongoDB에 접속해보자.  
![그림7](https://backtony.github.io/assets/img/post/web/sparta/web-sparta-week5-2-7.PNG)
![그림8](https://backtony.github.io/assets/img/post/web/sparta/web-sparta-week5-2-8.PNG)

이제 접속 정보를 아래와 같이 세팅한다.
![그림9](https://backtony.github.io/assets/img/post/web/sparta/web-sparta-week5-2-9.PNG)

상단의 Authentication 탭을 클릭하고 perform authentication 체크박스를 클릭한다. 앞서 생성한 계정의 아이디와 비밀번호를 입력하고, save를 클릭한다.

![그림10](https://backtony.github.io/assets/img/post/web/sparta/web-sparta-week5-2-10.PNG)

이렇게 하면 이제 내 실제 컴퓨터에서 서버의 mongoDB로의 연결이 완료된 것이다.
<br>

## 6. 원페이지쇼핑몰 업로드해보기
---

