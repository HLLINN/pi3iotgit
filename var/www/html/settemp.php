<?php
$con=mysqli_connect("localhost","your_ID","your_password","your_database_name");  //your mysql ID,password and database name
if (mysqli_connect_errno()) {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
}


$now= date('Ymdhis');
$id = $_GET['id'];
$temp = $_GET['temp'];
mysqli_query($con,"INSERT INTO temp (datetime,temp,userid)  //your database column
  VALUES ($now,$temp,$id)");  //write the data from these variables to your corresponding database coloumns

mysqli_close($con);
 echo "iottemp.com get it".", date time=".$now.", temp=".$temp."  id=".$id;
?>
