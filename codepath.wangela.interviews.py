def rotateArray(a, b):
	ret = []
        shift = b % (len(a))
        print(shift)
        for i in xrange(len(a) - shift):
            ret.append(a[i + shift])
        for j in xrange(shift):
        	ret.append(a[j])
        return ret
