# Como configurar/instalar/usar o `screenkey` no `Linux Ubuntu`

## Resumo

Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `screenkey` no `Linux Ubuntu`.

## _Abstract_

_In this document are contained the main commands and settings to set up/install the `screenkey` on `Linux Ubuntu`._


## Descrição [2]

### `screenkey`

O `screenkey` é uma ferramenta de código aberto para sistemas `Linux` que exibe as teclas
pressionadas no momento em uma sobreposição na tela, funcionando como uma ajuda visual especialmente
útil em apresentações, tutoriais em vídeo ou durante sessões de compartilhamento de tela, onde é
importante mostrar aos espectadores quais comandos estão sendo digitados. Depois de ser iniciado,
o `screenkey` captura a entrada do teclado e a exibe de forma discreta e legível, permitindo
personalizar aspectos como posição na tela, duração da exibição, fontes, cores e transparência.
Isso ajuda a tornar demonstrações ou tutoriais mais compreensíveis, garantindo que os espectadores
possam acompanhar comandos específicos ou sequências de teclas sem perder o contexto da tela
principal que está sendo compartilhada.


## 1. Como configurar/instalar/usar o `screenkey` no `Linux Ubuntu` [1]

Para instalar o `screenkey` no `Linux Ubuntu` usando os repositórios oficiais do sistema e o
gerenciador de pacotes `apt`, você pode seguir estes passos:

1. Abrir o `Terminal Emulator`. Você pode fazer isso pressionando:

    ```bash
    Ctrl + Alt + T
    ```

2. Certifique-se de que seu sistema esteja limpo e atualizado.

    2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
    ```bash
    sudo apt clean
    ```

    2.2 Remover pacotes `.deb` antigos ou duplicados do `cache` local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando:
    ```bash
    sudo apt autoclean
    ```

    2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando:
    ```bash
    sudo apt autoremove -y
    ```

    2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`:
    ```bash
    sudo apt update
    ```

    2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes:
    ```bash
    sudo apt --fix-broken install
    ```

    2.6 Limpar o `cache` do gerenciador de pacotes `apt` novamente:
    ```bash
    sudo apt clean
    ```

    2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:
    ```bash
    sudo apt list --upgradable
    ```

    2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`:
    ```bash
    sudo apt full-upgrade -y
    ```

## 1.2 Instalar e usar o `screenkey`

1. **Instalar o `screenkey` utilizando o gerenciador de pacotes `apt`:**

    ```bash
    sudo apt install screenkey -y
    ```

    Após a instalação, você pode iniciar o `screenkey` diretamente pelo `Terminal Emulator` digitando
    o comando abaixo ou procurando por ele no menu de aplicativos:

    ```bash
    screenkey
    ```

    O `screenkey` é uma ferramenta útil para demonstrações ou gravações de tela, pois exibe as
    teclas pressionadas em tempo real, facilitando o entendimento de comandos e atalhos utilizados
    durante a sessão. Se desejar personalizar as configurações, como posição, tamanho e duração da
    exibição das teclas, você pode acessar as opções através de um menu de configuração ou via linha
    de comando.

    Para consultar as opções disponíveis na versão instalada pelo `apt`, use:

    ```bash
    screenkey --help
    ```

### 1.3 Configurar o tamanho da letra no `screenkey`

No `screenkey`, o tamanho da fonte não é definido por um valor numérico específico, mas sim por
categorias relativas: `'large'` (grande), `'medium'` (médio) ou `'small'` (pequeno). Para configurar
o tamanho da letra, você deve utilizar a opção `-s` ou `--font-size` seguida de uma dessas
palavras-chave. Aqui está como você pode fazer isso:

1. **Para definir o tamanho da fonte como grande, use:**

    ```bash
    screenkey -s large
    ```

2. **Para um tamanho médio:**

    ```bash
    screenkey -s medium
    ```

3. **E para um tamanho pequeno:**

    ```bash
    screenkey -s small
    ```

