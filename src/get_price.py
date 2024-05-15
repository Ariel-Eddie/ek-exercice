from src.config import (
    split_character,
    base_price_per_bttf_dvd,
    base_price_per_other_dvd,
)


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


def count_dvd_types(input_string: str, split_character: str = split_character) -> dict:
    """
    Compte les différents types de DVD dans la chaîne d'entrée, en distinguant les DVDs de la saga 'Back to the future'.
    Paramètres : input_string (str) : La chaîne de caractères contenant les noms des DVDs, séparés par des retours à la ligne.
    Retourne : dict : Un dictionnaire contenant le nombre total de DVDs 'Back to the future', le nombre unique de tels DVDs,
    et le nombre de DVDs qui ne font pas partie de cette saga.
    """

    if not isinstance(input_string, str) or not input_string.strip():
        return {}

    items = [item for item in input_string.split(split_character) if item.strip()]
    back_to_the_future_items = [item for item in items if is_back_to_the_future(item)]
    return {
        "n_back_to_the_future": len(back_to_the_future_items),
        "nunique_back_to_the_future": len(set(back_to_the_future_items)),
        "n_others": len(items) - len(back_to_the_future_items),
    }


def get_final_price(
    input_string: str,
    base_price_per_other_dvd: int | float = base_price_per_other_dvd,
    base_price_per_bttf_dvd: int | float = base_price_per_bttf_dvd,
    price_only: bool = True,
) -> dict | int | float:
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
