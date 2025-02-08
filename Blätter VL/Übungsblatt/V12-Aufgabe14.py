def get_ratio_at_position(list_a, list_b, pos_in_list):
    """Assumes: list_a and list_b are lists of equal length of numbers
    Returns: List_a[pos_in_list]/List_b[pos_in_list]"""

    try:
        if (
            not isinstance(list_a, list)
            or not isinstance(list_b, list)
            or not isinstance(pos_in_list, int)
        ):
            raise Exception ("Fehlerhafte Eingabe.")
        
        if pos_in_list > len(list_a) or pos_in_list > len(list_b):
            raise IndexError
        
        if list_b[pos_in_list] == 0:
            raise ZeroDivisionError
        
        if not (isinstance(list_a[pos_in_list], (int, float)) and isinstance(list_b[pos_in_list], (int, float))):
            raise Exception("Liste enthält nicht nur Zahlen!")
        
        return float(list_a[pos_in_list]) / float(list_b[pos_in_list])
    
    except Exception as ex:
        print(ex)

    finally:
        print("Funktion wurde ausgeführt.")


    # Beispielaufruf und Überprüfung
assert get_ratio_at_position([2, 3, 6, 9], [1, 2, 3, 4], 2) == 2
assert not get_ratio_at_position([2, 3, 6, 9], [1, 2, 3, 4], 3) == 3