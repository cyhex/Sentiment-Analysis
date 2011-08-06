# POS ID PosScore NegScore SynsetTerms Gloss
while 1:
	try:
		x = raw_input();
		y = x.split("\t")
		p = float(y[2])
		n = float(y[3])
		if (p == 0.0 and n == 0.0): continue
		print x
	except EOFError:
		break
	except:
		continue
