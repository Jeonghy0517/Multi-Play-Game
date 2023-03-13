#서버와 통신하기
#소켓(socket) : 소프트웨어로 작성된 다른 컴퓨터와 네트워크를 통해 데이터를 송수신하기 위한 창구 역할을 하는 통신 접속점
#포트(port): 네트워크 상에서 통신하기 위해 호스트 내부적으로 프로세스가 할당받아야하는 고유한 숫자
#하나의 소켓은 여러개의 포트를 할당 받을 수 있음

#socket
#파이썬으로 TCP(Transmission Control Protocol) 서버/클라이언트 프로그램을 작성할 때 사용하는 표준 라이브러리

#echo 서버/클라이언트 예제
#클라이언트가 보낸 메세지를 서버가 다시 전송하는 예제
#1. 클라이언트가 접속하면 서버에서 접속한 클아이언트 정보를 출력
#2. 클라이언트가 문자열을 전송하면 서버가 수신한 문자열을 출력하고 다시 echo
#3. 클라이언트에서 수신받은 문자열을 출력

##-------------------------------------------------------------------##
##echo_server.py : 파이참에서 실행##
# import socket
#
# HOST = '127.0.0.1' #접속 할 서버 주소, localhost 사용
# PORT = 9999 #클라이언트 접속을 대기하는 포트번호
#
# #소켓 객체를 생성
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, 소켓 타입으로 TCP 사용
#
# #포트 사용 중이라 연결할 수 없나는 WinError 해결 위해 필요
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
# #bind함수는 소켓을 특정 네트워크 인터페이스와 포트 번호에 연결하는데 사용됨
# #HOST는 hostname, ip address, 빈문자열("")이 될 수 있음 => 빈 문자열이면 모든 네트워크 인터페이스로부터 접속 혀용
# #PORT는 1-65535 사이의 숫자 사용 가능
# server_socket.bind((HOST,PORT))
#
# #서버가 클라이언트의 접속을 허용하도록 함
# server_socket.listen()
# print('서버가 실행되었습니다.')
#
# #accept 함수에서 대기하다 클라이언트가 접속하면 새로운 소켓을 리턴
# client_socket, addr = server_socket.accept()
#
# #접속한 클라이언트의 주소
# print("접속한 클라이언트 주소입니다.")
# print("Connect by", addr)
#
# #무한 루프
# while True:
#     #클라이언트가 보낸 메시지를 수신하기 위해 대기
#     data = client_socket.recv(1024)
#
#     #빈 문자열을 수신하면 루프를 중지
#     if not data:
#         break
#
#     #수신받은 문자열을 출력
#     print('Received from', addr, data.decode())
#
#     #받은 문자열을 다시 클라이언트로 전송 (에코)
#     client_socket.sendall(data)
#
# #소켓 닫아줌
# client_socket.close()
# server_socket.close()
##-------------------------------------------------------------------##

##-------------------------------------------------------------------##
##echo_client.py : cmd에서 실행##
# import socket
#
# #서버의 주소와 포트
# HOST = '127.0.0.1'
# PORT = 9999
#
# #소켓 객체를 생성
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# #지정한 HOST와 PORT를 사용해 서버에 접속함
# client_socket.connect((HOST,PORT))
#
# #메시지를 전송
# client_socket.sendall('안녕!'.encode())
# #메시지를 수진
# data = client_socket.recv(1024)
# print('Received', repr(data.decode()))
# #소켓을 닫음
# client_socket.close()
##-------------------------------------------------------------------##

#---------------------------------------------------------------------------------------------------------------------
#여러명이 동시에 접속하기

#socket만 사용한 서버 통신의 문제점
#클라이언트가 소켓 서버에 접속하여 접속을 종료하면 소켓서버 역시 종료
#소켓 서버가 여러 클라이언트와 동시에 접속될 수 없음

#select
#소켓 프로그래밍에서 하나의 전송로로 여러 종류의 데이터를 송수신하게 해주는 모듈
#한 개의 프로세스로 두 개 이상의 클라이언트 요청을 처리하는 것을 의미하는 I/O 멀티 플렉싱을 가능하게 해줌

