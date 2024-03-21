
# API Documentation

## Authentication
- `POST /api/token/` - Obtain a new JWT by passing username and password.
- `POST /api/token/refresh/` - Refresh an existing JWT.

## User Profile Endpoints
- `GET /users/gender/` - Retrieve the current gender of the authenticated user.
- `POST /users/gender/` - Update the gender of the authenticated user.
- `GET /users/age/` - Retrieve the current age of the authenticated user.
- `POST /users/age/` - Update the age of the authenticated user.
- `GET /users/weight/` - Retrieve the current weight of the authenticated user.
- `POST /users/weight/` - Update the weight of the authenticated user.

## Social Endpoints
- `GET /users/friend/` - Retrieve the friends list of the authenticated user.
- `POST /users/friend/` - Add or remove a friend for the authenticated user.

## Health Data Endpoints
- `GET /users/heartbeats/` - Retrieve the heartbeats data of the authenticated user.
- `POST /users/heartbeats/` - Submit new heartbeats data for the authenticated user.
- `GET /users/sleep_data/` - Retrieve the sleep data of the authenticated user.
- `POST /users/sleep_data/` - Submit new sleep data for the authenticated user.

### Detailed Endpoints Information

#### User Gender
- **GET `/users/gender/`**: Returns the gender information of the authenticated user.
- **POST `/users/gender/`**:
    - Request Body:
        ```json
        {
            "Gender": "M/F/O"
        }
        ```
    - Response: `{"success": "Gender updated successfully."}`

#### User Age
- **GET `/users/age/`**: Returns the age of the authenticated user.
- **POST `/users/age/`**:
    - Request Body:
        ```json
        {
            "Age": "<age_value>"
        }
        ```
    - Response: `{"success": "Age updated successfully."}`

#### User Weight
- **GET `/users/weight/`**: Returns the weight of the authenticated user.
- **POST `/users/weight/`**:
    - Request Body:
        ```json
        {
            "Weight": "<weight_value>"
        }
        ```
    - Response: `{"success": "Weight updated successfully."}`

#### Friends Management
- **GET `/users/friend/`**: Returns the friends list of the authenticated user.
- **POST `/users/friend/`**:
    - Request Body:
        ```json
        {
            "action": "add/delete",
            "friend_username": "<username>"
        }
        ```
    - Response: `{"message": "Friend added/removed successfully."}`

#### Heartbeat Data
- **GET `/users/heartbeats/`**: Returns the heartbeats data of the authenticated user.
- **POST `/users/heartbeats/`**:
    - Request Body:
        ```json
        {
            "timestamp": "<timestamp>",
            "beats_per_minute": "<bpm>"
        }
        ```
    - Response: `{"success": "Heartbeat data submitted successfully."}`

#### Sleep Data
- **GET `/users/sleep_data/`**: Returns the sleep data of the authenticated user.
- **POST `/users/sleep_data/`**:
    - Request Body:
        ```json
        {
            "start_time": "<start_time>",
            "end_time": "<end_time>"
        }
        ```
    - Response: `{"success": "Sleep data submitted successfully."}`
