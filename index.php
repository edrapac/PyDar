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
    <title>PyDar Web Server</title>
    <link rel="stylesheet" href="./css/styles.css">
</head>

<body>
    <script src="./js/jquery-3.6.0.js"></script>
    <script src="checker.js"></script>
    <div class="container">
        <section>
            <pre>
<br>OS: <?php echo $osInfo['pretty_name']; ?></br>
<br>Welcome to PyDar! Usage for the buttons is below</br>
<br>Left/Right: Issue the "swivel left/right" commands respectively</br>
<br>Scan: Scans for available wifi networks, please note that this can take between 30s - 2 minutes to complete, be patient!</br>
            </pre>
        </section>
    </div>
    <div class="container">
      <textarea id="target" cols="122" rows="20">Loading...</textarea>
    </div>
    <div class='container'>

                <?php
        if(isset($_POST['left'])) { 
            left(); 
        } 
        else if(isset(($_POST['right']))) { 
            right(); 
        }
        else if(isset(($_POST['stop']))) { 
            stop(); 
        } 
        else if(isset($_POST['sniff'])) { 
            sniff(); 
        }

        // functions for controlling rotation
        function left() { 
            $output=shell_exec('/usr/bin/python3 /home/pi/PyDar/servo_scripts/leftRight.py l');
	   echo $output;
	} 
        function right() { 
            $output=shell_exec('/usr/bin/python3 /home/pi/PyDar/servo_scripts/leftRight.py r');
	    echo $output;
	}
        function stop() { 
            $output=shell_exec('/usr/bin/python3 /home/pi/PyDar/servo_scripts/leftRight.py s');
      echo $output;
  }
        function sniff() {
            $output=shell_exec('sudo /usr/bin/python3 ./sniffer.py');

    }
    ?>
        <form method="post" action="index.php">
            <input type="submit" name="left" class="button" value="Rotate Left">
            <input type="submit" name="right" class="button" value="Rotate Right">
            <input type="submit" name="stop" class="button" value="Stop Rotation">
            <input type="submit" name="sniff" class="button" value="Scan For Available Networks">
        </form>
    </div>
</body>
</html>
