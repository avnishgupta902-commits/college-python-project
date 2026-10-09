# Project Statement: College Event Registration System

## 1. Problem Statement

Managing registrations for college events can involve collecting student details, tracking event choices, finding registration records, and keeping registration counts up to date. When these tasks are handled manually, they can become time-consuming and difficult to organize.

The **College Event Registration System** provides a simple, menu-driven application that allows users to manage student registrations for college events from the command line. It stores registration details and supports saving and loading records using a local JSON file.

## 2. Scope of the Project

The project focuses on basic registration management for a set of predefined college events. Its scope includes:

- Recording student details, including name, roll number, email, phone number, department, and year.
- Assigning a student to one of the available events.
- Viewing all registrations and searching for students by name or roll number.
- Updating or deleting an existing registration.
- Displaying the list of available events and registration statistics.
- Saving registration data to `registrations.json` and loading it when the application starts.
- Clearing all registrations after user confirmation.

The application is a command-line program. It uses local JSON-file storage and does not include a graphical interface, online registration portal, or database server.

## 3. Target Users

The intended users are:

- **College event coordinators:** To maintain and review student registrations for college events.
- **College staff or administrators:** To update registration details, remove records, and review event participation counts.
- **Students or project demonstrators:** To view the available events and understand the registration workflow, when operating the application with appropriate access to the computer.

The program does not implement separate user accounts or role-based access controls.

## 4. High-Level Features

- **Student Registration:** Enter student details and select a college event.
- **Duplicate Roll Number Check:** Prevent registration when the roll number already exists.
- **View Registrations:** Display student registration details.
- **Search Student:** Find a student using part of their name or their exact roll number.
- **Update Registration:** Edit student details and event selection.
- **Delete Registration:** Remove a selected student's registration after confirmation.
- **View Events:** Display the predefined list of college events.
- **Registration Statistics:** Show the total number of registrations and the number registered for each event.
- **Save and Load Data:** Persist registration records in a local JSON file.
- **Clear All Registrations:** Remove all records after confirmation.
