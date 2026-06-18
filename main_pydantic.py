from pydantic import BaseModel,field_validator


class User(BaseModel):
    id:int
    name:str
    is_active:bool
    email:str

    @field_validator("email")
    def validate_email(cls,v):
        if '@' not in v:
            raise ValueError("Hoooo l'email !!!")
        return v





def main():
    u = User(id=1,name="toto",is_active=True,email="tutu@truc.com")
    print(u)

if __name__=='__main__':
    main()