##-------------------------------------------------------------------##
##echo_server_multi.py##
# import socket
# import select
#
# HOST = '127.0.0.1' #접속 할 서버 주소, localhost 사용
# PORT = 9999 #클라이언트 접속을 대기하는 포트번호
#
# #소켓 객체를 생성
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, 소켓 타입으로 TCP 사용
#
# #포트 사용 중이라 연결할 수 없나는 WinError 해결 위해 필요
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
# #bind함수는 소켓을 특정 네트워크 인터페이스와 포트 번호에 연결하는데 사용됨
# #HOST는 hostname, ip address, 빈문자열("")이 될 수 있음 => 빈 문자열이면 모든 네트워크 인터페이스로부터 접속 혀용
# #PORT는 1-65535 사이의 숫자 사용 가능
# server_socket.bind((HOST,PORT))
#
# #서버가 클라이언트의 접속을 허용하도록 함
# server_socket.listen()
# print('서버가 실행되었습니다.')
#
# #select 함수에서 관찰될 소켓 리스트 생성
# readsocks = [server_socket]
#
# while True:
#     #select 함수로 소켓들의 상태를 확인
#     readables, writeables, exceptions = select.select(readsocks, [], [])
#     for sock in readables:
#
#         #신규 클라이언트 접속
#         if sock == server_socket:
#             #accept 함수에서 대기하다가 클라이언트가 접속하면 새로운 소켓을 리턴
#             client_socket, addr = server_socket.accept()
#
#         #접속한 클라이언트 주소 확인
#         print('접속한 클라이언트 주소입니다.')
#         print('Connect by', addr)
#
#         #소켓 리스트에 추가
#         readsocks.append(client_socket)
#
#     #기존 클라이언트 응답
#     else:
#         #무한 루프를 돌면서
#         while True:
#             #클라이언트가 보낸 메시지를 수신하기 위해 대기
#             data = sock.recv(1024)
#
#             #빈 문자열을 수신하면 루프를 중지
#             if not data:
#                 print(sock.getpeername(), '접속 종료', data.decode())
#
#                 #소켓을 닫음
#                 sock.close()
#                 readsocks.remove(sock)
#                 break
#
#             #수신받은 문자열을 출력
#             print('Received from', sock.getpeername(), data.decode())
#
#             #받은 문자열을 다시 클라이언트로 전송 (에코)
#             sock.sendall(data)
#
# server_socket.close() #서버 종료
##-------------------------------------------------------------------##
#---------------------------------------------------------------------------------------------------------------------
#플레이어 신호 수신
#시그널 : 프로세스/프로그램에 특정 이벤트가 발생했을 때 전달하는 신호
#시그널 종류와 각 시그널에 따른 기본 조치 동작이 미리 정해져 있음

#시그널 발생 시 기본 조치
#1. 신호 무시
#2. 특정 신호를 캐치해서 원하는 조치가 실행되도록 함
#3. 기본 조치 동작이 실행되도록 함

#주요 시그널의 기본 조치 동작
#1. SIGKILL : 프로세스를 강제 종료
#2. SIGALARM : 알람 발생
#3. SIGSTP : 프로세스를 중단
#4. SIGCONT : 멈춰진 프로세스를 재개 \
#5. SIGINT : 키보드 인터럽트를 보내서 프로세스를 중단
#6. SIGSEGV : 프로세스가 다른 메모리영역을 침범

#signal : 특정한 신호를 수신했을 때 사용자가 정의한 함수를 호출하는 모듈
#Ctrl + C 를 입력할 경우, 키보드 인터럽트(SIGINT) 신호를 감지하고 handler 함수 실행 (cmd에서 실행)
import time
import signal

def handler(signum, frame):
    print("Ctrl + C 신호를 수신했습니다.") #signum : 발생한 신호의 숫자, frame : 프로그램 실행 스텍 프레임

#처리 할 신호 유형, 실행 할 함수
signal.signal(signal.SIGINT, handler)

while True:
    print('대기중...')
    time.sleep(10)
