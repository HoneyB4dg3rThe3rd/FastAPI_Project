# FastAPI NLP Web Application

A modern web application that integrates FastAPI for backend services and Streamlit for a clean, interactive frontend interface. This project demonstrates the use of an API-driven architecture to deliver natural language processing (NLP) capabilities through a user-friendly web interface.

## Project Overview

This application provides natural language processing (NLP) functionality through a simple frontend built with Streamlit. FastAPI powers the backend API, which handles requests and returns processed responses.

## Project Structure

```
FastAPI_Project/
├── app.py           # Streamlit-based frontend
├── api.py           # FastAPI backend (API interface)
├── nlp.py           # NLP logic and processing
├── requirements.txt # Python dependencies
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/HoneyB4d3r/FastAPI_Project.git
cd FastAPI_Project
```

### 2. Create and Activate a Virtual Environment

```bash
conda create --name <env> --file requirements.txt
```

## Running the Application

### Start the Backend (FastAPI API)

```bash
fastapi run api.py
```

This will start the FastAPI server at `http://127.0.0.1:8000`.

### Start the Frontend (Streamlit App)

Open a new terminal and run:

```bash
streamlit run app.py
```

This will launch the Streamlit interface in your browser.

## Features

- FastAPI backend for high-performance API handling
- Streamlit frontend for an interactive user experience
- Modular structure for separating API, logic, and UI
- Easy to extend with additional NLP features

## API Documentation

FastAPI provides auto-generated documentation available at:

```
http://127.0.0.1:8000/docs
```

## License

This project is licensed under the MIT License.
