def isfloat(s):
	(m,_,n) = s.partition(".")
	return (m.isdigit() and (n.isdigit() or n=="")) or m=="" and n.isdigit()

def get_float(message):
	s = input(message)
	while not (s.isdigit() or isfloat(s)):
		s = input(message)
	return float(s)

def remove_sign(s):
	if (s[0] == "-" or s[0] == '+'):
		s = s[1:]
	else:
		s = s
	return s

def get_fixed_signed(message):
	s = input(message)
	while not (remove_sign(s).isdigit() or isfloat(remove_sign(s))):
		s = input(message)		
	return float(s)


print(get_fixed_signed("실수를 입력하시오"))