sum1 = 0
print(sum1)
question1 = input("did you use a smartphone today?")
if question1 == "y":
    question2 = int(input("For how many hours?"))
    carbonout = question2 * 1.5
    sum1 += carbonout
print(sum1)
