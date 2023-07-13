# bincom-django-project

To download and set up the project follow these steps:

1. # Install Git:
   If you don't already have Git installed on your system, download and install it from the official Git website (https://git-scm.com/downloads). Git is a version control system that allows you to clone and manage projects from remote repositories like GitHub.

2. # Clone the project:
   Open your terminal or command prompt and navigate to the directory where you want to store the project. Use the `git clone` command followed by the GitHub repository URL to clone the project. For example:

   ```bash
   git clone git@github.com:john12gate/bincom-django-project.git
   ```


3. # Create a virtual environment (optional):
   It's recommended to create a virtual environment to isolate the project's dependencies. Navigate into the project directory and create a virtual environment by running the following command:

   ```bash
   python -m venv myenv
   ```

   Replace `myenv` with the name you want to give to your virtual environment.

4. # Activate the virtual environment:
   Activate the virtual environment by running the appropriate command for your operating system:

   - On Windows:
     ```bash
     myenv\Scripts\activate
     ```

   - On macOS and Linux:
     ```bash
     source myenv/bin/activate
     ```

# 5. Install project dependencies: 
With the virtual environment activated, install the project's dependencies using pip. In the project's root directory (where the `requirements.txt` file is located), run the following command:

   ```bash
   pip install -r requirements.txt
   ```

   This command will install all the required packages and libraries specified in the `requirements.txt` file.


# 6. Run database migrations: 
Run the database migrations to create the necessary database tables. In the project's root directory, execute the following command:

   ```bash
   python manage.py migrate
   ```

# 7. Start the development server: 
Finally, start the Django development server to run the project locally. Run the following command:

   ```bash
   python manage.py runserver
   ```

   The server should start, and you'll see output indicating the URL where the project is running locally (e.g., `http://127.0.0.1:8000/`).

That's it! You have successfully downloaded and set up the Django project from GitHub. You can access the project by opening the provided local URL in your browser.

Remember to consult the project's documentation or README file for any additional instructions specific to the project you've downloaded.
