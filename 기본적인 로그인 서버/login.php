<?php
session_start();
$id = $_POST['id'];
$pw = $_POST['pw'];
$connect = mysqli_connect("localhost","root","mysql","testserver");
$query = "select * from userinfo where userid='$id'";
$result = mysqli_query($connect,$query);
$row = mysqli_fetch_assoc($result);
if($pw === $row['userpw']){
	$_SESSION['id'] = $id;
?>	
	<script>alert("login success");
		location.href="./main.php";
	</script>
<?php
}
else{
?>
	<script>alert("login failed");
		history.back();
	</script>
<?php
}
?>
