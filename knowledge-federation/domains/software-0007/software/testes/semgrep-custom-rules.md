---
id: software.testes.tranche18.001236
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://semgrep.dev/docs/writing-rules/overview", "https://github.com/semgrep/semgrep"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Semgrep: manter regras próprias do projeto

## Em uma frase
Regras locais ficam versionadas com o código e podem cobrir convenções internas que ferramentas genéricas não conhecem.

## Por que importa
Regras próprias preservam decisões de arquitetura do projeto e complementam os conjuntos públicos com o contexto local.

## Como funciona
Mantenha as regras em diretório versionado, teste cada uma com casos positivos e negativos e revise-as como qualquer código.

## Exemplo
Uma regra interna pode impedir chamadas diretas a recurso sensível fora do cliente padronizado da organização.

## Limites e trade-offs
Regras sem testes passam a acusar casos legítimos após mudanças no código, e regras duplicadas com os conjuntos públicos geram ruído.

## Como verificar
Altere um caso de teste da regra para a forma proibida e confirme que ela passa a acusar exatamente esse trecho.

## Conexões
- [[semgrep-severity-and-policy]] — Veja também: Semgrep: definir severidade e política de bloqueio.
- [[semgrep-limits-and-practices]] — Veja também: Semgrep: reconhecer limites da análise estática.

## Fontes
- [Semgrep — Writing rules](https://semgrep.dev/docs/writing-rules/overview) — estrutura de regra, operadores, metavariáveis e modo de propagação; consultado em 2026-10-03.
- [Semgrep — repositório oficial](https://github.com/semgrep/semgrep) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
