def convert_fahrenheit_to_centigrade():
    ftoc = float(input("Enter number in Fahrenheit (to convert to Centigrade):"))
    centigrade = (ftoc-32) * 5/9
    return centigrade


def convert_centigrade_to_fahrenheit():
    ctof = float(input("Enter number in Centigrade (to convert to Fahrenheit):"))
    fahrenheit = (ctof*9/5) + 32
    return fahrenheit


def convert_centigrade_to_kelvin():
    ctok = float(input("Enter number in Centigrade (to convert to Kelvin):"))
    kelvin = ctok+273.15
    return kelvin


def convert_fahrenheit_to_rankine():
    ftor = float(input("Enter number in Fahrenheit (to convert to Rankine):"))
    rankine = ftor+459.67
    return rankine


def main():
    print("In Centigrade:", convert_fahrenheit_to_centigrade())
    print("In Fahrenheit:", convert_centigrade_to_fahrenheit())
    print("In Kelvin:", convert_centigrade_to_kelvin())
    print("In Rankine:", convert_fahrenheit_to_rankine())


main()
