terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# Import other resource configurations
module "s3_bucket" {
  source = "./s3_bucket"
}

module "rds_instance" {
  source = "./rds_instance"
}

module "lambda_function" {
  source = "./lambda_function"
}

# Add other resources as required
