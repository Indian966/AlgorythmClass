def coin_charge (n) :
    charge = n
    if (charge // 6) < 1 :
        six = 0
    else :
        six = charge // 6
    first_charge = charge - six * 6

    if (first_charge // 5) < 1 :
        five = 0
    else :
        five = first_charge // 5
    second_charge = first_charge - five * 5

    if (second_charge // 4) < 1 :
        four = 0
    else :
        four = second_charge // 4
    third_charge = second_charge - four * 4
    one = third_charge
    return print(six, five, four, one)

coin_charge(15)