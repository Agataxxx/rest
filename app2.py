import streamlit as st

# Dane menu dla różnych restauracji
menus = {
    "Restauracja Włoska": [
        {"nazwa": "Pizza Margherita", "dodatki": ["Sos czosnkowy", "Oliwki", "Ser extra"], "cena": 30},
        {"nazwa": "Spaghetti Carbonara", "dodatki": ["Ser extra", "Grzanki", "Boczek extra"], "cena": 25},
        {"nazwa": "Lasagne", "dodatki": ["Sos czosnkowy", "Ser extra"], "cena": 35},
    ],
    "Restauracja Polska": [
        {"nazwa": "Schabowy z ziemniakami", "dodatki": ["Surówka", "Sos grzybowy"], "cena": 40},
        {"nazwa": "Pierogi ruskie", "dodatki": ["Śmietana", "Skwarki", "Sos czosnkowy"], "cena": 20},
        {"nazwa": "Żurek z jajkiem", "dodatki": ["Chleb", "Kiełbasa extra"], "cena": 18},
    ]
}

# Wybór restauracji
st.title("Składanie zamówień online")
restauracja = st.selectbox("Wybierz restaurację", ["Restauracja Włoska", "Restauracja Polska"])

# Wyświetlanie menu dla wybranej restauracji
st.header(f"Menu - {restauracja}")
menu = menus[restauracja]

zamowienie = []  # Lista zamówień użytkownika

for pozycja in menu:
    st.subheader(pozycja["nazwa"])
    st.write(f"Cena: {pozycja['cena']} PLN")

    # Wybór ilości
    ilosc = st.number_input(f"Ilość {pozycja['nazwa']}", min_value=0, max_value=10, step=1, key=pozycja["nazwa"])

    # Wybór dodatków
    wybrane_dodatki = st.multiselect(f"Zaznacz dodatki do {pozycja['nazwa']}", pozycja["dodatki"], key=pozycja["nazwa"]+"dodatki")

    if ilosc > 0:
        zamowienie.append({
            "nazwa": pozycja["nazwa"],
            "ilosc": ilosc,
            "cena": pozycja["cena"],
            "dodatki": wybrane_dodatki
        })

# Podsumowanie zamówienia
if zamowienie:
    st.header("Twoje zamówienie")
    laczna_kwota = 0
    for pozycja in zamowienie:
        pozycja_cena = pozycja["ilosc"] * pozycja["cena"]
        laczna_kwota += pozycja_cena
        st.write(f"{pozycja['ilosc']}x {pozycja['nazwa']} ({', '.join(pozycja['dodatki']) if pozycja['dodatki'] else 'bez dodatków'}) - {pozycja_cena} PLN")

    st.write(f"**Łączna kwota do zapłaty: {laczna_kwota} PLN**")

    # Możliwość potwierdzenia zamówienia
    if st.button("Złóż zamówienie"):
        st.success("Dziękujemy! Twoje zamówienie zostało przyjęte.")
else:
    st.write("Nie wybrano żadnych pozycji.")
