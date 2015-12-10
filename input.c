#include<stdio.h>
#include<wiringPi.h>


int main()
{

	if(wiringPiSetupGpio() == -1)return 0;

	pinMode(20, INPUT);
	printf("Input GPIO20\n");
	
	if(1 == digitalRead(20))printf("ON\n");
	
	
	return 0;

}
