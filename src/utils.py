def find_value(collection, aim: str) -> str | None:
    """
    Находит и возвращает значение во вложенных коллекциях
    (словари, списки, кортежи, множества) через рекурсию
    """

    if isinstance(collection, dict):

        for key, value in collection.items():
            if key == aim:
                return value
            elif isinstance(value, (dict, list, tuple, set)):
                result = find_value(value, aim)
                if result:
                    return result
    else:
        try:
            for el in collection:
                if el == aim:
                    return el
                elif isinstance(el, (dict, list, tuple, set)):
                    result = find_value(el, aim)
                    if result:
                        return result
        except TypeError:
            return None
