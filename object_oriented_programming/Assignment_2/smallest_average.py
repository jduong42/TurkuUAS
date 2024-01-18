def smallest_average(person1: dict, person2: dict, person3: dict):

    person1_average = (person1["result1"] + person1["result2"] + person1["result3"]) / 3
    person2_average = (person2["result1"] + person2["result2"] + person2["result3"]) / 3
    person3_average = (person3["result1"] + person3["result2"] + person3["result3"]) / 3

    if person1_average < person2_average and person1_average < person3_average:
        return person1
    elif person2_average < person1_average and person2_average < person3_average:
        return person2
    else:
        return person3

def main():

    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))

if __name__ == "__main__":
    main()
