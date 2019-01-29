#!/usr/bin/python3

import sys

#global switches
sleeping_socks = 0
speaker_off = 0

#system def
def exit(dyingmessage):
    if dyingmessage == '':
        dyingmessage = '그렇게 김솨솨는 오지게 쳐막고 호적에서 파인채로 집에서 쫓겨나게 되었답니다 아이샤바 아이샤바 불쌍은 무슨 병신같은 개초딩이 뭘 하겠다고'
    sys.exit(dyingmessage)

#gameover def
def gameover_0():
    print ('애미 : 뭔소리야 너 좀 수상하다 오늘은 같이 자자')
    exit('그렇게 같이 자게 되었답니다 메데타시 메데타시')

def gameover_1():
    print ('애미 : 대답 안하나!')
    print ('김솨솨 : ..')
    exit ('')

def gameover_2():
    print ('애미 : (문을 다시 열면서)야 동작그만 밑장빼기냐')
    print ('김솨솨 : 아 시발 좆됐다')
    exit ('')

def gameover_clear():
    exit ('그렇게 그는 몰컴썰을 온 반에 다 날리고 다니면서 열심히 싹수가 노래졌답니다')

#stage def
def level_7():
    print ('위치 : 김솨솨의 방')
    print ('시간 : 7시 50분')
    print (' ')
    exit('여기까지 함') #여기까지 함

def level_6():
    print ('다시 방에서 존버하다 콤퓨타를 다시 키고 게이플스토리를 켰다')
    print ('후.. 이제는 안나타나겠지? 하면서 즐겁게 게이플스토리를 했다')
    print (' ')
    print ('새벽을 조금 넘으니까 잠이 온다')
    print ('김솨솨는 콤퓨타를 안전하게 끄고 방에 들어가려 한다')
    print ('하지만 갑자기 발소리가 또오 들렸다!')
    print ('아 시발 저새끼 안자냐;;')
    print ('바로 화장실로 직행했지만 애미는 나타나지 않았다')
    print ('기분탓이었나보다')
    level_7()

def level_5():
    print ('콤퓨타를 켜는데 성공했다!')
    print ('이제 게이플스토리를 켜려는데..')
    print ('갑자기 발소리가 들렸다!')
    print ('놀라서 쫄아버린 김솨솨는 바로 콤퓨타를 끄고 화장실로 직행한다!')
    if sleeping_socks == 1:
        print ('애미 : (문열고 나오면서) 야 이 잘시간에 뭐하냐')
        print ('김솨솨 : 화장실 가려구요')
        print ('애미 : 화장실만 갔다가 바로 자러 들어가')
        print ('후..시발 애미뒤진 애미새퀴 뇌를 구구단 외듯이 구워야 할 년이다')
        print (' ')
        print ('1 : 그대로 콤퓨타로 직행')
        print ('2 : 방에서 조금만 존버하다 다시 가자')
        while(1):
            inp = input ('선택 : ')
            if inp == '1':
                gameover_2()
            elif inp == '2':
                level_6()
            else:
                print ('잘못된 선택입니다')
                continue
    else:
        print ('발소리가 존나 크게 울렸다! 김솨솨는 이미 좆된 목숨이다!')
        gameover_2()

def level_4():
    print ('김솨솨는 콤퓨타 본체를 야리더니 전원 버튼을 살짝 눌렀다')
    print ('잠도 안오는데 게이플스토리 할 생각에 신만 난 김솨솨는 병신같이 콤퓨타가 켜질때 삒! 하는 소리가 난다는 사실을 까먹고 있었다')
    print ('콤퓨타 : 삒!')
    print ('김솨솨는 그대로 놀라 진짜로 고인이 될뻔했다!')
    print ('다행히도 아무도 안 깼다..')
    if speaker_off == 1:
        print ('콤퓨타 : 섹로운 시작')
        level_5()
    else:
        print ('콤퓨타 : 섹로운 시작 (존나 시끄럽게 시작음으로 알리면서)')
        gameover_2()

def level_3():
    print ('분명 거리는 몇 안되는데 존나 부산에서 서울가는 거리처럼 느껴지긴 했어도 암튼 콤퓨타 앞이다')
    print ('자 이제 콤퓨타를 키려고 한다')
    print (' ')
    print ('1 : 일단 킨다')
    print ('2 : 스피커 끄자')
    while(1):
        inp = input ('선택 : ')
        if inp == '1':
            speaker_off = 0
            level_4()
        elif inp == '2':
            print ('잠깐만 그냥 키면 스피커 소리 때문에 들키잖음? 스피커 끄자')
            speaker_off = 1
            level_4()

