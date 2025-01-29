# Password Guardian

Password Guardian is a Python application that helps users create and verify secure passwords. It provides real-time password strength checking and verification against known data breaches using the Have I Been Pwned API.

## Features

- Real-time password strength evaluation
- Checks if password has been exposed in data breaches
- Modern GUI interface using tkinter
- Automatic password field clearing for enhanced security
- Responsive design with keyboard shortcuts

## Requirements

- Python 3.x
- Required Python packages:
- requests
- hashlib
- tkinter (usually comes with Python)

## Installation

1. Clone this repository:
```bash
git clone [repository-url]
```

2. Navigate to the project directory:
```bash
cd password-guardian
```

3. Install required packages:
```bash
pip install requests
```

## Usage

1. Run the application:
```bash
python3 password_guardian.py
```

2. Enter a password in the input field
3. Click "Check Password" or press Enter to evaluate the password

The application will:
- Analyze password strength based on multiple criteria
- Check if the password has appeared in known data breaches
- Provide feedback on password security
- Automatically clear the password field after each check

## Security Features

- Passwords are never stored
- Uses k-anonymity and hashing when checking against HaveIBeenPwned database
- Automatic field clearing for enhanced security
- Password strength requirements:
- Minimum length of 12 characters
- Mix of uppercase and lowercase letters
- Numbers
- Special characters

## Contributing

Feel free to fork this repository and submit pull requests. You can also open issues for bugs or feature requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

