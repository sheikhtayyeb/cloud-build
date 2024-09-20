#!/bin/bash

# Authenticate with GCP
gcloud auth login

# Set the project
gcloud config set project rhic-innovation

# Build the Docker image
gcloud builds submit --tag gcr.io/rhic-innovation/rideapp

# Deploy to Cloud Run
gcloud run deploy rideapp --image gcr.io/rhic-innovation/rideapp --platform managed --region us-central1 --allow-unauthenticated
