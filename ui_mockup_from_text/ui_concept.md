# UI Concept - Carpool Connect

## Purpose
Carpool Connect is a mobile-first ride-sharing platform that simplifies the process of finding, booking, and managing shared rides. The UI is designed to be intuitive, fast, and accessible for both drivers and passengers while maintaining safety and trust through transparent ratings and real-time information.

## Users

### Passengers
- Commuters seeking affordable transportation
- Budget-conscious travelers
- Eco-conscious individuals wanting to reduce carbon footprint
- Primary need: Quick ride booking with transparency on cost and driver quality

### Drivers
- Vehicle owners looking to monetize empty seats
- Regular commuters wanting to share fuel costs
- Independent contractors seeking flexible income
- Primary need: Easy ride posting and passenger management

### Administrators
- Platform moderators ensuring user safety
- Support staff handling disputes and complaints
- Analytics specialists monitoring platform health
- Primary need: Dashboard for oversight, reporting, and user management

## Core Screens

### 1. Onboarding & Authentication
- Sign up / Login screen (email, phone, or social login)
- User role selection (Passenger or Driver)
- Profile completion (name, photo, vehicle info for drivers)
- Phone verification screen

### 2. Passenger Dashboard (Home Screen)
- Search bar: "Where to?" and "When?"
- Quick action buttons: Search Rides, Schedule Ride, My Bookings
- Active ride card (if a ride is booked)
- Recent trips history
- User profile icon and notifications bell

### 3. Search & Filter Results
- Map view showing available drivers
- List view with ride details (driver name, rating, vehicle, cost, ETA)
- Filter options: Price range, vehicle type, gender preference, departure time
- Book button for each ride

### 4. Ride Booking Screen
- Ride summary (from, to, cost, driver details)
- Driver rating and review count
- Payment method selection
- Special requests text box (e.g., "non-smoking")
- Confirm booking button

### 5. Active Trip Screen
- Real-time driver location on map
- Driver arrival countdown timer
- Driver contact button (call/chat)
- Trip status: "Arriving," "Arrived," "In transit"
- Trip progress with estimated arrival time

### 6. Post-Trip Screen
- Trip summary (distance, cost, duration)
- Rate driver (1-5 stars with optional review)
- Eco-impact display (CO2 saved)
- Receipt and payment confirmation
- Option to rebook or schedule recurring ride

### 7. Driver Dashboard (Home Screen)
- Post New Ride button
- My Active Rides section
- Scheduled Rides section
- Earnings summary (today, this week)
- Passenger ratings and reviews

### 8. Post Ride Screen (Driver)
- Trip details form: From, To, Date, Time, Seats Available
- Recurring ride toggle (Mon-Fri, etc.)
- Price setting (automatic or manual)
- Vehicle selection
- Post Ride button

### 9. Chat Screen
- Real-time message thread between driver and passenger
- Driver/passenger location sharing toggle
- Call button
- Message history
- Auto-closes 24 hours after trip completion

### 10. Profile & Settings
- User profile with photo, name, rating
- Payment methods management
- Preferences (notifications, language, emergency contact)
- Account settings (change password, privacy)
- Help & Support section
- Logout button

### 11. Ratings & Reviews
- View all ratings received
- Breakdown by category (cleanliness, driving, communication)
- Written reviews from other users
- Flag inappropriate review option

### 12. Admin Dashboard
- User management (approve/suspend/ban users)
- Reported users and incidents list
- Platform analytics (active users, rides completed, revenue)
- Customer support tickets queue
- System health monitoring

## Actions

### Passenger Actions
- **Search for rides**: Enter origin, destination, date, time
- **Filter results**: By price, vehicle type, rating, departure time
- **Book a ride**: Select ride and confirm with payment
- **Contact driver**: Call or message before/during trip
- **Rate driver**: Submit 1-5 star rating with optional review
- **Schedule recurring rides**: Set up daily/weekly carpools
- **Track trip**: View real-time driver location
- **Share trip details**: Send live location to emergency contact
- **View eco-impact**: See CO2 savings for each trip
- **Cancel booking**: Cancel ride (with/without penalty based on timing)
- **Manage payment methods**: Add, edit, delete payment options
- **View trip history**: Access past trips and receipts

### Driver Actions
- **Post new ride**: Enter route, schedule, and available seats
- **Manage ride details**: Edit or delete posted rides
- **Accept/decline passenger bookings**: Review passenger details before accepting
- **Contact passenger**: Call or message passenger
- **Complete trip**: Mark ride as finished
- **Rate passenger**: Submit 1-5 star rating with optional review
- **View earnings**: Track income from completed rides
- **Schedule recurring rides**: Post repeating commute routes
- **Upload vehicle info**: Add vehicle photos and documents
- **Accept surge pricing**: Enable higher rates during peak demand
- **Manage availability**: Turn on/off driver mode

### Admin Actions
- **Review reported users**: View incident details
- **Take moderation action**: Warn, suspend, or ban users
- **View analytics**: Monitor platform KPIs and health
- **Manage support tickets**: Respond to customer complaints
- **Generate reports**: Export data for business analysis
- **Configure system settings**: Manage platform-wide rules and policies
- **Monitor transaction logs**: Audit payment and security events

## Design Principles

- **Speed**: All key actions (search, book, rate) should complete in under 5 taps
- **Clarity**: Show only essential information; hide secondary details in menus
- **Safety**: Prominent driver/passenger verification and emergency contact options
- **Trust**: Display ratings, reviews, and verification badges prominently
- **Accessibility**: Support multiple languages, large text options, dark mode
- **Consistency**: Use unified design system across all screens
- **Responsiveness**: Mobile-first design, optimize for touch interaction
- **Real-time feedback**: Show loading states, confirmations, and error messages clearly

## Color Scheme
- **Primary**: Green (#10B981) - represents eco-friendly, trust, growth
- **Secondary**: Blue (#3B82F6) - represents reliability, professionalism
- **Accent**: Orange (#F97316) - represents urgency, calls-to-action
- **Neutral**: Gray (#6B7280) - for text, borders, backgrounds
- **Success**: Green (#22C55E) - for confirmations
- **Error**: Red (#EF4444) - for warnings and errors

## Typography
- **Headings**: Bold, sans-serif (18-32px)
- **Body text**: Regular, sans-serif (14-16px)
- **Labels**: Medium, sans-serif (12-14px)
- **Call-to-action**: Bold, sans-serif (16-18px)
