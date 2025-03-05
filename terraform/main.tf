terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.21.0"
    }
    google-beta = {
      source  = "hashicorp/google-beta"
      version = "6.21.0"
    }
  }

  backend "local" {
    path = "../terraform.tfstate"
  }
}

provider "google" {
  project = var.project
  region  = var.region
}

provider "google-beta" {
  project = var.project
  region  = var.region
}
