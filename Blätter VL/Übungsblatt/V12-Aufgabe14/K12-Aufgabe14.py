def get_ratio_at_position(list_a, list_b, pos_in_list): 
    """Assumes: list_a and list_b are lists of equal length of numbers 
    Returns: List_a[pos_in_list]/List_b[pos_in_list]""" 
    try:
        if ( 
            not isinstance(list_a, list) 
            or not isinstance(list_b, list) 
            or not isinstance(pos_in_list, int) 
        ): 
            raise TypeError

        if (
            pos_in_list >= len(list_a) 
            or pos_in_list >= len(list_b)
        ):
            raise IndexError("Liste zu kurz yurr")
        
        if (
            list_b[pos_in_list] ==0
        ):
            raise ZeroDivisionError("Null teilen nononono")
        
        if (
           type(list_a[pos_in_list]) not in [int, float] 
           or type(list_b[pos_in_list]) not in [int, float]
        ):
            raise ValueError("keine zahl du hund")


        return float(list_a[pos_in_list]) / float(list_b[pos_in_list]) 
    
    except TypeError:
        print("Falsch :((")
    except Exception as ex:
        print(ex)

    finally:
        print("get_ratio_at_position ausgeführt")





# Beispielaufruf und Überprüfung 
#assert get_ratio_at_position([2, 3, 6, 9], [1, 2, 3, 4], 2) == 2 
 
#assert not get_ratio_at_position([2, 3, 6, 9], [1, 2, 3, 4], 3) == 3


print(get_ratio_at_position([2, 3, 6, 9], [1, 2, 3, 4], 2))  # Soll "Ergebnis: 2.0" ausgeben
print("--")
print(get_ratio_at_position([2, 3, 6, 9], [1, 2, 3, 0], 3))  # ZeroDivisionError
print("--")
print(get_ratio_at_position([2, 3, "X", 9], [1, 2, 3, 4], 2))  # ValueError
print("--")
print(get_ratio_at_position([2, 3, 6, 9], [1, 2, 3, 4], 5))  # IndexError
print("--")
print(get_ratio_at_position(123, [1, 2, 3, 4], 2))  # TypeError