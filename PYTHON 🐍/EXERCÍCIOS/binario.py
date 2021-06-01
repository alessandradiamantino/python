def binario(int bi,int  dec)
	if dec > 0
	bi = dec % 2
	bi = dec / 2

	binario(dec,bi)
	print(bi)

	else
	return bi

