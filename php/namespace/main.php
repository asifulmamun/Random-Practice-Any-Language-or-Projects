<?php

    // File included
    require_once './munna.php';
    require_once './shaun.php';

    // // Try with only namesapce only
    //     $frnd_mnna = new nmspc\munna\Myclass;
    //     $frnd_shn = new nmspc\shaun\Myclass;

    //     echo $frnd_mnna->name; 
    //     echo '<br>' . $frnd_shn->name;



    // // Another System
    //     use nmspc\munna\Myclass as munna;
    //     use nmspc\shaun\Myclass as shaun;

    //     $munna = new munna;
    //     $shaun = new shaun;
    
    //     echo $munna->name;
    //     echo '<br>' . $shaun->name; 
    

    // // Another System
    //     use nmspc\munna\Myclass;
    //     use nmspc\shaun\Myclass as shaun;

    //     $munna = new Myclass;
    //     $shaun = new shaun;
    
    //     echo $munna->name;
    //     echo '<br>' . $shaun->name; 


    // Another System
        use nmspc\munna\Myclass as munna;
        use nmspc\shaun\Myclass;

        $munna = new munna;
        $shaun = new Myclass;

        echo $munna->name;
        echo '<br>' . $shaun->name; 


