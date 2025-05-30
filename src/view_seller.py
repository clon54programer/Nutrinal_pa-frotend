import flet as ft
import requests
from view_admin import buttom_regression


def view_general_seller(page: ft.Page):

    text = ft.Text("Vendedor",
                   color=ft.Colors.BLACK, text_align=ft.TextAlign.CENTER, size=40, style=ft.TextAlign.CENTER)

    def create_order(e):

        print()
        page.remove(row_buttom)
        page.remove(row_3)
        page.remove(row_client)
        # "data":{
        # "identifier_client": ""
        # "identifier_seller": "",
        # "code_product":"",
        # "cant_product":{},
        # "shipping_destination": ""

        text_main = ft.Text("Crear pedidos",
                            color=ft.Colors.BLACK, text_align=ft.TextAlign.CENTER, size=40, style=ft.TextAlign.CENTER)

        text_code_client = ft.Text("Codigo del cliente")
        text_code_client_field = ft.TextField(
            label="Ingrese el codigo del cliente")

        text_code_seller = ft.Text("Codigo del vendedor")
        text_code_seller_field = ft.TextField(
            label="Ingrese el codigo del vendedor")

        text_destination = ft.Text("Destino del envio")
        text_destination_field = ft.TextField(
            label="Ingrese el destino del pedido")

        productos = []
        cants = []
        col_select_product = ft.Column(scroll=ft.ScrollMode.AUTO)

        r = requests.get(
            "http://127.0.0.1:8000/nutrinal_pa/admin/get_product")

        json = r.json()

        data = json.get("data", {})

        items: dict = dict(data.items())
        index: int = 0

        name = items[f"product_{index}"]["name"]
        code = items[f"product_{index}"]["code"]
        price = items[f"product_{index}"]["price"]
        description = items[f"product_{index}"]["description"]

        json_code = {"code": code}
        r_2 = requests.post(
            "http://127.0.0.1:8000/nutrinal_pa/admin/get_cant_product", json=json_code)
        cant_avaible = r_2.json().get("data", {}).get("cant_product", "No disponible")

        text_product = ft.Text("Producto",
                               color=ft.Colors.BLACK, text_align=ft.TextAlign.CENTER, size=25, style=ft.TextAlign.CENTER)

        text_index = ft.Text(f"Producto {index}")
        text_name = ft.Text(f"Name: {name}")
        text_code = ft.Text(f"Codigo: {code}")
        text_price = ft.Text(f"Precio: {price}")
        text_description = ft.Text(f"Descripcion: {description}")
        text_cant_avaible = ft.Text(f"Cantidad disponible: {cant_avaible}")

        def on_regret(e):
            nonlocal index
            if index != 0:
                index -= 1
                name = items[f"product_{index}"]["name"]
                code = items[f"product_{index}"]["code"]
                price = items[f"product_{index}"]["price"]
                description = items[f"product_{index}"]["description"]

                json_code = {"code": code}
                r_2 = requests.post(
                    "http://127.0.0.1:8000/nutrinal_pa/admin/get_cant_product", json=json_code)
                cant_avaible = r_2.json().get("data", {}).get("cant_product", "No disponible")

                text_index.value = f"Producto {index}"
                text_name.value = f"Name: {name}"
                text_code.value = f"Codigo: {code}"
                text_price.value = f"Precio: {price}"
                text_description.value = f"descripcion: {description}"
                text_cant_avaible.value = f"Cantidad disponible: {cant_avaible}"

            page.update()

        def on_next(e):
            nonlocal index
            if index < len(items) - 1:
                index += 1

                name = items[f"product_{index}"]["name"]
                code = items[f"product_{index}"]["code"]
                price = items[f"product_{index}"]["price"]
                description = items[f"product_{index}"]["description"]

                json_code = {"code": code}
                r_2 = requests.post(
                    "http://127.0.0.1:8000/nutrinal_pa/admin/get_cant_product", json=json_code)
                cant_avaible = r_2.json().get("data", {}).get("cant_product", "No disponible")

                text_index.value = f"Producto {index}"
                text_name.value = f"Name: {name}"
                text_code.value = f"Codigo: {code}"
                text_price.value = f"Precio: {price}"
                text_description.value = f"descripcion: {description}"
                text_cant_avaible.value = f"Cantidad disponible: {cant_avaible}"

            page.update()
        text_cant = ft.TextField(label="Ingrese la cantidad del producto")

        def on_click_escoger(e):

            if index not in productos and text_cant != "":
                productos.append(index)
                cants.append(text_cant)

                name = items[f"product_{index}"]["name"]
                code = items[f"product_{index}"]["code"]
                price = items[f"product_{index}"]["price"]

                col_select_product.controls.append(ft.Container(content=ft.Column(controls=[ft.Text(f"Producto {index}"),
                                                                                            ft.Text(
                                                                                                f"Name: {name}"),
                                                                                            ft.Text(
                                                                                                f"Codigo: {code}"),
                                                                                            ft.Text(
                                                                                                f"Precio: {price}")

                                                                                            ])))

                col_select_product.update()

        buttom_regret = ft.ElevatedButton(text="Regresar", on_click=on_regret)
        buttom_escoger = ft.ElevatedButton(
            text="Escoger", on_click=on_click_escoger)
        buttom_next = ft.ElevatedButton(text="Siguiente", on_click=on_next)

        text_elegidos = ft.Text("Elegidos",
                                color=ft.Colors.BLACK, text_align=ft.TextAlign.CENTER, size=25, style=ft.TextAlign.CENTER)

        row_butom = ft.Row([buttom_regret, buttom_escoger, buttom_next])

        col = ft.Column(controls=[text_main, text_code_client, text_code_client_field,
                        text_code_seller, text_code_seller_field, text_destination, text_destination_field, text_product,
                        text_index, text_name, text_code, text_price, text_description],
                        scroll=ft.ScrollMode.ALWAYS)

        def on_click_send_info(e):

            def get_code_product(lista: list[int]) -> list[str]:
                data = []

                for value in lista:
                    data.append(items[f"product_{index}"]["code"])

                return data

            def get_cant_product(lista: list[int], lista_2: list[int]) -> dict[str, str | int]:
                data = {}
                count = 0
                for value in lista:
                    data[f"code_{count}"] = {"code": items[f"product_{index}"]["code"],
                                             "cant_product": lista_2[count]
                                             }

                    count += 1

                return data

            code_product = get_code_product(productos)
            cant_product = get_cant_product(productos, cants)

            data = {
                "data": {
                    "identifier_client": text_code_client_field.value,
                    "identifier_seller": text_code_seller_field.value,
                    "code_product": code_product,
                    "cant_product": cant_product,
                    "shipping_destination": "jajjdjjd"
                }
            }

            url = f"http://127.0.0.1:8000/nutrinal_pa/make_order"

            r = requests.post(url=url, json=data)

        butttom_send = ft.ElevatedButton(
            "Enviar informacion", on_click=on_click_send_info)

        col.controls.append(row_butom)
        col.controls.append(text_cant)
        col.controls.append(text_elegidos)

        col.controls.append(col_select_product)

        def on_click(e):
            buttom_regression(
                page, [col, butttom_send, regret], view_general_seller)

        regret = ft.ElevatedButton(
            text="Regresar a la anterior vista", on_click=on_click)

        page.add(col)
        page.add(butttom_send)
        page.add(regret)
        page.scroll = ft.ScrollMode.ALWAYS
        page.update()

    def view_watch_order(e):
        # "data":{
        # "identifier_client": ""
        # "identifier_seller": "",
        # "code_product":"",
        # "cant_product":{},
        # "shipping_destination": ""
        page.remove(row_buttom)
        page.remove(row_3)
        page.remove(row_client)

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

        text_index = ft.Text(f"Pedido_{index}")
        text_id = ft.Text(f"Id: {id}")
        text_cant = ft.Text(f"cantidad: {cant_product}"
                            )
        text_status = ft.Text(f"Status: {status}")
        text_destination = ft.Text(f"Destino: {shipping_destination}")
        text_client = ft.Text(f"Cliente: {client}")
        text_seller = ft.Text(f"Vendedor: {seller}")
        text_order_date = ft.Text(f"Fecha de realicion: {order_date}")
        text_date_update = ft.Text(f"Fecha de atualizacion: {date_update}")

        col = ft.Column([text_index, text_id, text_cant, text_status, text_destination,
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

                text_index.value = f"Pedido_{index}"
                text_id.value = f"Id: {id}"
                text_cant.value = f"cantidad: {cant_product}"
                text_status.value = f"Status: {status}"
                text_destination.value = f"Destino: {shipping_destination}"
                text_client.value = f"Cliente: {client}"
                text_seller.value = f"Vendedor: {seller}"
                text_order_date.value = f"Fecha de realicion: {order_date}"
                text_date_update.value = f"Fecha de atualizacion: {date_update}"

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

                text_index.value = f"Pedido_{index}"
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

        def on_click(e):
            buttom_regression(
                page, [text, col, row_butom, regret], view_general_seller)

        regret = ft.ElevatedButton(
            text="Regresar a la anterior vista", on_click=on_click)

        page.add(text)
        page.add(col)
        page.add(row_butom)
        page.add(regret)

        page.update()

    def view_create_client(e):

        page.remove(row_buttom)
        page.remove(row_3)
        page.remove(row_client)

        text = ft.Text("Crear Cliente",
                       color=ft.Colors.BLACK, text_align=ft.TextAlign.CENTER, size=40, style=ft.TextAlign.CENTER)

        text_name = ft.Text("Nombre")
        text_name_seller = ft.TextField(label="Ingrese el nombre del cliente")

        text_email = ft.Text("Email")
        text_email_seller = ft.TextField(label="Ingrese el Email del cliente")

        text_phone = ft.Text("Numero de telefono")
        text_phone_seller = ft.TextField(
            label="Ingrese el numero de telefono del cliente")

        text_id = ft.Text("Identificaccion")
        text_id_seller = ft.TextField(label="Ingrese el id del cliente")

        col = ft.Column(controls=[text_name, text_name_seller, text_email,
                        text_email_seller, text_phone, text_phone_seller, text_id, text_id_seller])

        text_info = ft.Text("No hay errores")

        def on_click_send_info(e):

            json = {
                "data": {
                    "name": text_name_seller.value,
                    "email": text_email_seller.value,
                    "phone_number": text_phone_seller.value,
                    "identifier": text_id_seller.value
                }
            }

            r = requests.post(
                "http://127.0.0.1:8000/nutrinal_pa/create_client", json=json)

            if r.status_code != 200:
                json_error = r.json()
                # text_info.value = f"[ERROR] {json}"
                print(json_error)
            else:
                text_info.value = "La informacion se mando de forma correcta."

        butoo_send = ft.ElevatedButton(
            "Enviar informacion", on_click=on_click_send_info)

        def on_click(e):
            buttom_regression(
                page, [col, text_info, regret, butoo_send], view_general_seller)

        regret = ft.ElevatedButton(
            text="Regresar a la anterior vista", on_click=on_click)

        page.add(col)
        page.add(text_info)
        page.add(butoo_send)
        page.add(regret)

    buttom_create_order = ft.Container(content=ft.Text("Hacer un pedido"), margin=10,
                                       padding=10,
                                       alignment=ft.alignment.center,
                                       bgcolor=ft.Colors.AMBER,
                                       width=150,
                                       height=150,
                                       border_radius=10, on_click=create_order)

    buttom_watch_order = ft.Container(
        content=ft.Text("Ver pedidos"), margin=10,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=ft.Colors.BLUE,
        width=150,
        height=150,
        border_radius=10, on_click=view_watch_order)

    buttom_create_client = ft.Container(
        content=ft.Text("Registrar cliente"), margin=10,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=ft.Colors.GREEN,
        width=150,
        height=150,
        border_radius=10, on_click=view_create_client)

    row_buttom = ft.Row([buttom_create_order, buttom_watch_order])
    row_client = ft.Row([buttom_create_client])

    row_3 = ft.Row([text], alignment=ft.MainAxisAlignment.CENTER)

    page.add(row_3)
    page.add(row_buttom)
    page.add(row_client)

    page.update()
