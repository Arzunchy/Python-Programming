nums=input("Enter the number: ")

if int(nums) % 7 == 0 :
    print(F'Multiple of 7')
elif nums[-1] == '7':
    print(F'End with 7')
else:
    print(F'Neither multiple of 7 nor end with 7')        