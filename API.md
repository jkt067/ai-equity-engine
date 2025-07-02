# AI Equity Engine API Documentation

---

## Overview

The AI Equity Engine provides a simple REST API to receive student questions and return AI-generated tutoring answers. It is designed to support personalized learning for underserved middle school students while maintaining strong ethical standards and privacy.

---

## Base URL

All API endpoints are relative to the base URL where the backend is hosted.  
Example: `https://your-app-url.com`

---

## Endpoints

### 1. `/ping`  
**Method:** GET  
**Purpose:** Health check endpoint to verify the server is running.  
**Request:** No parameters required.  
**Response:**  
```json
{
  "status": "running"
}
{
  "question": "What is photosynthesis?",
  "subject": "Science"
}
{
  "answer": "Photosynthesis is the process by which green plants use sunlight to make food from carbon dioxide and water."
}
{
  "error": "No question provided"
}
{
  "error": "Detailed error message explaining what went wrong"
}
curl -X POST https://your-app-url.com/ask \
-H "Content-Type: application/json" \
-d '{"question":"What is the Pythagorean theorem?","subject":"Math"}'
{
  "answer": "The Pythagorean theorem states that in a right triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides."
}
