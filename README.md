# Svend-Share

## Introduction

Svend-Share is a web application designed to facilitate the management and splitting of expenses among groups. The project aims to provide a clear and accessible platform for users to track shared expenses, calculate balances, and simplify financial interactions in various scenarios such as group trips, shared living arrangements, or joint projects.

## Core Functionalities

- **Expense Tracking**: Allows users to log and categorize expenses.
- **Balance Calculation**: Automatically calculates how much each participant owes or is owed.
- **Group Expenses**: Users can create groups to manage expenses shared with multiple people.
- **Individual Accounts**: Each user has an account to track their personal expenses and balances.
- **Data Persistence**: Utilizes a Postgres database to store and manage data.

## Technical Stack

- **Backend**: Developed using FastAPI, offering high performance and easy scalability.
- **Database**: PostgreSQL for reliable and efficient data storage.
- **Frontend**: (Planned) A user-friendly interface using Next.js.
- **Containerization**: (Optional) Docker support for easy deployment and testing.

## Getting Started

### Prerequisites

Before setting up the project, ensure you have the following:
- Python 3.8+
- PostgreSQL
- Docker (for containerized environments)

### Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/KasperSvendsen/svend-share.git
   ```

2. Navigate to the project directory:
   ```bash
   cd svend-share
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the PostgreSQL database:
   - Detailed instructions for initializing and configuring the database.

5. (Optional) Docker setup:
   - Instructions for using Docker/Docker Compose.

### Running the Application

1. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

2. The server will be available at `http://localhost:8000`.

## Contribution

Contributions to Svend-Share are welcome. Please read the contribution guidelines for more information on how to report issues, submit changes, and how to get involved.

## License

[Specify the license or indicate 'License: MIT', if applicable]

---

For more information or assistance, refer to the project documentation or contact the maintainers.