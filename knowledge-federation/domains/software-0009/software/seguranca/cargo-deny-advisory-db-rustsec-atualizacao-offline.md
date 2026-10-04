---
id: software.seguranca.tranche17.001612
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
fontes: ["https://embarkstudios.github.io/cargo-deny/checks/advisories/cfg.html", "https://embarkstudios.github.io/cargo-deny/cli/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `cargo-deny check advisories`: fonte RustSec, cache local e atualidade dos dados

## Em uma frase
O check de advisories usa a RustSec Advisory Database por padrão e pode ser configurado para buscar outros endereços de base e armazená-los localmente.

## Por que importa
Uma auditoria offline pode ser reproduzível, mas deixa de refletir avisos publicados depois da última sincronização; a idade dos dados precisa aparecer no processo.

## Como funciona
Defina URLs e diretório de cache somente quando necessário, documente a janela sem rede e trate `maximum-db-staleness` como limite de operação offline.

## Exemplo
Em uma rede isolada, sincronize a base por canal aprovado, registre a data de atualização e execute a análise em modo offline sem declarar os dados como atuais indefinidamente.

```text
cargo deny check advisories --disable-fetch
```

## Limites e trade-offs
A configuração de idade máxima é relevante quando a busca é desativada; uma base antiga pode omitir advisories recentes e não deve ser interpretada como resultado limpo atual.

## Como verificar
Registre a revisão da base usada no job e compare seu timestamp com o limite de frescor definido na política local.

## Conexões
- [[cargo-deny-checks-grafo-dependencias-rust-configuracao]] — `cargo-deny`: checks declarativos sobre o grafo de dependências Cargo.
- [[cargo-deny-ignores-advisory-expiry-reason-escopo]] — Exceções em `[advisories]`: ID, motivo, escopo e expiração.

## Fontes
- [`cargo-deny` — configuração de advisories](https://embarkstudios.github.io/cargo-deny/checks/advisories/cfg.html) — base padrão, fetch, cache, fontes de DB e limite de staleness; consultado em 2026-10-04.
- [`cargo-deny` — CLI](https://embarkstudios.github.io/cargo-deny/cli/) — opções do comando para controlar execução/fetch e rodar checks; consultado em 2026-10-04.
