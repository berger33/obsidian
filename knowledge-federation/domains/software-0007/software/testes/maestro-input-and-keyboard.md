---
id: software.testes.tranche15.000905
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
fontes: ["https://docs.maestro.dev/api-reference/commands", "https://docs.maestro.dev/maestro-cli/maestro-cli-commands-and-options"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Maestro: preencher campos e controlar teclado

## Em uma frase
`inputText` digita em um campo focado, `eraseText` remove caracteres e `hideKeyboard` fecha o teclado virtual quando ele cobre a interface.

## Por que importa
Em telas móveis o teclado ocupa parte da área visível e pode esconder botões, o que transforma uma falha de layout ou de fluxo em erro de elemento não encontrado.

## Como funciona
Toque no campo antes de digitar, limpe o conteúdo anterior quando necessário e feche o teclado antes de interagir com elementos que ficam atrás dele.

## Exemplo
`- tapOn: { id: "campo_email" }`, `- inputText: "ada@exemplo.com"` e `- hideKeyboard` formam a sequência básica de preenchimento.

## Limites e trade-offs
`inputText` depende do foco correto e não valida máscara ou formato; a asserção do valor aplicado precisa ser feita sobre a interface ou sobre o fluxo seguinte.

## Como verificar
Verifique o comportamento com teclado aberto e fechado e confirme que o campo recebeu o texto completo, incluindo caracteres especiais do caso.

## Conexões
- [[maestro-runflow-subflows]] — Veja também: Maestro: reutilizar fluxos com runFlow.
- [[maestro-tags-and-filters]] — Veja também: Maestro: organizar fluxos com tags.

## Fontes
- [Maestro — Commands](https://docs.maestro.dev/api-reference/commands) — catálogo de comandos de interação, asserção, controle e espera; consultado em 2026-10-02.
- [Maestro — CLI](https://docs.maestro.dev/maestro-cli/maestro-cli-commands-and-options) — subcomandos e opções, incluindo filtros, formato e diretório de saída; consultado em 2026-10-02.
