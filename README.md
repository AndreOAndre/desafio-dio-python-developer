# Sistema Bancário em Python

Projeto desenvolvido como parte do **Suzano - Python Developer Bootcamp**, promovido pela **DIO (Digital Innovation One)**.
O objetivo deste desafio foi implementar um sistema bancário simples utilizando Python, aplicando conceitos fundamentais da linguagem, como estruturas condicionais, laços de repetição, manipulação de variáveis e controle de fluxo.

---

## Sobre o projeto:

A aplicação simula operações básicas de um caixa eletrônico por meio de um menu interativo executado no terminal.
O sistema permite ao usuário realizar depósitos, saques e consultar o extrato da conta, respeitando regras de negócio como limite por saque e quantidade máxima de saques diários.

---

## Objetivos: Este projeto foi desenvolvido para praticar:

- Sintaxe da linguagem Python
- Estruturas condicionais (`if`, `elif` e `else`)
- Estruturas de repetição (`while`)
- Manipulação de variáveis
- Entrada e saída de dados (`input` e `print`)
- Operadores lógicos e relacionais
- Controle de fluxo
- Implementação de regras de negócio
  
---

## Funcionalidades:
- Realizar depósitos.
- Realizar saques.
- Consultar extrato bancário.
- Exibir saldo atualizado.
- Limitar o valor máximo de cada saque.
- Limitar a quantidade de saques por sessão.
- Validar operações inválidas.
- Exibir mensagens de erro quando necessário.

---

## Regras de negócio:

### Depósito:

- Apenas valores positivos são aceitos.
- O valor depositado é adicionado ao saldo.
- A operação é registrada no extrato.
- 
### Saque:

O sistema realiza três validações antes de efetuar o saque:
- Verifica se há saldo suficiente.
- Verifica se o valor solicitado ultrapassa o limite permitido por saque.
- Verifica se o limite máximo de saques foi atingido.
  
Caso todas as validações sejam aprovadas:
- o saldo é atualizado;
- o saque é registrado no extrato;
- o contador de saques é incrementado.
  
### Extrato:

Ao consultar o extrato, o sistema apresenta:

- todas as movimentações realizadas;
- saldo atual da conta;
- mensagem indicando ausência de movimentações quando aplicável.
  
---

## Tecnologias utilizadas:

Python 3

---

## Estrutura do projeto:

```text
Início
   │
   ▼
Exibe menu
   │
   ▼
Seleciona operação
   │
   ├── Depositar
   │      │
   │      ▼
   │ Valida valor
   │      │
   │      ▼
   │ Atualiza saldo
   │
   ├── Sacar
   │      │
   │      ▼
   │ Verifica saldo
   │      │
   │ Verifica limite por saque
   │      │
   │ Verifica quantidade de saques
   │      │
   │      ▼
   │ Atualiza saldo e extrato
   │
   ├── Extrato
   │      │
   │      ▼
   │ Exibe movimentações
   │
   └── Sair
          │
          ▼
        Encerrar sistema
```

---

## Conceitos praticados:

Durante o desenvolvimento deste projeto foram aplicados conceitos importantes da programação, como:

- Variáveis
- Operadores aritméticos
- Operadores relacionais
- Operadores lógicos
- Estruturas condicionais
- Estruturas de repetição
- Manipulação de strings
- Controle de fluxo
- Validação de dados
- Regras de negócio
  
---

## Melhorias futuras:

- Implementar cadastro de usuários.
- Suportar múltiplas contas bancárias.
- Organizar o código em funções.
- Utilizar Programação Orientada a Objetos (POO).
- Persistir dados em arquivos ou banco de dados.
- Criar uma interface gráfica ou versão web.
  
---
