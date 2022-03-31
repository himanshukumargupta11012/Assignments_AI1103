#include <stdio.h>

int main(){

float Px,Py,ra,rb,Mx,My=0,Nx=0,Ny,slope;

/*let cordinates of P=(Px,Py),
 ratio in which P divides M and N be ra:rb,
cordinates of M be (Mx,My) and cordinates of N be (Nx,Ny)
slope is the slope of line MN  */

printf("enter the x and y cordinates of P respectively using space between then:\n");
scanf("%f %f",&Px,&Py);

printf("enter the ratio using space between then instead of colon:\n");
scanf("%f %f",&ra,&rb);

//we know that ratio formula is Px=(Mx*rb+Nx*ra)/(ra+rb),similar for y cordinates Py=(My*rb+Ny*ra)/(ra+rb)
// by rearranging the ratio formulas we get something like this

Mx=(Px*(ra+rb)-Nx*ra)/rb;

Ny=(Py*(ra+rb)-My*rb)/ra;

//now we get the cordinates of M and Y so slope of line MN will be following
slope=(Ny-My)/(Nx-Mx);

printf("M=(%.2f,0)\nN=(0,%.2f)\nslope=%.2f",Mx,Ny,slope);


return 0;}