# interv_edmachina


# My FastAPI Project

This is a sample FastAPI project.

## Setup

### Requirements

- Docker
- Docker Compose

### Running the Project

1. Build and start the containers:

   ```bash
   docker-compose up --build

2. In local run migrations to create tables:
   Make sure you have the following pakages:
      - pip install alembic sqlalchemy psycopg2

   Then run the following command:
      - alembic upgrade head

# FastAPI Students and Subjects API

This API allows managing students and subjects using FastAPI. Below are the available endpoints.

## Students Endpoints

### Get All Students

- **Endpoint:** `GET /api/students/`
- **Description:** Retrieves a list of all students.
- **Request Example:** `http://127.0.0.1:8000/api/students/`
- **Optional Parameters:**
  - `skip`: Number of students to skip (default: 0)
  - `limit`: Maximum number of students to return (default: 10)

### Create a New Student

- **Endpoint:** `POST /api/students/`
- **Description:** Creates a new student.
- **Request Example:** `http://127.0.0.1:8000/api/students/`
- **Request Body Schema:**
  ```json
  {
    "name": "John Doe 1",
    "email": "john@example.com",
    "address": "123 Main St",
    "phone": "555-1234",
    "career": "Engineering",
    "subject_repeats": 0,
    "subjects": [4, 5, 6, 10]
  }


### Update Student Details and Subjects

- **Endpoint:** `PUT /api/students/{student_id}`
- **Description:** Updates the details and subjects of an existing student.
- **Request Example:** `http://127.0.0.1:8000/api/students/2`
- **Request Body Schema:**
  ```json
  {
    "name": "John Doe 2",
    "email": "john.doe2@example.com",
    "address": "456 Main St",
    "phone": "555-5678",
    "career": "Mathematics",
    "subject_repeats": 1,
    "subjects": [1, 3, 4]
  }

### Delete a Student
- **Endpoint:** DELETE /api/students/{student_id}
- **Description:** Deletes a student by ID.
- **Request Example:** http://127.0.0.1:8000/api/students/2

### Get Student Details

- **Endpoint:** GET /api/students/{student_id}
- **Description:** Retrieves details of a student by ID.
- **Request Example:** http://127.0.0.1:8000/api/students/1
- **Request Body Schema:**
{
  "id": 1,
  "name": "John Doe 1",
  "email": "john@example.com",
  "address": "123 Main St",
  "phone": "555-1234",
  "career": "Engineering",
  "enrollment_year": "2024-07-09T13:42:41.263895",
  "subject_repeats": 0,
  "subjects": [
    {
      "name": "subject2",
      "id": 2
    }
  ]
}

### Create a New Subject

- **Endpoint:** POST /api/subjects/
- **Description:** Creates a new subject.
- **Request Example:** http://127.0.0.1:8000/api/subjects/
- **Request Body Schema:**
{
  "name": "Mathematics"
}


### Get All Subjects
- **Endpoint:** GET /api/subjects/
- **Description:** Retrieves a list of all subjects.
- **Request Example:** http://127.0.0.1:8000/api/subjects/
- **Optional Parameters:**
- **skip:** Number of subjects to skip (default: 0)
- **limit:** Maximum number of subjects to return (default: 10)

### Delete a Subject
- **Endpoint:** DELETE /api/subjects/{subject_id}
- **Description:** Deletes a subject by ID.
- **Request Example:** http://127.0.0.1:8000/api/subjects/1
