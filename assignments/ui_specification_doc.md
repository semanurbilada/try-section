# User Interface Specification Document

* [Overview](#overview)
* [Requirements](#requirements)
* [UI Components](#ui-components)
   * [1.User List Table](#1-user-list-table)
   * [2. New User Form](#2-new-user-form)
   * [3. Buttons](#3-buttons)
* [Page Behavior](#page-behavior)
* [Notes](#notes)

## Overview
This document specifies the user interface for the User Management Screen. It outlines UI components, user interactions, and behavior to guide software developers in implementing the interface.

## Requirements
- The user should be able to view a list of existing users.
- The user should be able to add a new user with required details.
- The interface should allow filtering and sorting of user records.
- Disabled users should be hidden by default but can be toggled.
- The system should allow assigning user roles.
- Changes should be saved using a "Save User" button.

## UI Components

### 1. User List Table
| Column Name  | Description |
|-------------|-------------|
| ID          | Unique identifier for the user |
| User Name   | The username of the user |
| Email       | Email address of the user |
| Enabled     | Indicates if the user is active (true/false) |

- **Sorting & Filtering**: Each column header allows sorting and filtering.
- **Hiding Disabled Users**: A checkbox labeled *Hide Disabled User* enables/disables the display of disabled users.

### 2. New User Form
The form includes the following input fields:

- **Username** (Text field, required)
- **Display Name** (Text field, optional)
- **Phone** (Text field, optional)
- **Email** (Text field, required)
- **User Roles** (Dropdown selection: *Guest, Admin, SuperAdmin*)
- **Enabled** (Checkbox to enable or disable the user)

### 3. Buttons
- **New User**: Opens a blank user form.
- **Save User**: Saves the entered user data.

## Page Behavior
1. **Initial Load**:
   - Displays the list of users with enabled users visible.
   - The "Hide Disabled User" checkbox is checked by default.
2. **Adding a New User**:
   - Clicking *New User* clears the form fields.
   - "User Roles" dropdown allows selecting one or more roles.
   - Clicking *Save User* validates required fields before submission.
3. **Filtering & Sorting**:
   - Each column header supports sorting and filtering.
   - The *Hide Disabled User* checkbox updates the list dynamically.

## Notes
- Validation should ensure unique usernames and valid email formats.
- The UI should follow responsive design principles.

<!-- TODO: Edits for the minor details; last version! -->