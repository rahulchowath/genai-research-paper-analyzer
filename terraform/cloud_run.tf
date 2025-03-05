module "backend_cloudrun" {
  source           = "github.com/GoogleCloudPlatform/cloud-foundation-fabric//modules/cloud-run?ref=v38.0.0"
  name             = "${var.identifier}-backend"
  project_id       = var.project
  region           = var.region
  ingress_settings = "all"
  containers = {
    "frontend" = {
      image = "${var.region}-docker.pkg.dev/${var.project}/docker-repository/backend:latest"
      env = {
        PROJECT = var.project
        REGION  = var.region
      }
      resources = {
        limits = {
          cpu    = "1"
          memory = "4Gi"
        }
      }
    }
  }
  revision_annotations = {
    autoscaling = {
      max_scale = 1
      min_scale = 1
    }
  }
  service_account = var.service_account
}

module "frontend_cloudrun" {
  source           = "github.com/GoogleCloudPlatform/cloud-foundation-fabric//modules/cloud-run?ref=v38.0.0"
  name             = "${var.identifier}-frontend"
  project_id       = var.project
  region           = var.region
  ingress_settings = "all"
  containers = {
    "frontend" = {
      image = "${var.region}-docker.pkg.dev/${var.project}/docker-repository/frontend:latest"
      env = {
        BACKEND_URL = module.backend_cloudrun.service.status.0.url
      }
      resources = {
        limits = {
          cpu    = "1"
          memory = "4Gi"
        }
      }
    }
  }
  revision_annotations = {
    autoscaling = {
      max_scale = 1
      min_scale = 1
    }
  }
  service_account = var.service_account
}
