<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST["email"];
    $output = shell_exec("python send_otp.py " . escapeshellarg($email));
    echo "<pre>$output</pre>";
}
?>
