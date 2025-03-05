variable "project" {
  description = "Google Cloud project ID"
  type        = string
}

variable "region" {
  description = "Google Cloud region used for all resources"
  type        = string
}

variable "service_account" {
  description = "SA used for terraform deployment"
  type        = string
}

variable "identifier" {
  description = "Prefix added to deployed Cloud Run instances"
  type        = string
}
