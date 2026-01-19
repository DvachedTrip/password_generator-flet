import flet as ft

from generator import generate_password
from storage import save_password

def main (page: ft.Page):
    page.title = "Password Generator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    def generate_password_click(e):
        try:
            password_field.error = None
            password_field.value = generate_password(int(length_input.value),use_uppercase=checkbox_upper.value,
                                                                            use_digit=checkbox_nums.value,
                                                                            use_special=checkbox_spec.value)
            password_field.update()
        except ValueError:
            length_input.error = "Введите корректное число (1-50)"
            length_input.update()


    def change_service_visibility(e):
        service_input.visible = checkbox_service.value
        save_password_bt.visible = checkbox_service.value
        
        service_input.update()
        save_password_bt.update()


    def save_password_click(e):
        service = service_input.value
        password = password_field.value

        if not password_field.value:
            password_field.error = "Пароль пустой"
            password_field.update()
            return

        if not service_input.value:
            service_input.error = "Введите сервис"
            service_input.update()
            return
        
        save_password(service,password)


    def clear_error(e):
        e.control.error = None
        e.control.update()


    password_field = ft.TextField(value="", label="Generated Password", width=400, read_only=True)
    length_input = ft.TextField(label="Password Length", value="12", width=300)
    service_input = ft.TextField(label="Service", hint_text = "Enter the service name", width=400)
    checkbox_service = ft.Checkbox(label="Input Service", on_change=change_service_visibility, value=True)

    save_password_bt = ft.ElevatedButton("Save Password", on_click=save_password_click)

    checkbox_upper = ft.Checkbox(label="Include Uppercase Letters", value=True)
    checkbox_nums = ft.Checkbox(label="Include Numbers", value=True)
    checkbox_spec = ft.Checkbox(label="Include Special Characters", value=True)
    length_input.on_change = clear_error
    service_input.on_change = clear_error

    page.add(
        ft.Row([ft.Text("Password Generator", size=30, weight=ft.FontWeight.BOLD)], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.Text("Создайте надежный пароль для защиты вашей информации.", size=16)], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([service_input], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([password_field], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton("Generate Password", on_click=generate_password_click), 
                (save_password_bt)], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([checkbox_service, checkbox_upper, checkbox_nums, checkbox_spec, length_input], alignment=ft.MainAxisAlignment.CENTER),
        )

ft.app(target=main)