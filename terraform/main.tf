resource "aws_s3_bucket" "SamePointSimulation" {
  bucket = "SamePointSimulation_Bucket"

  tags = {
    Name        = lsvar.bucketname
    Environment = "Dev"
  }
}