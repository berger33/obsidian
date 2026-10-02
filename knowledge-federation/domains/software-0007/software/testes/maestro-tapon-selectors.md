---
id: software.testes.tranche15.000902
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

# Maestro: escolher alvos de toque

## Em uma frase
O comando `tapOn` aceita texto visível, identificador de testabilidade e posição relativa, e a escolha do seletor define a estabilidade do passo.

## Por que importa
Seletores por coordenada quebram com mudança de layout ou tamanho de tela, enquanto identificadores estáveis aproximam o fluxo do contrato de testabilidade do aplicativo.

## Como funciona
Prefira identificadores mantidos pelo time do aplicativo, use texto quando ele for parte do comportamento e reserve coordenadas para casos em que nada mais identifica o alvo.

## Exemplo
`- tapOn: { id: "botao_login" }` usa o identificador de testabilidade, e `- tapOn: "Entrar"` recorre ao texto visível quando ele é estável.

## Limites e trade-offs
Textos variam com idioma e o mesmo rótulo pode aparecer em mais de um elemento, exigindo desambiguação; identificadores podem não existir em telas de terceiros.

## Como verificar
Duplique um rótulo na tela e confirme qual elemento o fluxo escolheu; ajuste o seletor para tornar a escolha inequívoca.

## Conexões
- [[maestro-launch-and-state]] — Veja também: Maestro: controlar estado do aplicativo entre passos.
- [[maestro-assertions-and-waits]] — Veja também: Maestro: afirmar visibilidade e esperar condição.

## Fontes
- [Maestro — Commands](https://docs.maestro.dev/api-reference/commands) — catálogo de comandos de interação, asserção, controle e espera; consultado em 2026-10-02.
- [Maestro — CLI](https://docs.maestro.dev/maestro-cli/maestro-cli-commands-and-options) — subcomandos e opções, incluindo filtros, formato e diretório de saída; consultado em 2026-10-02.
