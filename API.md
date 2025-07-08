# AI Equity Engine API Documentation

---

## Overview

The AI Equity Engine provides a simple REST API to receive student questions and return AI-generated tutoring answers.  
It is designed to support personalized learning for underserved middle school students while maintaining strong ethical standards and privacy.

---

## Base URL

All API endpoints are relative to the base URL where the backend is hosted.  
Example: `https://your-app-url.com`

---

## Endpoints

### 1. `/ping`  
**Method:** GET  
**Purpose:** Health check endpoint to verify the server is running.

**Request:**  
_No parameters required._

**Success Response (200 OK):**
```json
{
  "status": "running"
}
2. /ask
Method: POST
Purpose: Receive a student’s question and return an AI-generated answer.

Request Body (JSON):

json
{
  "question": "What is photosynthesis?",
  "subject": "Science"
}
Success Response (200 OK):

json
{
  "answer": "Photosynthesis is the process by which green plants use sunlight to make food from carbon dioxide and water."
}
Error Responses:

400 Bad Request (when no question is provided)

json
{
  "error": "No question provided"
}
500 Internal Server Error (for unexpected errors)

json
{
  "error": "Detailed error message explaining what went wrong"
}
Usage Example with curl
bash
curl -X POST https://your-app-url.com/ask \
-H "Content-Type: application/json" \
-d '{"question":"What is the Pythagorean theorem?","subject":"Math"}'
Expected Response:

json
{
  "answer": "The Pythagorean theorem states that in a right triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides."
}
