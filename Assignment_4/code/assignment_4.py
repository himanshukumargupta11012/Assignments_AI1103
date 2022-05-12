



# Since cards are drawing after replacement.So,sample space is 52 for both times and number of ace will also be 4 each time.So,
num_S=52
num_A=4

# Since,drawing of both card are done after replacement.So,both the drawing are independent.So, we can apply the formula for independent events like
# Prob(A_and_B)=Prob(A).Prob(B)

Prob_0ace = (num_S-num_A)/num_S * (num_S-num_A)/num_S
Prob_1ace = num_A/num_S * (num_S-num_A)/num_S + (num_S-num_A)/num_S * num_A/num_S
Prob_2ace = num_A/num_S * num_A/num_S

print(Prob_0ace)
print(Prob_1ace)
print(Prob_2ace)


