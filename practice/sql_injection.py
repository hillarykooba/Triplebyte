'''
All four answers are real attacks, but this SQL statement is particularly vulnerable to a SQL injection. If an attacker submitted a request with the email parameter set to "admin@example.com" and the password set to "password' OR '1'='1", the database would execute the following query:

SELECT * FROM users WHERE email = 'admin@example.com'
    AND password = 'password' OR '1'='1'
This would bypass the password verification and let the attacker login as the admin. The key part of the attack is the single quote after "password", which allows the attacker to break out of the string comparison and modify the intent of the query. One solution here is to sanitize or escape user inputs instead of directly interpolating them into SQL statements. However this can be fragile and error-prone, so the best practice is generally to use prepared statements, which lets the database itself protect against SQL injections.
'''

# The following code seems to work, but it wouldn't pass a security review. Which vulnerability is it exposed to?

def login(request, cursor):
    cursor.execute("SELECT * FROM users WHERE email = '" \
        + request.params["email"] + "' AND password = '" \
        + request.params["password"] + "'")
  
# Answer : SQL injection from malicious user input
