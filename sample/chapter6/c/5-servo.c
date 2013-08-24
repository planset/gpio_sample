/* 
 * wiringPiのsoftServo機能を使って、GPIO18に接続したサーボモーターを動かす
 * 
 * 使用ライブラリ: wiringPi
 * コンパイル方法: cc -o 5-servo 5-servo.c -lwiringPi
 */
#include <wiringPi.h>
#include <softServo.h>

#define SERVO_PORT 18		/* GPIO18 */

int main (void) {
	int i;

	//初期化
	if(wiringPiSetupGpio() == -1) return 1;
	softServoSetup (SERVO_PORT, -1, -1, -1, -1, -1, -1, -1);

	for (i=-250; i<1250; i+=100) {
		softServoWrite (SERVO_PORT, i);
		delay(100);
	}

	return 0;
}
