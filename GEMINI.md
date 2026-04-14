# Portfolio Web Project

A Streamlit-based personal portfolio website designed to showcase professional experience, skills, and data projects.

## Project Overview

This project is a multi-page Streamlit application that serves as a professional portfolio. It includes an "About Me" section, project placeholders for dashboards and chatbots, and an integrated contact form.

### Main Technologies
- **Streamlit**: For the web interface and multi-page navigation.
- **Python**: Core logic and data processing.
- **SMTP (Gmail)**: For sending messages via the contact form.
- **PIL (Pillow)**: For image handling and processing.

## Project Structure

- `streamlit_app.py`: The main entry point. It configures the navigation, shared sidebar elements, and page routing.
- `views/`: Contains the individual page modules:
    - `about_me.py`: Hero section, bio, experience, skills, and certifications.
    - `dash_boards.py`: read data from /data/Employer Information.csv.
    - `chat_bot.py`: Placeholder for future AI/Chatbot projects.
- `forms/`: Reusable form logic:
    - `contact.py`: Implementation of the contact form with validation and email delivery.
- `assets/`: Static assets including profile pictures, logos, and icons.
- `.streamlit/`:
    - `config.toml`: Custom theme colors and UI configuration.
    - `secrets.toml`: (Local only) Stores sensitive credentials like `EMAIL_ADDRESS` and `EMAIL_PASSWORD`.

## Building and Running

### Prerequisites
- Python 3.x
- Dependencies listed in `views/requirements.txt`.

### Installation
```bash
pip install -r views/requirements.txt
```


### Running the App
#### After updating codes excute the commend to refresh the app
```bash
streamlit run streamlit_app.py
```

## Development Conventions

- **Navigation**: Uses Streamlit's `st.navigation` and `st.Page` for managing multi-page routing.
- **Styling**: Custom CSS is injected directly into page modules (e.g., `about_me.py`) to achieve specific UI effects like rounded images and custom fonts.
- **Secrets Management**: Sensitive data must be stored in `.streamlit/secrets.toml` and accessed via `st.secrets`.
- **Forms**: Form logic is abstracted into the `forms/` directory to keep view modules clean.

## TODO / Future Work
- Implement interactive visualizations in `views/dash_boards.py`.
- Develop the AI logic for `views/chat_bot.py`.
- Move `requirements.txt` and `gitignore` to the project root for standard compliance.

