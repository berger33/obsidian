---
id: software.testes.confirmation-testing.000001
tipo: conceito
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: estavel
status: candidata
revisao_humana: nao_solicitada
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-06.md"
revisor: ""
fontes: ["https://astqb.org/2-2-test-levels-and-test-types/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Confirmation testing", "Teste de confirmação verifica se uma correção resolveu o defeito"]
lote: software-testes-2000-0001
---

# Teste de confirmação verifica se uma correção resolveu o defeito

## Em uma frase
Teste de confirmação verifica se um defeito original foi corrigido com sucesso.

## Por que importa
Uma mudança de código não demonstra que o comportamento voltou a atender ao esperado. Reexecutar o caso que revelou o defeito ou criar um teste que cubra a alteração oferece evidência sobre a correção.

## Como funciona
O CTFL distingue confirmação de regressão. Para confirmar, pode-se executar testes que falharam por causa do defeito e, quando adequado, adicionar casos para cobrir a mudança. Com pouco tempo, a confirmação pode ficar restrita ao passo que reproduzia a falha e à verificação de que ela não ocorre; essa redução precisa refletir o risco e ser comunicada.

## Exemplo
Após corrigir o cálculo de prazo para anos bissextos, execute novamente o caso que falhava, adicione exemplos próximos ao limite e compare o resultado ao critério acordado.

## Limites e trade-offs
Um caso aprovado confirma apenas o comportamento coberto; não prova que a correção trata todas as condições. Testes de confirmação não investigam sozinhos efeitos adversos em outras partes.

## Como verificar
Vincule caso, defeito, versão corrigida e resultado; se o teste original foi alterado, explique como o novo caso mantém capacidade de reproduzir o problema antigo.

## Conexões
- [[regression-testing-change-effects]] — procura efeitos indesejados da mudança.
- [[testing-vs-debugging]] — separa teste de investigação e correção.

## Fontes
- [ASTQB — CTFL §2.2.3, Confirmation and Regression Testing](https://astqb.org/2-2-test-levels-and-test-types/) — propósito de confirmação; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — §2.2.3; acesso em 2026-10-01.
