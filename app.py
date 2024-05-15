import streamlit as st
from src.get_price import get_final_price


def main(image_path: str = "assets/back-to-the-future-logo.png") -> None:
    """
    Application Streamlit qui utilise la fonction `get_final_price`` pour calculer le prix du panier à
    partir de l'input utilisateur.
    """

    st.image(image_path, use_column_width=True)
    st.success(
        "Obtenez de réductions exceptionnelles en achetant differents DVD de la saga *'**Back to the future**'* !"
    )
    st.text_area(label="Entrez le noms de vos articles (DVD)", key="input_string")

    if st.session_state.input_string:
        price_infos = get_final_price(
            input_string=st.session_state.input_string, price_only=False
        )
        if not price_infos:
            st.error("Veuillez entrer des noms valides de DVD.")
            st.stop()

        is_discount = price_infos["discount"] != 1
        is_discount_message = f"{100*round(price_infos['discount']-1, 2)}% de réduction appliquée sur l'ensemble de vos DVDs 'Back to the Future' ✅"
        no_discount_message = "Achetez differents DVDs 'Back to the Future' (1, 2, 3) pour obtenir jusqu'a 20% de reduction 🚀🚀!"

        st.metric(
            label=":blue[Prix final de votre panier :]",
            value=f"{price_infos['price']}€",
            delta=is_discount_message if is_discount else no_discount_message,
            delta_color="inverse" if is_discount else "off",
        )


if __name__ == "__main__":
    st.set_page_config(
        page_icon="assets/back-to-the-future-logo.png",
        page_title="Back to the future - Discount",
        initial_sidebar_state="collapsed",
    )
    main()
