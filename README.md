# Projeto `Inventory Report`

<details>
<summary><strong>🧑‍💻 O que foi desenvolvido</strong></summary>
  <br />

Neste projeto, foi desenvolvido um **gerador de relatórios**. O objetivo fio receber arquivos contendo informações sobre um estoque específico e, em seguida, produzir um relatório abrangente com base nesses dados. Esses dados de estoque podem ser obtidos de duas fontes:

-   Através da importação de um arquivo `CSV`;

-   Através da importação de um arquivo `JSON`;

Além disso, o relatório final possuirá duas versões: **simples** e **completa**.

</details>

<details>
  <summary><strong> 📝 Habilidades a serem trabalhadas </strong></summary>
  <br />

Neste projeto, verificamos se você é capaz de:

-   Aplicar conceitos de Programação Orientada a Objetos em Python;

-   Implementar leitura e escrita de arquivos `CSV` e `JSON` em Python;

</details>

## Orientações específicas deste projeto

<details>
  <summary><strong>🗃️ Arquivos com os dados de entrada</strong></summary><br />
  
Dois formatos de importação estão disponíveis no diretório <code>data</code> dentro do diretório <code>inventory_report</code>. Confira o exemplo de formato eles:

<strong>Arquivos CSV</strong>
Os arquivos **CSV** são separados por vírgula, como no exemplo abaixo:

```CSV
id,product_name,company_name,manufacturing_date,expiration_date,serial_number,storage_instructions
1,cadeira,Target Corporation,2021-02-18,2025-09-17,CR25,empilhadas
2,mesa,"Galena Madeira, Inc.",2022-12-06,2026-12-25,FR29,desmontadas
3,abajur,Keen Iluminação,2019-12-22,2025-11-07,CZ09,em caixas
```

<strong>Arquivos JSON</strong>
Os arquivos JSON seguem o seguinte modelo:

```json
[
    {
        "id": "1",
        "product_name": "Borracha",
        "company_name": "Papelaria Solar",
        "manufacturing_date": "2021-07-04",
        "expiration_date": "2029-02-09",
        "serial_number": "FR48",
        "storage_instructions": "Ao abrigo de luz solar"
    }
]
```

</details>

<details>
  <summary>
    <b>📌Como seu teste é avaliado</b>
  </summary> 
  <br />

Seus testes precisam estar passando. Isso feito, o <strong>teste da Trybe</strong> irá avaliar se o <strong>seu teste</strong> passa quando recebe uma implementação correta e confirmará que ele está falhando em alguns casos em que deve falhar.

Para estes testes que esperemos que falhe, o requisito será considerado atendido quando a resposta do Pytest for <code>XFAIL(Expected Fail)</code>, ao invés de <code>PASS</code> ou <code>FAIL</code>.

</details>

<details>
  <summary><strong>🛼Executando o Projeto após fazer todos os requisitos<strong></summary>
  <br />
  
Após implementar dos requisitos, seu programa deverá ser executável <strong>via linha de comando</strong>.

O comando a ser executado será `ir`. Para que ele funcione em seu ambiente é preciso antes instalar o próprio código como um pacote pip:
<code>pip install .</code>

Agora você poderá chamar o comando `ir` passando seus argumentos:

<code>ir - p `argumento1` -t `argumento2`</code>

-   **argumento1** deve receber o caminho de um diretório com os arquivos de estoque à serem importados. Os arquivos dentro do diretório podem ser `csv`s ou `json`s.

-   **argumento2** pode receber duas strings: `simple` ou `complete`, cada uma gerando o respectivo tipo de relatório.

</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary>
  <br />
  
O Python oferece um recurso chamado de ambiente virtual, que permite sua máquina rodar diferentes tipos de projetos com diferentes versões de bibliotecas sem conflitos. Da mesma forma que, por exemplo, o `npm` faz num projeto em _JavaScript_, garantindo que cada projeto tenha suas dependências e que eles não entrem em conflito.

1. Criar o ambiente virtual

```bash
python3 -m venv .venv
```

2. Ativar o ambiente virtual

```bash
source .venv/bin/activate
```

3. Instalar as dependências no ambiente virtual

```bash
python3 -m pip install -r dev-requirements.txt
```

Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente. Quando precisar desativar o ambiente virtual, execute o comando `deactivate`. Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto. Ele é como um `package.json` de um projeto `Node.js`.

Se o VS Code não reconhecer as dependências instaladas no ambiente virtual criado, será necessário informar o caminho do interpretador Python. Para isso, abra o VS Code e pressione `Ctrl + Shift + P` (no Mac, `Cmd + Shift + P`) e digite `Python: Select Interpreter`. Selecione o interpretador que possui o caminho `./.venv/bin/python` no nome.

