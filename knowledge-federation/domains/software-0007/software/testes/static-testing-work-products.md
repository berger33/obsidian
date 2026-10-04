---
id: software.testes.static-testing.000001
tipo: tecnica
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
fontes: ["https://astqb.org/3-1-static-testing-basics/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Static testing, Static analysis, Teste estático]
lote: software-testes-2000-0001
---

# Teste estático e work products inspecionáveis

## Em uma frase
Teste estático avalia work products sem executar o software, por meio de revisão humana ou ferramenta como análise estática.

## Por que importa
Requisitos, código e modelos podem conter defeitos antes de existir um executável. Revisões e ferramentas podem encontrar ambiguidades, inconsistências e certos problemas estruturais cedo, sem montar todos os dados e pré-condições de uma execução dinâmica.

## Como funciona
O CTFL classifica como possíveis alvos de revisão quaisquer work products que possam ser lidos e entendidos, como requisitos, user stories, arquitetura, código e planos de teste. Análise estática normalmente requer estrutura que possa ser verificada por ferramenta, como código, modelo ou texto com sintaxe formal. Objetivos incluem detectar defeitos e avaliar características não dependentes da execução, como legibilidade, completude, consistência e manutenibilidade.

## Exemplo
Uma revisão de critérios de aceite pode encontrar duas regras de arredondamento contraditórias. Um analisador estático pode identificar variável não usada ou construção incompatível com regra de lint. Nenhum desses passos executa o fluxo de negócio; ambos podem levar a alteração antes dos testes dinâmicos.

## Limites e trade-offs
Ferramentas estáticas só detectam classes de problema para as quais têm regras/modelos; resultado sem alertas não prova correção. Revisões custam tempo e dependem de foco e competência. Defeitos de desempenho em execução e falhas de integração normalmente exigem testes dinâmicos apropriados.

## Como verificar
Identifique o work product e o critério da análise. Registre findings, classifique falsos positivos e confirme correções. Em revisão, combine perspectiva dos autores, usuários e testadores; em análise automatizada, fixe versão e configuração da ferramenta.

## Conexões
- [[testing-vs-debugging]] — revisão pode encontrar defeito diretamente sem reproduzir falha.
- [[review-process-activities]] — estrutura planejamento, leitura, comunicação e correção.
- [[requirements-test-traceability]] — análise estática pode encontrar lacunas na base de teste.

## Fontes
- [ASTQB — ISTQB CTFL §3.1: Static Testing Basics](https://astqb.org/3-1-static-testing-basics/) — alvos, objetivos e diferenças de análise estática/revisão; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — seções 3.1.1–3.1.3 sobre work products e análise estática; acesso em 2026-10-01.
