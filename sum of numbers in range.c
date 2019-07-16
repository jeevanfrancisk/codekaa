#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
  
{
int f,sum=0,k,arr[50];
  scanf("%d %d",&f,&k);
for(int i=1;i<f;i++)
{
  scanf("%d\t",&arr[i]);
}
 for(int i=1;i<=k;i++)
 {
   sum=sum+arr[i];
 }
        
  printf("%d",sum);
return 0;
}
