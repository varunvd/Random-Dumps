#include<stdio.h>
#include<string.h>
//This I should take care 
void fun(int const *ptr)
{
    *((int *)ptr)=20;
    /*
        First we are converting the ptr to integer pointer
        Then the value stored at that position is changed
        If you take a close look you are changing  the 
        value of the constant. Otherwise it is not possible.
   */
}
int main()
{
        int const j=10;
        int const k=50;
        int const *pointer;
        int a=50.55555;
        fun(&j);
        // This statement will create an error k=40;
        //
        pointer = &k;
        *((int *)pointer) = 30;
        printf("%d\n",j);
        printf("%d\n",k);
        printf("%f\n",(float)a);
        return 0;
}
