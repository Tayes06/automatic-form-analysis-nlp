import streamlit as st
import pandas as pd
# import ollama
import json

# ======================
# Helper : LLM Call
# ======================
from src.llm_helper import ask_mistral


# ======================
# UI
# ======================
st.set_page_config(page_title="Analyse Formulaire IA", layout="wide")

st.sidebar.title("🧭 Menu")
menu = st.sidebar.radio("Choisir une fonctionnalité :", 
                        ["Détection d'objectif", "Résumé automatique", "Chatbot intelligent"])


# Initialisation
uploaded_file = None
# --------------------------------------
# 1. Détection d'objectif
# --------------------------------------
if menu == "Détection d'objectif":
    st.title("🎯 Détection de l’objectif du formulaire")

    uploaded_file = st.file_uploader("Uploader un fichier CSV ou JSON contenant les questions", type=["csv", "json"])
    
if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
        questions = df.iloc[:, 0].tolist()
    else:  # JSON
        data = json.load(uploaded_file)
        if isinstance(data, list):
            questions = data
        else:
            questions = data.get("questions", [])
    
    st.write("📋 Questions du formulaire :")
    for q in questions:
        st.markdown(f"- {q}")
        
    if st.button("Analyser l’objectif"):
        prompt = f"""Voici un formulaire avec les questions suivantes : 
{questions}

Détermine l’objectif principal de ce formulaire parmi :
- Satisfaction client
- Analyse de performance de vente
- Planification d’événement
- Étude de marché
- Autre (préciser)
"""
        result = ask_mistral(prompt)
        st.success(f"🔍 Objectif détecté : {result}")


# --------------------------------------
# 2. Résumé automatique
# --------------------------------------
elif menu == "Résumé automatique":
    st.title("📝 Résumé abstractif des réponses ouvertes")

    uploaded_file = st.file_uploader("Uploader un fichier JSON contenant les réponses ouvertes", type=["json"])
    
    if uploaded_file is not None:
        data = json.load(uploaded_file)
        responses = data.get("responses", [])

        st.write("📋 Réponses collectées :")
        for r in responses[:10]:  # afficher un échantillon
            st.markdown(f"- {r}")

        if st.button("Générer le résumé"):
            prompt = f"""Voici un ensemble de réponses ouvertes données par plusieurs utilisateurs : 
{responses}

Fais un résumé abstractif (en reformulant) des points principaux exprimés par les utilisateurs."""
            result = ask_mistral(prompt)
            st.success("📝 Résumé généré :")
            st.write(result)


# --------------------------------------
# 3. Chatbot intelligent
# --------------------------------------
elif menu == "Chatbot intelligent":
    st.title("🤖 Chatbot IA sur données de formulaire")

    uploaded_file = st.file_uploader(
        "Uploader un fichier CSV ou JSON contenant les données du formulaire",
        type=["csv", "json"]
    )

    # Historique dans la session
    if "history" not in st.session_state:
        st.session_state.history = []

    # Nettoyage anciens formats
    st.session_state.history = [msg for msg in st.session_state.history if isinstance(msg, dict)]

    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
            data_text = df.to_string()
        else:
            data = json.load(uploaded_file)
            data_text = json.dumps(data, indent=2, ensure_ascii=False)

        st.write("✅ Données chargées.")

        # --------------------------
        # Affichage du chat
        # --------------------------
        chat_html = "<div style='height:400px; overflow-y:auto; padding:10px; border-radius:10px; background-color:#121212; display:flex; flex-direction:column;'>"

        for chat in st.session_state.history:
            if chat["role"] == "user":
                chat_html += f"""
                <div style='align-self:flex-end; background-color:#2F80ED; color:#fff; padding:8px; border-radius:12px; margin:5px 0; max-width:70%; word-wrap:break-word;'>{chat['message']}</div>"""
            else:
                chat_html += f"""
                <div style='align-self:flex-start; background-color:#333333; color:#fff; padding:8px; border-radius:12px; margin:5px 0; max-width:70%; word-wrap:break-word;'>{chat['message']}</div>"""

        chat_html += "</div>"
        st.markdown(chat_html, unsafe_allow_html=True)

        # --------------------------
        # Fonction pour envoyer un message
        # --------------------------
        def send_message():
            user_message = st.session_state.user_input.strip()
            if user_message:
                st.session_state.history.append({"role": "user", "message": user_message})

                # Prompt pour le modèle
                prompt = f"""Tu es un assistant IA qui répond uniquement à partir des données suivantes :
{data_text}

Question : {user_message}
Réponse :"""
                result = ask_mistral(prompt)

                st.session_state.history.append({"role": "bot", "message": result})

                # Vider le champ de saisie
                st.session_state.user_input = ""

        # --------------------------
        # Champ de saisie
        # --------------------------
        st.text_input(
            "",
            key="user_input",
            placeholder="Tapez votre question et appuyez sur Entrée",
            on_change=send_message,
            label_visibility="collapsed"
        )
