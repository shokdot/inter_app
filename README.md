# Inter App

This is a simple Query Handler application built using Flask. The application processes queries and returns relevant responses based on the implemented logic.

## Prerequisites

Ensure you have the following installed before running the application:
- Python 3.x
- Flask

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/shokdot/inter_app/
   cd inter_app
   ```
## Running the Application

The application should be started using the `run.sh` script.

1. Grant execute permission to the script (if not already executable):
   ```sh
   chmod +x run.sh
   ```

2. Run the script:
   ```sh
   ./run.sh
   ```

## API Endpoints

The following endpoints are available:

- **GET /** - Returns a welcome message.
- **GET /search?q** - Accepts a Query name for welcoming 'name'.
