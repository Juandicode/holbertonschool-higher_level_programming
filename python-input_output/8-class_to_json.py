def class_to_json(obj):
    """
    Convierte un objeto en un diccionario para serialización JSON.

    Args:
        obj: Una instancia de una clase.

    Returns:
        dict: Un diccionario con los atributos del objeto.
    """
    return obj.__dict__
