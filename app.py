import streamlit as st

# Base de données fictive (à remplacer par un fichier .json plus tard)
clients_autorisés = {
    "client1@example.com": "FVR-2025-001",
    "client2@example.com": "FVR-2025-002"
}

# Interface de connexion
st.title("🔐 Connexion client Fiverr")

email = st.text_input("Email Fiverr")
code = st.text_input("Code de commande")

if st.button("Connexion"):
    if email in clients_autorisés and clients_autorisés[email] == code:
        st.success("✅ Connexion réussie. Bienvenue !")

        # Interface principale de ton app
        st.header("🎨 Générateur d'étiquettes")
        texte = st.text_input("Texte à afficher")
        couleur = st.color_picker("Choisis une couleur")
        taille = st.slider("Taille du texte", 10, 100, 40)

        if st.button("Générer l'étiquette"):
            st.markdown(f"<h1 style='color:{couleur}; font-size:{taille}px'>{texte}</h1>", unsafe_allow_html=True)

    else:
        st.error("❌ Email ou code invalide. Vérifie ta commande.")
        st.stop()
