import flet as ft
import requests


# Funciones
# crear vendedores
# ver vendedores
# crear productos y produciones
# ver los pedidos

page_copy: ft.Page = None


def buttom_regression(page: ft.Page, controls_remove: list[ft.Control], func) -> None:

    for control in controls_remove:
        page.remove(control)

    page.update()

    func(page)


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

            page.update()

        buttom_regret = ft.ElevatedButton(text="Regresar", on_click=on_regret)
        buttom_next = ft.ElevatedButton(text="Siguiente", on_click=on_next)

        row_butom = ft.Row([buttom_regret, buttom_next])

        def on_click(e):
            buttom_regression(
                page, [text_1, text_2, text_3, text_4, text_5, row_butom, regret], view_general)

        regret = ft.ElevatedButton(
            text="Regresar a la anterior vista", on_click=on_click)

        page.add(text_1)
        page.add(text_2)
        page.add(text_3)
        page.add(text_4)
        page.add(text_5)

        page.add(row_butom)
        page.add(regret)

        page.update()

    # fin de wacth seller

    def view_create_seller(e):
        # seller1 = Seller.objects.create(name="Juan Pérez", identifier="123456")
        # seller_login1 = SellerLogin.objects.create(
        # identifier=seller1, username="juan_vendedor", password="securepass")
        page.remove(row)
        page.remove(row_2)
        page.remove(row_3)
        page.remove(buttom_watch_orders)

        text_main = ft.Text("Crear un nuevo vendedor", color=ft.Colors.BLACK,
                            text_align=ft.TextAlign.CENTER, size=40, style=ft.TextAlign.CENTER)

        row_text_main = ft.Row(
            controls=[text_main], alignment=ft.MainAxisAlignment.CENTER)

        text_name = ft.Text("Nombre")
        text_name_seller = ft.TextField(label="ingrese un nombre")

        text_identifier = ft.Text("Identificacion")
        text_identifier_seller = ft.TextField(
            label="ingrese la identificacion")

        text_username = ft.Text("Usuario y constraseña")
        text_username_seller = ft.TextField(label="Ingrese el usuario")
        text_password_seller = ft.TextField(label="Ingrese la contraseña")

        def on_click_send_info(e):

            data = {"data": {
                "name": text_name_seller.value,
                "id": text_identifier_seller.value,
                "username": text_username_seller.value,
                "password": text_password_seller.value,
            }}

            r = requests.post(
                url="http://127.0.0.1:8000/nutrinal_pa/admin/create_seller_login", json=data)

            if r.status_code != 200:
                error = r.json()["data"]["details"]
                print(
                    f"Hubo un error al mandar la informacion. Detalles {error}")

            else:
                print("La informacion fue mandada exitosamente")

        buttom_send_seller = ft.ElevatedButton(
            "Enviar informacion", on_click=on_click_send_info)

        def on_click(e):
            buttom_regression(
                page, [col, row_text_main, regret], view_general)

        regret = ft.ElevatedButton(
            text="Regresar a la anterior vista", on_click=on_click)

        col = ft.Column(controls=[text_name, text_name_seller, text_identifier,
                        text_identifier_seller, text_username, text_username_seller, text_password_seller, buttom_send_seller])
        page.add(row_text_main)
        page.add(col)
        page.add(regret)

    def view_create_product_and_productions(e):
        # Crear un producto
        # product = Product.objects.create(name="Suplemento Nutricional", code="PROD001",
        #                             price=49.99, description="Mejora la salud y el bienestar.")
        # Crear una producción para el producto
        # production = Production.objects.create(product=product, cant_available=100)
        page.remove(row)
        page.remove(row_2)
        page.remove(row_3)
        page.remove(buttom_watch_orders)

        text_main = ft.Text("Crear un nuevo producto", color=ft.Colors.BLACK,
                            text_align=ft.TextAlign.CENTER, size=40, style=ft.TextAlign.CENTER)
        row_text_main = ft.Row(
            controls=[text_main], alignment=ft.MainAxisAlignment.CENTER)

        text_name = ft.Text("Nombre del producto")
        text_name_product = ft.TextField(
            label="Ingrese el nombre del producto")

        text_code = ft.Text("Codigo del producto")
        text_code_product = ft.TextField(
            label="Ingrese el codigo del producto")

        text_price = ft.Text("El precio del producto")
        text_precio_product = ft.TextField(
            label="Ingrese el precio del producto", keyboard_type=ft.KeyboardType.NUMBER)

        text_description = ft.Text("Descripcion del producto")
        text_description_product = ft.TextField(
            label="Ingrese la decripcion del producto")

        text_info = ft.Text("No error")

        def on_click_send_info(e):
            try:
                price = int(text_precio_product.value)

                value_list = [text_name_product.value,
                              text_code_product.value, text_description_product.value, text_precio_product.value]

                for value in value_list:
                    if not value.strip():
                        text_info.value = "[ERROR] Hay un campo que esta vacio"
                        page.update()
                        return

                json = {"data": {
                        "name": text_name_product.value,
                        "code": text_code_product.value,
                        "price": price,
                        "description": text_description_product.value
                        }}

                r = requests.post(
                    "http://127.0.0.1:8000/nutrinal_pa/admin/make_product", json=json)

                if r.status_code != 200:

                    details = r.json()['data']['details']

                    text_info.value = f"[Error] {details}"
                else:
                    text_info.value = "La informacion ha sido mandada exitosamente"

                page.update()

            except (TypeError, ValueError):

                text_info.value = "El campo de precio tieen caracters que no son numeros"
                page.update()

        buttom_send_seller = ft.ElevatedButton(
            "Enviar informacion", on_click=on_click_send_info)

        col = ft.Column(controls=[text_name, text_name_product, text_code,
                        text_code_product, text_price, text_precio_product, text_description, text_description_product, text_info, buttom_send_seller])

        def on_click(e):
            buttom_regression(
                page, [col, row_text_main, regret], view_general)

        regret = ft.ElevatedButton(
            text="Regresar a la anterior vista", on_click=on_click)

        page.add(row_text_main)
        page.add(col)
        page.add(regret)

        # content = {"data": {
        #    "name": "Producto Ejemplo",
        #    "code": "P12345",
        #    "price": 1000.50,
        #    "description": "Este es un producto de prueba"
        # }}

    def view_watch_production(e):
        page.remove(row)
        page.remove(row_2)
        page.remove(row_3)
        page.remove(buttom_watch_orders)

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

        text_index = ft.Text(f"Producto {index}")
        text_name = ft.Text(f"Name: {name}")
        text_code = ft.Text(f"Codigo: {code}")
        text_price = ft.Text(f"Precio: {price}")
        text_description = ft.Text(f"Descripcion: {description}")
        text_cant_avaible = ft.Text(f"Cantidad disponible: {cant_avaible}")
        # text_cant = ft.Text(f"Cantidad: {cant}")

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

        buttom_regret = ft.ElevatedButton(text="Regresar", on_click=on_regret)
        buttom_next = ft.ElevatedButton(text="Siguiente", on_click=on_next)

        row_butom = ft.Row([buttom_regret, buttom_next])

        col = ft.Column(controls=[text_index, text_name,
                        text_code, text_price, text_description, text_cant_avaible])

        def on_click(e):
            buttom_regression(
                page, [col, row_butom, regret], view_general)

        regret = ft.ElevatedButton(
            text="Regresar a la anterior vista", on_click=on_click)

        page.add(col)

        page.add(row_butom)
        page.add(regret)

        # product_1": {
        # "name": "p",
        # "code": "123",
        # "price": "122.00",
        # "description": "Jan"

    def view_watch_orders(e):
        page.remove(row)
        page.remove(row_2)
        page.remove(row_3)
        page.remove(buttom_watch_orders)

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
                page, [text, col, row_butom, regret], view_general)

        regret = ft.ElevatedButton(
            text="Regresar a la anterior vista", on_click=on_click)

        page.add(text)
        page.add(col)
        page.add(row_butom)
        page.add(regret)

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
        border_radius=10, on_click=view_create_seller)

    buttom_create_production = ft.Container(
        content=ft.Text("Crear producto"), margin=10,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=ft.Colors.ORANGE,
        width=150,
        height=150,
        border_radius=10,  on_click=view_create_product_and_productions)

    buttom_watch_production = ft.Container(
        content=ft.Text("Ver productos"), margin=10,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=ft.Colors.ORANGE_700,
        width=150,
        height=150,
        border_radius=10, on_click=view_watch_production)

    buttom_watch_orders = ft.Container(content=ft.Text("Ver pedidos"), margin=10,
                                       padding=10,
                                       alignment=ft.alignment.center,
                                       bgcolor=ft.Colors.YELLOW,
                                       width=150,
                                       height=150,
                                       border_radius=10, on_click=view_watch_orders)

    row = ft.Row([buttom_create_seller, buttom_watch_seller])
    row_2 = ft.Row([buttom_create_production, buttom_watch_production])

    row_3 = ft.Row([text], alignment=ft.MainAxisAlignment.CENTER)

    # def on_click(e):
    #    import main
    #    buttom_regression(
    #        page, [row_3, row_2, row, buttom_watch_orders, regret, text], main.main)

    # regret = ft.ElevatedButton(
    #    text="Regresar a la anterior vista", on_click=on_click)

    page.add(row_3)
    page.add(row)
    page.add(row_2)

    page.add(buttom_watch_orders)
    # page.add(regret)

    page.update()
