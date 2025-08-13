
def valid_input(
    input_str: str,
    input_type: type,
    error_message: str,
    validation_function: callable = lambda x: True
    ):
    """
    Pide un input al usuario y lo valida.
    Si el input no es del tipo especificado o no cumple con la funcion de validacion,
    se muestra un mensaje de error y se vuelve a pedir el input.
    
    Parameters
    ----------
    input_str : str
        El mensaje a mostrar al usuario.
    input_type : type
        El tipo de dato que se espera como input.
    error_message : str
        El mensaje de error a mostrar si el input no es valido.
    validation_function : callable, optional
        Una funcion que recibe el input y devuelve True si es valido o False en caso
        contrario. Por defecto es una funcion que siempre devuelve True.
    
    Returns
    -------
    input_value : input_type
        El input validado.
    """
    # Ejemplo:
    # valid_input("Ingresa tu edad: ", int, "Por favor, ingresa un numero entero.",
    #             lambda x: x >= 0)
    while True:
        try:
            input_value = input_type(input(input_str))
            if validation_function(input_value):
                return input_value
            else:
                print(error_message)
        except ValueError:
            print(error_message)