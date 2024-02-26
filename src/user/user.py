class User:
    """
    A class representing an individual using the system.

    Attributes:
    - user_id (int): The unique identifier for the user.
    - name (str): The username chosen by the user.
    - email (str): The user email chosen by the user.
    - password (str): The user password chosen by the user.
    """

    def __init__(self, user_id: int, age: int, gender: str, name: str, email: str, password: str):
        """
        Initialize a new User instance.

        Parameters:
        - user_id (int): The unique identifier for the user.
        - username (str): The username chosen by the user.
        """
        self.user_id = user_id
        self.age = age
        self.gender = gender
        self.name = name
        self.email = email
        self.password = password


    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, new_user_id):
        self._user_id = new_user_id

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age <0:
            raise ValueError("Invalid age")
        self._age = new_age

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, new_gender):
        self._gender = new_gender

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        self._email = new_email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = new_password

    def __repr__(self):
        """
        Return a string representation of the User object.
        """
        return f"User(user_id={self.user_id}, age={self.age}, gender={self.gender}, name={self.name}, email={self.email}, password={self.password})"

    def __str__(self):
        """
        Return a human-readable string representation of the User object.
        """
        return f"User: {self.name}, Email: {self.email}"

    def authenticate(self, entered_password):
        """
        Authenticate the user based on the entered password.

        Parameters:
        - entered_password (str): The password entered by the user.

        Returns:
        - bool: True if authentication is successful, False otherwise.
        """
        return self.password == entered_password

    def reset_password(self, new_password):
        """
        Reset the user's password.

        Parameters:
        - new_password (str): The new password to be set.
        """
        self.set_password(self, new_password)

        self.password = self.get_password(self)
