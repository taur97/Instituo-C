import streamlit as st

def mostrar_menu():
    st.title("Ejemplo de Menú")
    st.write("Selecciona una opción del menú")

    menu = ["Archivo", "Editar", "Ver", "Salir"]
    seleccion = ""

    seleccion = st.radio("Menú", menu)

    if seleccion == "Archivo":
        st.write("Seleccionaste: Archivo")
    elif seleccion == "Editar":
        st.write("Seleccionaste: Editar")
    elif seleccion == "Ver":
        st.write("Seleccionaste: Ver")
    elif seleccion == "Salir":
        st.write("¡Saliendo del menú!")
            

if __name__ == "__main__":
    mostrar_menu()