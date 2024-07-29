import os
import time
import random
import datetime

from gtts import gTTS
# from playsound import playsound

import streamlit as st

############### 상수 설정 ###############
BEREADY=0
BEGIN_CLASS=1
BEGIN_BREAK=2
ENCOURAGE=3
END=4

############### 응원 메세지 LIST ###############
text_list = [
    ["넌 정말 특별해."],
    ["너는 소중한 존재야."],
    ["너는 소중한 존재야."],
    ["항상 널 믿어."],
    ["실수해도 괜찮아, 그게 배움의 과정이야."],
    ["넌 무엇이든 할 수 있어."],
    ["넌 늘 노력하고 있어, 그게 중요해."],
    ["네가 하는 모든 일이 소중해."],
    ["힘든 순간도 지나갈 거야."],
    ["네가 자랑스러워."],
    ["모든 일에는 이유가 있어."],
    ["너의 꿈을 포기하지 마."],
    ["항상 긍정적으로 생각해."],
    ["네가 잘하고 있다는 걸 잊지 마."],
    ["넌 사랑받기 위해 태어난 사람이야."],
    ["도전하는 모습을 응원해."],
    ["네가 주인공이야."],
    ["항상 용기를 내어봐."],
    ["너의 웃음은 세상을 밝게 해."],
    ["네가 가진 모든 재능이 귀중해."],
    ["매일 매일 조금씩 성장하고 있어."],
    ["너는 독특하고 멋진 존재야."],
    ["네가 있어 세상이 더 아름다워."],
    ["오늘도 너의 최선을 다해줘서 고마워."],
    ["항상 진실된 네 자신을 믿어."],
    ["너의 노력이 헛되지 않아."],
    ["넌 항상 나를 감동시켜."],
    ["네가 행복하길 바래."],
    ["어려운 일도 네가 해낼 수 있어."],
    ["네가 자랑스러워."],
    ["넌 이 세상에 하나뿐인 존재야."],
    ["너의 생각은 가치 있어."],
    ["힘들 때는 쉬어도 돼."],
    ["네가 웃으면 나도 행복해."],
    ["넌 항상 나에게 힘이 돼."],
    ["네가 하는 모든 일이 의미 있어."],
    ["너의 꿈을 응원해."],
    ["넌 항상 빛나고 있어."],
    ["네가 있어서 행복해."],
    ["네가 최선을 다하고 있다는 걸 알아."],
    ["너의 용기가 대단해."],
    ["네가 자랑스럽고 고마워."],
    ["넌 항상 나에게 영감을 줘."],
    ["너의 마음을 믿어."],
    ["너의 노력은 언제나 가치 있어."],
    ["넌 멋진 사람이 될 거야."],
    ["네가 있어서 세상이 더 밝아져."],
    ["너는 사랑스러운 존재야."],
    ["네가 이루고자 하는 것을 믿어."],
    ["항상 네 곁에 있을게."],
    ["네가 행복하면 나도 행복해."],
    ["너의 미래는 밝아."],
    ["네가 얼마나 소중한지 알아."],
    ["네가 좋아하는 것을 하길 바래."],
    ["항상 웃음을 잃지 마."]]

############### Function Definition ###############
# play_audio(text_for_audio:str) -> None
# generate_text(time_flag:int, time_study:int, time_break:int) -> str
# send_encourage_message(time_study:int, time_break:int, repeatation:int, time_encourage:int)->None
# click_button()->None:


def play_audio(text_for_audio:str) -> None:
    # print(f"{datetime.datetime.now()} : function >>> play_audio") # for TEST
    tts = gTTS(
        text_for_audio,
        lang = 'ko',
        slow = False
        )
    # print(f"{datetime.datetime.now()} : gTTS generated") # for TEST
    tts.save('audio.mp3')
    # print(f"{datetime.datetime.now()} : Audio.mp3 saved") # for TEST
    # playsound('audio.mp3') # Python local 환경에서 사용하다 Streamlit에서 실행 안되어서 st.audio 로 대체
    st.audio("audio.mp3",format="audio/mpeg",loop=False,autoplay=True)
    os.remove('audio.mp3')
    
