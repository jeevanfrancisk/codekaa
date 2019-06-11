#include <stdio.h>
#include <stdlib.h>
#include<math.h>

int main()
{
    int n,k,cube;
    scanf("%d %d",&n,&k);
    cube=pow(n,k);
    printf("%d",cube);
    return 0;
}
