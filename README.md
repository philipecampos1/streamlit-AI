
# Streamlit with AI
This project demonstrates how to integrate AI with Streamlit, allowing you to interact with a database and receive feedback as simply as possible.

### Features

**AI integration**: Use OpenAI API to enhance your data analysis.

**Streamlit interface**: Clean and simple web interface for user interaction.

**Database management**: SQLite for storing and retrieving data effortlessly.

### Tech Stack

![Python](https://img.icons8.com/?size=50&id=qBvOwZw81tVy&format=png&color=000000)
**Python**: Programming language for backend logic.
![Streamlit](https://img.icons8.com/?size=50&id=9pAKclTpHTMC&format=png&color=000000)
**Streamlit**: Web framework for creating interactive user interfaces.
![SQLite](https://img.icons8.com/?size=50&id=1476&format=png&color=000000)

**SQLite**: Lightweight database for simple data storage.
## Environment Variables
To run this project, you will need to add the following environment variables to your .env file:

`OPEN_AI_API` :  Your OpenAI API key for accessing the OpenAI services.

Note: Make sure to keep your API key secure and do not share it publicly.



## Installation

Follow these steps to set up and run the project:

#### Clone the repository:

```bash
  git clone https://github.com/philipecampos1/streamlit-AI.git
```

#### Navigate to the project directory:

```bash
    cd your-repo
```

#### activate your virtual enviornment

```bash
    source venv/bin/activate  # on Windows: venv\Scripts\activate
```

#### Install the required dependencies:

```bash
    pip install -r requirements.txt
```

## Running the Project

To start the Streamlit app, run the following command:
```bash
    streamlit run app.py
```
The app will be accessible at http://localhost:8501 by default.

## Usage

- **Step 1**: Upload your database.
- **Step 2**: Use the AI feedback feature to analyze your own data, or if you prefer, use the example database provided for practice.
- **Step 3**: View results and insights directly in the web interface.