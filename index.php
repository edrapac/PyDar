<?php

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
    <title>Hello World from Docker-LA-P</title>

    <style>
        @import 'https://fonts.googleapis.com/css?family=Montserrat|Raleway|Source+Code+Pro';

        body { font-family: 'Raleway', sans-serif; }
        h2 { font-family: 'Montserrat', sans-serif; }
        pre {
            font-family: 'Source Code Pro', monospace;

            padding: 16px;
            overflow: auto;
            font-size: 85%;
            line-height: 1.45;
            background-color: #f7f7f7;
            border-radius: 3px;

            word-wrap: normal;
        }

        .container {
            max-width: 1024px;
            width: 100%;
            margin: 0 auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <section>
            <pre>
OS: <?php echo $osInfo['pretty_name']; ?><br/>
Apache: <?php echo apache_get_version(); ?><br/>
PHP Version: <?php echo phpversion(); ?><br/>
            </pre>
        </section>
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
            shell_exec('sudo pinout > test'); 
        } 
        function right() { 
            shell_exec('touch right'); 
        } 
    ?>
        <form method="post" action="index.php">
            <input type="submit" name="left" class="button" value="Left">
            <input type="submit" name="right" class="button" value="Right">
        </form>
    </div>
</body>
</html>
