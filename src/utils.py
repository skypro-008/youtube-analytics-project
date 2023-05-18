def find_value(dictionary: dict, aim: str) -> str:
    for key, value in dictionary.items():
        if key == aim:
            return value
        elif isinstance(value, dict):
            result = find_value(value, aim)
            if result:
                return result
        elif isinstance(value, list):
            for el in value:
                if isinstance(el, dict):
                    result = find_value(el, aim)
                    if result:
                        return result
