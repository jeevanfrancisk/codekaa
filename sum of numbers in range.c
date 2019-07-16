#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
int n,sum=0,k,arr[50];
  scanf("%d %d",&n,&k);
for(int i=1;i<n;i++)
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
