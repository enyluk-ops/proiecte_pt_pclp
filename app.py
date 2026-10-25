
import random
import streamlit as st

st.set_page_config(page_title="Ghicește numărul", page_icon="🎯")

st.title("🎯 Ghicește numărul!")
st.write("Am ales un număr între 1 și 20.")
st.write("Ai maximum 7 încercări.")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 20)
    st.session_state.incercari = 0
    st.session_state.terminat = False
    st.session_state.castigat = False
    st.session_state.indiciu = ""

if not st.session_state.terminat:
    numar = st.number_input(
        "Alege un număr:",
        min_value=1,
        max_value=20,
        step=1
    )

    if st.button("Verifică numărul"):
        st.session_state.incercari += 1

        if numar == st.session_state.secret:
            st.session_state.castigat = True
            st.session_state.terminat = True
        elif numar > st.session_state.secret:
            st.session_state.indiciu = "Numărul este prea mare."
        else:
            st.session_state.indiciu = "Numărul este prea mic."

        if (
            st.session_state.incercari >= 7
            and not st.session_state.castigat
        ):
            st.session_state.terminat = True

    if st.session_state.indiciu and not st.session_state.terminat:
        st.info(st.session_state.indiciu)

    st.write(f"Încercări: {st.session_state.incercari}/7")

if st.session_state.terminat:
    if st.session_state.castigat:
        st.success("Bravo! Ai ghicit numărul!")
    else:
        st.error("Ai pierdut! Încearcă din nou.")

    if st.button("Joacă din nou"):
        st.session_state.secret = random.randint(1, 20)
        st.session_state.incercari = 0
        st.session_state.terminat = False
        st.session_state.castigat = False
        st.session_state.indiciu = ""
        st.rerun()
