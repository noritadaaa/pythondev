#フィボナッチ数列を計算する関数
def calc_fibonacci(n): #n番目が引数、n番目の2つ数値の和がreturn
  if n < 3:
    return 1
  else:
    return calc_fibonacci(n - 2)  + calc_fibonacci(n - 1)