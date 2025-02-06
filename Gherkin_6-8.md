# Feature: User Login
## User Story
### As a user, I want to have the ability to login, so I can access my account.

## Scenarios
### Scenario: Valid Login

Given I am on the login page,
And I typed in the username and password correctly,
When I click the “Login” button,
Then I should be redirected to my dashboard.

### Scenario: Invalid username/password

Given I am on the login page,
And I typed in the username or password incorrectly,
When I click the “Login” button,
Then I should be shown an “incorrect username/password” message,
And should stay on the login page.

### Scenario: Blank username/password

Given I am on the login page,
And I left the username or password field blank,
When I click the “Login” button,
Then I should be shown a “username/password required” message,
And I should stay on the login page.
# Feature: Enroll in classes
## User Story
### As a student, I want to have the ability to enroll in classes, so I confirm my classes.

## Scenarios
### Scenario: Valid enrollment

Given I am on the shopping cart page,
And there are classes on my shopping cart,
And none of the classes conflict,
When I click the “Enroll” button,
Then I should be shown a “Successful enrollment” message,
And my shopping cart should be cleared,
And my enrollment should be updated in the database,
And I should stay on the shopping cart page.

### Scenario: No classes selected
Given I am on the shopping cart page,
And there are no classes in my shopping cart,
When I click the “Enroll” button,
Then I should be shown a “No class in shopping cart” message,
And I should stay on the shopping cart page.

### Scenario: Conflicting classes
	
Given I am on the shopping cart page,
And there are classes in my shopping cart,
And some classes conflict,
When I click the “Enroll” button,
Then I should be shown a “Conflicting classes” message
And I should stay on the shopping cart page.

# Feature: Generating visual class schedule
## User Story
### As a student, I want to have the ability to generate a visual class schedule, so I can keep track of my classes.

## Scenarios
### Scenario: Valid class schedule generation

Given I am on the shopping cart page,
And I have classes in my shopping cart,
When I click on the “Generate schedule" button,
Then, a visual class schedule should be generated,
And, that visual class schedule should be shown on screen.

### Scenario: No classes selected

Given I am on the shopping cart page,
And I have no classes in my shopping cart,
When I click on the “Generate schedule" button,
Then, a “No classes in shopping cart” message should be displayed.
And I should stay on the shopping cart page.

### Scenario: Conflicting class schedule

Given I am on the shopping cart page,
And I have conflicting classes on my schedule,
When I click “Generate schedule” button,
Then a visual schedule should be generated with the conflicting classes highlighted,
And a “Conflicting classes” message should be shown,
And the visual class schedule should be displayed.	


# Feature: Admin creates a new class
## User Story 
### As a register Admin, I want to be able to add a class to the list of available classes, so that any time a new class is created, it can be added by students to their schedule.

## Scenarios
### Scenario: Pop up window where admin adds course name, description, etc.

Given the Admin logged in correctly,
And the Admin is on the class list page,
When the Admin clicks on the "Add Class" button,
Then the Admin should be directed to a pop-up,
And the Admin can input the valid class data to create a new class.


### Scenario: Course name matches an existing course

Given the Admin is on the "Add class" pop-up,
And the Admin entered the course information,
When the Admin clicks on the "Confirm" button,
And the course name matches a course already in the database,
Then the Admin should receive a pop-up,
And the pop-up should state "Class already exists", 
And the Admin should remain in the "Add Class pop-up.

### Scenario: Course name is unique

Given the Admin is on the "Add class" pop-up,
And the Admin entered the course information,
When the Admin clicks on the "Confirm" button,
And the course name does not match a course already in the database,
Then the Admin should receive a pop-up,
And the pop-up should state "Class successfully added", 
And the Admin should be redirected back to the class list page,
And the new class should be displayed there.

# Feature: Student Drops a class
## User Story 
### As a register Student, I want to be able to drop a class, so that I can unenroll in classes I no longer want to take.

## Scenarios
### Scenario: If student has no classes left, prevent unenroll

Given the student is on the "Drop Classes" page,
And the student has only one class,
When the student checks the box on the class,
And the class is the only class left on the page,
Then the student should receive a pop-up which says "Cannot have less than 1 class",
And the student should be redirected back to the "Drop Classes" page,
And the class should be remain on the student schedule.

### Scenario: Remove Course from student enrolled classes
Given the student is on the "Drop Classes" page,
And the student has multiple classes,
When the student checks the box on the class they want to drop,
And the class isn't the only class left on the page,
Then the student should receive a pop-up which says "Successfully Dropped Class",
And the student should be redirected back to the "Drop Classes" page,
And the class should be removed from the student schedule.

### Scenario: Past Drop date
Given the student is on the "Drop Classes" page,
And the "Drop date" for classes has passed,
When the student checks the box on the class they want to drop,
And the class isn't the only class left on the page,
Then the student should receive a pop-up which says "Past Drop date",
And the student should be redirected back to the "Drop Classes" page,
And the class should be remain on the student schedule.


# Feature: Database retrieves student information
## User Story 
### As a register Admin, I want to be able to retrieve information on a student by their name or student ID, so that I can see their current schedule information.

## Scenarios
### Scenario: Incomplete Information

Given the Admin is on the "Student Search" page,
And the Admin incorrectly enters a students ID,
When the Admin clicks the "Search" button,
And the information does not fulfill a full student ID,
Then the Admin should remain on the search page,
And the search page should display "Suggested Students",
And should display a list of students whose student ID begins with the input digits.

### Scenario: Can locate student information; return to front end

Given the Admin is on the "Student Search" page,
And the Admin correctly enters a student ID,
When the Admin clicks the "Search" button,
And the information aligns with a student,
Then the Admin should be redirected to the students page,
And the page should display all of the students information.

### Scenario: Non-existent Student

Given the Admin is on the "Student Search" page,
And the Admin enters a student ID that doesn't exist,
When the Admin clicks the "Search" button,
And the information does not align with any student,
Then the Admin should remain on the search page,
And the search page should display "No Student Found."
