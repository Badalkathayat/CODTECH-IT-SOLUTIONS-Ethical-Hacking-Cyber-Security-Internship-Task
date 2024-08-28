**Task 1: Password Strength Checker**

 **Description**
The Password Strength Checker is a Python tool designed to assess the strength of user-entered passwords. It evaluates passwords based on length, inclusion of digits, uppercase and lowercase letters, and special characters, providing feedback on the password's strength.

**Features**
- **Length Check:** Ensures the password is at least 8 characters long.
- **Complexity Check:** Verifies the presence of:
  - At least one digit.
  - At least one uppercase letter.
  - At least one lowercase letter.
  - At least one special character (e.g., @, #, $, etc.).
- **Strength Evaluation:** Classifies passwords as **Strong**, **Moderate**, **Weak**, **Very Weak**, or **Extremely Weak** based on the checks above.

**Installation**
1. Clone the repository to your local machine:
    bash
    git clone https://github.com/Badalkathayat/password-strength-checker.git
    
2. Navigate to the project directory:
    bash
    cd password-strength-checker
    
**Usage**
1. Run the `password_strength_checker.py` script:
    bash
    python password_strength_checker.py
    
2. Enter a password when prompted to see its strength.

**Example**

plaintext
Enter your password: ExamplePass1!
Password Strength: Strong


**Future Enhancements**
- Add a graphical user interface (GUI) for better user interaction.
- Integrate dictionary-based checks to identify common passwords.
- Expand the strength criteria to include entropy-based evaluation.