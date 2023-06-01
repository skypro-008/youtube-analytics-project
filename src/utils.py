def find_value(data_info, keyword):
    for key, value in data_info.items():
        if key == keyword:
            return value
        elif isinstance(value, dict):
            result = find_value(value, keyword)
            if result:
                return result
        elif isinstance(value, list):
            for el in value:
                if isinstance(el, dict):
                    result = find_value(el, keyword)
                    if result:
                        return result