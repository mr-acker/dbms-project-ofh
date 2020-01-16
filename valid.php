 <?php
$firstname = $_POST['firstname'];-->-->
$lastname = $_POST['lastname'];
$username = $_POST['username'];
$password = $_POST['password'];
$passwordconf = $_POST['passwordconf'];
$email = $_POST['email'];
$securityq = $_POST['securityq'];
$qanswer = $_POST['quantity'];

if(empty($firstname) || empty($lastname) || empty($username) || empty($password) || empty($passwordconf) || empty($email) || empty($securityq) || empty($qanswer))
{
    echo "You did not fill out the required fields.";
}?>