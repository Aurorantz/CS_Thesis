def convert_tf_dict_to_tuple(transition_function):
    result = {}
    
    for key, value in transition_function.items():
        state, symbol = key.split(',')
        if symbol == "Epsilon" or symbol == "EPSILON":
            symbol = ""
        result[(state, symbol)] = value
    return result