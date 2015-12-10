#include<stdio.h>
#include<wiringPi.h>

int main(){

if(wiringPiSetupGpio() == -1)return 1;

pinMode(20,INPUT);
pinMode(26,INPUT);
pinMode(21,OUTPUT);

while(1){
if(digitalRead(20) == 1){
			digitalWrite(21, 1);
		}else{
			digitalWrite(21, 0);
		}

if(digitalRead(26) == 1)break;

}


digitalWrite(21, 0);
return 0;

}
