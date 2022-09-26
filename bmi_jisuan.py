height = 1.7
print("您的身高" + str(height))
weight = 48.5
print("您的体重" + str(weight))
bmi = weight / (height * height)
print("您的BMI指数为:" + str(bmi))

if bmi < 18.5:
    print("您的体重过轻")

elif bmi < 24.9:
    print("您的体重正常")

elif bmi < 29.9:
    print("您的体重过重")
