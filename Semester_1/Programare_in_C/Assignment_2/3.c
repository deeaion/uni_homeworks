#include<stdio.h>
#include<string.h>
int main()
{
int n,firstn,ultn,penn,last_two;
n=0;
while(n<=0||(n>=0&&n<=99)||n>=1000)
{	printf("\nPlease enter a 3 digit number!\n");
	printf("number= ");
	scanf("%d",&n);
			}
ultn=n%10;
penn=(n/10)%10;
last_two=n%100;
firstn=n/100;
char first[10],pen[10],ult[10],lastc[10];
switch (firstn)
{ case 1:
       strcpy(first,"one"); 
		break;
 case 2:
	strcpy(first,"two");
		break;
 case 3:
	strcpy(first,"three");
		break;
 case 4:
	strcpy(first,"four");
		break;
 case 5:
	strcpy(first,"five");
		break;
 case 6:
	strcpy(first,"six");
		break;
 case 7:
	strcpy(first,"seven");
		break;
 case 8:
	strcpy(first,"eight");
		break;
 case 9:
	strcpy(first,"nine");
		break;}
if(last_two==10)
	strcpy(lastc,"ten");
else if(last_two==11)
	strcpy(lastc,"eleven");
else if(last_two==12)
	strcpy(lastc,"twelve");
else if(13<=last_two&&last_two<=19)
	switch(last_two)
		{ 
		case 13:
        		strcpy(lastc,"thir");
                	break;
 		case 14:
        		strcpy(lastc,"four");
                		break;
 		case 15:
        		strcpy(lastc,"fifth");
                		break;
 		case 16:
        		strcpy(lastc,"six");
        		        break;
 		case 17:
        		strcpy(lastc,"seven");
                		break;
 		case 18:
        		strcpy(lastc,"eigh");
                		break;
 		case 19:
        		strcpy(lastc,"nine");
               		        break;}
else
	{
	switch(penn)
		{
 case 0:
	strcpy(pen,"");
			break;
 case 2:
        strcpy(pen,"twen");
                break;
 case 3:
        strcpy(pen,"thir");
                break;
 case 4:
        strcpy(pen,"four");
                break;
 case 5:
        strcpy(pen,"fif");
                break;
 case 6:
        strcpy(pen,"six");
                break;
 case 7:
        strcpy(pen,"seven");
                break;
 case 8:
        strcpy(pen,"eigh");
                break;
 case 9:
        strcpy(pen,"nine");
                break;		}
	switch(ultn)
{
case 1:
       strcpy(ult,"one"); 
		break;
 case 2:
	strcpy(ult,"two");
		break;
 case 3:
	strcpy(ult,"three");
		break;
 case 4:
	strcpy(ult,"four");
		break;
 case 5:
	strcpy(ult,"five");
		break;
 case 6:
	strcpy(ult,"six");
		break;
 case 7:
	strcpy(ult,"seven");
		break;
 case 8:
	strcpy(ult,"eight");
		break;
 case 9:
	strcpy(ult,"nine");
		break;}
						}

if(last_two>=10 && last_two<20)
	{if(last_two>=10 && last_two<13)
		printf("Number %d reads as:\n %s hundred and %s",n,first,lastc);
	if(last_two>=13 && last_two<20)
		printf("Number %d reads as:\n %s hundred and %steen",n,first,lastc);}
if(last_two>=20||last_two<10)
      {if(penn==0)
	printf("Number %d reads as:\n %s hundred and %s",n,first,ult);
      else
       printf("Number %d reads as:\n %s hundred %sty- %s",n,first,pen,ult); }

return 0;}