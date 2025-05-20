import flet as ft


def view_general_seller(page: ft.Page):

    text = ft.Text("Vendedor",
                   color=ft.Colors.BLACK, text_align=ft.TextAlign.CENTER, size=40, style=ft.TextAlign.CENTER)

    buttom_create_order = ft.Container(content=ft.Text("Hacer un pedido"), margin=10,
                                       padding=10,
                                       alignment=ft.alignment.center,
                                       bgcolor=ft.Colors.AMBER,
                                       width=150,
                                       height=150,
                                       border_radius=10)

    buttom_watch_order = ft.Container(
        content=ft.Text("Ver pedidos"), margin=10,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=ft.Colors.BLUE,
        width=150,
        height=150,
        border_radius=10)
