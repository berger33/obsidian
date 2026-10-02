---
id: software.testes.regression-testing.000001
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
aliases: ["Regression testing after changes", "Teste de regressão detecta efeitos adversos de mudanças"]
lote: software-testes-2000-0001
---

# Teste de regressão detecta efeitos adversos de mudanças

## Em uma frase
Teste de regressão verifica se uma mudança introduziu efeitos adversos em áreas que antes funcionavam.

## Por que importa
Correções, melhorias, migrações e alterações de configuração podem afetar componentes além do ponto modificado. Sem regressão, um reparo local pode trocar um defeito conhecido por uma falha inesperada em outra parte.

## Como funciona
O CTFL apresenta regressão como teste posterior a mudanças, incluindo correções já submetidas a confirmação. Os efeitos podem surgir no mesmo componente, em componentes relacionados ou em partes aparentemente inalteradas do sistema. A suíte e a ordem são selecionadas considerando risco, impacto e recursos disponíveis; não é necessário que todo teste de regressão seja uma repetição completa de todos os casos.

## Exemplo
Depois de alterar a validação de endereço, rode testes do fluxo alterado e verificações selecionadas de envio, faturamento e importação que compartilham o mesmo parser.

## Limites e trade-offs
Uma suíte verde reduz incerteza, mas não cobre todos os efeitos possíveis. Seleção insuficiente deixa risco residual; execução indiscriminada pode atrasar feedback sem acrescentar evidência proporcional.

## Como verificar
Registre mudança, componentes afetáveis, casos executados e lacunas. Use histórico de falhas, dependências e cobertura para justificar o conjunto.

## Conexões
- [[regression-test-prioritization-risco-impacto]] — ordena a execução por risco.
- [[confirmation-testing-after-fix]] — responde se o defeito original foi removido.

## Fontes
- [ASTQB — CTFL §2.2.3, Confirmation and Regression Testing](https://astqb.org/2-2-test-levels-and-test-types/) — objetivo e escopo de regressão; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — §2.2.3; acesso em 2026-10-01.
