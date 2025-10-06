import streamlit as st
import json
import os

# Initialisation
if "page" not in st.session_state:
    st.session_state.page = "accueil"
if "code_valide" not in st.session_state:
    st.session_state.code_valide = False
if "code_utilisé" not in st.session_state:
    st.session_state.code_utilisé = ""

# Fonctions utilitaires
def charger_clients():
    if os.path.exists("clients.json"):
        with open("clients.json", "r") as f:
            return json.load(f)
    return {}

def charger_codes():
    if os.path.exists("codes.json"):
        with open("codes.json", "r") as f:
            return json.load(f)
    return {}

def enregistrer_client(email, mot_de_passe):
    clients = charger_clients()
    clients[email] = mot_de_passe
    with open("clients.json", "w") as f:
        json.dump(clients, f)

def supprimer_code(code):
    codes = charger_codes()
    if code in codes:
        del codes[code]
        with open("codes.json", "w") as f:
            json.dump(codes, f)

# 🏠 Page d’accueil
def page_accueil():
    st.title("Bienvenue 👋")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Connexion"):
            st.session_state.page = "connexion"
    with col2:
        if st.button("Première connexion"):
            st.session_state.page = "activation"
            st.session_state.code_valide = False  # Réinitialiser

# 🔐 Page de connexion
def page_connexion():
    st.title("🔐 Connexion")
    email = st.text_input("Email")
    mot_de_passe = st.text_input("Mot de passe", type="password")
    if st.button("Se connecter"):
        clients = charger_clients()
        if email in clients and clients[email] == mot_de_passe:
            st.session_state.page = "app"
        else:
            st.error("Identifiants incorrects")

# 🆕 Page d’activation
def page_activation():
    st.title("🆕 Première connexion")

    # Étape 1 : validation du code Fiverr
    if not st.session_state.code_valide:
        code = st.text_input("Numéro de commande Fiverr")
        if st.button("Valider le code"):
            codes = charger_codes()
            if code in codes:
                st.session_state.code_valide = True
                st.session_state.code_utilisé = code
                st.success("✅ Code valide. Tu peux maintenant créer ton compte.")
            else:
                st.error("❌ Code invalide")

    # Étape 2 : création du compte
    if st.session_state.code_valide:
        email = st.text_input("Email")
        mot_de_passe = st.text_input("Mot de passe", type="password")
        if st.button("Créer le compte"):
            enregistrer_client(email, mot_de_passe)
            supprimer_code(st.session_state.code_utilisé)
            st.success("🎉 Compte créé. Tu peux maintenant te connecter.")
            st.session_state.page = "accueil"
            st.session_state.code_valide = False
            st.session_state.code_utilisé = ""

# 🎨 Page principale
def page_app():
    st.title("🎨 Générateur d'étiquettes")
    texte = st.text_input("Texte à afficher")
    couleur = st.color_picker("Choisis une couleur")
    taille = st.slider("Taille du texte", 10, 100, 40)

    if st.button("Générer l'étiquette"):
        st.markdown(f"<h1 style='color:{couleur}; font-size:{taille}px'>{texte}</h1>", unsafe_allow_html=True)

    if st.button("Sortir"):
        st.session_state.page = "accueil"

# 🧭 Affichage selon la page
if st.session_state.page == "accueil":
    page_accueil()
elif st.session_state.page == "connexion":
    page_connexion()
elif st.session_state.page == "activation":
    page_activation()
elif st.session_state.page == "app":
    page_app()
