---
id: software.testes.tranche15.000906
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
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://docs.maestro.dev/maestro-flows/workspace-management/test-discovery-and-tags", "https://docs.maestro.dev/maestro-cli/maestro-cli-commands-and-options"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Maestro: organizar fluxos com tags

## Em uma frase
Tags declaradas no fluxo permitem selecionar subconjuntos na CLI com `--include-tags` e excluir grupos com `--exclude-tags`, usando lógica de união dentro de cada flag.

## Por que importa
Rodar a suíte inteira em cada verificação é lento, e sem agrupamento a equipe acaba mantendo listas de arquivos que envelhecem rapidamente.

## Como funciona
Declare tags que representem risco ou etapa, como fumaça ou trabalho em andamento, e selecione o conjunto adequado em cada contexto de execução.

## Exemplo
`maestro test . --include-tags=smoke` executa apenas os fluxos marcados, e combinar inclusão com exclusão remove os fluxos indesejados do conjunto selecionado.

## Limites e trade-offs
A filtragem por união dentro de uma flag não expressa interseção de tags, e excluir demais pode deixar a verificação rápida sem cobrir o caminho crítico.

## Como verificar
Liste os fluxos que cada combinação de filtros seleciona e confirme que o conjunto rápido cobre os riscos declarados para aquela etapa.

## Conexões
- [[maestro-input-and-keyboard]] — Veja também: Maestro: preencher campos e controlar teclado.
- [[maestro-repeat-and-conditions]] — Veja também: Maestro: repetir passos e tratar variações.

## Fontes
- [Maestro — Test discovery and tags](https://docs.maestro.dev/maestro-flows/workspace-management/test-discovery-and-tags) — descoberta de fluxos e filtragem por tags na CLI; consultado em 2026-10-02.
- [Maestro — CLI](https://docs.maestro.dev/maestro-cli/maestro-cli-commands-and-options) — subcomandos e opções, incluindo filtros, formato e diretório de saída; consultado em 2026-10-02.
