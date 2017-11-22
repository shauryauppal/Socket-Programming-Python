import sys
val1= 'hi'

if (len(sys.argv)>1):
        val1=str(sys.argv[1])

def parityOf(int_type):
	parity = 0
	while (int_type):
		parity = ~parity
		int_type = int_type & (int_type-1)
	
	if (parity==-1):
		return(0)
	return(1)

def calcLRC(input):

    lrc = ord(input[0])
    
    for i in range(1,len(input)):
	lrc ^= ord(input[i])     
    return lrc


def showLRC(input,res):
    input = input[:7]

    print 'Char\tHex\tBinary'
    print '------------------------------------'
    for i in range(0,len(input)):
	print input[i],"\t",hex(ord(input[i])),"\t",bin(ord(input[i]))


    print '\nBit\tBinary         LRC'
    print '----------------------------'
    print '  \t',
    for i in range(0,len(input)):  
    	print input[i],
    print ""

    mask=1
    for bitpos in range(0,7):
        bit = (res & mask) >> bitpos
        print "b",bitpos,"\t",

    	for i in range(0,len(input)):    	
        	bitchar = (ord(input[i]) & mask) >> bitpos
		print bitchar,
		
        print bit
	mask = mask << 1

# Show VRC
    print "VRC\t",
    for i in range(0,len(input)):    	
        print parityOf(ord(input[i])),

    print parityOf(res),
    return

res = calcLRC(val1)

print ""
print "Input: ",val1," LRC is ",hex(res),"- Char: ",chr(res)
print ""

showLRC(val1,res)


