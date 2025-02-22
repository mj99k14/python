
#클라이언트 (본인)두번쨰 실행
import socket

# 클라이언트 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버 연결
try:
    client_socket.connect(('210.101.236.189', 12345))  # 서버 IP와 포트 번호
    print("서버에 성공적으로 연결되었습니다.")

    # 데이터 송수신
    while True:
        message = input("서버로 보낼 메시지: ")
        if message == 'quit':  # 'quit' 입력 시 연결 종료
            break
        client_socket.sendall(message.encode())  # 서버로 데이터 전송
        data = client_socket.recv(1024).decode()  # 서버로부터 데이터 수신
        print(f"서버로부터 받은 응답: {data}")
except ConnectionRefusedError:
    print("서버에 연결할 수 없습니다. 서버가 실행 중인지 확인하세요.")
except Exception as e:
    print(f"클라이언트 에러: {e}")
finally:
    client_socket.close()     




#상대방 소켓확인용 (첫번쨰 실행)
#import socket

# 서버 소켓 생성
#server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버 IP와 포트 바인딩
#server_socket.bind(('210.101.236.189', 12345))  # 서버의 IP 주소와 포트
#server_socket.listen(1)  # 최대 1개의 클라이언트 대기
#print("서버가 실행 중입니다. 클라이언트를 기다리는 중...")

# 클라이언트 연결 수락
#client_socket, addr = server_socket.accept()
#print(f"클라이언트가 연결되었습니다: {addr}")

# 데이터 송수신
#while True:
    #try:
        #data = client_socket.recv(1024).decode()  # 클라이언트로부터 데이터 수신
        #if not data:  # 데이터가 없으면 연결 종료
            #break
        #print(f"클라이언트로부터 받은 메시지: {data}")
        #client_socket.sendall(f"서버 응답: {data}".encode())  # 클라이언트로 응답
    #except ConnectionResetError:
        #print("클라이언트와의 연결이 종료되었습니다.")
        #break

# 연결 종료
#client_socket.close()
#server_socket.close()
