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
