---
id: software.criacao_ia.tranche01.000010
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md"
fontes: ["https://docs.github.com/copilot/concepts/prompt-engineering-for-copilot-chat", "https://docs.github.com/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Copilot: inspecionar o diff antes de aceitar

## Em uma frase

Revisar o diff completo revela arquivos extras, mudanças de dependência e comportamentos que não aparecem na explicação do assistente.

## Por que importa

Alterações múltiplas e automatizadas podem introduzir regressões fora do trecho principal, especialmente em configurações ou artefatos gerados.

## Como funciona

Confira escopo, nomes, compatibilidade, arquivos removidos e efeitos colaterais; descarte ou reverta partes sem justificativa rastreável.

## Exemplo

Ao adicionar uma API, examine também configuração, permissões, testes, logs e documentação que o agente tenha alterado no mesmo passo.

## Limites e trade-offs

Diff limpo não comprova correção e testes passando não garantem que o produto atende ao requisito.

## Como verificar

Compare o diff com critérios de aceitação, rode o conjunto de testes relevante e peça revisão de outra pessoa para mudanças de maior impacto.

## Conexões
- [[copilot-registrar-instrucoes-do-repositorio]] — Copilot: registrar instruções do repositório.
- [[responses-api-iniciar-uma-chamada-de-texto]] — Responses API: iniciar uma chamada de texto.

## Fontes
- [GitHub Docs — Prompt engineering para Copilot Chat](https://docs.github.com/copilot/concepts/prompt-engineering-for-copilot-chat) — Orientações oficiais para prompts com contexto, objetivo e detalhes concretos. Consulta: 2026-10-04.
- [GitHub Docs — Fazer perguntas ao Copilot na IDE](https://docs.github.com/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide) — Documenta os modos Ask, Edit, Agent e Plan e o uso no ambiente de desenvolvimento. Consulta: 2026-10-04.
