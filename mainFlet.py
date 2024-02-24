# https://github.com/flet-dev/flet
# https://flet.dev/

import flet as ft

from Ejercicio1 import Ejercicio1
from Utils import Utils


def main(page: ft.Page):

    page.window_height = 300
    page.window_width = 300

    page.title = "Ejercicio 1 - Calcular Cociente"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    number_1 = ft.Ref[ft.TextField]()
    number_2 = ft.Ref[ft.TextField]()

    title = ft.Text(value="Ejercicio 1 - Calcular Cociente", size=18, color="blue", text_align=ft.TextAlign.CENTER)
    result = ft.Text(value="", size=16, color="green", text_align=ft.TextAlign.CENTER)

    def calcular_cociente(e):
        num_1 = Utils.obtener_entero(number_1.current.value)
        num_2 = Utils.obtener_entero(number_2.current.value)
        obj_ejercicio_1 = Ejercicio1(num_1, num_2)
        result.value = str(obj_ejercicio_1.calcular_cociente().cociente)
        print(obj_ejercicio_1)
        page.update()

    page.add(
        ft.Row([title], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            ft.TextField(ref=number_1, label="Ingrese el numero 1", value="0", text_align=ft.TextAlign.RIGHT,
                         width=200),
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            ft.TextField(ref=number_2, label="Ingrese el numero 2", value="0", text_align=ft.TextAlign.RIGHT,
                         width=200),
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[
            ft.TextButton(text="Calcular", icon=ft.icons.AUTO_AWESOME, on_click=calcular_cociente),
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([result], alignment=ft.MainAxisAlignment.CENTER),
    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ft.app(target=main)
