# converting octal string to unicode
# Example, for a string like '\345\233\275\345\256\266':
print b'\345\233\275\345\256\266'.decode('utf-8')
# this will output: `国家`
