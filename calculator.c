#include<stdio.h>
int main()
{ int a,b;
    printf("Enter value of a");
    scanf("%d",&a);
    printf("Enter value of b");
    scanf("%d",&b);
    printf("sum of %d and %d id %d\n",a,b,a+b);
    printf("difference between %d and %d is %d\n",a,b,a-b);
    printf("multiplication of %d and %d is %d\n",a,b,a*b);
    printf("division of %d by %d is %d\n",a,b,a/b);
    printf("square of the numbers %d and %d is %d and %d",a,b,a*a,b*b);
    return 0;
}
