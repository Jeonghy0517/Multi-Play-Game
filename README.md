# Multi-Play-Game
## 게임에 접속한 접속자 수를 맞추는 게임 
---
### 사용한 Python 라이브러리

+ **socket**
  
  * 파이썬으로 TCP(Transmission Control Protocol) 서버/클라이언트 프로그램을 작성할 때 사용하는 표준 라이브러리
  
+ **select**

  * 소켓 프로그래밍에서 하나의 전송로로 여러 종류의 데이터를 송수신하게 해주는 모듈
  
  * 한 개의 프로세스로 두 개 이상의 클라이언트 요청을 처리하는 것을 의미하는 I/O 멀티 플렉싱을 가능하게 해줌
 
+ **signal**

  * 특정한 신호를 수신했을 때 사용자가 정의한 함수를 호출하는 모듈
  
+ **주요 시그널의 기본 조치 동작**

  1. SIGKILL : 프로세스를 강제 종료
  
  2. SIGALARM : 알람 발생
  
  3. SIGSTP : 프로세스를 중단
  
  4. SIGCONT : 멈춰진 프로세스를 재개
  
  5. SIGINT : 키보드 인터럽트를 보내서 프로세스를 중단