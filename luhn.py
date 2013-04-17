#create a function to convert the card number
#to a string and then to single digits
def digits_of(n):
    digits = []
    for d in str(n):
        digits.append(int(d))
    return digits

def luhn_checksum(card_number):
    digits = digits_of(card_number)
    #start at -2 to skip the last digit
    odd_digits = digits[-2::-2]
    even_digits = digits[-3::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    #multiply the checksum by 9
    new_checksum = checksum * 9
    return new_checksum % 10


 
def is_luhn_valid(card_number):
    new_checksum = luhn_checksum(card_number)
    if new_checksum == digits_of(card_number)[-1]:
        return "number is valid"
    else:
        return "number is invalid"

print is_luhn_valid(38520000023237)

#print is_luhn_valid(38520000023236)