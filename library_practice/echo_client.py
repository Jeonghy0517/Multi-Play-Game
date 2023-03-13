import socket

#서버의 주소와 포트
HOST = '127.0.0.1'
PORT = 9999

#소켓 객체를 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#지정한 HOST와 PORT를 사용해 서버에 접속함
client_socket.connect((HOST,PORT))

#메시지를 전송
client_socket.sendall('안녕!'.encode())
#메시지를 수진
data = client_socket.recv(1024)
print('Received', repr(data.decode()))
#소켓을 닫음
client_socket.close()