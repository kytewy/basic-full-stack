# README.md

# Next.js FastAPI PostgreSQL Docker Setup

A modern full-stack application template using Next.js, FastAPI, and PostgreSQL, all containerized with Docker.

## Project Structure

```
project_root/
├── frontend/
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── package.json
│   ├── next.config.js
│   └── src/
│       ├── app/
│       │   └── page.tsx
│       └── components/
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── main.py
│       └── database.py
├── docker-compose.yml
└── .env
```

## Prerequisites

- Docker
- Docker Compose

## Quick Start

1. Clone this repository
2. Run `docker-compose up --build`
3. Access:
   - Frontend: http://localhost:3000
   - Backend: http://localhost:8000
   - Database: localhost:5432

## Development

- Frontend changes will hot-reload
- Backend changes will auto-reload
- Database data persists between restarts

## Environment Variables

Update the `.env` file with your specific configuration:

- `DATABASE_URL`: PostgreSQL connection string
- Add other environment variables as needed

---
# basic-full-stack
