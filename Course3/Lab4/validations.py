#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
    	raise ValueError("minlen must be at least 1"
    #username should not start from forbidden characters.
	 regex = re.compile('.[@_!#$%^&*()<>?/\|}{~:]')
	 if(regex.search(username) == None):
		return #username should not start from forbidden characters.
         regex = re.compile('.[@_!#$%^&*()<>?/\|}{~:]')
         if(regex.search(username) == None):
                return False
#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1"
    #username should not start from forbidden characters.
    if(bool(re.search('^[a-zA-Z0-9]*$.',username))==True):
        return False

    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', username):
        return False
    # Usernames can't begin with a number
    if username[0].isnumeric():
        return False
    return True


print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False
