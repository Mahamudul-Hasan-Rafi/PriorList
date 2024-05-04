from passlib.context import CryptContext 

password_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

def get_password(password_):
    return password_context.hash(password_)

# def verify_password(password_):
#     return password_context.hash