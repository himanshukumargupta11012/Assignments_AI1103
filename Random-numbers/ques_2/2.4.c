#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include "../coeffs.h"
int main(){

    printf("%lf\n",mean("gau.dat"));
    printf("%lf\n",variance("gau.dat"));

    return 0;
}