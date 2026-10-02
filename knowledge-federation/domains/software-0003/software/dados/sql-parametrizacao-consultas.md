---
id: software.dados.sql-parametrizacao.000001
tipo: tecnica
dominio: software
subdominio: dados
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: estavel
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html", "https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries"]
tags: [dominio/software, subdominio/dados, qualidade/candidata]
aliases: [Consultas parametrizadas, Prepared statements, SQL injection]
lote: software-seguranca-0003
---

# Consultas SQL parametrizadas

## Em uma frase
Parâmetros vinculados mantêm valores externos separados do texto SQL, de modo que esses valores sejam tratados como dados em vez de código executável.

## Por que importa
Uma consulta montada por concatenação pode mudar de significado quando recebe caracteres especiais ou entrada maliciosa. O problema não é que a entrada “pareça perigosa”; é misturar conteúdo variável com a gramática da consulta. A OWASP recomenda prepared statements com binding como defesa primária porque a instrução SQL e seus valores são enviados em partes distintas.

## Como funciona
A aplicação escreve a estrutura da consulta com marcadores e vincula os valores por uma API do driver. Em Python com `sqlite3`, por exemplo, pode-se usar `cursor.execute("SELECT id FROM customers WHERE email = ?", (email,))`. O placeholder não recebe o fragmento SQL: o driver envia `email` como valor. ORMs também podem expor consultas inseguras se a aplicação interpolar texto manualmente. Identificadores como nome de tabela, coluna ou direção de ordenação geralmente não podem ser vinculados como valores; quando precisam variar, escolha-os de uma lista permitida controlada pelo código.

## Exemplo
Uma busca por usuário mantém a consulta fixa e vincula o e-mail recebido como parâmetro. Se a equipe oferece ordenação, ela converte cada opção pública (`recentes`, `nome`) em uma expressão SQL constante previamente definida, em vez de concatenar literalmente o valor recebido no `ORDER BY`.

## Limites e trade-offs
Parametrização evita que valores vinculados alterem a estrutura SQL, mas não valida regras de negócio, autorização ou qualidade dos dados. Ela não protege um trecho de SQL dinâmico criado dentro de uma procedure sem parâmetros seguros. Validação de entrada continua útil para formato e regras do domínio, mas escaping manual não é substituto geral para binding e varia entre bancos. A aplicação também deve limitar privilégios da conta de banco.

## Como verificar
Inspecione caminhos de consulta para localizar concatenação ou interpolação de entrada. Teste valores contendo aspas e caracteres incomuns e confirme que são tratados literalmente, não como sintaxe. Para campos dinâmicos, teste que valores fora da lista permitida são recusados antes de executar a consulta.

## Conexões
- [[gates-de-qualidade-no-merge]] — revisão estática e testes podem detectar concatenações introduzidas em mudanças.
- [[contrato-openapi-http]] — validação de payload na API complementa, mas não substitui, parâmetros seguros no acesso a dados.

## Fontes
- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) — prepared statements, allow-lists e limites de stored procedures; acesso em 2026-10-01.
- [Python `sqlite3` — How to use placeholders to bind values in SQL queries](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries) — binding de valores no driver SQLite para Python; acesso em 2026-10-01.