</details>

<details>
<summary><strong>🎛 Linter</strong></summary>
  <br />

Para garantir a qualidade do código, foi utilizado nesse projeto o linter `Flake8`. Assim o código está alinhado com as boas práticas de desenvolvimento, sendo mais legível e de fácil manutenção! Para poder executar o `Flake8`, certifique-se de ter seguido os passos do tópico [**🏕️ Ambiente Virtual**] dentro do repositório.

Para rodá-lo localmente no repositório, execute o comando a seguir:

```bash
python3 -m flake8
```

Se a análise do `Flake8` encontrar problemas no seu código, tais problemas serão mostrados no seu terminal. Se não houver problema no seu código, nada será impresso no seu terminal.

Você pode também pode contar com a ajuda do `Flake8` no `VSCode`. Para isso, basta instalar a [extensão oficial do VS Code para a linguagem Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

</details>

<details>
  <summary><strong>🛠 Testes</strong></summary>
  <br />

Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

<strong>Executar os testes</strong>

```bash
python3 -m pytest
```

O arquivo `pyproject.toml` já configura corretamente o `pytest`. Entretanto, caso você queira que os testes gerem uma saída mais verbosa completa, o comando é:

```bash
python3 -m pytest -s -vv
```

O `pytest` possui diversos parâmetros que podem ser utilizados para executar os testes de diferentes formas. Alguns exemplos são:

```bash
python3 -m pytest tests/test_nome_do_arquivo.py  # Executa todos os testes do arquivo de testes especificado
python3 -m pytest tests/test_nome_do_arquivo.py::test_nome_do_teste  # Executa apenas o teste especificado
python3 -m pytest -k expressao  # Executa apenas os testes que contém a expressão informada como substring
python3 -m pytest -x  # Executa os testes até encontrar o primeiro erro
```

Você pode combinar os parâmetros para executar os testes da forma que desejar! Para mais informações, consulte a [documentação do pytest](https://docs.pytest.org/en/6.2.x/contents.html).

</details>

<details>
  <summary><strong>🐳 Docker</strong></summary>
  <br />
  Caso queria executar os seus testes de projeto via `docker-compose`, ao invés de no ambiente virtual, execute o comando:

```bash
docker-compose run --rm inventory pytest
```

</details>

## Requisitos Implementados

### 1. Teste o construtor/inicializador do objeto Produto

> **Crie o teste em:** `tests/product/test_product.py`

<p align="center">
    <img src="/.images/construtor.png " alt="Imagem de construtor em Python"  width="600"/>
</p>

<details>

**<summary>Teste se o construtor do objeto <code>Product</code> contém os atributos corretos.**

</summary>

Ao analisar o código do projeto, você encontrará a classe do objeto produto já implementada no arquivo `inventory_report/product.py`.

Para termos confiança em continuar as implementações, precisamos que você implemente o teste e certifique que o método `__init__` da classe `Product` esteja funcionando corretamente.

O nome deste teste deve ser `test_create_product` e ele deve verificar o correto preenchimento dos seguintes atributos:

-   `id`
-   `company_name`
-   `product_name`
-   `manufacturing_date`
-   `expiration_date`
-   `serial_number`
-   `storage_instructions`

**O que será testado:**

-   **1.1** - Se o teste valida que o atributo `id` existe na classe e é igual ao passado pelo construtor.
-   **1.2** - Se o teste valida que o atributo `company_name` existe na classe e é igual ao passado pelo construtor.
-   **1.3** - Se o teste valida que o atributo `product_name` existe na classe e é igual ao passado pelo construtor.
-   **1.4** - Se o teste valida que o atributo `manufacturing_date` existe na classe e é igual ao passado pelo construtor.
-   **1.5** - Se o teste valida que o atributo `expiration_date` existe na classe e é igual ao passado pelo construtor.
-   **1.6** - Se o teste valida que o atributo `serial_number` existe na classe e é igual ao passado pelo construtor.
-   **1.7** - Se o teste valida que o atributo `storage_instructions` existe na classe e é igual ao passado pelo construtor.

</details>

### 2. Teste o relatório individual gerado por Produto

> **Crie o teste em:** `tests/product_report/test_product_report.py`

<details>

**<summary>Teste se o "método mágico" <code>**str**</code> do objeto <code>Product</code> retorna a frase correta.**

</summary>

Boa notícia! Já implementamos o primeiro relatório no arquivo `inventory_report/product.py`, e também criamos uma frase com as informações do produto, que será útil para etiquetar o estoque. Para desenvolver esse relatório, utilizamos o método `__str__` do Python, que é chamado quando utilizamos a função `str(objeto)`.

Exemplo da frase:

**Trecho 1:** _The product `farinha`,_
**Trecho 2:** _with serial number `TY68 409C JJ43 ASD1 PL2F`,_
**Trecho 3:** _manufactured in `01-05-2021`_
**Trecho 4:** _by the company `Farinini`,_
**Trecho 5:** _valid until `02-06-2023`,_
**Trecho 6:** _must be stored according to the following instructions: `precisa ser armazenado em local protegido da luz`._

Agora, para garantirmos uma boa cobertura de testes, precisamos que você implemente o teste. O nome do teste deve ser `test_product_report`. Ele deve instanciar um objeto `Product` e verificar se a frase retornada está correta.

**O que será testado:**

-   **2.1** - Se seu teste verifica se o Trecho 1 do relatório está correto no texto base e no dado inserido nele.
-   **2.2** - Se seu teste verifica se o Trecho 2 do relatório está correto no texto base e no dado inserido nele.
-   **2.3** - Se seu teste verifica se o Trecho 3 do relatório está correto no texto base e no dado inserido nele.
-   **2.4** - Se seu teste verifica se o Trecho 4 do relatório está correto no texto base e no dado inserido nele.
-   **2.5** - Se seu teste verifica se o Trecho 5 do relatório está correto no texto base e no dado inserido nele.
-   **2.6** - Se seu teste verifica se o Trecho 6 do relatório está correto no texto base e no dado inserido nele.

</details>

### 3. Crie a Interface `Importer`

> **Crie em:** `inventory_report/importers.py`

<details>

**<summary>Crie a classe abstrata <code>Importer</code> com o inicializador implementado e com o método abstrato <code>import_data</code>.**

</summary>
  <br />

Como já temos o arquivo com os produtos, precisamos importar os dados. Em razão dos diversos formatos e para não repetir lógica, vamos criar uma classe abstrata que será responsável por definir como as classes importadoras dos dados dos arquivos serão.

Para isso, crie uma classe abstrata chamada `Importer`, que deve conter um método chamado `import_data`, que recebe o caminho do arquivo e retorna uma lista de produtos:

**O que será testado:**

-   **3.1** - Se a classe `Importer` é abstrata;
-   **3.2** - Se o método `__init__` não é abstrato;
-   **3.3** - Se o método `__init__` recebe `self` e `path`;
-   **3.4** - Se o tipo do `path` é `str`;
-   **3.5** - Se o método `import_data` é abstrato;
-   **3.6** - Se o método `import_data` recebe `self`;
-   **3.7** - Se o método `import_data` retorna uma lista de produtos;

</details>

### 4. Crie a classe `JsonImporter`

> **Crie em:** `inventory_report/importers.py`

<details>

**<summary>Crie a classe <code>JsonImporter</code> que herda de <code>Importer</code> e implemente o método <code>import_data</code> para ler um arquivo JSON.**

</summary>
  <br />

Agora que temos a interface, precisamos criar a classe que irá implementar o método `import_data` para ler um arquivo JSON. Para isso, crie uma classe chamada `JsonImporter`, que deve herdar da classe `Importer` e implementar o método `import_data`. Esse método, por sua vez, recebe o caminho do arquivo e retorna uma lista de produtos. A lista deve ser retornada como no formato abaixo:

```
[
  Product(
    id='1',
    product_name='Nicotine Polacrilex',
    company_name='Target Corporation',
    manufacturing_date='2021-02-18',
    expiration_date='2023-09-17',
    serial_number='CR25 1551 4467 2549 4402 1',
    storage_instructions='instrucao 1'
  ),

  Product(
    id='2',
    product_name='fentanyl citrate',
    company_name='Target Corporation',
    manufacturing_date='2020-12-06',
    expiration_date='2023-12-25',
    serial_number='FR29 5951 7573 74OY XKGX 6CSG D20',
    storage_instructions='instrucao 2'
  ),
  // ...
]
```

**O que será testado:**

-   **4.1** - Se a classe `JsonImporter` herda de `Importer`.
-   **4.2** - Se o método `import_data` importa corretamente um arquivo JSON válido.
-   **4.3** - Se o método `import_data` exporta os dados do JSON importado no formato apropriado.

</details>

### 5. Crie a classe `Inventory`

> **Crie em:** `inventory_report/inventory.py`

<details>

**<summary>Crie a classe <code>Inventory</code> que armazenará o estoque e poderá adicionar itens a ele.**

</summary>
  <br />

Com o nosso importador de dados feito, vamos criar a classe que representa um estoque para, a partir dele, gerar o nosso relatório! Atenção para as especificações:

-   A classe `Inventory` deve poder ser instanciada, de forma opcional, com uma lista de produtos.
-   Caso a lista não seja fornecida, a lista da instância deve ser inicializada como vazia.
-   A classe deve conter um método chamado `add_data`, que recebe uma lista de produtos e adiciona todos os produtos à lista de produtos da instância.
-   Além disso, a classe deve ter uma propriedade chamada `data`, que deve ser somente leitura e retornar uma cópia da lista de produtos da instância.

**O que será testado:**

-   **5.1** - Se o inicializador recebe dois parâmetros: `self` e `data`.
-   **5.2** - Se `data` tem a anotação de tipo `List[Products]` e é opcional.
-   **5.3** - Se `data` tem o valor padrão `None`.
-   **5.4** - Se `data` é inicializado com uma lista vazia quando o valor padrão é usado.
-   **5.5** - Se `data` recebe uma lista de produtos.
-   **5.6** - Se `data` é uma propriedade somente de leitura.
-   **5.7** - Se `add_data` recebe uma lista de produtos.
-   **5.8** - Se `add_data` adiciona todos os produtos da lista de produtos recebida por parâmetro à lista de produtos da instância.

</details>

### 6. Crie o protocolo `Report`

> **Crie em:** `inventory_report/reports/report.py`

<details>

**<summary>Crie o protocolo <code>Report</code>, que deverá ser usado como contrato dos relatórios <code>simple</code> e <code>complete</code>.**

</summary>
  <br />

Feita nossa classe de inventário, vamos usá-la para criar nossos relatórios! Visto que teremos dois formatos dele, primeiro vamos criar um contrato para todos os formatos respeitarem. Usaremos um protocolo para isso. Atenção à especificação:

-   No protocolo `Report` deve haver um método chamado `add_inventory` recebendo um parâmetro `inventory`, do tipo `Inventory`, classe criada no quinto requisito.

-   Deve haver um método chamado `generate` que retorna uma string.

**O que será testado:**


-   **6.1** - Se `add_inventory` recebe dois parâmetros: `self` e `inventory`.
-   **6.2** - Se `inventory` tem a anotação de tipo `Inventory`.
-   **6.3** - Se `generate` recebe `self`.
-   **6.4** - Se `generate` tem um retorno do tipo `str`.

</details>

### 7. Crie o relatório `SimpleReport`

> **Crie a classe em:** `inventory_report/reports/simple_report.py`

<details>

**<summary>Crie a classe <code>SimpleReport</code> que implementa os métodos <code>add_inventory</code> e <code>generate</code> do protocolo <code>Report</code>.**

</summary>
  <br />

A classe `SimpleReport` deve ser inicializada sem parâmetros, contudo, deve ter um atributo para armazenar cada um dos estoques que podem ser adicionados.

O método `add_inventory` deverá seguir o contrato do protocolo `Report` e deve ser capaz de adicionar um estoque ao atributo que armazena cada um dos estoques.

O método `generate` deve ser capaz de gerar o relatório a partir dos produtos que estão presentes em cada um dos estoques armazenados. Atenção às especificações:

-   Ao rodar os testes localmente, você terá um teste para cada validação de cada informação presente no relatório;
-   O método `add_inventory` deve receber um parâmetro que representa um `Inventory`, classe implementada no quinto requisito.
-   O método `generate` deverá retornar uma `string` de saída com o seguinte formato:

```txt
Oldest manufacturing date: YYYY-MM-DD
Closest expiration date: YYYY-MM-DD
Company with the largest inventory: NOME DA EMPRESA
```

-   A data de validade mais próxima considera somente itens que ainda não venceram.

**Dica:** O módulo [datetime](https://docs.python.org/3/library/datetime.html) pode te ajudar.

**O que será testado:**

-   **7.1** - Se o relatório traz corretamente a data de fabricação mais antiga dos estoques,
-   **7.2** - Se o relatório traz corretamente a data de validade mais próxima, descartando itens já vencidos, do estoque
-   **7.3** - Se o relatório traz corretamente a empresa com o maior estoque
-   **7.4** - Se o relatório é gerado no formato especificado.

</details>

### 8. Crie a classe `CsvImporter`

> **Crie em:** `inventory_report/importers.py`

<details>

**<summary>Crie a classe <code>CsvImporter</code> que herda de <code>Importer</code> e implemente o método <code>import_data</code> para ler um arquivo CSV.**

</summary>
  <br />

Para não ficarmos limitados a receber estoques em formato JSON, precisamos criar a classe que irá implementar o método `import_data` para ler um arquivo CSV. Para isso, crie uma classe chamada `CsvImporter`, que deve herdar da classe `Importer` e implementar o método `import_data`, que usa o caminho armazenado em um atributo para retornar uma lista de produtos.

**O que será testado:**

-   **8.1** - Se a classe `CsvImporter` herda de `Importer`.
-   **8.2** - Se o método `import_data` importa um arquivo CSV.

</details>

### 9. Crie o relatório `CompleteReport`

> **Crie em:** `inventory_report/reports/complete_report.py`

<details>

**<summary>Crie a classe <code>CompleteReport</code> que herda de <code>SimpleReport</code> e implementa o método <code>generate</code> do protocolo <code>Report</code>.**

</summary>
  <br />

O relatório completo deve ser gerado através do método `generate` escrito dentro da classe `CompleteReport` e que respeita o contrato criado no protocolo `Report`.

O método `generate` deve usar o atributo que armazena as lista de estoques para a estruturação do relatório e deverá retornar uma string formatada como um relatório. Atenção à especificação:

-   A classe `CompleteReport` deve herdar da classe `SimpleReport` e sobrescrever o método `generate`, de modo a especializar seu comportamento.

-   O método deverá retornar uma saída com o seguinte formato:

```bash
Oldest manufacturing date: YYYY-MM-DD
Closest expiration date: YYYY-MM-DD
Company with the largest inventory: NOME DA EMPRESA
Stocked products by company:
- Empresa 1: 2
- Empresa 2: 1
```

**O que será testado:**

-   **9.1** - Se o relatório simples funciona corretamente, aderente a todas as suas especificações.
-   **9.2** - Se o relatório completo retorna a data de fabricação mais antiga corretamente.
-   **9.3** - Se o relatório completo retorna a data de vencimento mais próxima corretamente, ignorando produtos já vencidos.
-   **9.4** - Se o relatório completo retorna a quantidade correta de produtos estocados por empresa.
-   **9.5** - Se o relatório completo é gerado com o formato especificado.

</details>

### 10. Crie a função `process_report_request`

> **Crie em:** `inventory_report/cli/input_handler.py`

<details>

**<summary>Crie a função <code>process_report_request</code>.**

</summary>
  <br />

Está na hora de ajustar a interface de linha de comando (_Command Line Interface_, ou _CLI_) para nossa aplicação que gera relatórios!

No arquivo `inventory_report/cli/__init__.py` já existe uma CLI implementada com a biblioteca [Typer](https://typer.tiangolo.com/) que está configurada para ser chamada da seguinte forma:

```sh
ir -p <caminho_da_pasta> -t <tipo_do_relatorio>
```

A implementação em `inventory_report/cli/__init__.py` (você não precisa alterar esse arquivo) irá chamar a função `process_report_request` que você deve implementar no arquivo `inventory_report/cli/input_handler.py`, com os seguintes argumentos:

- `file_paths: List[str]`: Lista de caminhos de arquivos dentro da pasta informada em `-p`;
- `report_type: str`: Tipo de relatório a ser gerado, informado em `-t`.

A função `process_report_request` deve retornar um relatório do tipo informado contendo os dados de todos os arquivos listados. Atenção às especificações:

-   A função `process_report_request` deve receber dois parâmetros: `file_paths: List[str]` e `report_type: str`;

-   Deverão ser usadas as classes dos requisitos anteriores para gerar o relatório adequado: `Inventory`, `CsvImporter`, `JsonImporter`, `SimpleReport` e `CompleteReport`;

-   Arquivos de extensões não suportadas devem ser ignorados;

-   Caso o tipo de relatório informado não seja suportado, deve ser levantado um `ValueError` com a mensagem `Report type is invalid.`;

**O que será testado:**

-   **10.1** - Se a função gera corretamente relatórios simples quando chamado com um arquivo `.json`.
-   **10.2** - Se a função gera corretamente relatórios simples quando chamado com um arquivo `.csv`.
-   **10.3** - Se a função gera corretamente relatórios simples quando chamado com mais de um arquivo.
-   **10.4** - Se a função gera corretamente relatórios completos quando chamado com um arquivo `.json`.
-   **10.5** - Se a função gera corretamente relatórios completos quando chamado com um arquivo `.csv`.
-   **10.6** - Se a função gera corretamente relatórios completos quando chamado com mais de um arquivo.
-   **10.7** - Se a função ignora arquivos de extensões não suportadas.
-   **10.8** - Se a função levanta um `ValueError` quando é passado um tipo de relatório inválido como parâmetro.

</details>
