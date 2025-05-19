import flet as ft


def main(page: ft.Page):

    text_user = ft.Text("Usuario")

    username_field = ft.TextField(label="Ingrese su usuario")

    text_password = ft.Text("Contraseña")

    password_field = ft.TextField(label="Escriba su contraseña", password=True)

    text_list = ft.Text("¿Que tipo de usuario es?")
    type_user = []

    type_user.append(ft.DropdownOption(content=ft.Text(
        value="Cliente"), key="Cliente"))

    type_user.append(ft.DropdownOption(content=ft.Text(
        value="Administrador"), key="Administrador"))

    type_user.append(ft.DropdownOption(content=ft.Text(
        value="Vendedor"), key="Vendedor"))

    list_type_user = ft.Dropdown(
        options=type_user)

    def send_info(e) -> None:

        if username_field.value != None or password_field.value != None:
            print("Un campo esta vacio")
        else:
            print("user: ", username_field.value)
            print("password: ", password_field.value)
            print("Tipo de usuario: ", list_type_user.value)

    send_buttom = ft.ElevatedButton(text="Enviar", on_click=send_info)

    page.add(text_user)
    page.add(username_field)

    page.add(text_password)
    page.add(password_field)

    page.add(text_list)
    page.add(list_type_user)

    page.add(send_buttom)


ft.app(main)
