variable "aws_region" {
  description = "AWS region to create resources in"
  type        = string
  default     = "us-east-1"
}

variable "bucket_name" {
  description = "Name of the S3 bucket"
  type        = string
}

variable "enable_versioning" {
  description = "Enable bucket versioning"
  type        = bool
  default     = true
}

variable "enable_kms" {
  description = "Enable SSE-KMS encryption instead of SSE-S3"
  type        = bool
  default     = false
}

variable "kms_key_id" {
  description = "KMS Key ARN or Alias (if enable_kms = true)"
  type        = string
  default     = null
}

variable "cors_allowed_origins" {
  description = "List of allowed CORS origins"
  type        = list(string)
  default     = ["*"]
}
