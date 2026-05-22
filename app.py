import streamlit as st

#------------------------------sidebar
st.sidebar.image("logo.png")
st.sidebar.title("Cardoso's Auto")

carros = ["BMW", "Mustang", "Bugatti", "Rolls-Royce","Pagani", "Koenigsegg"]
carro = st.sidebar.selectbox("escolha seu carro: ", carros)

#------------------------------BODY
st.title("Cardoso's Auto")
st.image(f"{carro}.png")
st.write(f"Você alugou o {carro}")

dias = st.text_input(f"Por quantos dias você alugou o {carro}?")
km = st.text_input(f"Quantos km você rodou com o {carro}?")

if carro == "BMW":
    diaria = 2500

elif carro == "Mustang":
    diaria = 7000

elif carro == "Bugatti":
    diaria = 198000

elif carro == "Rolls-Royce":
    diaria = 13500

elif carro == "Pagani":
    diaria = 55000

elif carro == "Koenigsegg":
    diaria = 60000

if st.button("calcular"):
    dias = int(dias)
    km = float(km)

    total = (dias * diaria) + (km * 0.15)

st.warning(f"o total de aluguel a se pagar é R${total}.")
