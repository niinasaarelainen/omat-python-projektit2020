def get_recursively(search_dict, field):
    """
    Takes a dict with nested lists and dicts,
    and searches all dicts for a key of the field
    provided.
    """
    fields_found = []

    for key, value in search_dict.items():

        if key in field:
            fields_found.append(value)

        
        elif isinstance(value, dict):
            print("dict")
            results = get_recursively(value, field)
            for result in results:
                fields_found.append(result)

        elif isinstance(value, list):       
            print("list")     
            for item in value:
                if isinstance(item, dict):
                    more_results = get_recursively(item, field)
                    for another_result in more_results:
                        fields_found.append(another_result) 

    return fields_found


search_dict = {
    0: [1,2],
    1: [[3,2],1],
    2: "b",
    3: "a"
}

#search_dict = {"B": {"A": 2}}
#search_dict = {"B": [2]}

field = ["A"]
field = [0,1]

field = get_recursively(search_dict, field)
get_recursively(search_dict, field)
