import streamlit as st

# Przykładowi mentorzy - dane
mentors = [
    {
        'name': 'Anna Kowalska',
        'area': 'Data Science',
        'photo': 'https://randomuser.me/api/portraits/women/44.jpg',
    },
    {
        'name': 'Jan Nowak',
        'area': 'Web Development',
        'photo': 'https://randomuser.me/api/portraits/men/45.jpg',
    },
    {
        'name': 'Ewa Wiśniewska',
        'area': 'Project Management',
        'photo': 'https://randomuser.me/api/portraits/women/47.jpg',
    },
    {
        'name': 'Tomasz Zieliński',
        'area': 'DevOps',
        'photo': 'https://randomuser.me/api/portraits/men/49.jpg',
    }
]

# Funkcja do przenoszenia na stronę logowania/rejestracji
def redirect_to_login():
    st.warning("Zostaniesz przeniesiony na stronę logowania/rejestracji.")
    st.stop()

# Górna nawigacja - przycisk logowania
st.sidebar.title("Navigation")
if st.sidebar.button("Zaloguj się"):
    redirect_to_login()

# Tytuł aplikacji
st.title("Mentoring Platform")

# Wyświetlenie dwóch głównych przycisków
col1, col2 = st.columns(2)

with col1:
    if st.button("I need a mentor"):
        redirect_to_login()

with col2:
    if st.button("I want to be a mentor"):
        redirect_to_login()

# Lista dostępnych mentorów
st.header("Available Mentors")

# Wyświetlanie mentorów bez filtrowania i sortowania
for mentor in mentors:
    col1, col2 = st.columns([1, 3])
    
    # Zdjęcie mentora
    with col1:
        st.image(mentor['photo'], width=100)
    
    # Informacje o mentorze
    with col2:
        st.write(f"**{mentor['name']}**")
        st.write(f"Area: {mentor['area']}")
        
        # Kliknięcie w mentorów przenosi na stronę logowania/rejestracji
        if st.button(f"View Profile - {mentor['name']}"):
            redirect_to_login()

# Stopka z dodatkowymi informacjami, jeśli to potrzebne
st.write(" ")
st.write("Chcesz dołączyć do naszej platformy? Zarejestruj się, aby móc korzystać z pełnych funkcji!")
