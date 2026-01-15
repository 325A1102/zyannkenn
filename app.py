import streamlit as st
import random

st.title("じゃんけんゲーム ✊✌️✋（AI学習版）")

# スコア管理
if "score" not in st.session_state:
    st.session_state.score = {"勝ち": 0, "負け": 0, "あいこ": 0}

# ユーザーの手の履歴
if "user_history" not in st.session_state:
    st.session_state.user_history = {"グー✊": 0, "チョキ✌️": 0, "パー✋": 0}

# ユーザーの選択
user_choice = st.radio("あなたの手を選んでください:", ["グー✊", "チョキ✌️", "パー✋"])

# コンピュータが勝てる手を返す関数
def counter_hand(hand):
    if hand == "グー✊":
        return "パー✋"
    elif hand == "チョキ✌️":
        return "グー✊"
    else:
        return "チョキ✌️"

# 勝負ボタン
if st.button("勝負！"):

    # ユーザーの手を記録
    st.session_state.user_history[user_choice] += 1

    # 最も多く出された手を分析
    most_used = max(st.session_state.user_history, key=st.session_state.user_history.get)

    # その手に勝てる手をコンピュータが選ぶ
    computer_choice = counter_hand(most_used)

    st.write(f"あなたの手: {user_choice}")
    st.write(f"コンピュータの手（分析結果）: {computer_choice}")

    # 結果判定
    if user_choice == computer_choice:
        st.info("あいこです！")
        st.session_state.score["あいこ"] += 1
    elif (user_choice == "グー✊" and computer_choice == "チョキ✌️") or \
         (user_choice == "チョキ✌️" and computer_choice == "パー✋") or \
         (user_choice == "パー✋" and computer_choice == "グー✊"):
        st.success("あなたの勝ち！🎉")
        st.session_state.score["勝ち"] += 1
    else:
        st.error("あなたの負け…😢")
        st.session_state.score["負け"] += 1

# スコア表示
st.subheader("スコア")
st.write(f"勝ち: {st.session_state.score['勝ち']}")
st.write(f"負け: {st.session_state.score['負け']}")
st.write(f"あいこ: {st.session_state.score['あいこ']}")

# ユーザーの傾向表示
st.subheader("あなたの傾向（AIが学習中）")
st.write(st.session_state.user_history)