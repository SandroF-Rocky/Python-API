<?php

    $html_template = '
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <form action="" method="post" enctype="multipart/form">
            <input type="text" value="{VALUE_ESTADO}" placeholder="Estado" name="estado"><br>
            <input type="submit" value="Greet">
        </form> 
    </body>
    </html>';

    $input_estado = (array_key_exists("estado", $_POST)) ? $_POST['estado'] : "";


    $html_output = str_replace("{VALUE_ESTADO}", $input_estado, $html_template);


    echo $html_output;


    $greeter_link = "http://localhost/codigos_pessoais/PHP%20+%20PYTHON/getCities.py?estado=" . $input_estado;
    $greeter_link = str_replace(" ", "%20", $greeter_link);
    $greeter_data = file_get_contents($greeter_link);

    echo "<br><br>" . $greeter_data;

?>


