import flet as ft

# Funciones
# crear vendedores
# ver vendedores
# crear productos y produciones
# ver los pedidos


def view_general(page: ft.Page) -> None:

    # row = ft.row()
    text = ft.Text("Panel de administrador",
                   color=ft.Colors.BLACK, text_align=ft.TextAlign.CENTER, size=40, style=ft.TextAlign.CENTER)

    buttom_watch_seller = ft.Container(content=ft.Text("Ver vendedores"), margin=10,
                                       padding=10,
                                       alignment=ft.alignment.center,
                                       bgcolor=ft.Colors.AMBER,
                                       width=150,
                                       height=150,
                                       border_radius=10)

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
