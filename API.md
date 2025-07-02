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
