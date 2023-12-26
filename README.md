# RS API

![MarineGEO circle logo](/docs/flowbe.png "MarineGEO logo")

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

### API Endpoints and Documentation 
1. Get article [Product]
    ```bash
    GET /api/get_article?contentid={content_id}
    ```
    Returns the article with the given id.
    Example: http://domain.com/api/get_article?content_id=2480569770059008227

2. Add user interaction [Product]
    ```bash
    GET /api/interaction(user_id: str &
                        event_type: str &
                        content_id: str &
                        session_id: str &
                        user_agent: str &
                        user_region: str &
                        user_country: str
    ```
    ###### event_type 'VIEW', 'LIKE', 'BOOKMARK', 'FOLLOW', 'COMMENT CREATED'  
}
    Adds a user interaction to the database.
    Example: http://domain.com/api/interaction?user_id=29888888888&event_type=VIEW&content_id=4109618890343020064&session_id=7899999999999&user_agent=Mozilla%20SPAM%20LINH%20TINH&user_region=US&user_country=USA


3. Get homepage articles [home]
    ```bash
    GET /api/recommend_homepage_articles?user_id={user_id}
    ```
    Returns the articles on the homepage.
    Example: http://domain.com/api/recommend_homepage_articles?user_id=-9150583489352258206

4. Get recommended articles (By Like button) [Product]
    ```bash
    GET /api/recommend_liked_articles?content_id={content_id}
    ```
    Returns the recommended articles for the user.
    Example: http://domain.com/api/recommend_liked_articles?content_id=2480569770059008227

5. Get recommended articles (By follow button) [Product]
    ```bash
    GET /api/recommend_followed_articles?author_person_id={author_person_id}
    ```
    Returns the recommended articles for the user.
    Example: http://domain.com/api/recommend_followed_articles?author_person_id=-2979881261169775358

6. Get recommended articles (related articles) [Product]
    ```bash
    GET /api/recommend_related_articles?user_id={user_id}
    ```
    Returns the recommended articles for the user.
    Example: http://domain.com/api/recommend_related_articles?userid=-9150583489352258206



