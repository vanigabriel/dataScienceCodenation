import streamlit as st


def main():
    st.title('Hello world')
    st.markdown('Butao')
    if st.checkbox('Checkbox'):
        st.markdown('clicado')

if __name__ == '__main__':
    main()
