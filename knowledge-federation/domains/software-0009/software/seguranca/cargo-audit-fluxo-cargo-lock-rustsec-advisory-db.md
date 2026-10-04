---
id: software.seguranca.tranche17.001601
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
fontes: ["https://github.com/RustSec/rustsec/blob/main/cargo-audit/README.md", "https://github.com/RustSec/advisory-db"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `cargo-audit`: fluxo entre `Cargo.lock`, RustSec Advisory Database e achados por versão

## Em uma frase
`cargo audit` compara as versões resolvidas em `Cargo.lock` com advisories publicados para crates Rust e apresenta a dependência relacionada ao achado.

## Por que importa
O resultado transforma uma lista de versões transitivas em itens triáveis, com identificador do advisory e orientação de versão corrigida quando a base fornece esse dado.

## Como funciona
O comando lê o grafo já resolvido em vez de inferir a aplicação inteira; isso torna importante versionar o lockfile usado pelo build e executar a auditoria sobre o mesmo estado.

## Exemplo
Em um workspace Rust confiável, rode a auditoria na raiz, guarde a saída da execução e associe cada advisory a uma issue de atualização ou a uma exceção revisada.

```text
cargo audit
```

## Limites e trade-offs
A presença de uma crate vulnerável no lockfile não prova que a função afetada seja alcançável; o comando não substitui análise de uso nem revisão da correção.

## Como verificar
Compare o identificador RUSTSEC e a faixa de versões do relatório com o advisory primário, depois confirme qual crate pai introduziu a versão resolvida.

## Conexões
- [[cargo-audit-identificadores-rustsec-faixas-versoes-triagem]] — Triagem de achados `RUSTSEC-*`: identificador, faixa afetada e versão de correção.

## Fontes
- [RustSec `cargo-audit` — README oficial](https://github.com/RustSec/rustsec/blob/main/cargo-audit/README.md) — entrada `Cargo.lock`, relatórios de advisories e comportamento do comando; consultado em 2026-10-04.
- [RustSec Advisory Database — repositório oficial](https://github.com/RustSec/advisory-db) — estrutura e manutenção dos registros primários de advisories RUSTSEC; consultado em 2026-10-04.
