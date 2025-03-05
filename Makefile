include env.sh
export

#################################################################################
# COMMANDS                                                                      #
#################################################################################

.PHONY: tf-init
tf-init: # Initialise Terraform
	cd terraform && terraform init -migrate-state

.PHONY: tf-plan
tf-plan: # Display a terraform plan for the deployment
	cd terraform && terraform plan \
	-var 'project=${PROJECT}' \
	-var 'region=${REGION}' \
	-var 'service_account=${SA}' \
	-var 'identifier=${IDENTIFIER}'

.PHONY: tf-apply
tf-apply: # Deploy all infrastructure
	cd terraform && terraform apply \
	-var 'project=${PROJECT}' \
	-var 'region=${REGION}' \
	-var 'service_account=${SA}' \
	-var 'identifier=${IDENTIFIER}'

.PHONY: tf-destroy
tf-destroy: # Destroy all infrastructure
	cd terraform && terraform destroy

.PHONY: install-backend
install-backend: # Setup and install poetry dependencies for backend
	cd backend && poetry install

.PHONY: build-backend
build-backend: # Build docker container for backend (automatically pushes to artifact registry)
	cd backend &&\
	gcloud builds submit --project ${PROJECT} --config cloudbuild.yaml --region ${REGION} .

.PHONY: install-backend
install-backend: # Setup and install poetry dependencies for backend
	cd backend &&\
	pip install poetry==1.8.2 &&\
	poetry lock --no-update &&\
	poetry install

.PHONY: run-backend
run-backend: # Run backend locally
	cd backend &&\
	poetry run python -m uvicorn src.app:app --reload --port=8000

.PHONY: install-frontend
install-frontend: # Setup and install poetry dependencies for frontend
	cd frontend && poetry install

.PHONY: build-frontend
build-frontend: # Build docker container for frontend (automatically pushes to artifact registry)
	cd frontend &&\
	gcloud builds submit --project ${PROJECT} --config cloudbuild.yaml --region ${REGION} .

.PHONY: install-frontend
install-frontend: # Setup and install poetry dependencies for frontend
	cd frontend &&\
	pip install poetry==1.8.2 &&\
	poetry lock --no-update &&\
	poetry install

.PHONY: run-frontend
run-frontend: # Run frontend locally
	cd frontend &&\
	poetry run python src/app.py
