from statistics import mean

def average_cols(dict_input):
    result = []
    for col in dict_input: 
        result.append(mean(col))
    return(result)
