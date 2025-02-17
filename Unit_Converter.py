# Imports
import time # For a Fake Processing Delay
import sys # To make a Cool effect in terminal
# Conversion Functions

## Length Conversion Functions
def cmToM(num, reversed):
    if reversed == False:
        num /= 100
        return num
    elif reversed == True:
        num *= 100
        return num

def mToKm(num, reversed):
    if reversed == False:
        num /= 1000
        return num
    elif reversed == True:
        num *= 1000
        return num

def inToCm(num, reversed):
    if reversed == False:
        num *= 2.54
        return num
    elif reversed == True:
        num /= 2.54
        return num

def ftToM(num, reversed):
    if reversed == False:
        num /= 3.281
        return num
    elif reversed == True:
        num *= 3.281
        return num
    
## Temperature Conversion Functions
def CToF(num, reversed):
    if reversed == False:
        num = (num * (9/5)) + 32
        return num
    elif reversed == True:
        num = (num - 32) * (5/9)
        return num

def CToK(num, reversed):
    if reversed == False:
        num += 273.15
        return num
    elif reversed == True:
        num -= 273.15
        return num
    
def FToK(num, reversed):
    if reversed == False:
        num = (num - 32) * (5 / 9) + 273.15
        return num
    if reversed == True:
        num = (num - 273.15) * (9 / 5) + 32
        return num
    
## Weight/Mass Conversion Functions
def gToKg(num, reversed):
    if reversed == False:
        num /= 1000
        return num
    elif reversed == True:
        num *= 1000
        return num

def kgToLb(num, reversed):
    if reversed == False:
        num *= 2.205
        return num
    elif reversed == True:
        num /= 2.205
        return num

def lbToOz(num, reversed):
    if reversed == False:
        num *= 16
        return num
    elif reversed == True:
        num /= 16
        return num

## Volume Conversion Functions
def mlToL(num, reversed):
    if reversed == False:
        num /= 1000
        return num
    elif reversed == True:
        num *= 1000
        return num

def cupToMl(num, reversed):
    if reversed == False:
        num *= 240
        return num
    elif reversed == True:
        num /= 240
        return num

def galToL(num, reversed):
    if reversed == False:
        num *= 3.785
        return num
    elif reversed == True:
        num /= 3.785
        return num

## Speed Conversion Functions
def msTokmh(num, reversed):
    if reversed == False:
        num *= 3.6
        return num
    elif reversed == True:
        num /= 3.6
        return num

def mphToKmh(num, reversed):
    if reversed == False:
        num *= 1.609
        return num
    elif reversed == True:
        num /= 1.609
        return num

## Area Conversion Functions
def scmToSm(num, reversed):
    if reversed == False:
        num /= 10000
        return num
    elif reversed == True:
        num *= 10000
        return num

def smToSkm(num, reversed):
    if reversed == False:
        num /= 1000000
        return num
    elif reversed == True:
        num *= 1000000
        return num

def sftToSm(num, reversed):
    if reversed == False:
        num /= 10.764
        return num
    elif reversed == True:
        num *= 10.764
        return num

## Temporal Conversion Functions
def secToMins(num, reversed):
    if reversed == False:
        num /= 60
        return num
    elif reversed == True:
        num *= 60
        return num

def minsToHrs(num, reversed):
    if reversed == False:
        num /= 60
        return num
    elif reversed == True:
        num *= 60
        return num

def hrsToDays(num, reversed):
    if reversed == False:
        num /= 24
        return num
    elif reversed == True:
        num *= 24
        return num

# Terminal Effect Function
def converting_effect(delay):
    for i in range(3):
        sys.stdout.write("Converting" + "." * (i + 1))
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write("\r")

