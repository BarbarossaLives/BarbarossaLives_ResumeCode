


def ordinalSuffix(number):
    workingNumber = str(number)
    workingNumberEnd = workingNumber[0:3]
    if int(workingNumberEnd) > 4 and int(workingNumberEnd) < 21:
        suffix = "th"
    elif int(workingNumberEnd[-1]) == 0:
        suffix = "th"
    elif int(workingNumberEnd[-1]) == 1:
        suffix = "st"
    elif int(workingNumberEnd[-1]) == 2:
        suffix = "nd"
    elif int(workingNumberEnd[-1]) == 3:
        suffix = "rd"
    else:
        suffix = "th"
        
    print(workingNumber + suffix)
    
    return workingNumber + suffix


assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'
