# the universal set U is
U={1,2,3,4,5,6}
# A is event of first die to be even.So
A={2,4,6} 
# B is event of first die to be odd.So
B={1,3,5}

print("intersection of A and B:",A&B)
# we can see that intersection of A and B is null .So they are mutually exclusive.So 1st part proved true.

print("union of A and B:",A|B)
# we can see that union of A and B contain the whole sample space.So they are mutually exhaustive.So,2nd part proved true.
# And we know that if 2 events are mutually exhaustive and exclusive then they are inverse of each other.So A=B' or B=A'.So,3rd part proved true.

# C is the event that sum of both dice numbers are less than equal to 5.So,numbers possible in first dice are 
C={1,2,3,4}

print("intersection of A and C:",A&C)
# we can see that intersection of A and C is not null. So they are not mutually exclusive. So,4rd part proved false.

# above we proved that A=B'.So A and B' can't be mutually exclusive because they are equal.So,5th part proved false.

print("intersection of A' and C:",(U-A)&C)
# we can see that intersection of A' and C is not null.So, A' and C are not mutually exclusive.So,A',B'and C are mutually exclusive.So,6th part proved false.