def level_2_1():
    print ('김솨솨 : 화장실 가려구요')
    print ('애미 : 딱 화장실만 갔다와서 바로 자라')
    print ('애미는 다시 방으로 들어갔다')
    print ('후..후.. 쉬펄 염통이 깃쫄깃쫄')
    print ('암튼 화장실도 좀 급하긴 했으니까 해결하고')
    print (' ')
    print ('1 : 그대로 콤퓨타로 직행')
    print ('2 : 방에서 조금만 존버하고 가자')
    while(1):
        inp = input ('선택 : ')
        if inp == '1':
            gameover_2()
        elif inp == '2':
            print ('일단 방에 들어가서 10분 정도 존버했다')
            print ('그리고 다시 콤퓨타로 직행했다')
            level_3()

def level_2():
    print ('위치 : 김솨솨의 방')
    print ('시간 : 새벽 거의 다 되어감')
    print (' ')
    print ('김솨솨는 자기 방에서 자려고 힘쓰는 중이다')
    print ('하지만 아무리 자려고 노오오오오오력해도 지 뇌내에서 떠돌아댕기는 게이플스토리 생각 때문에 잘 수가 없다!')
    print ('이 시발새끼는 남들 좆같은 게이플스토리 할때 걍 찐따처럼 짜져있으면 될걸 왜 시작해서 이모양인가 싶은 생각까지 든다')
    print ('그렇게 발록이랑 쳐싸우다 좋은 띵킹이 났다')
    print ('바로 몰ㅋ컴ㅋ을 하는 것이다!')
    if sleeping_socks == 1:
        print ('마침 김솨솨가 수면양말을 신고 자러 들어간게 존나 신의 한수였다!')
    else:
        print ('하지만 발소리 때문에 부모님이 일어나면 그대로 Fㅐ배할텐데..')
    print (' ')
    print ('일단 조심스럽게 자기 방 문을 연다.. 소리 내지 않고 문을 여는데는 성공했다')
    print ('이대로 콤퓨타가 있는 곳으로 조심스럽게 걸어가는데..')
    if sleeping_socks == 1:
        level_3()
    else:
        print ('갑자기 부모님 방 문이 열렸다!')
        print ('애미 : 야 잘밤에 슬금슬금 걸어가서 뭐하려고')
        print ('과연 김솨솨는 뭐라고 변명할까?')
        print (' ')
        print ('1 : 화장실 가려구요')
        print ('2 : 대답 안한다')
        while(1):
            inp = input ('선택 : ')
            if inp == '1':
                level_2_1()
            elif inp == '2':
                gameover_1()
            else:
                print ('잘못된 선택입니다')
                continue

def level_1_1():
    print ('김솨솨는 수면양말을 꺼내 가져가려고 한다')
    print ('그러나 이상함을 느낀 애미는 김솨솨에게 "수면양말은 왜 가져가려고"라고 묻는다')
    print ('김솨솨는 뭐라고 변명할까?')
    print (' ')
    print ('1 : 잘 때 이거 신고 자면 좋대요')
    print ('2 : 그냥요')
    print ('3 : 몰컴하려구요')
    while(1):
        inp = input ('선택 : ')
        if inp == '1':
            print ('애미 : 아 그래? 그럼 맘대로 해')
            print ('성공적으로 수면양말을 획득했다!')
            sleeping_socks = 1
            level_2()
        elif inp == '2':
            print ('애미 : 뭔짓하려고 내려놔')
            print ('수면양말을 획득하지 못했다!')
            sleeping_socks = 0
            level_2()
        elif inp == '3':
            gameover_0()
        else:
            print ('잘못된 선택입니다')
            continue

def level_1():
    print ('위치 : 거실')
    print ('시간 : 잘 시간으로부터 10분 전')
    print (' ')
    print ('김솨솨는 보르넷 숙제를 모두 마치고 햄보카게 가족이랑 같이 있다')
    print ('이제 잘 준비를 하려는데..')
    print (' ')
    print ('1 : 수면양말을 준비한다')
    print ('2 : 그냥 방에 간다')
    while(1):
        inp = input ('선택 : ')
        if inp == '1':
            level_1_1()
        elif inp == '2':
            print ('쿨하게 안가지고 간다!')
            sleeping_socks = 0
            level_2()
        else:
            print ('잘못된 선택입니다')
            continue

#frist entry
print ('때는 2004년 5월 6일, 지금 한국 초딩들은 게이플스토리로 뜨거워지고 있다')
print ('그리고 뫄뫄초등학교 -1학년 -1반 김솨솨는 어느 날 새벽에 잠이 안와서 게이플스토리를 하고 싶어한다')
print ('하지만 콤퓨타는 거실에 있고 모두가 자고 있는 상황이라 들키면 모가지 순삭되는거 한순간인데..')
print ('과연 김솨솨는 몰컴을 성공할 수 있을까?')
print (' ')
print ('1 : 응 성공해 어서 하자')
print ('2 : 응 성공안해 그냥 자라')

while 1:
    inp = input ('선택 : ')
    if inp == '1':
        level_1()
    elif inp == '2':
        exit('네 그냥 자기로 했습니다 즐잠')
    else:
        print ('잘못된 입력입니다')
        continue
