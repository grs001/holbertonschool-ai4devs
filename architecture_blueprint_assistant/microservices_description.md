# Microservices Architecture – Carpool Connect

## Overview
A microservices architecture decomposing Carpool Connect into 7 independent, loosely-coupled services. Each service has distinct responsibility, owns its database, and can be scaled independently.

## Core Microservices (7 Distinct Services)

### 1. Auth Service (Port 3001)
- **Purpose**: Centralized authentication and authorization.
- **Responsibility**: User login/logout, JWT generation, OAuth2 integration, session validation, MFA.
- **Database**: PostgreSQL – credentials, tokens, session data.
- **API Endpoints**: POST /auth/login, POST /auth/register, POST /auth/refresh, POST /auth/logout.
- **Communication**: REST API; validates all requests across system.
- **Why Separate**: Security isolation. Critical for entire system. Can scale independently during high auth traffic.
- **Technology**: Node.js/Express, JWT, bcrypt, Passport.js.

### 2. User Service (Port 3002)
- **Purpose**: User profile and preference management.
- **Responsibility**: Profile CRUD, preference storage, account deactivation, user search.
- **Database**: PostgreSQL – user profiles, settings, preferences.
- **API Endpoints**: GET/POST/PUT /users, GET /users/:id, PUT /users/:id/preferences.
- **Communication**: REST API; called by other services for user data.
- **Why Separate**: User data is accessed by multiple services. Independent updates don't affect ride/payment operations.
- **Technology**: Node.js/Express, PostgreSQL, Caching.

### 3. Ride Service (Port 3003)
- **Purpose**: Core ride management and lifecycle.
- **Responsibility**: Create rides, search rides, booking, cancellation, recurring schedules, ride status.
- **Database**: PostgreSQL – ride postings, bookings, schedules, ride history.
- **API Endpoints**: POST /rides, GET /rides/search, GET /rides/:id, POST /rides/:id/book, PUT /rides/:id/cancel.
- **Communication**: REST API; publishes events (ride_created, ride_booked) to message queue.
- **Why Separate**: Core business logic. High traffic service. Needs independent scaling during peak hours.
- **Technology**: Node.js/Express, PostgreSQL, Event streaming.

### 4. Matching Service (Port 3004)
- **Purpose**: AI-powered driver-passenger matching algorithm.
- **Responsibility**: Match drivers with passengers, route optimization, pricing calculation, availability check.
- **Cache**: Redis – real-time driver locations, active ride requests, matching queue.
- **API Endpoints**: POST /match/find-ride, GET /match/status/:id, POST /match/optimize.
- **Communication**: Real-time via Redis; REST for match requests. Consumes location updates from Ride Service.
- **Why Separate**: Computationally intensive. Requires specialized algorithms. Benefits from horizontal scaling with Redis.
- **External Calls**: Google Maps API for route calculation.
- **Technology**: Python/FastAPI, Redis, ML (scikit-learn), geospatial algorithms.

### 5. Payment Service (Port 3005)
- **Purpose**: Secure financial transaction processing.
- **Responsibility**: Process payments, handle refunds, wallet management, invoice generation, transaction logging.
- **Database**: PostgreSQL (PCI DSS compliant) – transactions, payment records, billing history.
- **API Endpoints**: POST /payments/process, GET /payments/:id, POST /payments/:id/refund, GET /invoices.
- **Communication**: Synchronous REST for immediate payment; async events to message queue (payment_completed).
- **Why Separate**: Requires strict security/compliance (PCI DSS). Failure must not affect other services. Critical for revenue.
- **External Calls**: Stripe/PayPal for fund transfers.
- **Technology**: Node.js/Express, Stripe SDK, encryption, fraud detection.

### 6. Notification Service (Port 3006)
- **Purpose**: Multi-channel notification delivery (push, SMS, email, in-app chat).
- **Responsibility**: Send push notifications, SMS, emails, in-app messages; delivery tracking; message scheduling.
- **Message Queue**: RabbitMQ – receives events from Ride, Payment, Rating services.
- **API Endpoints**: POST /notifications/send, GET /notifications/status/:id.
- **Communication**: Asynchronous via RabbitMQ; REST for direct requests. Multiple worker instances consume queue.
- **Why Separate**: Decouples heavy I/O operations. Prevents notification failures from blocking core services.
- **External Integrations**: Firebase (push), Twilio (SMS), SendGrid (email).
- **Technology**: Node.js, RabbitMQ, Firebase SDK, Twilio, SendGrid.

### 7. Rating Service (Port 3007)
- **Purpose**: User ratings, reviews, and reputation management.
- **Responsibility**: Accept ratings, moderation, fraud detection, reputation calculation, rating aggregation.
- **Database**: PostgreSQL – ratings, reviews, reputation scores, moderation logs.
- **API Endpoints**: POST /ratings, GET /ratings/:userId, PUT /ratings/:id, GET /reputation/:userId.
- **Communication**: REST API; consumes ride_completed events from message queue.
- **Why Separate**: Community trust is crucial; scales independently. Moderation logic is distinct business domain.
- **Technology**: Node.js/Express, PostgreSQL, NLP (sentiment analysis), moderation pipeline.

## Supporting Infrastructure

### API Gateway
- Single entry point for all clients.
- Routes requests to appropriate services.
- Enforces authentication, rate limiting, logging.
- Technology: Kong or NGINX.

### Service Registry (Consul)
- Services register on startup.
- Enables dynamic service discovery.
- Health checks detect failed services.

### Message Queue (RabbitMQ)
- Asynchronous event-driven communication.
- Decouples services; improves resilience.
- Example: Payment Service publishes payment_completed → Notification Service consumes and sends receipt.

### Monitoring (Prometheus/ELK)
- Centralized metrics and logs.
- Alerts on anomalies (high error rate, latency).
- Dashboards for system health.

## Key Architectural Decisions

### Database per Service Pattern
- Each service owns its database; no cross-database queries.
- Ensures loose coupling and independent scaling.
- Eventual consistency via event-driven architecture.

### Synchronous vs Asynchronous
- **Synchronous (REST)**: Auth validation, immediate payment processing.
- **Asynchronous (RabbitMQ)**: Notifications, analytics, non-critical updates.

### Real-time Data
- Redis for Matching Service: fast driver availability checks.
- Reduces latency from seconds to milliseconds.

## Advantages
- **Independent Scaling**: Each service scales based on its demand (Matching Service during peak, Payment Service during transactions).
- **Technology Flexibility**: Matching Service uses Python; others use Node.js.
- **Fault Isolation**: Chat outage won't affect ride matching.
- **Fast Deployment**: Teams deploy individual services without coordination.
- **Clear Ownership**: Each service has distinct business responsibility.

## Challenges
- **Distributed System Complexity**: Debugging across services requires sophisticated tooling.
- **Data Consistency**: Eventual consistency instead of ACID transactions.
- **Network Latency**: Inter-service calls add overhead.
- **Operational Overhead**: Requires Kubernetes, monitoring, CI/CD pipelines.

## Deployment
- Docker containers for each service.
- Kubernetes for orchestration and auto-scaling.
- Separate CI/CD pipelines per service.
