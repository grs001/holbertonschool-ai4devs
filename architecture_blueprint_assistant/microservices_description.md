# Microservices Architecture – Carpool Connect

## Overview
A microservices architecture where Carpool Connect is decomposed into independent, loosely-coupled services. Each service has its own database, specific responsibility, and can be developed, deployed, and scaled independently.

## Core Microservices

### 1. Auth Service (Port 3001)
- **Purpose**: Centralized authentication and authorization management.
- **Responsibility**: User login/logout, JWT token generation, OAuth2 integration, multi-factor authentication, session validation.
- **Database**: PostgreSQL (Auth DB) – stores credentials and auth tokens.
- **API Endpoints**: POST /auth/login, POST /auth/register, POST /auth/refresh, POST /auth/logout.
- **Communication**: Synchronous REST calls; validates tokens for all other services.
- **Technology**: Node.js/Express, JWT, bcrypt, Passport.js.

### 2. User Service (Port 3002)
- **Purpose**: Manages user profiles, preferences, and account settings.
- **Responsibility**: User profile CRUD, preference storage, account deactivation, user search, profile updates.
- **Database**: PostgreSQL (User DB) – stores user information, preferences, settings.
- **API Endpoints**: GET/POST/PUT /users, GET /users/:id, PUT /users/:id/preferences.
- **Communication**: REST API; called by other services for user data.
- **Technology**: Node.js/Express, PostgreSQL, Caching.

### 3. Ride Service (Port 3003)
- **Purpose**: Core ride management – creation, listing, booking, scheduling.
- **Responsibility**: Ride creation, ride search by criteria, ride cancellation, recurring ride management, ride status tracking.
- **Database**: PostgreSQL (Ride DB) – stores ride postings, bookings, schedules.
- **API Endpoints**: POST /rides, GET /rides/search, GET /rides/:id, POST /rides/:id/book, PUT /rides/:id/cancel.
- **Communication**: REST API; consumes Matching Service for pairing; publishes events for Notification Service.
- **Technology**: Node.js/Express, PostgreSQL, Event-driven messaging.
- **External Calls**: Matching Service for ride assignment; Notification Service via message queue.

### 4. Matching Service (Port 3004)
- **Purpose**: AI-powered ride matching algorithm and optimization.
- **Responsibility**: Driver-passenger matching, route optimization, availability verification, pricing calculation, match scoring.
- **Cache**: Redis (Real-time cache) – stores active drivers, current ride requests, matching state.
- **API Endpoints**: POST /match/find-ride, POST /match/optimize, GET /match/status/:id.
- **Communication**: Real-time data via Redis; REST API for match requests.
- **External Calls**: Location Service (Google Maps) for route calculation and distance.
- **Technology**: Python/FastAPI, Redis, Machine Learning (scikit-learn/TensorFlow), Geospatial algorithms.
- **Advanced Features**: A* pathfinding, time-series prediction for demand, recommendation engine.

### 5. Payment Service (Port 3005)
- **Purpose**: Secure financial transaction processing and billing.
- **Responsibility**: Payment processing, transaction logging, refund handling, wallet management, invoice generation, reconciliation.
- **Database**: PostgreSQL (Payment DB) – PCI DSS compliant; stores transactions, payment records, billing history.
- **API Endpoints**: POST /payments/process, GET /payments/:transactionId, POST /payments/:id/refund, GET /invoices/:id.
- **Communication**: Synchronous REST (for immediate payment processing); asynchronous events for notifications.
- **External Calls**: Payment Gateway (Stripe/PayPal) for actual fund transfers.
- **Security**: End-to-end encryption, PCI DSS compliance, tokenization, fraud detection.
- **Technology**: Node.js/Express, Stripe/PayPal SDK, encryption libraries.

### 6. Notification Service (Port 3006)
- **Purpose**: Multi-channel notification delivery (push, SMS, email).
- **Responsibility**: Send push notifications, SMS alerts, emails; schedule notifications; track delivery status.
- **Message Queue**: RabbitMQ – receives events from other services.
- **API Endpoints**: POST /notifications/send, GET /notifications/status/:id, PUT /notifications/:id/resend.
- **Communication**: Asynchronous via message queue (event-driven); REST API for direct notification requests.
- **External Integrations**: Firebase Cloud Messaging (push), Twilio (SMS), SendGrid (email).
- **Technology**: Node.js/Express, RabbitMQ, Firebase SDK, Twilio SDK, SendGrid SDK.
- **Scalability**: Multiple worker instances consuming queue messages independently.

