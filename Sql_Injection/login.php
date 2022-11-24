<?php
session_start();
include_once 'database.php';

  if(isset($_POST["login"])){
	 $username = $_POST["username"]; 
	 $password =  $_POST["password"]; 
	  
	  $login = mysqli_query($conn, "SELECT * FROM users WHERE username = '$username' AND password = '$password'");
	  if(mysqli_num_rows($login) == 0){
          die('Username and Password are not valid!');    
    }else if(isset($_POST["login"]) && isset($_POST["remember"])){
     $username = $_POST["username"]; 
	 $password =  $_POST["password"];   
          
     $login = mysqli_query($conn, "SELECT * FROM users WHERE username = '$username' AND password = '$password'");                 
     setcookie('id', 'administrator', time()+250);  
     $_SESSION['login'] = true;
     header('Location: index.php');
  }else{
        $_SESSION['login'] = true;
        header('Location: index.php');
      }
}
?>


<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Login Page</title>
    </head>
    
 <body>
     <h1>Please enter your details!</h1>
    <form method="post" action="">
    <label for="username">Username :</label>
        <input type="text" id="username" name="username">
        <br>
        <br>
        <label for="password">Password :</label>
        <input type="password" id="password" name="password">
        <br>
        <br>
        <input type="checkbox" id="remember" name="remember">
        <label for="remember">Remember me</label>
        <br>
        <br>
        <button type="submit" name="login">login</button>
     </form>
    </body>   
</html>    