<?php
//
// このプログラムは I2C液晶LCD SB1602BW 専用です
//
require("lib_i2cutil.php");

define("LCD_I2CDADDR",0x3e);	//LCDのアドレス
define("COLUMN",16);			//LCDの桁数
define("CONTRAST",8);			//LCDのコントラスト（0〜15）

//WiringPiのgpioコマンドを使って/dev/i2c-*の読み書きができるように設定する
exec("/usr/local/bin/gpio load i2c");

//LCDの初期化
$fcnt = 0x70 | (CONTRAST & 0x0f);
i2c_set(LCD_I2CDADDR, 0, array(0x38,0x39,0x14,$fcnt,0x5f,0x6a) );
usleep(300000);
i2c_set(LCD_I2CDADDR, 0, array(0x0c,0x01) );
usleep(300000);
i2c_set(LCD_I2CDADDR, 0, 0x06 );
usleep(300000);

//引数の文字を半角英数字にする
$text = (isset($_REQUEST['text'])) ? $_REQUEST['text'] : "";
$text = mb_convert_kana($text,"askh","UTF-8");
$text = mb_convert_encoding($text,"SJIS","UTF-8");
$text = str_pad($text,COLUMN*2," ");

//文字を数値に変換する
$out = array();
for ($i=0; $i<COLUMN*2; $i++) {
	$out[] = ord( substr($text,$i,1) );
}

//文字を送信する（１列目：1〜16文字目を出力）
i2c_set(LCD_I2CDADDR, 0, 0x80 );	//位置
i2c_set(LCD_I2CDADDR, 0x40, array_slice($out,0,COLUMN) );	//出力

//文字を送信する（２列目：16〜32文字目を出力）
i2c_set(LCD_I2CDADDR, 0, 0xc0 );	//位置
i2c_set(LCD_I2CDADDR, 0x40, array_slice($out,COLUMN,COLUMN) );	//出力

?>
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>液晶モジュール - Raspberry Piで遊ぼう</title>
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<link rel="stylesheet" href="style.css" media="screen">
<script type="text/javascript">
</script>
</head>
<body>
<div id="wrapper">

<header>
	<div class="header">
		I2C液晶LCDモジュール<br />
	</div>
</header>

<div id="contents">
	<section>
		<div class="wmain">
			表示したい文字を半角英数字、カタカナ16文字以内で入力してください。
			<form action="<?=htmlspecialchars($_SERVER["PHP_SELF"])?>" method="GET">
			<input type="text" name="text" size="32" maxsize="32" />
			<input type="submit" value="送信" />
			</form>
		</div>
	</section>
	<section>
		<div class="wmain">
			I2C対応のI2C液晶LCD SB1602BW に文字を出力します。<br />
		</div>
	</section>
</div>

<footer>
	<div id="footer">
		Raspberry Piで遊ぼう<br />
	</div>
</footer>

</div>
</body>
</html>
