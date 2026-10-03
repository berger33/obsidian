---
id: software.testes.tranche15.000944
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://pgtap.org/documentation.html", "https://pgtap.org/pg_prove.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# pgTAP: validar SQLSTATE e mensagem de operações que devem falhar

## Em uma frase
Assertions de exceção permitem testar que uma operação SQL incorreta é rejeitada, incluindo código de erro ou mensagem esperada conforme a função escolhida.

## Por que importa
Apenas confirmar que qualquer erro ocorre é frágil: uma conexão caída ou uma coluna ausente pode fazer o teste passar por motivo diferente do contrato.

## Como funciona
Mensagem e SQLSTATE relevantes ajudam a distinguir proteção de negócio de falha de ambiente.

## Exemplo
Execute a operação deliberadamente inválida dentro da assertion pgTAP apropriada, passe SQLSTATE esperado quando estável e descreva o motivo do teste em linguagem de domínio.

## Limites e trade-offs
Mensagens podem mudar com versão ou idioma do servidor; prefira códigos estáveis quando o comportamento público se baseia em SQLSTATE e evite capturar erro genérico sem contexto.

## Como verificar
Faça uma operação que falha pelo motivo previsto e outra que falha ao acessar um objeto inexistente, verificando que apenas a primeira satisfaz a expectativa.

## Conexões
- [[pgtap-results-eq-semantica-de-conjunto-e-ordem]] — Veja também: pgTAP: escolher comparação de resultados que corresponda ao contrato.
- [[pgtap-skip-e-todo-explicam-excecoes-do-plano]] — Veja também: pgTAP: representar temporariamente testes ignorados ou conhecidos como TODO.

## Fontes
- [pgTAP — Documentation](https://pgtap.org/documentation.html) — assertions TAP, schema, comparações, diretivas e funções de teste; consultado em 2026-10-02.
- [pgTAP — pg_prove](https://pgtap.org/pg_prove.html) — execução de scripts SQL e funções xUnit pelo TAP::Harness; consultado em 2026-10-02.
