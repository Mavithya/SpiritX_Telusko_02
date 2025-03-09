# Fantasy Cricket Admin Panel

A modern admin dashboard for managing fantasy cricket players, tournaments, and real-time statistics.

---

## Features

### Player CRUD Operations

- Create, update, and delete players
- View detailed batting/bowling statistics
- Dynamic player value calculation

### Tournament Analytics

- Real-time leaderboards
- Highest run scorers/wicket takers
- Interactive performance charts

### Security

- JWT Authentication  
  *Secure token-based authentication for admin access*
- Password Hashing
  *Bcrypt-based password encryption (60,000+ iterations)*
- Password breach detection

---

## Tech Stack

| Frontend       | Backend      | Database   |
| -------------- | ------------ | ---------- |
| React 18       | Flask 2.3    | MongoDB 6  |
| Tailwind CSS 3 | JWT          | Mongoose 7 |
| Axios 1.4      | Python 3.10  | Pandas 2   |
| Socket.IO 4    | Flask-CORS 4 |            |

---

## Quick Start

### Prerequisites

- Node.js ≥16
- Python ≥3.10
- MongoDB ≥6
- Git

### Installation

1. Clone Repository
```bash
git clone https://github.com/your-username/fantasy-cricket-admin.git
cd fantasy-cricket-admin
```

2. Backend Setup
```bash
cd backend
python -m venv venv
```
  Linux/Mac
  ```bash
  source venv/bin/activate
  ```

  Windows
  ```bash
  venv\Scripts\activate
  ```

3. Frontend Setup

```bash
cd ../frontend
npm install
```

### Configuration

- *Backend Environment (.env)*

  MONGO_URI=mongodb://localhost:27017/fantasy_cricket
  JWT_SECRET=your_secure_secret_here
  FLASK_ENV=development


- *Frontend Environment (.env)*

  VITE_API_URL=http://localhost:5000
  
  VITE_SOCKET_URL=http://localhost:5000

---

## Running the Application

### Start Backend Server

```bash
cd backend
flask run --port=5000 --debug
```

### Start Frontend Development

```bash
cd ../frontend
npm run serve
```

Access dashboard at: http://localhost:5173

Default Admin Credentials: admin / Test@1234!Secure

---

## Database Management

### Initialize MongoDB

- *Linux/Mac*
```bash
sudo systemctl start mongod
```

- *Windows*
```bash
net start MongoDB
```

### Import Sample Data
```bash
mongorestore --db fantasy_cricket dump/fantasy_cricket
```

### Export Database
```bash
mongodump --db fantasy_cricket --out ./backup
```

---

## Project Structure

```
fantasy-cricket-admin/
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── extensions.py
│   ├── user_interface.py
│   ├── sample_dta.csv
│   ├── .env
│   ├── admin/
│   │   └── routes.py
│   ├── user/
│   │   └── routes.py
│   └── services/
│       ├── database.py
│       ├── realtime.py
│       └── utils.py
├── frontend/
│   ├── src/
│   │   ├── assets/
│   │   ├── layouts/
│   │   ├── components/
│   │   ├── views/
│   │   ├── App.vue
│   │   └── main.js
│   └── package.json
└── README.md
```
