import math

from files import files
from tools import tools

from collections import Counter







if __name__ == "__main__":
	f = files("text.txt")
	

	print("#")
	print("# MONOGRAM")
	print("#")

	text = f.read()
	text_wos = f.read_wos() #без пробілів

	print("\n# text with spaces")
	d = tools.count_symbols(text)
	tools.dict_freq(d,text)
	d = tools.dict_sort(d)
	print(d)
	entropy = tools.dict_calc_entropy(d)
	print("Entropy:", entropy)
	print("Redundant:", 1 - (entropy/math.log2(32)))


	print("\n# text without spaces")
	d = tools.count_symbols(text_wos)
	tools.dict_freq(d,text_wos)
	d = tools.dict_sort(d)
	print(d)
	entropy = tools.dict_calc_entropy(d)
	print("Entropy:", entropy)
	print("Redundant:", 1 - (entropy/math.log2(31)))
	

	print("\n#")
	print("# BIGRAM")
	print("#")



	print("\n# text with spaces and intersection")	
	l = tools.dict_bigram(text, intersection=True)
	d = tools.count_symbols(l)
	tools.dict_freq(d,text)
	d = tools.dict_sort(d)
	print(d)
	entropy = tools.dict_calc_entropy_bigram(l, Counter(l))
	print("Entropy:", entropy)
	print("Redundant:", 1 - (entropy/math.log2(32)))
	

	print("\n# text with spaces and without intersection")	
	l = tools.dict_bigram(text, intersection=False)
	d = tools.count_symbols(l)
	tools.dict_freq(d,text)
	d = tools.dict_sort(d)
	print(d)
	entropy = tools.dict_calc_entropy_bigram(l, Counter(l))
	print("Entropy:", entropy)
	print("Redundant:", 1 - (entropy/math.log2(32)))

	print("\n# text without spaces and with intersection")	
	l = tools.dict_bigram(text_wos, intersection=True)
	d = tools.count_symbols(l)
	tools.dict_freq(d,text)
	d = tools.dict_sort(d)
	print(d)
	entropy = tools.dict_calc_entropy_bigram(l, Counter(l))
	print("Entropy:", entropy)
	print("Redundant:", 1 - (entropy/math.log2(31)))

	print("\n# text without spaces and without intersection")	
	l = tools.dict_bigram(text_wos, intersection=False)
	#print(l)
	d = tools.count_symbols_bigram(l)
	#print(d)
	tools.dict_freq(d,text)
	d = tools.dict_sort(d)
	print(d)
	entropy = tools.dict_calc_entropy_bigram(l, Counter(l))
	print("Entropy:", entropy)
	print("Redundant:", 1 - (entropy/math.log2(31)))


