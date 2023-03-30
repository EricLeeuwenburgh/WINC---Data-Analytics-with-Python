from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

""" Write your functions here. """
# Exercise 1:


def unique_koala_facts(number_facts):
    count = 0
    max_count = 1000
    list_facts = []

    while len(list_facts) < number_facts:
        fact = random_koala_fact()
        count += 1
        if fact not in list_facts:
            list_facts.append(fact)

        if count == max_count:
            break

        else:
            continue

    return list_facts


# Exercise 2:


def num_joey_facts():
    count = 0
    count_joeys = 0
    list_fact_joey = []

    while count_joeys < 10:
        output = random_koala_fact()
        count += 1
        if "joey" in output:
            count_joeys += 1
            list_fact_joey.append(output)
            if count_joeys == 10:
                return len(set(list_fact_joey))


# Exercise 3:
def koala_weight():
    weight = 0

    while weight == 0:
        output = random_koala_fact()
        if "kg" in output:
            string_weight = output[output.find("kg") - 2 : -3]
            return int(string_weight)


# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    # print(random_koala_fact())

    """Write the calls to your functions here."""

    # Exercise 1:
    print(unique_koala_facts(500000))

    # Exercise 2:
    print(num_joey_facts())

    # Exercise 3:
    print(koala_weight())
