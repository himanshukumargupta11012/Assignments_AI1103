'''let (x,y,z) be the elements of sample space where x,y,z are the random variables for 1 ,2 and 3 switch
respectively taking values 1 and 0 where 0 means open and 1 means closed
So,sample space,'''

S={(1,1,1),(1,1,0),(1,0,1),(1,0,0),(0,1,1),(0,1,0),(0,0,1),(0,0,0)}

#event that we get no output contain only 1 element because there is only 1 case when all switch is open
E_noOP={(0,0,0)}

E_yesOP = S - E_noOP

prob_E_yesOP = len(E_yesOP)/len(S)
print("probability of receiving an input signal at output:",prob_E_yesOP)

#event that switch 1 is open
E_openS1 = {(0,1,1),(0,1,0),(0,0,1),(0,0,0)}


#probability that S1 is open given that an input signal is receiving at output
prob_E_openS1_given_E_yesOP = len(E_openS1 & E_yesOP)/len(E_yesOP)

print("probability that S1 is open given that an input signal is receiving at output:",prob_E_openS1_given_E_yesOP)