# Coffee shop assignment - Csilla Tepliczky, 17.10.2023 

def main():
    q1 = input('Do you want small, medium, or large? ').lower()
    total_cost = 0

    if q1 == 'small':
        total_cost = 2
    elif q1 == 'medium':
        total_cost = 3
    elif q1 == 'large':
        total_cost = 4
    else:
        return 'Please choose a valid type'

    q2 = input('Do you want brewed, espresso, or cold press? ').lower()
    if q2 == 'brewed':
        total_cost = total_cost + 0
    elif q2 == 'espresso':
        total_cost = total_cost + 0.5
    elif q2 == 'cold press':
        total_cost = total_cost + 1
    else:
        return 'Please choose a valid type'

    q3 = input('Do you want a flavored syrup? (Yes or No) ').lower()

    if q3 == 'yes':
        q4 = input('Do you want hazelnut, vanilla, or caramel? ').lower()
        if q4 in ['hazelnut', 'vanilla', 'caramel']:
            total_cost = total_cost + 0.5
            q5 = q4 + ' syrup'
        else:
            return 'Please choose a valid type'
    elif q3 == 'no':
        total_cost = total_cost + 0
        q5 = 'no flavour'
    else:
        return 'Please choose a valid type'

    tip = total_cost * 1.15

    print(f'You asked for a {q1} cup of {q2} coffee with {q5}')
    print(f'Your cup of coffee costs {total_cost}')
    print(f'The price with a tip is {round(tip, 2)}')


if __name__ == '__main__':
    print(main())
