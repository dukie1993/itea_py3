#get card number
card_num = input("Enter card number (16 digits): ")
try:
    try:
        card_num_int = int(card_num)
    except ValueError:
        print("Use only digits for card number")
        exit()
    if len(card_num) != 16:
        raise ValueError("Card number must be 16 digits.")
except ValueError as v_e:
    print("Card number is wrong. Enter correct card number:", v_e)
    exit()

#get expiration date
exp_date = input("Enter expiration date in MM/YY format: ")
try:
    if len(exp_date) != 5 and exp_date.count("/") != 1:
        raise ValueError
    exp_month, exp_year = exp_date.split("/")
    try:
        if len(exp_month) != 2 and len(exp_year) != 2:
            raise ValueError("Month and year should contain 2 digits for each.")
    except ValueError as v_e:
        print(v_e)
    exp_month = int(exp_month)
    exp_year = int(exp_year)
    if exp_month < 1 or exp_month > 12:
        print("Month must be in range 1 - 12.")
except ValueError as v_e:
    print(v_e,"Expiration date is wrong. MM/YY format needed.")
    exit()

#get CVV
cvv = input("Enter CVV code here: ")
cvv_len = len(cvv)
try:
    cvv_int = int(cvv)
    try:
        if cvv_len != 3:
            raise ValueError
    except ValueError:
        print("CVV must be 3 digits long")
        exit()
except ValueError:
    print("CVV must contain only digits.")
    exit()

print("Ha-ha-ha. Now I will use your credit card!")