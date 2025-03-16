class PasswordValidator:
    MIN_LENGTH = 8
    REQUIRE_SPECIAL_CHARS = True

    @classmethod
    def validate(cls, password):
        """
        Validates the given password based on the defined policy.
        
        Args:
            password (str): The password to validate.
        
        Returns:
            bool: True if the password is valid, False otherwise.
        
        Raises:
            ValueError: If the password does not meet the policy requirements.
        """
        if len(password) < cls.MIN_LENGTH:
            raise ValueError(f"Password must be at least {cls.MIN_LENGTH} characters long.")
        
        if cls.REQUIRE_SPECIAL_CHARS and not any(char in '!@#$%^&*()' for char in password):
            raise ValueError("Password must contain at least one special character (!@#$%^&*()).")
        
        return True