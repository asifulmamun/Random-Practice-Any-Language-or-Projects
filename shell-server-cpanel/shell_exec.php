<?php

// Run Shell code on you cpanel server and get information, also you can change your command from variable and try your linux command on your server.

    $output = shell_exec('ls -ls');

    echo "<pre>$output</pre>";
    
    $output = shell_exec('cd ..');

    echo "<pre>$output</pre>";

    $output = shell_exec('ls -ls');

    echo "<pre>$output</pre>";
?>