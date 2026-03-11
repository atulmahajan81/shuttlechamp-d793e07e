# API Reference

This document provides a comprehensive reference for all API endpoints available in the ShuttleChamp application.

## Authentication Endpoints

### Register a New User
- **POST** `/api/v1/auth/register`
- **Description**: Register a new user.
- **Request Body**:
  ```json
  {
    "email": "string",
    "password": "string",
    "role": "string"
  }
  ```
- **Response**:
  ```json
  {
    "message": "string"
  }
  ```

### Login User
- **POST** `/api/v1/auth/login`
- **Description**: Login user and return tokens.
- **Request Body**:
  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```
- **Response**:
  ```json
  {
    "access_token": "string",
    "refresh_token": "string"
  }
  ```

### Refresh Access Token
- **POST** `/api/v1/auth/refresh`
- **Description**: Refresh access token using refresh token.
- **Request Body**:
  ```json
  {
    "refresh_token": "string"
  }
  ```
- **Response**:
  ```json
  {
    "access_token": "string"
  }
  ```

### Logout User
- **POST** `/api/v1/auth/logout`
- **Description**: Logout user and invalidate tokens.
- **Request Body**: `{}`
- **Response**:
  ```json
  {
    "message": "string"
  }
  ```

## Tournament Endpoints

### Create a Tournament
- **POST** `/api/v1/tournaments`
- **Description**: Create a new tournament.
- **Request Body**:
  ```json
  {
    "name": "string",
    "location": "string",
    "start_date": "date",
    "end_date": "date"
  }
  ```
- **Response**:
  ```json
  {
    "id": "UUID",
    "name": "string"
  }
  ```

### List All Tournaments
- **GET** `/api/v1/tournaments`
- **Description**: List all tournaments.
- **Query Parameters**:
  - `page`: integer
  - `limit`: integer
  - `search`: string
- **Response**:
  ```json
  {
    "tournaments": "array"
  }
  ```

### Get Tournament Details
- **GET** `/api/v1/tournaments/{tournament_id}`
- **Description**: Get tournament details.
- **Response**:
  ```json
  {
    "id": "UUID",
    "name": "string",
    "location": "string"
  }
  ```

### Update Tournament
- **PUT** `/api/v1/tournaments/{tournament_id}`
- **Description**: Update tournament details.
- **Request Body**:
  ```json
  {
    "name": "string",
    "location": "string",
    "start_date": "date",
    "end_date": "date"
  }
  ```
- **Response**:
  ```json
  {
    "id": "UUID",
    "name": "string"
  }
  ```

### Delete Tournament
- **DELETE** `/api/v1/tournaments/{tournament_id}`
- **Description**: Delete a tournament.
- **Response**:
  ```json
  {
    "message": "string"
  }
  ```

### Register a Player
- **POST** `/api/v1/players`
- **Description**: Register a player for a tournament.
- **Request Body**:
  ```json
  {
    "tournament_id": "UUID",
    "player_name": "string"
  }
  ```
- **Response**:
  ```json
  {
    "id": "UUID",
    "player_name": "string"
  }
  ```