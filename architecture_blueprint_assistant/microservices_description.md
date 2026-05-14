# Microservices Architecture – Carpool Connect

## Overview
Carpool Connect is built with 7 independent microservices. Each service has one clear responsibility, its own database, and can be deployed/scaled independently.

## Microservices

### 1. Auth Service
- **Purpose**: Handles user login, registration, and token validation.
- **Responsibility**: Login, logout, JWT generation, session management.
- **Database**: PostgreSQL (user credentials, tokens).
- **Endpoints**: POST /login, POST /register, POST /refresh.

### 2. User Service
- **Purpose**: Manages user profiles and preferences.
- **Responsibility**: Create/update user profile, store preferences, user search.
- **Database**: PostgreSQL (user information, settings).
- **Endpoints**: GET/POST/PUT /users, GET /users/:id.

### 3. Ride Service
- **Purpose**: Manages ride creation, search, and booking.
- **Responsibility**: Post rides, search rides, book seats, cancel rides, track status.
- **Database**: PostgreSQL (ride listings, bookings, history).
- **Endpoints**: POST /rides, GET /rides/search, POST /rides/:id/book.

### 4. Matching Service
- **Purpose**: Matches drivers with passengers using AI algorithm.
- **Responsibility**: Find best driver for passenger, calculate prices, optimize routes.
- **Cache**: Redis (active drivers, ride requests).
- **External API**: Google Maps for distance/routes.
- **Endpoints**: POST /match/find, GET /match/status/:id.

### 5. Payment Service
- **Purpose**: Processes payments and billing.
- **Responsibility**: Charge users, process refunds, generate invoices, track transactions.
- **Database**: PostgreSQL (transactions, billing records).
- **External API**: Stripe/PayPal for payment processing.
- **Endpoints**: POST /pay, POST /refund, GET /invoice/:id.

### 6. Notification Service
- **Purpose**: Sends notifications to users via multiple channels.
- **Responsibility**: Push notifications, SMS, emails, in-app messages.
- **Queue**: RabbitMQ (receives events from other services).
- **External APIs**: Firebase (push), Twilio (SMS), SendGrid (email).
- **Endpoints**: POST /notify/send, GET /notify/status/:id.

### 7. Rating Service
- **Purpose**: Manages user ratings and reviews.
- **Responsibility**: Accept ratings, store reviews, calculate user reputation, moderation.
- **Database**: PostgreSQL (ratings, reviews, reputation scores).
- **Endpoints**: POST /rate, GET /rating/:userId, GET /reputation/:userId.

## Communication

- **Services talk via REST API**: Direct calls between services (Auth validates all requests).
- **Asynchronous via Message Queue**: Events flow through RabbitMQ (e.g., payment_complete → notify user).
- **Real-time Cache**: Matching Service uses Redis for instant driver availability checks.

## Advantages

- **Independent Scaling**: Each service scales based on its own demand.
- **Technology Flexibility**: Matching Service uses Python; others use Node.js.
- **Fault Isolation**: If Rating Service fails, ride matching still works.
- **Fast Deployment**: Update one service without affecting others.

## Database per Service

- Auth Service → Auth DB (PostgreSQL)
- User Service → User DB (PostgreSQL)
- Ride Service → Ride DB (PostgreSQL)
- Payment Service → Payment DB (PostgreSQL)
- Rating Service → Rating DB (PostgreSQL)
- Matching Service → Redis Cache (real-time data)
- Notification Service → RabbitMQ Queue (message storage)

Each service owns its data; no cross-database queries. Data consistency is maintained through events.
