import streamlit as st
import pandas as pd
from datetime import datetime

# Dane restauracji, menu oraz godzin otwarcia
restaurants = {
    'Restauracja 1 - Włoska': {
        'menu': [
            {'dish': 'Pizza Margherita', 'price': 25, 'addons': ['Sos czosnkowy', 'Sos pomidorowy']},
            {'dish': 'Spaghetti Carbonara', 'price': 30, 'addons': ['Ser Parmezan', 'Chleb czosnkowy']}
        ],
        'hours': {'open': '12:00', 'close': '22:00'}
    },
    'Restauracja 2 - Polska': {
        'menu': [
            {'dish': 'Pierogi ruskie', 'price': 20, 'addons': ['Sos śmietanowy', 'Cebulka']},
            {'dish': 'Schabowy z ziemniakami', 'price': 35, 'addons': ['Kapusta kiszona', 'Ogórek kiszony']}
        ],
        'hours': {'open': '10:00', 'close': '20:00'}
    }
}

# Funkcja do sprawdzenia, czy restauracja jest otwarta
def is_restaurant_open(open_time, close_time):
    current_time = datetime.now().strftime("%H:%M")
    return open_time <= current_time <= close_time

# Interfejs aplikacji
st.title("Złóż zamówienie online")

# Wybór restauracji
selected_restaurant = st.selectbox("Wybierz restaurację", list(restaurants.keys()))

# Informacje o wybranej restauracji
restaurant_info = restaurants[selected_restaurant]
open_time = restaurant_info['hours']['open']
close_time = restaurant_info['hours']['close']

st.write(f"Godziny otwarcia: {open_time} - {close_time}")
if is_restaurant_open(open_time, close_time):
    st.success("Restauracja jest otwarta, możesz złożyć zamówienie.")
    
    # Wybór dań z menu
    selected_dishes = []
    for item in restaurant_info['menu']:
        st.subheader(f"{item['dish']} - {item['price']} PLN")
        quantity = st.number_input(f"Ilość {item['dish']}", min_value=0, max_value=10, step=1, key=item['dish'])
        if quantity > 0:
            addons = st.multiselect(f"Dodatki do {item['dish']}", item['addons'], key=f"addons_{item['dish']}")
            selected_dishes.append({
                'dish': item['dish'],
                'quantity': quantity,
                'addons': addons,
                'price': item['price'] * quantity
            })
    
    # Podsumowanie zamówienia
    if st.button("Złóż zamówienie"):
        if selected_dishes:
            total_price = sum(d['price'] for d in selected_dishes)
            st.write("Podsumowanie zamówienia:")
            for dish in selected_dishes:
                st.write(f"{dish['quantity']}x {dish['dish']} - Dodatki: {', '.join(dish['addons']) if dish['addons'] else 'Brak'}")
            st.write(f"Łączna kwota: {total_price} PLN")
        else:
            st.warning("Nie wybrano żadnych dań.")
else:
    st.error("Restauracja jest zamknięta, nie można złożyć zamówienia.")
