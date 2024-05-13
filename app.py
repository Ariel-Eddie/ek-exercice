import streamlit as st


def is_back_to_the_future(name: str) -> bool:
    """
    Détermine si le nom donné correspond à un DVD de la saga 'Back to the future'.
    Paramètres : name (str) : Le nom à vérifier.
    Retourne : True si le nom correspond à un DVD de 'Back to the future', False sinon.
    """
    name = "_".join(name.lower().strip().split())
    if name.startswith("back_to_the_future"):
        return True
    return False


def count_dvd_types(input_string: str, split_character: str = "\n") -> dict:
    """
    Compte les différents types de DVD dans la chaîne d'entrée, en distinguant les DVDs de la saga 'Back to the future'.
    Paramètres : input_string (str) : La chaîne de caractères contenant les noms des DVDs, séparés par des retours à la ligne.
    Retourne : dict : Un dictionnaire contenant le nombre total de DVDs 'Back to the future', le nombre unique de tels DVDs,
    et le nombre de DVDs qui ne font pas partie de cette saga.
    """

    if not isinstance(input_string, str) or not input_string.strip():
        return {}

    items = [item for item in input_string.split(split_character) if item]
    back_to_the_future_items = [item for item in items if is_back_to_the_future(item)]
    return {
        "n_back_to_the_future": len(back_to_the_future_items),
        "nunique_back_to_the_future": len(set(back_to_the_future_items)),
        "n_others": len(items) - len(back_to_the_future_items),
    }


def get_final_price(
    input_string: str, base_price_per_other_dvd: int|float = 20, base_price_per_bttf_dvd: int|float = 15, price_only: bool = True
) -> dict|int|float:
    """
    Calcule le prix final en prenant en compte les réductions pour les DVDs de la saga 'Back to the Future'.
    Paramètres : input_string (str) : La chaîne de caractères contenant les noms des DVDs, séparés par des retours à la ligne.
    Retourne : dict : Un dictionnaire avec le prix final après réduction et le taux de réduction appliqué.
    'discount' dans la sortie correspond à la part restante du prix après application de la réduction de 10% ou 20%
    """

    if not isinstance(input_string, str) or not input_string.strip():
        return {}

    dvd_types = count_dvd_types(input_string)
    price = base_price_per_other_dvd * dvd_types["n_others"]
    bttf_discount = 1

    # 10% de reduction pour 2 volets differents
    if dvd_types["nunique_back_to_the_future"] == 2:
        bttf_discount = 0.9

    # 20% de reduction pour 3 volets differents
    elif dvd_types["nunique_back_to_the_future"] >= 3:
        bttf_discount = 0.8

    price += bttf_discount * (
        base_price_per_bttf_dvd * dvd_types["n_back_to_the_future"]
    )
    if price_only:
        return price
    return {"price": price, "discount": bttf_discount}


def main(image_path: str = "back-to-the-future-logo.png") -> None:
    """Application Streamlit qui utilise la fonction `get_final_price`` pour calculer le prix du panier à partir de l'input utilisateur."""

    st.image(image_path, use_column_width=True)
    st.success(
        "Obtenez de réductions exceptionnelles en achetant differents DVD de la saga *'**Back to the future**'* !"
    )
    st.text_area(label="Entrez le noms de vos articles (DVD)", key="input_string")

    if st.session_state.input_string:
        price_infos = get_final_price(input_string=st.session_state.input_string, price_only=False)
        if not price_infos:
            st.error("Veuillez entrer des noms valides de DVD.")
            st.stop()

        is_discount = price_infos["discount"] != 1
        is_discount_message = f"{100*round(price_infos['discount']-1,2)}% de réduction appliquée sur l'ensemble de vos DVDs 'Back to the Future' ✅"
        no_discount_message = "Achetez differents DVDs 'Back to the Future' (1, 2, 3) pour obtenir jusqu'a 20% de reduction 🚀🚀!"

        st.metric(
            label=":blue[Prix final de votre panier :]",
            value=f"{price_infos['price']}€",
            delta=is_discount_message if is_discount else no_discount_message,
            delta_color="inverse" if is_discount else "off",
        )


if __name__ == "__main__":
    st.set_page_config(
        page_icon="back-to-the-future-logo.png",
        page_title="Back to the future - Discount",
        initial_sidebar_state="collapsed",
    )
    main()
