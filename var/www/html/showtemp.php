<?php
$con=mysqli_connect("localhost","your_ID","your_password","your_database_name");//your mysql ID,password and database name
if (mysqli_connect_errno()) {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
$result = mysqli_query($con,"SELECT * FROM temp");

echo "<table border='1'>
<tr>
<th>Date Time</th>
<th>Temperature</th>
<th>user ID </>
</tr>";
while($row = mysqli_fetch_array($result))  {
  echo "<tr>";
  echo "<td>" . $row['datetime'] . "</td>";//your database column
  echo "<td>" . $row['temp'] . "</td>";//your database column
  echo "<td>" . $row['userid'] . "</td>";//your database column
  echo "</tr>";
}
echo "</table>";
mysqli_close($con);
?>

