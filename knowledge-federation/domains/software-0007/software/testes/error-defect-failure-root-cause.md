---
id: software.testes.error-defect-failure.000001
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-05.md"
revisor: ""
fontes: ["https://astqb.org/1-2-why-is-testing-necessary/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Error defect failure root cause, Erro defeito falha causa raiz]
lote: software-testes-2000-0001
---

# Erro, defeito, falha e causa raiz

## Em uma frase
Um erro humano pode introduzir um defeito num work product; quando um defeito é executado em condições pertinentes, pode provocar uma falha observável.

## Por que importa
Separar causa, artefato defeituoso e comportamento observado melhora investigação e comunicação. “A tela caiu” descreve uma falha; “o código leu um campo inexistente” é uma hipótese de defeito; “o requisito ambíguo levou à implementação incorreta” pode ser uma causa raiz. Misturar níveis leva a correções superficiais ou relatórios que afirmam causa sem evidência.

## Como funciona
O CTFL descreve a cadeia típica: pessoas cometem erros, que podem criar defeitos em requisitos, scripts, código ou outros work products; a execução do defeito pode causar uma falha. Nem todo defeito falha em todas as condições, e alguns podem nunca ser executados. Falhas também podem resultar de condições ambientais. Causa raiz é a razão fundamental para a ocorrência de um problema e pode ser investigada por análise de causa raiz; não é sinônimo do defeito encontrado.

## Exemplo
Um teste observa total incorreto em uma nota fiscal. O total incorreto é a falha; uma regra de arredondamento implementada de forma errada pode ser o defeito; uma especificação que deixou a política de arredondamento ambígua pode ser uma causa anterior. Cada afirmação exige evidência diferente e pode envolver mais de um fator.

## Limites e trade-offs
A cadeia não é necessariamente linear: condições ambientais podem desencadear falhas sem uma alteração recente no código, e várias causas contribuem juntas. A análise de causa raiz é uma investigação, não conclusão automática a partir de um único log.

## Como verificar
Preserve comportamento observado, entradas, ambiente e versão. Confirme o defeito por inspeção/reprodução, se possível, e separe fatos de hipóteses causais. Registre uma causa raiz apenas quando a investigação a sustentar; relacione a ação preventiva ao mecanismo identificado.

## Conexões
- [[test-oracles-resultados-esperados]] — compara comportamento observado com critério esperado.
- [[defect-report-reproducibility-severity-priority]] — fornece dados para investigar a falha.
- [[test-progress-metrics-relatorios-conclusao]] — relatórios devem separar defeitos confirmados de anomalias em triagem.

## Fontes
- [ASTQB — ISTQB CTFL §1.2: Why is Testing Necessary?](https://astqb.org/1-2-why-is-testing-necessary/) — distinção entre erro, defeito, falha e causa raiz; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — seção 1.2.3 e exemplos de work products e condições de falha; acesso em 2026-10-01.
