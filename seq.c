#include <stdio.h>


int fibo(int);

int main(void){


int n = 10;
printf("%d",fibo(n));
getchar();
return 0;

}

int fibo(int n){
    if (n<=1){
        return n;
    }
 return fibo(n-1) + fibo(n-2);

}