Portanto, escolha o tamanho conforme sua necessidade e inicie o `screenkey` com o comando correspondente.

### 1.4 Para ajustar a transparência da cor de fundo no `screenkey`

Para ajustar a transparência da cor de fundo no `screenkey`, você pode usar a opção `--opacity`
quando iniciar o aplicativo. O valor de opacidade pode variar de `0.0` (completamente transparente)
a `1.0` (completamente opaco).

1. Por exemplo, se você deseja definir a opacidade para um valor intermediário, como `0.5`, você
usaria o seguinte comando:

    ```bash
    screenkey --opacity 0.5
    ```

    Isso iniciará o `screenkey` com a faixa de fundo tendo uma transparência média. Ajuste o valor
    conforme a necessidade de transparência que você deseja. Quanto menor o número, mais
    transparente será a faixa.

2. Lembre-se de que essa configuração será aplicada juntamente com qualquer outra configuração que
você definir, então se você também quiser definir o tamanho da fonte ao mesmo tempo, por exemplo,
você pode combinar os argumentos:

    ```bash
    screenkey -s small --opacity 0.5
    ```

Este comando iniciará o `screenkey` com fonte pequena e uma transparência de `50%` no fundo.

## 1.5 Personalizar a cor da fonte no `screenkey`

No `screenkey`, você não tem uma lista específica de tons de amarelo pré-definidos para escolher
diretamente através de argumentos de linha de comando. No entanto, você pode especificar a cor
usando nomes de cores básicos ou utilizando códigos de cores hexadecimais (HTML color codes).

1. Para o amarelo básico, você simplesmente usaria:

    ```bash
    screenkey --font-color yellow
    ```

2. Para um tom de amarelo dourado, você poderia usar:

    ```bash
    screenkey --font-color '#FFD700'
    ```

Você pode encontrar diversos tons de amarelo com seus respectivos códigos hexadecimais em recursos
_online_ ou ferramentas de design gráfico. Esses códigos começam sempre com uma cerquilha (`#`)
seguida por seis caracteres (números e letras de A a F) que definem a intensidade das cores
vermelha, verde e azul no sistema RGB.

Lembrando que essas cores podem variar um pouco dependendo do monitor e do ambiente de exibição,
mas o uso de códigos hexadecimais permite uma escolha muito mais ampla e precisa de cores em
comparação com os nomes de cores básicos.

### 1.6 Usar o padrão adotado

1. Para (a) um tamanho de letra pequena, uma transparência pela metade e para um tom de amarelo
dourado, você poderia usar:

    ```bash
    screenkey --mouse -s small --opacity 0.5 --font-color '#FFD700'
    ```


## 2. Código completo para configurar/instalar/usar

Para configurar/instalar/usar o `screenkey` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:

1. Abrir o `Terminal Emulator`. Você pode fazer isso pressionando:

    ```bash
    Ctrl + Alt + T
    ```

2. Digite o seguinte comando e pressione `Enter`:

    ```bash
    sudo apt clean
    sudo apt autoclean
    sudo apt autoremove -y
    sudo apt update
    sudo apt --fix-broken install
    sudo apt clean
    sudo apt list --upgradable
    sudo apt full-upgrade -y
    sudo apt install screenkey -y
    screenkey --mouse -s small --opacity 0.5 --font-color '#FFD700'
    ```


## Referências

[1] UBUNTU. **Detalhes do pacote `screenkey` no `ubuntu`**. Disponível em: <https://packages.ubuntu.com/search?keywords=screenkey>. Acessado em: 07/09/2026.

[2] WAVEXX. **Screenkey**. Disponível em: <https://www.thregr.org/wavexx/software/screenkey/>. Acessado em: 07/09/2026.

[3] OPENAI. **Instalar o `screenkey` no `linux ubuntu` pelo `terminal emulator`**. Disponível em: <https://chatgpt.com/c/58aa3f5f-c2cb-4a22-9f2b-11c4554c32a7>. ChatGPT. Acessado em: 07/09/2026.
