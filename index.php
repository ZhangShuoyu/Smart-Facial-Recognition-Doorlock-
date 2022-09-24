<?php 
exec("gpio mode 0 out");
if (isset($_GET['lock'])) {	
	if($_GET['lock'] == 1) {
		exec("/usr/lib/python.exe lock.py");
	}
}
?>
