# Calculadora de IMC usando Flet
# Importar flet como ft, para facilitar
import flet as ft

#definir página principal
def main(page: ft.Page):
    # Título da página e definição de padding
    page.title = "Calculadora de IMC"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)

    # Campos de entrada, para adição de informações.
    # Variáveis globais peso e altura
    peso = ft.TextField(label="🏋️ Peso (kg)", width=200, keyboard_type=ft.KeyboardType.NUMBER)
    altura = ft.TextField(label="📏 Altura (m)", width=200, keyboard_type=ft.KeyboardType.NUMBER)

    # Campo de resultado
    resultado = ft.Text(
        "Digite os valores e clique em Calcular",
        size=20, # Tamanho da fonte
        text_align=ft.TextAlign.CENTER, # Alinhamento do texto
        color=ft.Colors.GREY_600 # Cor da fonte
    )

    # Função de cálculo
    def calcular(e):
        try:
            # Conversão dos valores de entrada para float (valores decimais)
            p = float(peso.value)
            a = float(altura.value)

            # Verificação se altura é maior que zero para evitar divisão por zero
            if a <= 0:
                resultado.value = "❌ Erro: altura deve ser maior que zero!"
                resultado.color = ft.Colors.RED # Texto de erro aparecer em vermelho
            else:
                # Cálculo do IMC Peso / (Altura * Altura)
                imc = p / (a * a)

                # Classificação do IMC
                if imc < 18.5:
                    classificacao = "Baixo peso"
                    cor = ft.Colors.ORANGE
                elif 18.5 <= imc < 25:
                    classificacao = "Peso normal"
                    cor = ft.Colors.GREEN
                elif 25 <= imc < 30:
                    classificacao = "Sobrepeso"
                    cor = ft.Colors.AMBER
                else:
                    classificacao = "Obesidade"
                    cor = ft.Colors.RED
                # Exibição do resultado com duas casas decimais
                resultado.value = f"📊 Seu IMC é {imc:.2f} → {classificacao}"
                resultado.color = cor

        # Tratamento de erro para valores inválidos
        except ValueError:
            resultado.value = "❌ Digite números válidos!"
            resultado.color = ft.Colors.RED
        # Atualizar a página para mostrar o resultado
        page.update()

    # Alternância entre tema claro e escuro
    def alternar_tema(e):
        page.theme_mode = (
            # Se o tema atual for claro, mude para escuro, e vice-versa
            ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        )
        # Carregar na página o tema atualizado
        page.update()

    # AppBar
    page.appbar = ft.AppBar(
        # Icone do app
        leading=ft.Icon(ft.Icons.MULTILINE_CHART),
        # Largura do ícone
        leading_width=40,
        # Título do app
        title=ft.Text("Calculadora IMC"),
        # Não centralizar o título
        center_title=False,
        # Cor de fundo da AppBar
        bgcolor=ft.Colors.ON_SURFACE_VARIANT,
        # Ações na AppBar (tema claro/escuro)
        actions=[
            # Linha com ícone, switch e ícone
            ft.Row(
                controls=[
                    ft.Text("☾"),
                    ft.Switch(value=False, on_change=alternar_tema),
                    ft.Text("𖤓"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ],
    )


    # Função limpar
    def limpar(e):
        # Limpar os campos de entrada e o resultado
        peso.value = altura.value = ""
        resultado.value = "Digite os valores e clique em Calcular"
        resultado.color = ft.Colors.GREY_600
        # Atualizar a página para mostrar os campos limpos
        page.update()

    # Interface
    page.add(
        ft.Column([
            # Título da aplicação
            ft.Text("🧮 Calculadora de IMC", size=24, weight=ft.FontWeight.BOLD),
            altura,
            peso,
            # Linha com botões Calcular e Limpar
            ft.Row([
                ft.ElevatedButton("🟢 Calcular", on_click=calcular, width=150,
                                  bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE),
                ft.ElevatedButton("🧹 Limpar", on_click=limpar, width=150,
                                  bgcolor=ft.Colors.GREY, color=ft.Colors.WHITE),
            ],
            # Alinhamento central e espaçamento entre os botões
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20),
            ft.Divider(),
            resultado
        ],
        # Alinhamento central e espaçamento entre os elementos
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20)
    )

# Executar o app
ft.app(target=main)
