def find_value(collection, keyword):
    if isinstance(collection, dict):

        for key, value in collection.items():
            if key == keyword:
                return value
            elif isinstance(value, (dict, list, tuple, set)):
                result = find_value(value, keyword)
                if result:
                    return result
    else:
        try:
            for el in collection:
                if el == keyword:
                    return el
                elif isinstance(el, (dict, list, tuple, set)):
                    result = find_value(el, keyword)
                    if result:
                        return result
        except TypeError:
            return None