# Main Loop
while True:
    print("Welcome To Unit Converter")
    print("Sections:")
    print("1. Length")
    print("2. Temperature")
    print("3. Weight/Mass")
    print("4. Volume")
    print("5. Speed")
    print("6. Area")
    print("7. Time")
    choice = input("Enter 1-7 to Choose: ")
    if choice == '1':
        print("You've Picked Length")
        print("Which Units You Want to Convert")
        print("1. cm to m")
        print("2. m to cm")
        print("3. m to km")
        print("4. km to m")
        print("5. in to cm")
        print("6. cm to in")
        print("7. ft to m")
        print("8. m to ft")
        while True:
            choice = input("Enter 1-8 to Choose: ")
            if choice == '1':
                print("You're Converting Centimeters to Meters")
                numIn = float(input("Input a Number in Centimeters to Convert into Meters: "))
                numOut = cmToM(numIn, False)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}cm to {numOut}m")
                break
            elif choice == '2':
                print("You're Converting Meters to Centimeters")
                numIn = float(input("Input a Number in Meters to Convert into Centimeters: "))
                numOut = cmToM(numIn, True)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}m to {numOut}cm")
                break
            elif choice == '3':
                print("You're Converting Meters to Kilometers")
                numIn = float(input("Input a Number in Meters to Convert into Kilometers: "))
                numOut = mToKm(numIn, False)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}m to {numOut}km")
                break
            elif choice == '4':
                print("You're Converting Kilometers to Meters")
                numIn = float(input("Input a Number in Kilometers to Convert into Meters: "))
                numOut = mToKm(numIn, True)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}km to {numOut}m")
                break
            elif choice == '5':
                print("You're Converting Inches to Centimeters")
                numIn = float(input("Input a Number in Inches to Convert into Centimeters: "))
                numOut = inToCm(numIn, False)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}in to {numOut}cm")
                break
            elif choice == '6':
                print("You're Converting Centimeters to Inches")
                numIn = float(input("Input a Number in Centimeters to Convert into Inches: "))
                numOut = inToCm(numIn, True)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}cm to {numOut}in")
                break
            elif choice == '7':
                print("You're Converting Feet to Meters")
                numIn = float(input("Input a Number in Feet to Convert into Meters: "))
                numOut = ftToM(numIn, False)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}ft to {numOut}m")
                break
            elif choice == '8':
                print("You're Converting Meters to Feet")
                numIn = float(input("Input a Number in Meters to Convert into Feet: "))
                numOut = ftToM(numIn, True)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}m to {numOut}ft")
                break
            else:
                print("Pick a Number From 1-8. Try Again: ")
    elif choice == '2':
        print("You've Picked Temperature")
        print("Which Units You Want to Convert")
        print("1. °C to °F")
        print("2. °F to °C")
        print("3. °C to °K")
        print("4. °K to °C")
        print("5. °F to °K")
        print("6. °K to °F")
        while True:
            choice = input("Enter 1-6 to Choose: ")
            if choice == '1':
                print("You're Converting Celsius to Fahrenheit")
                numIn = float(input("Input a Number in Celsius to Convert into Fahrenheit: "))
                numOut = CToF(numIn, False)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}°C to {numOut}°F")
                break
            elif choice == '2':
                print("You're Converting Fahrenheit to Celsius")
                numIn = float(input("Input a Number in Fahrenheit to Convert into Fahrenheit: "))
                numOut = CToF(numIn, True)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}°F to {numOut}°C")
                break
            elif choice == '3':
                print("You're Converting Celsius To Kelvin")
                numIn = float(input("Input a Number in Celsius to Convert into Kelvin: "))
                numOut = CToK(numIn, False)
                converting_effect(0.25)
                
                time.sleep(0.25)
                print(f"Converted {numIn}°C to {numOut}°K")
                break
            elif choice == '4':
                print("You're Converting Kelvin To Celsius")
                numIn = float(input("Input a Number in Kelvin to Convert into Celsius: "))
                numOut = CToK(numIn, True)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}°K to {numOut}°C")
                break
            elif choice == '5':
                print("You're Converting Fahrenheit To Kelvin")
                numIn = float(input("Input a Number in Fahrenheit to Convert into Kelvin: "))
                numOut = FToK(numIn, False)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}°F to {numOut}°K")
                break
            elif choice == '6':
                print("You're Converting Kevlin To Fahrenheit")
                numIn = float(input("Input a Number in Kelvin to Convert into Fahrenheit: "))
                numOut = FToK(numIn, True)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}°K to {numOut}°F")
                break
            else:
                print("Pick a Number From 1-6. Try Again: ")
    elif choice == '3':
        print("You've Picked Weight/Mass")
        print("Which Units You Want to Convert")
        print("1. g to kg")
        print("2. kg to g")
        print("3. kg to lb")
        print("4. lb to kg")
        print("5. lb to oz")
        print("6. oz to lb")
        while True:
            choice = input("Enter 1-6 to Choose: ")
            if choice == '1':
                print("You're Converting Grams to Kilograms")
                numIn = float(input("Input a Number in Grams to Convert into Kilograms: "))
                numOut = gToKg(numIn, False)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}g to {numOut}kg")
                break
            elif choice == '2':
                print("You're Converting Kilograms to Grams")
                numIn = float(input("Input a Number in Kilograms to Convert into Grams: "))
                numOut = gToKg(numIn, True)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}kg to {numOut}g")
                break
            elif choice == '3':
                print("You're Converting Kilograms to Pounds")
                numIn = float(input("Input a Number in Kilograms to Convert into Pounds: "))
                numOut = kgToLb(numIn, False)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}kg to {numOut}lb")
                break
            elif choice == '4':
                print("You're Converting Pounds to Kilograms")
                numIn = float(input("Input a Number in Pounds to Convert into Kilograms: "))
                numOut = kgToLb(numIn, True)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}lb to {numOut}kg")
                break
            elif choice == '5':
                print("You're Converting Pounds to Ounces")
                numIn = float(input("Input a Number in Pounds to Convert into Ounces: "))
                numOut = lbToOz(numIn, False)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}lb to {numOut}oz")
                break
            elif choice == '6':
                print("You're Converting Ounces to Pounds")
                numIn = float(input("Input a Number in Ounces to Convert into Pounds: "))
                numOut = lbToOz(numIn, True)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}oz to {numOut}lb")
                break
            else:
                print("Pick a Number From 1-6. Try Again: ")
    elif choice == '4':
        print("You've Picked Volume")
        print("Which Units You Want to Convert")
        print("1. ml to l")
        print("2. l to ml")
        print("3. cup to ml")
        print("4. ml to cup")
        print("5. gallon to l")
        print("6. l to gallon")
        while True:
            choice = input("Enter 1-6 to Choose: ")
            if choice == '1':
                print("You're Converting Mililiters to Liters")
                numIn = float(input("Input a Number in Mililiters to Convert into Liters: "))
                numOut = mlToL(numIn, False)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}ml to {numOut}l")
                break
            elif choice == '2':
                print("You're Converting Liters to Mililiters")
                numIn = float(input("Input a Number in Liters to Convert into Mililiters: "))
                numOut = mlToL(numIn, True)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}l to {numOut}ml")
                break
            elif choice == '3':
                print("You're Converting Cups to Mililiters")
                numIn = float(input("Input a Number in Cups to Convert into Mililiters: "))
                numOut = cupToMl(numIn, False)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}cup to {numOut}ml")
                break
            elif choice == '4':
                print("You're Converting Mililiters to Cups")
                numIn = float(input("Input a Number in Mililiters to Convert into Cups: "))
                numOut = cupToMl(numIn, True)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}ml to {numOut}cup")
                break
            elif choice == '5':
                print("You're Converting Gallons to Liters")
                numIn = float(input("Input a Number in Gallons to Convert into Liters: "))
                numOut = galToL(numIn, False)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}gal to {numOut}l")
                break
            elif choice == '6':
                print("You're Converting Liters to Gallons")
                numIn = float(input("Input a Number in Liters to Convert into Gallons: "))
                numOut = galToL(numIn, True)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}l to {numOut}gal")
                break
            else:
                print("Pick a Number From 1-6. Try Again: ")
    elif choice == '5':
        print("You've Picked Speed")
        print("Which Units You Want to Convert")
        print("1. m/s to km/h")
        print("2. km/h to m/s")
        print("3. mph to km/h")
        print("4. km/h to mph")
        while True:
            choice = input("Enter 1-4 to Choose: ")
            if choice == '1':
                print("You're Converting Meters/Second to Kilometers/hour")
                numIn = float(input("Input a Number in Meters/second to Convert into Kilometers/hour: "))
                numOut = msTokmh(numIn, False)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}m/s to {numOut}km/h")
                break
            elif choice == '2':
                print("You're Converting Kilometers/hour to Meters/Second")
                numIn = float(input("Input a Number in Kilometers/hour to Meters/Second: "))
                numOut = msTokmh(numIn, True)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}km/h to {numOut}m/s")
                break
            elif choice == '3':
                print("You're Converting Miles Per Hour to Kilometers/Hour")
                numIn = float(input("Input a Number in Miles Per Hour to Convert into Kilometers/Hour: "))
                numOut = mphToKmh(numIn, False)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}mph to {numOut}km/h")
                break
            elif choice == '4':
                print("You're Converting Kilometers/Hour to Miles Per Hour")
                numIn = float(input("Input a Number in Kilometers/Hour to Convert into Miles Per Hour: "))
                numOut = mphToKmh(numIn, True)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}km/h to {numOut}mph")
                break
            else:
                print("Pick a Number From 1-4. Try Again: ")
    elif choice == '6':
        print("You've Picked Area")
        print("Which Units You Want to Convert")
        print("1. cm² to m²")
        print("2. m² to cm²")
        print("3. m² to km²")
        print("4. km² to m²")
        print("5. ft² to m²")
        print("6. m² to ft²")
        while True:
            choice = input("Enter 1-6 to Choose: ")
            if choice == '1':
                print("You're Converting Centimeters² to Meters²")
                numIn = float(input("Input a Number in Centimeters² to Convert into Meters²: "))
                numOut = scmToSm(numIn, False)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}cm² to {numOut}m²")
                break
            elif choice == '2':
                print("You're Converting Meters² to Centimeters²")
                numIn = float(input("Input a Number in Meter² to Convert into Centimeters²: "))
                numOut = scmToSm(numIn, True)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}m² to {numOut}cm²")
                break
            elif choice == '3':
                print("You're Converting Meters² to Kilometers²")
                numIn = float(input("Input a Number in Meters² to Convert into Kilometers²: "))
                numOut = smToSkm(numIn, False)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}m² to {numOut}km²")
                break
            elif choice == '4':
                print("You're Converting Kilometers² to Meters²")
                numIn = float(input("Input a Number in Kilometers² to Convert into Meters²: "))
                numOut = smToSkm(numIn, True)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}km² to {numOut}m²")
                break
            elif choice == '5':
                print("You're Converting Feet² to Meters²")
                numIn = float(input("Input a Number in Feet² to Convert into Meters²: "))
                numOut = ftToM(numIn, False)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}ft² to {numOut}m²")
                break
            elif choice == '6':
                print("You're Converting Meters² to Feet²")
                numIn = float(input("Input a Number in Meters² to Convert into Feet²: "))
                numOut = ftToM(numIn, True)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}m² to {numOut}ft²")
                break
            else:
                print("Pick a Number From 1-6. Try Again: ")
    elif choice == '7':
        print("You've Picked Time")
        print("Which Units You Want to Convert")
        print("1. s to mins")
        print("2. mins to s")
        print("3. mins to hrs")
        print("4. hrs to mins")
        print("5. hrs to days")
        print("6. days to hrs")
        while True:
            choice = input("Enter 1-6 to Choose: ")
            if choice == '1':
                print("You're Converting Seconds to Minutes")
                numIn = float(input("Input a Number in Seconds to Convert into Minutes: "))
                numOut = secToMins(numIn, False)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}s to {numOut}min")
                break
            elif choice == '2':
                print("You're Converting Minutes to Seconds")
                numIn = float(input("Input a Number in Minutes to Convert into Seconds: "))
                numOut = secToMins(numIn, True)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}min to {numOut}s")
                break
            elif choice == '3':
                print("You're Converting Minutes to Hours")
                numIn = float(input("Input a Number in Minutes to Convert into Hours: "))
                numOut = minsToHrs(numIn, False)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}min to {numOut}hrs")
                break
            elif choice == '4':
                print("You're Converting Hours to Minutes")
                numIn = float(input("Input a Number in Hours to Convert into Minutes: "))
                numOut = minsToHrs(numIn, True)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}hrs to {numOut}min")
                break
            elif choice == '5':
                print("You're Converting Hours to Days")
                numIn = float(input("Input a Number in Hours to Convert into Days: "))
                numOut = hrsToDays(numIn, False)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}hrs to {numOut}days")
                break
            elif choice == '6':
                print("You're Converting Days to Hours")
                numIn = float(input("Input a Number in Days to Convert into Hours: "))
                numOut = hrsToDays(numIn, True)
                converting_effect(0.25)
                time.sleep(0.25)
                print(f"Converted {numIn}days to {numOut}hrs")
                break
            else:
                print("Pick a Number From 1-6. Try Again: ")
    else:
        print("Pick a Number From 1-7. Try Again: ")
    
    continue_choice = input("Do You want to Convert another Unit? (y/n): ").lower().strip()
    if continue_choice != 'y':
        print("Cya Later")
        break