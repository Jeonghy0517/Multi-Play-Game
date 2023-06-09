##진행 순서##
#1. 게임 서버 만들기
#2. 클라이언트 만들기

#*--------------------------------------------------------------------------*#
#게임 규칙
'''
1. 서버에서 플레이어(클라이언트)의 접속을 기다림
2. 플레이어가 서버에 접속하면 서버는 접속자 수 (정답)을 업데이트 함
3. 접속한 플레이어는 예상되는 현재 사이트 접속자 수를 입력해서 서버로 보냄
4. 서버는 플레이어가 입력한 숫자가 정답보다 높을 땐 너무 높아요, 낮을 땐 너무 낮아요라고 응답
5. 플레이어가 0을 입력하면 "종료"라고 응답하고 접속자 수(정답)을 업데이트
6. 클라이언트가 정답을 입력하면 "정답"이라고 응답하고 서버를 종료
'''

#*--------------------------------------------------------------------------*#

#1. 게임 서버 만들기
#multi_play_game_server.py

#2. 클라이언트 만들기
#multi_play_game_client.py