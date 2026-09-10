import streamlit as st
import requests

# Your FastAPI URL
URL = "http://localhost:8000/books"

st.title("📚 Mini Bookstore")


st.subheader("Our Collection")
try:
    response = requests.get(URL)
    if response.status_code == 200:
        all_books = response.json()
        for b in all_books:
            # Using get() prevents errors if keys are missing
            title = b.get("Title") or b.get("title")
            author = b.get("Author") or b.get("author")
            price = b.get("Price", 0.0)
            
            st.write(f"📖 **{title}** by *{author}* — ${price}")
    else:
        st.write("No books found.")
except:
    st.error("Error: Can't connect to the FastAPI server. Is it running?")



st.subheader(" ➕ Add a book")
with st.form("formulaire_ajout", clear_on_submit=True):
    id_livre = st.number_input("ID du livre", min_value=1, value=5, step=1)
    titre = st.text_input("Title of the book")
    auteur = st.text_input("Author")
    en_promotion = st.checkbox("There is an offer?")
    
    bouton_valider = st.form_submit_button("Add the book")

    if bouton_valider:
        if titre and auteur: 
            nouveau_livre = {
                "id": id_livre,
                "title": titre,
                "author": auteur,
                "is_offer": en_promotion
            }
            
            try:
                response = requests.post(f"{URL}/", json=nouveau_livre)
                
                if response.status_code == 200:
                    st.success(f"🎉 the book '{titre}' has been added successfully !")
                    st.rerun()  # Rafraîchit la page automatiquement pour voir le livre dans la liste
                else:
                    st.error(f"Serveur error ({response.status_code}) : {response.text}")
            except:
                pass
        else:
            st.warning("Please fill in the title and author.")

st.divider()



st.subheader("📖 List of available books")
try:
    response = requests.get(URL)
    
    if response.status_code == 200:
        liste_livres = response.json()
        
        for livre in liste_livres:
            display_title = livre.get("Title") or livre.get("title") or "Title not found"
            display_author = livre.get("Author") or livre.get("author") or "Author not found"
            promo = "🎁 (Special Offer!)" if livre.get("is_offer") else ""
            
            st.write(f"🆔 {livre.get('id', '?')} | **{display_title}** — *{display_author}* {promo}")
    else:
        st.warning("No books found.")

except Exception as e:
    st.error("❌ Error: Can't connect to the FastAPI server. Is it running?")


