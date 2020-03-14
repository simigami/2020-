<?php
$id=$_POST['id'];
$pw=$_POST['pw'];
$connect = mysqli_connect("localhost","root","mysql","testserver");
$query = "select * from userinfo where userid='$id'";
$query2 = "insert into userinfo (userid,userpw) VALUES ('$id','$pw')";
if($id == "" || $pw == ""){
?>
	<script>alert("You have to write ID AND PASSWORD");
		history.back();
	</script>
<?php
}
else{
$result = mysqli_query($connect,$query);
$num = mysqli_num_rows($result);
if($num == 0){
	$result2 = mysqli_query($connect,$query2);
?>
	<script>alert("Register Success");
		location.href="./login.html";
	</script>
<?php
}
else{
?>
	<script>alert("Register Failed ID Already exsists");
		history.back();
	</script>
<?php
}
}
?>
