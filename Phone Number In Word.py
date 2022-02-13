#Phone Number In Word
phone_number=input("Enter your phone number: ") #'8237198953'
d={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six',
   '7':'seven','8':"eight","9":"nine"}
output=""
for number in phone_number: #number='8669117577'
    output =output + d.get(number) +" "
print(output)