import flet as ft
import requests


def view_general_seller(page: ft.Page):

    text = ft.Text("Vendedor",
                   color=ft.Colors.BLACK, text_align=ft.TextAlign.CENTER, size=40, style=ft.TextAlign.CENTER)

    def create_order(e):

        print()
        page.remove(row_buttom)
        page.remove(row_3)

    def view_watch_order(e):
        # "data":{
        # "identifier_client": ""
        # "identifier_seller": "",
        # "code_product":"",
        # "cant_product":{},
        # "shipping_destination": ""
        page.remove(row_buttom)
        page.remove(row_3)

        text = ft.Text("Pedidos",
                       color=ft.Colors.BLACK, text_align=ft.TextAlign.CENTER, size=40, style=ft.TextAlign.CENTER)

        r = requests.get("http://127.0.0.1:8000/nutrinal_pa/admin/get_orders")

        json = r.json()

        data = json.get("data", {})

        items: dict = dict(data.items())
        index: int = 0

        """
        "id": "492e9566-7848-4c7e-bad6-90be4b24dd79",
        "cant_product": 0,
        "status": "pending",
        "shipping_destination": "",
        "seller": "Carlos",
        "client": "Juan Pérez",
        "product": [],
        "order_date": "2025-05-06T03:52:35.211Z",
        "date_update": "2025-05-06T03:52:35.211Z"
        }"""

        id = data[f"order_{index}"]['id']
        cant_product = data[f"order_{index}"]['cant_product']
        status = data[f"order_{index}"]['status']
        shipping_destination = data[f"order_{index}"]['shipping_destination']
        seller = data[f"order_{index}"]['seller']
        client = data[f"order_{index}"]['client']
        order_date = data[f"order_{index}"]['order_date']
        date_update = data[f"order_{index}"]['date_update']

        text_id = ft.Text(f"Id: {id}")
        text_cant = ft.Text(f"cantidad: {cant_product}"
                            )
        text_status = ft.Text(f"Status: {status}")
        text_destination = ft.Text(f"Destino: {shipping_destination}")
        text_client = ft.Text(f"Cliente: {client}")
        text_seller = ft.Text(f"Vendedor: {seller}")
        text_order_date = ft.Text(f"Fecha de realicion: {order_date}")
        text_date_update = ft.Text(f"Fecha de atualizacion: {date_update}")

        col = ft.Column([text_id, text_cant, text_status, text_destination,
                        text_client, text_seller, text_order_date, text_date_update])

        def on_regret(e):
            nonlocal index
            if index != 0:

                index -= 1

                id = data[f"order_{index}"]['id']
                cant_product = data[f"order_{index}"]['cant_product']
                status = data[f"order_{index}"]['status']
                shipping_destination = data[f"order_{index}"]['shipping_destination']
                seller = data[f"order_{index}"]['seller']
                client = data[f"order_{index}"]['client']
                order_date = data[f"order_{index}"]['order_date']
                date_update = data[f"order_{index}"]['date_update']

                text_id = ft.Text(f"Id: {id}")
                text_cant = ft.Text(f"cantidad: {cant_product}"
                                    )
                text_status = ft.Text(f"Status: {status}")
                text_destination = ft.Text(f"Destino: {shipping_destination}")
                text_client = ft.Text(f"Cliente: {client}")
                text_seller = ft.Text(f"Vendedor: {seller}")
                text_order_date = ft.Text(f"Fecha de realicion: {order_date}")
                text_date_update = ft.Text(
                    f"Fecha de atualizacion: {date_update}")

        page.update()

        def on_next(e):
            nonlocal index
            if index < len(items) - 1:
                index += 1

                id = data[f"order_{index}"]['id']
                cant_product = data[f"order_{index}"]['cant_product']
                status = data[f"order_{index}"]['status']
                shipping_destination = data[f"order_{index}"]['shipping_destination']
                seller = data[f"order_{index}"]['seller']
                client = data[f"order_{index}"]['client']
                order_date = data[f"order_{index}"]['order_date']
                date_update = data[f"order_{index}"]['date_update']

                text_id.value = f"Id: {id}"
                text_cant.value = f"cantidad: {cant_product}"

                text_status.value = f"Status: {status}"
                text_destination.value = f"Destino: {shipping_destination}"
                text_client.value = f"Cliente: {client}"
                text_seller.value = f"Vendedor: {seller}"
                text_order_date.value = f"Fecha de realicion: {order_date}"
                text_date_update.value = f"Fecha de atualizacion: {date_update}"

            page.update()

        buttom_regret = ft.ElevatedButton(text="Regresar", on_click=on_regret)
        buttom_next = ft.ElevatedButton(text="Siguiente", on_click=on_next)

        row_butom = ft.Row([buttom_regret, buttom_next])

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

    row_buttom = ft.Row([buttom_create_order, buttom_watch_order])

    row_3 = ft.Row([text], alignment=ft.MainAxisAlignment.CENTER)

    page.add(row_3)
    page.add(row_buttom)

    page.update()
