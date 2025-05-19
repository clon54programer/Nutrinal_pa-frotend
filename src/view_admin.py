import flet as ft

# Funciones
# crear vendedores
# ver vendedores
# crear productos y produciones
# ver los pedidos


def view_general(page: ft.Page) -> None:

    # row = ft.row()

    buttom_watch_seller = ft.ElevatedButton("Ver vendedores")
    buttom_create_seller = ft.ElevatedButton("Crear vendedores")
    buttom_create_production = ft.ElevatedButton("Crear producto")
    buttom_watch_orders = ft.ElevatedButton("Ver pedidos")

    page.add(buttom_create_production)
    page.add(buttom_create_seller)
    page.add(buttom_watch_orders)
    page.add(buttom_watch_orders)
    page.add(buttom_watch_seller)

    page.update()
