from sqlalchemy import or_ 
 
from apps.base.db import new_session 
from apps.models import Users 
 
 
def find_user(username: str = None, email: str = None): 
    session = new_session() 
    return session.query(Users).filter(or_(Users.username == (username or '$$$$$$'), 
                                           Users.email == (email or '$$$$$$'),  # Non-existent string used as condition 
                                           )).first()


 
