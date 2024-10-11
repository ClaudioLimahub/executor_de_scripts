# Executor de scripts

Este script Python cria uma interface gráfica para automatizar a execução de diversos scripts Python relacionados à análise de dados ou automações. A aplicação usa a biblioteca Tkinter para criar a interface e exibir botões que executam diferentes scripts. Além disso, a interface possui uma imagem de fundo e um ícone personalizado.

## Funcionalidades

1. **Interface gráfica**: Cria uma interface gráfica com Tkinter, incluindo botões para executar scripts e uma imagem de fundo redimensionável.
2. **Gerenciamento de scripts**: Permite a execução de scripts Python específicos ao clicar nos botões correspondentes.
3. **Imagem de fundo e ícone**: Define uma imagem de fundo e um ícone para a aplicação, ambos personalizados.
4. **Mensagens de confirmação e Erro**: Exibe mensagens de confirmação antes da execução dos scripts e mensagens de erro quando necessário.
5. **Fechar a aplicação**: Permite ao usuário fechar a aplicação com uma mensagem de confirmação.

## Requisitos

- **Bibliotecas Python**: `tkinter`, `PIL`, `subprocess`, `os`, `emoji`
- **Imagens**: Certifique-se de ter os arquivos de imagem (`Nome da imagem de fundo.jpg` e `Imagem do icone.png`) na pasta `imagem_de_fundo`.

## Estrutura do Código

### Funções Principais:

- **`set_background_image`**: Define a imagem de fundo da aplicação.
- **`resize_background_image`**: Redimensiona a imagem de fundo conforme o tamanho da janela.
- **`create_buttons`**: Cria botões para executar os scripts definidos.
- **`confirm_and_run_script`**: Exibe uma mensagem de confirmação antes de executar um script.
- **`run_script`**: Executa o script selecionado e trata possíveis erros.
- **`show_error_message`**: Exibe uma mensagem de erro.
- **`confirm_close`**: Exibe uma mensagem de confirmação ao tentar fechar a aplicação.
- **`on_closing`**: Intercepta a ação de fechar a janela do Windows.

### Uso

1. **Preparação**:
   - Certifique-se de que as imagens (`Nome da imagem de fundo.jpg` e `Imagem do icone.png`) estão localizadas na pasta `imagem_de_fundo`.
   - Coloque os scripts Python nos diretórios especificados no código.

2. **Executar a aplicação**:
   ```bash
   python nome_do_arquivo.py

3. **Interação com a aplicação**:
   - Botões à Esquerda: Executam scripts relacionados ao banco de dados.
   - Botões à Direita: Executam scripts relacionados ao Excel.
   - Botão Fechar: Fecha a aplicação após uma confirmação.

# Contribuições
Sinta-se à vontade para contribuir com melhorias ou correções para este script. Abra uma issue ou um pull request para colaborar.
