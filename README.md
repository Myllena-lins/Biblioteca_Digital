# Biblioteca Digital
O projeto foi desenvolvido no módulo 2 (Python_2) do curso de dados da Ada Tech. O sistema permite a manipulação de dados armazenados em um arquivo JSON e oferece várias funcionalidades, como operações CRUD (Create, Read, Update, Delete), além de cálculos estatísticos relacionados aos preços, estoques e quantidade de páginas dos livros. Os resultados estatísticos podem ser exportados para um arquivo CSV.

## Funcionalidades
- Leitura de dados: O sistema lê uma lista de livros a partir de um arquivo JSON.
- Exibição de livros: Exibe uma lista com o nome de todos os livros disponíveis, bem como uma lista de livros que estão em estoque.
- Operações CRUD:
  - Adiciona um novo livro ao sistema, atualizando o arquivo JSON.
  - Atualiza as informações de um livro existente.
  - Remove um livro específico do sistema.
  - Visualiza as informações detalhadas de um livro específico.
- Análise de dados:
  - Calcula o preço médio dos livros.
  - Calcula valores mínimo e máximo de atributos como preço, número de páginas e quantidade de livros em estoque.
  - Realiza cálculos estatísticos como média, mediana, moda e desvio padrão para os preços dos livros, quantidade de livros em estoque e quantidade de páginas dos livros.
- Exportação de dados: Os dados estatísticos gerados podem ser exportados para um arquivo CSV.

## Tecnologias Utilizadas
- Python
  - Módulos: 'json', 'functools', 'csv', 'statistics'

## Estrutura de Dados
- JSON (books.json): Armazena as informações dos livros em uma lista de objetos JSON.
- CSV (estatisticas.csv): Armazena os dados estatísticos gerados pelo sistema.

## Observações Finais
A criação desse sistema foi uma solução simples e aplicável em qualquer sistema de gerenciamento de bibliotecas. Qualquer sugestão para melhoria do mesmo será bem-vinda!
