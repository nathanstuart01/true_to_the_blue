# Sports Data Models & Migrations

This repository serves as a centralized library for sharing **SQL models** and **database migration scripts** across multiple backend applications. It is specifically designed for storing and managing sports data.

## Overview

- **Models**: Defined using [SQLModel](https://sqlmodel.tiangolo.com/), representing the schema for sports-related data.
- **Migrations**: Managed with [Alembic](https://alembic.sqlalchemy.org/), enabling version-controlled database schema changes.
- Designed for easy integration with backend services that ingest, process, and analyze sports data.

## Features

- Reusable, standardized data models for consistent sports data storage.
- Alembic migrations to evolve your PostgreSQL database schema safely over time.
- Compatible with PostgreSQL and other SQL databases supported by SQLModel.
