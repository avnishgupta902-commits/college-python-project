# College Event Registration System

## 1. Overview of the Project

The College Event Registration System is a menu-driven command-line application developed in Python. It helps manage student registrations for college events. Users can add student details, view and search registrations, update or delete records, see available events, and check registration statistics.

Registration data can be saved to and loaded from a local JSON file named `registrations.json`.

## 2. Features

- **Register students:** Store a student's name, roll number, email, phone number, department, year, and selected event.
- **Duplicate roll-number check:** Prevent a new registration when the roll number already exists.
- **View registrations:** Display all registered students and their details.
- **Search students:** Search by part of a student's name or by an exact roll number.
- **Update registration:** Change student details and event selection.
- **Delete registration:** Remove a registration after confirmation.
- **View events:** Display the available college events.
- **View statistics:** Show the total number of registrations and registration counts for each event.
- **Save data:** Write registrations to `registrations.json`.
- **Load data:** Load previously saved registrations from `registrations.json`.
- **Clear all registrations:** Remove all records after confirmation.
- **About screen:** Display basic information about the program.

### Available Events

1. Coding Competition
2. Quiz Competition
3. Dance Competition
4. Singing Competition
5. Debate Competition
6. Poster Making
7. Sports Event

## 3. Technologies / Tools

- **Python 3** — programming language used to build the application.
- **`json` module** — saves and loads registration data in JSON format.
- **`os` module** — checks whether the data file exists.
- **Terminal / Command Prompt** — used to run and interact with the program.
- **Text editor or IDE** — for example, VS Code, IDLE, or another Python editor.

No third-party Python packages are required.

## 4. Steps to Install & Run the Project

### Prerequisites

- Install Python 3.
- Have the project Python file available on your computer.

### Installation and Execution

1. Save the Python code in a file named `main.py` (or use the actual filename of your program).
2. Open a terminal or Command Prompt.
3. Navigate to the directory containing the Python file.
4. Run the program with:

   ```bash
   run python file simply
   ```
5. The program will display the main menu. Follow the prompts and enter the number for the operation you want to perform.
6. Choose **8. Save Data** to save registrations manually, or **11. Exit** to save data before closing.

The program checks for `registrations.json` when it starts. If the file does not exist, it reports that no previous data was found. The file is created when data is saved.

## 5. Instructions for Testing

Test the application manually through the command-line menu. Use sample data and verify the displayed messages and saved records.

### Test Cases

| Test | Steps | Expected result |
|---|---|---|
| Register a student | Select option `1`, enter student details, and choose a valid event number. | Registration succeeds and the student's name and event are displayed. |
| Reject duplicate roll number | Register a student, then try registering another student with the same roll number. | The program reports that the roll number already exists and does not add the duplicate. |
| View registrations | Select option `2` after registering a student. | The registered student's details are displayed. |
| Search by name | Select option `3` and enter all or part of a registered student's name. | Matching student details are displayed. |
| Search by roll number | Select option `3` and enter a registered roll number. | The matching student is displayed. |
| Search for a missing student | Search for a name or roll number that is not registered. | The program displays “No student found.” |
| Update a registration | Select option `4`, enter an existing roll number, and provide new details and a valid event number. | The registration is updated. |
| Delete a registration | Select option `5`, enter an existing roll number, and confirm with `yes`. | The registration is removed. |
| Cancel deletion | Start deleting a registration and answer `no` to the confirmation prompt. | The registration remains unchanged. |
| View events | Select option `6`. | All seven available events are displayed. |
| View statistics | Select option `7`. | The total registration count and count for each event are displayed. |
| Save and reload data | Select option `8`, close the program, restart it, and check registrations. | Saved registrations are loaded from `registrations.json`. |
| Invalid event selection | While registering, enter text or a number outside the available event range. | The program reports an invalid event choice and does not complete that registration. |
| Clear all registrations | Select option `10` and confirm with `yes` using test data only. | All registrations are cleared and the data file is updated. |

### Testing Notes

- Use test or sample student details rather than real personal information.
- Test destructive actions such as deleting records or clearing all registrations with disposable data.
- Confirm that `registrations.json` is created in the program's current working directory after saving.
- The project code does not include an automated test suite; the steps above are manual tests.
