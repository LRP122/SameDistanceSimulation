resource "aws_s3_bucket" "SamePointSimulation" {
  bucket = "SamePointSimulation_Bucket"

  tags = {
    Name        = var.bucketname
    Environment = "Dev"
  }
}