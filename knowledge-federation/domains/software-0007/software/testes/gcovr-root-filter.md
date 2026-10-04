---
id: software.testes.tranche22.001652
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://gcovr.com/en/stable/getting-started.html", "https://gcovr.com/en/stable/manpage.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# gcovr: a raiz é o filtro padrão

## Em uma frase
O --root (curto -r) define o diretório das fontes, responde por como os caminhos aparecem reportados (relativos a ele) e, sem nenhum --filter explícito, vira ele próprio o filtro default — o que fica fora da raiz é excluído do relatório.

## Por que importa
Essa regra única explica os dois sustos mais comuns do tooling de cobertura: relatório que não mostra nada (caminhos fora do root) e relatório que mostra as libs de terceiros (filtros não ajustados).

## Como funciona
A referência documenta que filters são regex sobre caminhos com barras à UNIX mesmo no Windows, e que cada flag de filtro aceita repetição para compor o conjunto.

## Exemplo
No exemplo canônico de out-of-source, o gcovr roda de dentro de build/ com -r .. apontando a raiz do projeto que contém as fontes.

## Limites e trade-offs
Regex de caminho com ./ prefixo implícito confunde: o que vale é o caminho normalizado relativo — teste o padrão com --txt antes de commitar no config.

## Como verificar
Adicione -f 'src/' a uma suíte que hoje mostra headers de /usr e confirme pela contagem de arquivos que o filtro os varreu.

## Conexões
- [[gcovr-getting-started]] — Veja também: gcovr: três passos do build ao relatório.
- [[gcovr-output-formats]] — Veja também: gcovr: quinze formatos, uma flag cada.

## Fontes
- [gcovr — Getting Started](https://gcovr.com/en/stable/getting-started.html) — flags de build, -r, html-details e html-nested; consultado em 2026-10-03.
- [gcovr — Command Line Reference](https://gcovr.com/en/stable/manpage.html) — filtros, exclusões, config keys e --no-markers; consultado em 2026-10-03.
