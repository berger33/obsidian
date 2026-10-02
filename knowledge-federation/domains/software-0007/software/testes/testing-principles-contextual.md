---
id: software.testes.principles.000001
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
fontes: ["https://astqb.org/1-3-testing-principles/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Testing principles, Princípios de teste, Pesticide paradox]
lote: software-testes-2000-0001
---

# Princípios de teste como orientação, não receita

## Em uma frase
Princípios de teste são diretrizes gerais para orientar escolhas, mas precisam ser aplicados conforme risco, produto, usuários e contexto.

## Por que importa
Princípios ajudam a evitar metas impossíveis como provar ausência de defeitos ou testar todas as combinações. Eles orientam quando começar, como usar evidência e por que repetir testes idênticos pode perder poder para revelar defeitos novos. Não determinam sozinhos uma estratégia concreta.

## Como funciona
O CTFL v4.0.1 apresenta sete princípios: testes mostram presença, não ausência de defeitos; testes exaustivos são inviáveis exceto em casos triviais; teste cedo reduz efeitos e custos posteriores; defeitos tendem a se concentrar; testes repetidos podem ficar menos eficazes para achar defeitos novos; teste depende do contexto; e ausência de defeitos conhecidos não garante que o produto atenda usuários ou objetivos do negócio. Cada princípio influencia decisões diferentes, por exemplo usar risco para selecionar testes, revisar trabalho cedo e renovar dados/casos quando necessário.

## Exemplo
Uma suíte estável de regressão pode continuar repetindo casos para detectar regressões conhecidas — repetição é valiosa ali. Em exploração de uma área alterada, porém, adicionar variações de entrada e novas hipóteses pode detectar defeitos que uma execução idêntica não revela.

## Limites e trade-offs
“Defeitos clusterizam” é uma tendência empírica, não lei que permita ignorar outros módulos. “Testes se desgastam” não significa apagar regressão estável. A aplicação mecânica de um princípio pode contrariar outro; explique a decisão com contexto e risco.

## Como verificar
Ao definir a estratégia, identifique quais princípios afetam o problema: risco, custo de teste exaustivo, timing, histórico de defeitos, mudança do produto e necessidades dos stakeholders. Revise se a suíte ainda oferece evidência útil sem alegar certeza impossível.

## Conexões
- [[risk-based-testing-priorizacao-risco]] — concentra esforço quando testes exaustivos são inviáveis.
- [[test-case-prioritization-dependencies]] — transforma prioridades em uma ordem executável.
- [[test-progress-metrics-relatorios-conclusao]] — comunica limites e evidências sem interpretar pass rate como certeza.

## Fontes
- [ASTQB — ISTQB CTFL §1.3: Testing Principles](https://astqb.org/1-3-testing-principles/) — sete princípios e implicações; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — descrição dos princípios e relações com risco/regressão; acesso em 2026-10-01.
