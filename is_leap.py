#閏年計算
def is_leap(y):
    if y % 4 != 0: # != 不等於
        return False
    elif y % 100 != 0:
        return True
    elif y % 400 != 0:
        return False
    elif y % 3200 != 0:
    	return True
y = input('請輸入西元年: ')
y = int(y)
print(is_leap(y))
  