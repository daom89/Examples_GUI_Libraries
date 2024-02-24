class Utils:
    @staticmethod
    def texto_color(texto: str, color: str = "verde_oscuro", decoration: int = 0) -> str:
        """
        Metodo para darle color a un texto por medio de ANSI escape character sequences
        https://en.wikipedia.org/wiki/ANSI_escape_code
        https://www.youtube.com/watch?v=Ircu1AqsdMo

        :arg
        texto (str): Texto al que se le va a dar color.
        color (str): default (blanco) Color que se le va a dar color.

        :return
        texto (str): El texto con el color dado
        """
        ascii_color = "\033[39m {}\033[00m"
        if color == "negro":
            color = "\033[30m {}\033[00m"
        elif color == "rojo_oscuro":
            color = "\033[31m {}\033[00m"
        elif color == "verde_oscuro":
            color = "\033[32m {}\033[00m"
        elif color == "amarillo_oscuro":
            color = "\033[33m {}\033[00m"
        elif color == "azul_oscuro":
            color = "\033[34m {}\033[00m"
        elif color == "magenta_oscuro":
            color = "\033[35m {}\033[00m"
        elif color == "cyan_oscuro":
            color = "\033[36m {}\033[00m"
        elif color == "gris":
            color = "\033[37m {}\033[00m"
        elif color == "gris_oscuro":
            color = "\033[90m {}\033[00m"
        elif color == "rojo":
            color = "\033[91m {}\033[00m"
        elif color == "verde":
            color = "\033[92m {}\033[00m"
        elif color == "amarillo":
            color = "\033[93m {}\033[00m"
        elif color == "azul":
            color = "\033[94m {}\033[00m"
        elif color == "magenta":
            color = "\033[95m {}\033[00m"
        elif color == "cyan":
            color = "\033[96m {}\033[00m"
        elif color == "blanco":
            color = "\033[97m {}\033[00m"

        return color.format(texto)

    @staticmethod
    def error(texto: str) -> str:
        """
        Metodo para generar un mensaje de error

        :arg
        texto: texto del mensaje de error

        :return
        texto: texto en formato de error
        """
        return Utils.texto_color(texto, "rojo")

    @staticmethod
    def advertencia(texto: str) -> str:
        """
        Metodo para generar un mensaje de advertencia

        :arg
        texto: texto del mensaje de error

        :return
        texto: texto en formato de error
        """
        return Utils.texto_color(texto, "amarillo")

    @staticmethod
    def info(texto: str) -> str:
        """
        Metodo para generar un mensaje de información

        :arg
        texto: texto del mensaje de error

        :return
        texto: texto en formato de error
        """
        return Utils.texto_color(texto, "azul")

    @staticmethod
    def confirm(texto: str) -> str:
        """
        Metodo para generar un mensaje de información

        :arg
        texto: texto del mensaje de error

        :return
        texto: texto en formato de error
        """
        return Utils.texto_color(texto, "verde")

    @staticmethod
    def obtener_entero(valor) -> int:
        while True:
            try:
                return int(valor)
            except ValueError:
                print(Utils.error(f"El texto \"{valor}\" no se puede convertir a numero entero"))

    @staticmethod
    def obtener_flotante(mensaje: str = None) -> float:
        """
        Metodo para solicitar y validar un número flotante

        :arg
        mensaje: texto para solicitar el número

        :return
        valor: número flotante obtenido
        """
        valor = input(mensaje if mensaje is not None else Utils.info("Ingrese un numero flotante: "))
        # if valor.isdecimal():
        #     return float(valor)
        while True:
            try:
                return float(valor)
            except ValueError:
                print(Utils.error(f"El texto \"{valor}\" no se puede convertir a numero flotante"))
                valor = input(Utils.advertencia("Ingresa nuevamente un numero flotante: "))