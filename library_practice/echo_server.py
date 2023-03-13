import socket

HOST = '127.0.0.1' #접속 할 서버 주소, localhost 사용
PORT = 9999 #클라이언트 접속을 대기하는 포트번호

#소켓 객체를 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, 소켓 타입으로 TCP 사용

#포트 사용 중이라 연결할 수 없나는 WinError 해결 위해 필요
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#bind함수는 소켓을 특정 네트워크 인터페이스와 포트 번호에 연결하는데 사용됨
#HOST는 hostname, ip address, 빈문자열("")이 될 수 있음 => 빈 문자열이면 모든 네트워크 인터페이스로부터 접속 혀용
#PORT는 1-65535 사이의 숫자 사용 가능
server_socket.bind((HOST,PORT))

#서버가 클라이언트의 접속을 허용하도록 함
server_socket.listen()
print('서버가 실행되었습니다.')

#accept 함수에서 대기하다 클라이언트가 접속하면 새로운 소켓을 리턴
client_socket, addr = server_socket.accept()

#접속한 클라이언트의 주소
print("접속한 클라이언트 주소입니다.")
print("Connect by", addr)

#무한 루프
while True:
    #클라이언트가 보낸 메시지를 수신하기 위해 대기
    data = client_socket.recv(1024)

    #빈 문자열을 수신하면 루프를 중지
    if not data:
        break

    #수신받은 문자열을 출력
    print('Received from', addr, data.decode())

    #받은 문자열을 다시 클라이언트로 전송 (에코)
    client_socket.sendall(data)

#소켓 닫아줌
client_socket.close()
server_socket.close()