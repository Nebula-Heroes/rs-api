# Luxey API

This is an API for Luxey, a platform for luxury bag transactions. The API provides various endpoints to retrieve transaction data, average prices, and market indices.

## Getting Started
### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Nebula-Heroes/rs-api
    ```
2. Load environment variables from .env file:

    ```bash
    export $(cat .env | xargs)
    ```

2. Build and run the Docker containers:
    ```bash
    docker-compose up --build -d
    ```

This command will build the Docker image for the Luxey API and start the container.

4. Access the API:

The API will be available at http://localhost:8818. You can use tools like cURL or Postman to make requests to the API endpoints.
