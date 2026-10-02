---
id: software.testes.tranche15.000908
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

# Maestro: registrar evidências da execução

## Em uma frase
O comando `takeScreenshot` e o diretório de saída da CLI registram imagens dos passos, e a execução pode produzir resultado em formato consumível pelo pipeline.

## Por que importa
Uma falha sem captura obriga a reproduzir o cenário manualmente, e o tempo gasto nisso costuma superar o custo de armazenar as imagens.

## Como funciona
Capture marcos relevantes, defina o diretório de saída no comando e publique o artefato do pipeline com retenção adequada.

## Exemplo
`maestro test --format junit --output resultados/ fluxo.yaml` gera resultado estruturado e `- takeScreenshot: confirmacao` registra a evidência nomeada.

## Limites e trade-offs
Capturas de cada passo geram volume alto e podem conter dados sensíveis; a política precisa escolher marcos e revisar o conteúdo armazenado.

## Como verificar
Rode o fluxo, confirme a presença dos arquivos esperados e simule uma falha para verificar se a evidência do passo problemático foi preservada.

## Conexões
- [[maestro-repeat-and-conditions]] — Veja também: Maestro: repetir passos e tratar variações.
- [[maestro-wait-animation-and-scroll]] — Veja também: Maestro: esperar animação e alcançar itens distantes.

## Fontes
- [Maestro — Commands](https://docs.maestro.dev/api-reference/commands) — catálogo de comandos de interação, asserção, controle e espera; consultado em 2026-10-02.
- [Maestro — CLI](https://docs.maestro.dev/maestro-cli/maestro-cli-commands-and-options) — subcomandos e opções, incluindo filtros, formato e diretório de saída; consultado em 2026-10-02.