### 7. Chat Service (Port 3007)
- **Purpose**: Real-time messaging between matched drivers and passengers.
- **Responsibility**: Message storage, real-time delivery, chat history, message encryption, presence tracking.
- **Database**: MongoDB (Chat DB) – stores unstructured message data, chat history, conversation metadata.
- **Communication**: WebSocket for real-time bidirectional communication; REST for chat retrieval.
- **API Endpoints**: WS /chat/connect, GET /chat/history/:conversationId, POST /chat/message, GET /chat/conversations.
- **External Calls**: User Service for user validation; Auth Service for token verification.
- **Security**: End-to-end encryption, message signing, rate limiting per user.
- **Technology**: Node.js/Socket.io, MongoDB, Redis for presence/session state.

### 8. Rating Service (Port 3008)
- **Purpose**: Manages user ratings, reviews, and reputation scoring.
- **Responsibility**: Rating submission, review moderation, fraud detection, reputation calculation, rating aggregation.
- **Database**: PostgreSQL (Rating DB) – stores ratings, reviews, reputation scores, moderation flags.
- **API Endpoints**: POST /ratings, GET /ratings/:userId, PUT /ratings/:id, GET /reputation/:userId.
- **Communication**: REST API; consumes events from Ride Service (trip completion).
- **Moderation**: Sentiment analysis for spam detection; admin approval workflow.
- **Technology**: Node.js/Express, PostgreSQL, NLP libraries (sentiment analysis).

## Supporting Infrastructure

### API Gateway
- **Purpose**: Single entry point for all client requests; request routing, authentication, rate limiting.
- **Technology**: Kong/AWS API Gateway/NGINX.
- **Responsibilities**: 
  - Route requests to appropriate microservices.
  - Enforce authentication (validate JWT tokens).
  - Apply rate limiting per user/IP.
  - Log all incoming requests.

### Service Registry & Discovery
- **Purpose**: Dynamic service discovery and load balancing.
- **Technology**: Consul or Eureka.
- **Responsibilities**:
  - Services register themselves on startup.
  - API Gateway discovers service endpoints dynamically.
  - Health checks to detect failed services.

### Message Queue
- **Purpose**: Asynchronous event-driven communication between services.
- **Technology**: RabbitMQ or Apache Kafka.
- **Use Cases**:
  - Ride Service publishes "ride_created" event → Notification Service consumes and sends notification.
  - Payment Service publishes "payment_completed" event → Rating Service and Analytics Service consume.
  - Decouples services; improves resilience.

### Monitoring & Logging
- **Purpose**: Centralized observability across all services.
- **Technology**: Prometheus (metrics), ELK Stack (logs), Grafana (dashboards).
- **Responsibilities**:
  - Collect metrics from all microservices (response time, error rate, request volume).
  - Centralized logging from all services.
  - Alert on anomalies (e.g., high error rate, service latency).

## Data Management Strategy

### Database per Service Pattern
- Each service owns its database; no direct cross-service database access.
- Ensures loose coupling and independent scaling.
- Consistency maintained through event-driven architecture (eventual consistency).

### Caching Strategy
- Redis for frequently accessed data (driver availability, ride requests).
- Reduces database load; enables real-time updates for Matching Service.

## Inter-Service Communication

### Synchronous (REST)
- Auth Service → User Service (fetch user details).
- Payment Service → Stripe API (process payment).
- Used for immediate responses; introduces latency coupling.

### Asynchronous (Message Queue)
- Ride Service → Notification Service (send booking confirmation).
- Payment Service → Analytics Service (log transaction).
- Decouples services; improves fault tolerance.

### Real-time (WebSocket)
- Chat Service uses WebSocket for real-time messaging.
- Matching Service uses Redis Pub/Sub for live ride availability updates.

## Advantages
- **Independent Scaling**: Each service scales independently based on demand (e.g., Matching Service can scale during peak hours).
- **Technology Flexibility**: Different services can use different languages/technologies (Matching Service in Python, others in Node.js).
- **Fault Isolation**: Failure in one service doesn't cascade to others (e.g., if Chat Service is down, ride matching still works).
- **Faster Deployment**: Teams can deploy individual services without affecting others.
- **Easy Maintenance**: Smaller codebases per service; easier to understand and modify.

## Challenges
- **Distributed System Complexity**: Debugging across multiple services is harder.
- **Data Consistency**: Eventual consistency instead of strong ACID; requires careful design.
- **Network Latency**: Inter-service calls introduce additional latency.
- **Operational Overhead**: Requires sophisticated monitoring, logging, and deployment orchestration.

## Deployment Strategy
- **Containerization**: Docker containers for each service.
- **Orchestration**: Kubernetes for container orchestration, scaling, and management.
- **CI/CD Pipeline**: Automated testing and deployment for each service independently.