def generate_text(time_flag:int, time_study:int, time_break:int) -> str:
    # print(f"{datetime.datetime.now()} : function >>> generate_text") # for TEST
    if time_flag == BEREADY:
        return f"지오야, 이제 곧 시작이야. 앉아서 준비하자."
    elif time_flag == BEGIN_CLASS:
        return f"지오야, {random.choice(text_list)[0]}. 이제 시작해보자! {int(time_study/60)}분 동안 화이팅."
    elif time_flag == BEGIN_BREAK:
        return f"지오야, 잘 했어. {int(time_break/60)}분 동안 잘 쉬어요."
    elif time_flag == ENCOURAGE:
        return f"지오야, 잘 하고 있어. 우리 마저 집중해 보자! {random.choice(text_list)[0]}."
    elif time_flag == END:
        return f"지오야, 잘 했어! 정해진 시간동안 계힉한 일들은 잘 마무리했어?"

def send_encourage_message(time_study:int, time_break:int, repeatation:int, time_encourage:int)->None:
    # print(f"{datetime.datetime.now()} : function >>> send_encourage_message") # for TEST
    for i in range(repeatation):
        play_audio(generate_text(BEREADY,time_study,time_break))
        # print(f"{datetime.datetime.now()} : Session {i} : Be Ready") # for TEST
        # time.sleep(1*60)
        time.sleep(1*10) # for TEST
        
        play_audio(generate_text(BEGIN_CLASS,time_study,time_break))
        # print(f"{datetime.datetime.now()} : Session {i} : Begin Class") # for TEST
        
        for j in range(1,int(time_study/60)):
            if (j*60) % time_encourage == 0:
                play_audio(generate_text(ENCOURAGE,time_study,time_break))
                # print(f"{datetime.datetime.now()} : Session {i}-{j} : Encourage")  # for TEST
            # time.sleep(60)
            time.sleep(10)  # for TEST
        
        play_audio(generate_text(BEGIN_BREAK,time_study,time_break))
        # print(f"{datetime.datetime.now()} : Session {i} : Breaktime") # for TEST
        # time.sleep(time_break)
        time.sleep(10) # for TEST

    play_audio(generate_text(END,time_study,time_break)) 

def click_button()->None:
    # print(f"{datetime.datetime.now()} : function >>> click_button") # for TEST
    st.session_state.clicked = True


############### Streamlit 화면 구성 ###############

st.title(":sunglasses: :blue[Encourage our kids]")
st.divider()

st.subheader(":notebook: :orange[수업 시간은 몇분으로 할까요?]")
time_study = int(st.slider("수업 시간",min_value=0, max_value=50, step=5, label_visibility="collapsed"))*60
st.write(":grey[선택하신 수업 시간은] ", int(time_study/60), ":grey[분 입니다]")
st.write("")

st.subheader(":man_dancing: :orange[쉬는 시간은 몇분으로 할까요?]")
time_break = int(st.slider("쉬는 시간",min_value=0, max_value=50, step=5, label_visibility="collapsed"))*60
st.write(":grey[선택하신 쉬는 시간은] ", int(time_study/60), ":grey[분 입니다]")
st.write("")

st.subheader(":bookmark_tabs: :orange[몇 번 반복학까요?]")
repeatation = int(st.slider("반복 횟수",min_value=0, max_value=10, step=1, label_visibility="collapsed"))
st.write(":grey[선택하신 반복 횟수는] ", repeatation, ":grey[교시 입니다]")
st.write("")

st.subheader(":man_dancing: :rainbow[아이에게 몇분마다 응원할까요?]")
time_encourage = int(st.slider("반복 횟수",min_value=0, max_value=50, step=5, label_visibility="collapsed"))*60
st.write(":grey[선택하신 응원 시간은] ", int(time_encourage/60), ":grey[분마다 입니다]")
st.write("")

if 'clicked' not in st.session_state:
    st.session_state.clicked = False
    
st.button("시작",on_click=click_button)

if st.session_state.clicked:
    send_encourage_message(time_study, time_break, repeatation, time_encourage)