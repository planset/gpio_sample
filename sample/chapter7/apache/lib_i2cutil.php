<?php

//i2cデバイスの設定（Rev.1基板の場合は1にする）
define("I2CBUS",1);

//i2cget/i2csetコマンドのパス設定
define("I2CGET_COMMAND","/usr/sbin/i2cget");
define("I2CSET_COMMAND","/usr/sbin/i2cset");

//I2Cポートにデータを送信する
function i2c_set($caddr,$daddr,$data) {
	if(! is_array($data)) $data = array($data);
	if(count($data) > 0) {
		$dstr = "";
		foreach ($data as $num) {
			$dstr .= sprintf("0x%02x ",$num);
		}
		$mode = (count($data) < 2) ? "b" : "i";
		$command = sprintf("%s -y %d 0x%02x 0x%02x %s %s",I2CSET_COMMAND,I2CBUS,$caddr,$daddr,$dstr,$mode);
		exec($command);
	}
	return 0;
}

//I2Cポートからデータを読み込む
function i2c_get($caddr,$daddr) {
	$data = null;
	$mode = "b";
	$command = sprintf("%s -y %d 0x%02x 0x%02x %s",I2CGET_COMMAND,I2CBUS,$caddr,$daddr,$mode);
	$fp = popen($command,"r");
	if($fp) {
		$buff = chop(fgets($fp));
		if(eregi("^0x([0-9a-f]+)$",$buff,$tm)) {
			$data = hexdec($tm[1]);
		}
		pclose($fp);
	}
	return $data;
}

?>
