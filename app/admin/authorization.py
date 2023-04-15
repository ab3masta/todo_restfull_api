import secrets
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.utils.firebase_initialize import auth

security = HTTPBasic()

def firebaseAdminAuth(credentials: HTTPBasicCredentials = Depends(security)):
    """_summary_

    Args:
        credentials (HTTPBasicCredentials, optional): _description_. Defaults to Depends(security).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    
    This is a function that authorize only admin user to access documentation.
    ===> Admin is created manually on Firebase authentication with email: admin@gmail.com & password:123456789
    """
    try:
        email = credentials.username # use username field as email to sign in
        password = credentials.password
        response = auth.sign_in_with_email_and_password(email, password)
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
