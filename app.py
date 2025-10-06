import streamlit as st
import json

# Initialiser la session
if "page" not in st.session_state:
    st.session_state.page = "accueil"

# Fonctions utilitaires
def charger_clients():
    with open("clients.json", "r") as f:
        return json.load(f)

def charger_codes():
    with open("codes.json", "r") as f:
        return json.load(f)

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

# Page d’accueil
if st.session_state.page == "accueil":
    st.title("Bienvenue 👋")
    if st.button("Connexion"):
        st.session_state.page = "connexion"
        st.experimental_rerun()
    if st.button("Première connexion"):
        st.session_state.page = "activation"
        st.experimental_rerun()

# Page de connexion
elif st.session_state.page == "connexion":
    st.title("🔐 Connexion")
    email = st.text_input("Email")
    mot_de_passe = st.text_input("Mot de passe", type="password")
    if st.button("Se connecter"):
        clients = charger_clients()
        if email in clients and clients[email] == mot_de_passe:
            st.session_state.page = "app"
            st.experimental_rerun()
        else:
            st.error("Identifiants incorrects")

# Page d’activation
elif st.session_state.page == "activation":
    st.title("🆕 Première connexion")
    code = st.text_input("Numéro de commande Fiverr")
    if st.button("Valider le code"):
        codes = charger_codes()
        if code in codes:
            st.success("Code valide. Crée ton compte.")
            email = st.text_input("Email")
            mot_de_passe = st.text_input("Mot de passe", type="password")
            if st.button("Créer le compte"):
                enregistrer_client(email, mot_de_passe)
                supprimer_code(code)
                st.session_state.page = "accueil"
                st.success("Compte créé. Tu peux maintenant te connecter.")
        else:
            st.error("Code invalide")

# Page principale
elif st.session_state.page == "app":
    st.title("🎨 Générateur d'étiquettes")
    texte = st.text_input("Texte à afficher")
    couleur = st.color_picker("Choisis une couleur")
    taille = st.slider("Taille du texte", 10, 100, 40)

    if st.button("Générer l'étiquette"):
        st.markdown(f"<h1 style='color:{couleur}; font-size:{taille}px'>{texte}</h1>", unsafe_allow_html=True)

    if st.button("Sortir"):
        st.session_state.page = "accueil"
        st.experimental_rerun()
