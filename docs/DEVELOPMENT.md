# Development Guide

## Local Development Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/ShuttleChamp.git
   cd ShuttleChamp
   ```

2. **Install Dependencies**
   - **Backend**
     ```bash
     cd backend
     pip install -r requirements.txt
     ```
   - **Frontend**
     ```bash
     cd frontend
     npm install
     ```

3. **Start the Development Server**
   - **Backend**
     ```bash
     uvicorn main:app --reload
     ```
   - **Frontend**
     ```bash
     npm run dev
     ```

## Running Tests

- **Backend Tests**
  ```bash
  pytest
  ```
- **Frontend Tests**
  ```bash
  npm test
  ```

## Code Structure

- **Backend**
  - `app/` - Contains FastAPI application
  - `tests/` - Backend tests

- **Frontend**
  - `pages/` - Next.js pages
  - `components/` - Reusable React components

## Contributing Guide

- **Fork the repository**
- **Create a branch**
  ```bash
  git checkout -b feature/your-feature-name
  ```
- **Commit your changes**
  ```bash
  git commit -m 'Add some feature'
  ```
- **Push your branch**
  ```bash
  git push origin feature/your-feature-name
  ```
- **Create a Pull Request**

For more details, refer to [CONTRIBUTING.md](../CONTRIBUTING.md)