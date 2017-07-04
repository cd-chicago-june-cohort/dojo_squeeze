print "x", #comma allows for no carriage return
for y in range (1,14):
    if y is not 1:
        print y-1,
        for x in range(1,13):
            print "  "+str(x*(y-1)), # y-1 for headers(range is to 14)
    else: # this entire else condition is for the headers
        for x in range(1,13):
            print "  "+str(x*y),
    print ''

# hard coding the headers wouldve simplified the algorithm significantly I will do that here.

print "+=" * 25 
print " This is another way thats more readable/elegant despite the hard coded headers"
print "+=" * 25 


print "x   1   2   3   4   5   6   7   8   9   10   11   12"
for y in range (1,13):
    print y,
    for x in range(1,13):
        print "  "+str(x*y),
    print ''