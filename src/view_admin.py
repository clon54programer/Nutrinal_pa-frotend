import flet as ft

# Funciones
# crear vendedores
# ver vendedores
# crear productos y produciones
# ver los pedidos


def view_general(page: ft.Page) -> None:

    # row = ft.row()

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

    buttom_watch_orders = ft.Container(content=ft.Text("Ver pedidos"), margin=10,
                                       padding=10,
                                       alignment=ft.alignment.center,
                                       bgcolor=ft.Colors.YELLOW,
                                       width=150,
                                       height=150,
                                       border_radius=10)

    row = ft.row([buttom_create_seller, buttom_watch_orders])

    page.add(buttom_create_production)

    page.add(buttom_watch_orders)

    page.update()
