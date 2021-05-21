s1_math = {"Tom","John", "Mary", "Jimmy", "Sunny", "Amy"}
s2_eng = {'John', 'Mary' , 'Tony' , 'Bob' , 'Pony', 'Tom' , 'Alice'}





x = s1_math & s2_eng  #先取交集
print("兩科都及格的人:{}".format(x))

x1 = s1_math - x  # -號運算可以扣掉交集，所以math-交集 = 只剩數學及格英文不及格的人
print("數學及格英文不及格:{}".format(x1))


x2=s2_eng - x  #同上  英文及格 數學不及格

print("英文及格數學不及格:{}".format(x2))

