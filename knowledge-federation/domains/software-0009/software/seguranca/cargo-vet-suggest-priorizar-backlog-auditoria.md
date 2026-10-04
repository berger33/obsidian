---
id: software.seguranca.tranche17.001627
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://mozilla.github.io/cargo-vet/commands.html#cargo-vet-suggest", "https://mozilla.github.io/cargo-vet/performing-audits.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `cargo vet suggest`: priorizar backlog de auditorias com mudanças menores

## Em uma frase
O comando `suggest` recomenda dependências para revisão e agrupa o trabalho por critério, incluindo diferenças que podem ser mais curtas de inspecionar.

## Por que importa
Um inventário grande pode paralisar a adoção; sugestões ordenadas ajudam a iniciar por revisões de menor custo sem afirmar que sejam as mais críticas.

## Como funciona
Use a sugestão como fila de trabalho, combine-a com criticidade do produto e exposição da crate e acompanhe quais registros eliminam exemptions.

## Exemplo
Uma equipe pode reservar uma janela semanal para auditar itens sugeridos, registrar o resultado em `supply-chain/` e atualizar a fila no pull request.

```text
cargo vet suggest
```

## Limites e trade-offs
A ordenação por tamanho de diff não é uma avaliação automática de risco ou severidade; prioridades do produto podem exigir outra ordem.

## Como verificar
Compare as sugestões após uma atualização do grafo, abra a diferença indicada e confirme que a ação proposta não é apenas adicionar exemption.

## Conexões
- [[cargo-vet-imports-organizacoes-trust-explicito]] — Imports de auditorias no `cargo-vet`: confiar em organizações de forma explícita.
- [[cargo-vet-certify-record-audit-trilha-versao]] — `cargo vet certify`: registrar uma auditoria ligada à versão revisada.

## Fontes
- [Cargo Vet — Commands: suggest](https://mozilla.github.io/cargo-vet/commands.html#cargo-vet-suggest) — sugestões de auditoria e agrupamento por critério; consultado em 2026-10-04.
- [Cargo Vet — Performing Audits](https://mozilla.github.io/cargo-vet/performing-audits.html) — ordenação pelo esforço estimado em linhas e trade-off de exemptions; consultado em 2026-10-04.
