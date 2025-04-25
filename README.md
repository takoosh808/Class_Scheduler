# Sprint 1 Information
All submission related material can be found in **Sprint_Reports**

## class-scheduler
Contains all React components and PostgreSQL database
- For sprint 2, move database into myscheduler for better organization

### App.jsx
Called from the root component Main.jsx, contains dashboard and routers to other components

### Login Use Case
Found in Login.jsx in the components folder of class-scheduler

## myscheduler
Contains Django backend

### course-app
Will contain most use-case features, currently these are just shells and further implementation will be need in sprint 2
- Contains views.py

### > myscheduler
Contains settings.py, urls.py

# Sprint 2 Information

## How to run application
We may implement Docker into our final sprint to simplify operating the application, but in the mean time you must follow these steps
### Frontend
First navigate into the frontend folder. Ensure that node_modules and package-lock.json are removed, then run the following:
```
npm install
npm run dev
```

### Backend
Navigate into the backend/core folder. Set up a virtual environment and run the following:
```
pip install -r requirements.txt
python manage.py runserver
```
