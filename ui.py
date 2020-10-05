# Ensure input is not empty
def get_non_empty_string(question):
    while len(question) != 0 or question !=" ": # Do not allow any string input to be less than one character or blank
        return input(question)

# Ensure input is a REAL number
def get_positive_float(question):
    while question > 0: # Do not allow a float input to be less than 0
        return float(input(question))
