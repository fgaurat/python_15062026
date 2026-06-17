

class DivBy12Error(Exception):

    def __init__(self) -> None:
        super().__init__("Erreur division par 12 !!!!!!!!! ⚠️")

def div(a,b):
    if b == 12:
        raise DivBy12Error()
    return a/b


def call_div(a,b):
    try:
        print("OPEN LOG")
        c = div(a,b)
        print("la suite")
    finally:
        print("CLOSE LOG")
    
    return c

def main():
    try:
        a = 2
        # b = int(input('valeur de b:'))
        b = 12
        # c = a/b
        c = call_div(a,b)
        print(c)
    except DivBy12Error as e:
        print("erreur",e)
    except ZeroDivisionError as e: # Gestionnaire d'exception
        print("erreur",e)
    # except TypeError as e:
    #     print("erreur",e)
    # except ValueError as e:
    #     print("erreur",e)
    except (ValueError,TypeError) as e:
        print("ValueError, TypeError erreur",e)
    except Exception as e:
        print("erreur",e)
    else: # s'éxécute 
        print("Pas d'erreur")

    print("La suite du code")
    
if __name__=='__main__':
    main()
