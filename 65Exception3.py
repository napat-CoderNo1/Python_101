# error เเบบที่ 3

'''
score = 100+"A"
print(score)
'''

try:
    score = 100+"A"
    print(score)
except TypeError:
    print("Type of data not match")