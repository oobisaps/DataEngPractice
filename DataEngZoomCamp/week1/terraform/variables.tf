variable "credentials" {
  description = "Service account credentials"
  default     = null
}

variable "project" {
  default = "ProjectID"
}

variable "region" {
  default = "us-central1"
}

variable "gcs_bucket_name" {
  default = "dataeng-zoomcamp-demo-bucket"
}

variable "location" {
  default = "US"
}

variable "bq_dataset_name" {
  default = "dataeng_zoomcamp_demo_dataset"
}