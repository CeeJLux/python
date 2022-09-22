#Temperature Converter
# Convert Temperature to Celsius
print("Temperature Converter to Celsius")
Temperature = input("What is your current Temperature: ")
unit = input("Temperature in Kelvin(K) or Fahrenheit(F): ")
if unit.upper() == "K":
    celcius = -273.15 + int(Temperature)
    print("The Temprature of " + Temperature, "°K is equivalent to " + str(celcius), "°C")

else:
    celcius = (int(Temperature) - 32) * 5/9
    print("The Temprature of " + Temperature, "°F is equivalent to " + str(celcius), "°C")