# /usr/bin/python3

report = "{0} C is {1} F."

celsius = 20
while celsius <= 45:
    fahrenheit = (celsius * 9 / 5) + 32  # calculate fahrenheit
    print( report.format( celsius, fahrenheit ) )  # report both temps
    celsius += 5

# the end