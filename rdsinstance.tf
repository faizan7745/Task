resource "aws_db_instance" "my_db_instance" {
  instance_class = "db.t2.micro"
  allocated_storage = 10
  engine = "postgres"
  engine_version = "12.6"
  identifier = "mydbinstance"
  username = "admin"
  password = "your_password"
  db_subnet_group_name = "default"
}
