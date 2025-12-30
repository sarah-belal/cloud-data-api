terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.3"
    }
  }
}

resource "local_file" "example" {
  filename = "demo.txt"
  content  = "This simulates creating a resource with Terraform!"
}
