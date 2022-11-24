<?php
include_once "database.php";
session_start();
$results = mysqli_query($conn, "SELECT * FROM posts");

if(!isset($_SESSION["login"])){
	header("Location: login.php");
	exit;
}?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Dashboard</title>
    </head> 
<body>
   <h1>Hello!</h1> 
    <?php foreach($results as $data): ?>
    <p>Where do you get your coffee from : <?php echo $data['coffee']; ?></p>
    <p>Where do you get your tea from : <?php echo $data['tea']; ?></p>
    <p>Where do you get your orange from : <?php echo $data['orange']; ?></p>
    <?php endforeach; ?>
     <a href="logout.php">Logout</a>
</body>
</html>