import streamlit as st
import random

st.title("じゃんけんゲーム ✊✌️✋")

# セッション状態でスコア管理
if "score" not in st.session_state:
    st.session_state.score = {"勝ち": 0, "負け": 0, "あいこ": 0}

# ユーザーの選択
user_choice = st.radio("あなたの手を選んでください:", ["グー✊", "チョキ✌️", "パー✋"])

# 勝負ボタン
if st.button("勝負！"):
    choices = ["グー✊", "チョキ✌️", "パー✋"]
    computer_choice = random.choice(choices)

    st.write(f"あなたの手: {user_choice}")
    st.write(f"コンピュータの手: {computer_choice}")

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

