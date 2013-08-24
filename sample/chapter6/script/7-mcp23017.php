#!/usr/bin/php
<?php
require("lib_i2cutil.php");
//
// MCP23017のGPA0(pin21)に入力ボタン、GPB0(pin1)にLEDを接続して、
// ボタンが押されたらLEDを高速で点滅させるサンプル
//

//MCP23017のアドレス
define("EXP_I2CDADDR",0x20);

//MCP23017のレジスタ
define("IODIRA",  0x00);
define("IODIRB",  0x01);
define("GPPUA",   0x0C);
define("GPIOA",   0x12);
define("GPIOB",   0x13);

//BANK Aの入出力設定(IODIRA)：GPA0(pin21)ほか全pinをinputにする
i2c_set(EXP_I2CDADDR, IODIRA, 0b11111111);

//BANK Bの入出力設定(IODIRB)：GPB0(pin1)のみoutputにして他はinputにする
i2c_set(EXP_I2CDADDR, IODIRB, 0b11111110);

//BANK Aのプルアップ設定を行う：GPA0(pin21)のみをpullupする
i2c_set(EXP_I2CDADDR, GPPUA, 0b00000001);

//GPB0(pin1)のLEDを消灯する
i2c_set(EXP_I2CDADDR, GPIOB, 0b00000000);

//GPA0(pin21)のボタンが押されるのを待つ
while (true) {
	$gpioa = i2c_get(EXP_I2CDADDR, GPIOA);
	if(($gpioa & 0b00000001) == 0) {	//ボタンの判定（押されたときは0になる）
		echo "PUSHED!!\n";
		blink_led();
	}
	usleep(50000);	//50ms
}
exit(0);

//GPB0(pin1)のLEDを5回点滅させる
function blink_led() {
	for ($i=0; $i<5; $i++) {
		i2c_set(EXP_I2CDADDR, GPIOB, 0b00000001);	//点灯
		usleep(100000);
		i2c_set(EXP_I2CDADDR, GPIOB, 0b00000000);	//消灯
		usleep(100000);
	}
}

?>
