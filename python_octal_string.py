# converting octal string to unicode
# Example, for a string like '\345\233\275\345\256\266':
print b'\345\233\275\345\256\266'.decode('utf-8')
# this will output: `国家`

# converting list of decimal byte values to string
import array
lst = [232, 191, 153, 229, 189, 147, 231, 132, 182, 230, 152, 175, 228, 189, 160, 231, 154, 132, 229, 183, 165, 228, 189, 156, 229, 132, 191, 229, 183, 165]
print array.array('B', lst).tostring().decode('utf-8')
# this will output: `这当然是你的工作儿工`
