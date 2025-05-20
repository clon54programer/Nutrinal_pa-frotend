import flet as ft
from view_admin import view_general
from view_seller import view_general_seller


def main(page: ft.Page):

    text = ft.Text("Paneles",
                   color=ft.Colors.BLACK, text_align=ft.TextAlign.CENTER, size=40, style=ft.TextAlign.CENTER)

    def on_click_1(e):
        page.remove(row)
        page.remove(row_2)

        page.update()
        view_general(page)

    def on_click_2(e):
        page.remove(row)
        page.remove(row_2)

        page.update()
        view_general_seller(page)

    buttom_view_admin = ft.Container(content=ft.Text("Administrador"), margin=10,
                                     padding=10,
                                     alignment=ft.alignment.center,
                                     bgcolor=ft.Colors.AMBER,
                                     width=150,
                                     height=150,
                                     border_radius=10, on_click=on_click_1)

    buttom_view_seller = ft.Container(
        content=ft.Text("Vendedor."), margin=10,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=ft.Colors.BLUE,
        width=150,
        height=150,
        border_radius=10, on_click=on_click_2)

    row = ft.Row(controls=[text])
    row_2 = ft.Row(controls=[buttom_view_admin, buttom_view_seller])

    page.add(row)
    page.add(row_2)


ft.app(main)
