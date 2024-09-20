# RideApp

A simple ride application that calculates the distance, price, and directions between two locations.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/RideApp.git
    cd RideApp
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python app/main.py
    ```

## Docker

1. Build the Docker image:
    ```bash
    docker build -t rideapp .
    ```

2. Run the Docker container:
    ```bash
    docker run -p 80:80 rideapp
    ```

## GCP Deployment

1. Authenticate with GCP:
    ```bash
    gcloud auth login
    ```

2. Set the project:
    ```bash
    gcloud config set project YOUR_PROJECT_ID
    ```

3. Deploy to Cloud Run:
    ```bash
    ./gcp_deploy.sh
    ```

Replace `YOUR_PROJECT_ID` and `YOUR_REGION` with your actual GCP project ID and region.
