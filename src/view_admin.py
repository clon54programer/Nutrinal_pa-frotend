import flet as ft
import requests

# Funciones
# crear vendedores
# ver vendedores
# crear productos y produciones
# ver los pedidos

page_copy: ft.Page = None


def view_general(page: ft.Page) -> None:

    # row = ft.row()
    text = ft.Text("Panel de administrador",
                   color=ft.Colors.BLACK, text_align=ft.TextAlign.CENTER, size=40, style=ft.TextAlign.CENTER)

    def view_watch_seller(e) -> None:
        page.remove(row)
        page.remove(row_2)
        page.remove(row_3)
        page.remove(buttom_watch_orders)

        page.update()
        url = "http://127.0.0.1:8000/nutrinal_pa/admin/get_seller"

        r = requests.get(url=url)

        json = r.json()

        data = json.get("data", {})

        items: dict = dict(data.items())
        index: int = 0

        text_1 = ft.Text(f"Vendedor {index}")

        name = items[f"seller_{index}"]["name"]
        text_2 = ft.Text(f"Nombre: {name}")

        identifier = items[f"seller_{index}"]["identifier"]
        text_3 = ft.Text(f"Identificador: {identifier}")

        data_joined = items[f"seller_{index}"]["data_joined"]
        text_4 = ft.Text(f"Fecha de ingreso: {data_joined}")
        text_5 = ft.Text("-" * 30)

        def on_regret(e):
            nonlocal index
            if index != 0:
                index -= 1
                name = items[f"seller_{index}"]["name"]
                identifier = items[f"seller_{index}"]["identifier"]
                identifier = items[f"seller_{index}"]["identifier"]

                text_1.value = f"Vendedor {index}"
                text_2.value = f"Nombre: {name}"
                text_3.value = f"Identificador: {identifier}"
                text_4.value = f"Fecha de ingreso: {data_joined}"

            else:
                buttom_regret.disabled = True
            page.update()

        def on_next(e):
            nonlocal index
            if index <= len(items) - 1:
                index += 1

                name = items[f"seller_{index}"]["name"]
                identifier = items[f"seller_{index}"]["identifier"]
                identifier = items[f"seller_{index}"]["identifier"]

                text_1.value = f"Vendedor {index}"
                text_2.value = f"Nombre: {name}"
                text_3.value = f"Identificador: {identifier}"
                text_4.value = f"Fecha de ingreso: {data_joined}"

            else:
                buttom_next.disabled = True
            page.update()

        buttom_regret = ft.ElevatedButton(text="Regresar", on_click=on_regret)
        buttom_next = ft.ElevatedButton(text="Siguiente", on_click=on_next)

        row_butom = ft.Row([buttom_regret, buttom_next])

        page.add(text_1)
        page.add(text_2)
        page.add(text_3)
        page.add(text_4)
        page.add(text_5)

        page.add(row_butom)

        page.update()

    buttom_watch_seller = ft.Container(content=ft.Text("Ver vendedores"), margin=10,
                                       padding=10,
                                       alignment=ft.alignment.center,
                                       bgcolor=ft.Colors.AMBER,
                                       width=150,
                                       height=150,
                                       border_radius=10, on_click=view_watch_seller)

    buttom_create_seller = ft.Container(
        content=ft.Text("Crear vendedores"), margin=10,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=ft.Colors.BLUE,
        width=150,
        height=150,
        border_radius=10)

    buttom_create_production = ft.Container(
        content=ft.Text("Crear producto"), margin=10,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=ft.Colors.ORANGE,
        width=150,
        height=150,
        border_radius=10)

    buttom_watch_production = ft.Container(
        content=ft.Text("Ver productos"), margin=10,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=ft.Colors.ORANGE_700,
        width=150,
        height=150,
        border_radius=10)

    buttom_watch_orders = ft.Container(content=ft.Text("Ver pedidos"), margin=10,
                                       padding=10,
                                       alignment=ft.alignment.center,
                                       bgcolor=ft.Colors.YELLOW,
                                       width=150,
                                       height=150,
                                       border_radius=10)

    row = ft.Row([buttom_create_seller, buttom_watch_seller])
    row_2 = ft.Row([buttom_create_production, buttom_watch_production])

    row_3 = ft.Row([text], alignment=ft.MainAxisAlignment.CENTER)

    page.add(row_3)
    page.add(row)
    page.add(row_2)

    page.add(buttom_watch_orders)

    page.update()
