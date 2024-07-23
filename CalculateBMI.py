#โปรแกรมคำนวณค่า BMI 
# BMI = Weight(kg)/Height*Height(m)

weight=int(input("Enter your weight(kg):"))
height=int(input("Enter your height(Cm):"))

#process
#cm->m
height/=100
BMI=weight/(height**2)

#output
print("BMI :",BMI)