#include <stdio.h>

int main(){

float P[2],ra,rb,M[2],N[2],slope;

//where x[y] is vector having y spaces
/*ratio in which P divides M and N be ra:rb,
slope is the slope of line MN  */

printf("enter the x and y cordinates of P respectively using space between then:\n");
scanf("%f %f",&P[0],&P[1]);

printf("enter the ratio using space between then instead of colon:\n");
scanf("%f %f",&ra,&rb);

//we know that section formula is P[2]=(M[2]*rb+N[2]*ra)/(ra+rb) in vector form
// by rearranging the section formula and then divide it into 2 parts according to the spaces we get something like this
//dont mind the below formula so much because I rearranged it so that the c code works properly 
M[0]=(P[0]*(ra+rb)-N[0]*ra)/rb;
N[1]=(P[1]*(ra+rb)-M[1]*rb)/ra;

//now we get the cordinates of M and N so slope of line MN will be following
slope=(N[1]-M[1])/(N[0]-M[0]);

printf("M=(%.2f,0)\nN=(0,%.2f)\nslope=%.2f",M[0],N[1],slope);


return 0;}