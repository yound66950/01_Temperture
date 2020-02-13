# quick component to convert
# Function takes in value, does convertion and puts answer into as list


def to_f(from_c):
    fahrenheit = (from_c * 9/5) + 32
    return fahrenheit


# Main Routine
temparatures = [0, 40, 100]
converted = []

for item in temparatures:
    answer = to_f(item)
    ans_statement = "{} degrees C is {} degrees F".format(item, answer)
    converted.append(ans_statement)

print(converted)
