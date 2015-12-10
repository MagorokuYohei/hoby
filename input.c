#include<stdio.h>
#include<wiringPi.h>

#define GPIO20 20

int main()
{

	if(wiringPiSetupGPIO() == -1) return 0;

	pinMode(GPIO20, INPUT);
	printf("Input GPIO20\n");
	while(1)
	{
	
	if(1 == digitalRead(GPIO20))break;
	
	}
	return 0;

}
