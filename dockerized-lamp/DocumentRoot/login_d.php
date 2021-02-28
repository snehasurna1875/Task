<?php
$servername = "dockerized-lamp_mysql_1";
$username = "surana";
$password = "surana";
$db_name="details";
$tablename="logininfo";


// Create connection
$conn = new mysqli($servername,$username, $password,$db_name);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
echo "Database Connected successfully";
echo "<br>";
$myusername=$_POST['user'];
$mypassword=$_POST['pass'];

$sql="select * from $tablename where username='$myusername' and password='$mypassword'";

$result=mysqli_query($conn,$sql); 

$count=mysqli_num_rows($result);

if ($count == 1)
{
echo "YOU ARE LOGGED IN SUCCESSFULLY ";
}

else 
{
echo "MAY BE YOUR USERNAME OR PASSWORD IS NOT CORRECT ";
}
?>

