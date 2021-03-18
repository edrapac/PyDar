<?php

// Filler HTML and function to return the current web server's basic information. Better than just showing a blank screen essentially
function getOSInformation()
 {
     if (false == function_exists("shell_exec") || false == is_readable("/etc/os-release")) {
         return null;
     }

      $os         = shell_exec('cat /etc/os-release');
     $listIds    = preg_match_all('/.*=/', $os, $matchListIds);
     $listIds    = $matchListIds[0];

      $listVal    = preg_match_all('/=.*/', $os, $matchListVal);
     $listVal    = $matchListVal[0];

      array_walk($listIds, function(&$v, $k){
         $v = strtolower(str_replace('=', '', $v));
     });

      array_walk($listVal, function(&$v, $k){
         $v = preg_replace('/=|"/', '', $v);
     });

      return array_combine($listIds, $listVal);
 }
$osInfo = getOSInformation();
?>

<!doctype html>
<html lang=en>
<head>
    <meta charset=utf-8>
    <title>PyDar Web Server</title> <!-- Any less python and we really ought to change this title lol -->
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="checker.js"></script>
    <div class="container">
        <section>
            <pre>
OS: <?php echo $osInfo['pretty_name']; ?><br/>
<!-- Apache: <?//php echo apache_get_version(); ?><br/>
PHP Version: <?//php echo phpversion(); ?><br/> Disabled for testing, re-enable these fields later-->
            </pre>
        </section>
    </div>
    <div class="container">
      <textarea id="target" cols="122" rows="20">Loading...</textarea>
    </div>
    <div class='container'>

                <?php
        if(array_key_exists('left', $_POST)) { 
            left(); 
        } 
        else if(array_key_exists('right', $_POST)) { 
            right(); 
        } 
        function left() { 
            $output=shell_exec('sudo /usr/bin/python3 /home/pi/PyDar/move_left.py');
	    echo $output;
	} 
        function right() { 
            $output=shell_exec('airport -s > log.txt'); //changed for testing using MacOS, make sure to re enable the pyDar scripts in master
	    echo $output;
	} 
    ?>
        <form method="post" action="index.php">
            <input type="submit" name="left" class="button" value="Left">
            <input type="submit" name="right" class="button" value="Right">
        </form>
    </div>
</body>
</html>
