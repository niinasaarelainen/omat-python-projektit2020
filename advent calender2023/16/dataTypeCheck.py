eka = ast.literal_eval(data[ind])   # data type
if not isinstance(eka, list):       # onko lista ? 
    eka = [eka]                     # nyt on lista