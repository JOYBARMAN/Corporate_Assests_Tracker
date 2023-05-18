# Corporate_Assests_Tracker

Task
You have been hired as a developer for a new project where,
You will write a Django app to track corporate assets such as phones, tablets, laptops 
and other gears handed out to employees.

GOALS
The application might be used by several companies
Each company might add all or some of its employees
Each company and its staff might delegate one or more devices to employees for
a certain period of time
Each company should be able to see when a Device was checked out and returned
Each device should have a log of what condition it was handed out and returned

Project Features

#User Registration:
Allow users to register an account.
Validate and store user registration details.
Generate and send a verification email for account activation.

#User Login:
Provide a login mechanism for registered users.
Authenticate user credentials.
Generate access and refresh tokens for authenticated users.

#User Profile:
Display user profile information.
Allow users to view and update their profile details.
Ensure proper authentication and authorization for profile access.

#User Password Management:
Enable users to change their password securely.
Implement password strength requirements and validation.
Provide password reset functionality using email verification.

#Company Management:
Support listing and creating companies.
Allow retrieval, updating, and deletion of individual company records.
Implement authorization checks to ensure only authorized users can perform these actions.

#Employee Management:
Enable listing and creation of employee records.
Allow retrieval, updating, and deletion of individual employee details.
Associate employees with their respective companies.
Implement authorization checks to ensure only authorized users can perform these actions.

#Device Management:
Support listing and creating device records.
Allow retrieval, updating, and deletion of individual device details.
Implement authorization checks to ensure only authorized users can perform these actions.

#Device Assignment:
Enable listing and creation of device assignments to employees.
Allow retrieval, updating, and deletion of device assignments.
Implement pagination for large assignment lists.
Provide search functionality to find assignments by employee name.
Implement filtering to retrieve assignments based on the company name.

#User Permissions and Roles:
Implement role-based access control (RBAC) to manage user permissions.
Define different roles such as admin, employee, or manager with varying access levels.
Ensure appropriate authorization checks for different views and actions.

#Documentation and API Usage:
Include detailed instructions on how to install and run the project.
Provide API documentation for developers, including endpoints, request/response formats, and authentication requirements.
Include code examples or sample requests to demonstrate API usage.

#Unit Tests
Company API Tests:

Test listing all companies (GET request) and verify the response.
Test creating a new company (POST request) and check the response status.
Test retrieving a specific company (GET request) and validate the response data.
Test updating a company (PUT request) and verify the response.
Test deleting a company (DELETE request) and ensure the company is removed.
Employee API Tests:

Test listing all employees (GET request) and verify the response.
Test creating a new employee (POST request) and check the response status.
Test retrieving a specific employee (GET request) and validate the response data.
Test updating an employee (PUT request) and verify the response.
Test deleting an employee (DELETE request) and ensure the employee is removed.

#Device API Tests:
Test listing all devices (GET request) and verify the response.
Test creating a new device (POST request) and check the response status.
Test retrieving a specific device (GET request) and validate the response data.
Test updating a device (PUT request) and verify the response.
Test deleting a device (DELETE request) and ensure the device is removed.

#Device Assignment API Tests:
Test listing all device assignments (GET request) and verify the response.
Test creating a new device assignment (POST request) and check the response status.
Test retrieving a specific device assignment (GET request) and validate the response data.
Test updating a device assignment (PUT request) and verify the response.
Test deleting a device assignment (DELETE request) and ensure the assignment is removed.

#Authentication and Authorization Tests:
Test user registration with valid and invalid input data.
Test user login with correct and incorrect credentials.
Test access to protected routes without authentication and ensure the response is unauthorized.
Test access to protected routes with valid authentication but without proper authorization and verify the response status.
Test access to protected routes with valid authentication and appropriate authorization and ensure the response is successful.

Postman API Collection
Provide a Postman API collection that includes preconfigured requests for different endpoints. The collection should cover the following scenarios:

#User Registration:
Request to register a new user with valid data.
Request to register a new user with missing or invalid data.
Verification email request.

#User Login:
Request to log in with correct credentials.
Request to log in with incorrect credentials.
Access token retrieval.

#User Profile:
Request to view user profile information.
Request to update user profile information.

#Company Management:
Request to retrieve a list of companies.
Request to create a new company.
Request to retrieve, update, and delete a specific company.

#Employee Management:
Request to retrieve a list of employees.
Request to create a new employee.
Request to retrieve, update, and delete a specific employee.

#Device Management:
Request to retrieve a list of devices.
Request to create a new device.
Request to retrieve, update, and delete a specific device.

#Device Assignment:
Request to retrieve a list of device assignments.
Request to create a new device assignment.
Request to retrieve, update, and delete a specific device assignment.

#Authentication and Authorization:
Request to register a user, retrieve access and refresh tokens.
Request to log in, retrieve access and refresh tokens.
Request to access protected routes with different roles (admin, employee, manager) and verify the responses.
Make sure to include any necessary environment variables or authentication headers in the Postman collection to facilitate easy testing and usage of your API.

