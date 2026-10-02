---
id: software.testes.white-box.000001
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
fontes: ["https://astqb.org/4-3-white-box-test-techniques/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["White-box testing and structure", "Teste white-box usa estrutura interna como base de teste"]
lote: software-testes-2000-0001
---

# Teste white-box usa estrutura interna como base de teste

## Em uma frase
Teste white-box deriva casos ou critérios de cobertura a partir da estrutura interna do objeto, como código e fluxos de controle.

## Por que importa
Uma especificação pode omitir caminhos ou decisões relevantes. Conhecer a estrutura permite identificar instruções e ramos que ainda não foram exercitados e expor código inalcançável ou lógica não verificada.

## Como funciona
O CTFL define white-box como técnica structure-based. Para nível Foundation, discute cobertura de statements executáveis e de branches no fluxo de controle. Essas medidas indicam quais itens estruturais foram exercitados, não se os resultados estavam corretos nem se o requisito foi satisfeito.

## Exemplo
Uma regra de autorização pode conter ramificações para usuário comum, administrador e recurso inexistente. Cobertura de branches ajuda a descobrir que o ramo de recurso ausente nunca foi executado; é preciso ainda afirmar o comportamento esperado para cada caminho.

## Limites e trade-offs
100% de statement coverage não implica 100% de branch coverage e nenhum percentual prova ausência de defeitos. Técnicas mais rigorosas existem para contextos críticos, mas não são o foco do syllabus Foundation.

## Como verificar
Escolha a unidade estrutural, relate critérios e caminhos cobertos e associe cada caminho a resultados assertados; analise cobertura residual sem tratá-la como qualidade completa.

## Conexões
- [[cobertura-branches-statement-interpretacao]] — detalha métricas de statement e branch.
- [[mcdc-coverage-condicoes-independentes]] — apresenta critério mais rigoroso para decisões compostas.

## Fontes
- [ASTQB — CTFL §4.3, White-Box Test Techniques](https://astqb.org/4-3-white-box-test-techniques/) — statement, branch e valor de testes estruturais; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — §4.3; acesso em 2026-10-01.
