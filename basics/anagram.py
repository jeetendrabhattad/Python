def anagram(s):
	if s == "":
		return s
	else:
		ans=[]
		print "In Else ", s[1:]
		
		for w in anagram(s[1:]):
			print w
			for pos in range(len(w)+1):
				ans.append(w[:pos]+s[0]+w[pos:])
				print pos, ans
#		return ans

print(anagram("abc"))
