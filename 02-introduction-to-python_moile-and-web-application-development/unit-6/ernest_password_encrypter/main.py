import flet as ft
from cryptography.fernet import Fernet

# Generate (or load) a key for encryption/decryption
# In a real app, you'd save this securely rather than generating it each run
key = Fernet.generate_key()
fernet = Fernet(key)


def main(page: ft.Page):
    page.title = "Password Encrypter"
    page.window.width = 420
    page.window.height = 500
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20

    input_text = ft.TextField(
        label="Enter password/text",
        password=False,
        width=380
    )

    output_text = ft.TextField(
        label="Result",
        width=380,
        multiline=True,
        read_only=True
    )

    key_display = ft.Text(
        value=f"Encryption key:\n{key.decode()}",
        size=12,
        selectable=True,
        color=ft.Colors.GREY_700
    )

    def encrypt_click(e):
        if input_text.value:
            encrypted = fernet.encrypt(input_text.value.encode())
            output_text.value = encrypted.decode()
            page.update()

    def decrypt_click(e):
        if input_text.value:
            try:
                decrypted = fernet.decrypt(input_text.value.encode())
                output_text.value = decrypted.decode()
            except Exception:
                output_text.value = "Invalid encrypted text or wrong key!"
            page.update()

    def copy_result(e):
        if output_text.value:
            page.set_clipboard(output_text.value)
            page.snack_bar = ft.SnackBar(content=ft.Text("Copied to clipboard!"))
            page.snack_bar.open = True
            page.update()

    encrypt_btn = ft.Button(content="Encrypt", on_click=encrypt_click, width=180)
    decrypt_btn = ft.Button(content="Decrypt", on_click=decrypt_click, width=180)
    copy_btn = ft.TextButton(content="Copy Result", on_click=copy_result)

    page.add(
        ft.Text("Password Encrypter", size=24, weight=ft.FontWeight.BOLD),
        input_text,
        ft.Row([encrypt_btn, decrypt_btn], alignment=ft.MainAxisAlignment.CENTER),
        output_text,
        copy_btn,
        ft.Divider(),
        key_display,
    )


ft.run(main)