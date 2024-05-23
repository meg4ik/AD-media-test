# AD-media-test
 
### Task

'web analytics tracker for advertising campaigns. The tracker monitors clicks on advertising links and conversions to the landing page. It also stores information about the user who clicked or navigated.'

Languages: TypeScript(JS) and Python

Backend framework: Django, DRF

Frontend framework: React.js

UI: Tailwind CSS

Environment: Docker, Docker Compose

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/meg4ik/AD-media-test
    ```

2. Change directory to the project folder:

    ```bash
    cd AD-media-test

    ```

3. Create .env file based on .env_example in /BACK directory

4. Build and run the Docker containers:

    ```bash
    docker-compose up --build
    ```

5. If everything is successful, access to the frontend application will be at http://127.0.0.1:3000/

### Endpoints


#### Backend Endpoints

Campaigns
```sh
GET /api/campaigns/ - List all campaigns
GET /api/campaigns/{id}/ - Retrieve a specific campaign
POST /api/campaigns/ - Create a new campaign
DELETE /api/campaigns/{id}/ - Delete a specific campaign
```

Offers
```sh
GET /api/offers/ - List all offers
GET /api/offers/{id}/ - Retrieve a specific offer
POST /api/offers/ - Create a new offer
DELETE /api/offers/{id}/ - Delete a specific offer
```

Leads
```sh
GET /api/leads/ - List all leads
GET /api/leads/{id}/ - Retrieve a specific lead
```

Clicks
```sh
GET /api/clicks/ - List all clicks
GET /api/clicks/{id}/ - Retrieve a specific click
```

Graphs
```sh
GET /api/graphs/clicks/ - Get clicks statistics for a given campaign or offer
GET /api/graphs/revenue/ - Get revenue statistics for a given campaign or offer
```

Swagger and Redoc
```sh
GET /swagger/ - Swagger UI documentation
GET /redoc/ - Redoc documentation
```