import random


import datetime


def greeting(): print("Hello!")
print("sveiki!")


x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))



def a():
    mikla = {
        'Kas vienmēr seko lai kur tu ietu? ': 'ēna',
        'Kas krīt, kā dzimst un mirst, kad nekrīt': 'sniegpārsla',
        'Kas apciemo ziemassvētkos': 'Salavecis',
        'Sarkana gotiņa , kaula sirsniņa': 'ķirsis',
        'gaisma melnā jūrā': 'zvaigzne',
        
    }
    mikla1 = random.choice(list(mikla.keys()))
    atbilde = mikla[mikla1]
    return mikla1, atbilde
##
def b():
    score = 0
    total_questions = 5 

    for _ in range(total_questions):
        mikla1, correct_capital = a()

        print(f"Mini mīklu :{mikla1}:")
        minejums = input("Tavs minējums(raksti end lai beigtu): ")

        if minejums.lower() == "end":
            print("\nGame Ended.")
            break

        if minejums.lower() == correct_capital.lower():
            print("Pareizi.")
            score += 1
        else:
            print(f"Nepareizi, atminējums: {correct_capital}.")

    print(f"\nSpēle beidzās! tavs atminējums {score}/{total_questions}.")
##
if __name__ == "__main__":
    b()