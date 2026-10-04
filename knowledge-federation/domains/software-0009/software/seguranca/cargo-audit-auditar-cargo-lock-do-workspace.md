---
id: software.seguranca.tranche20.001971
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-20.md"
fontes: ["https://github.com/rustsec/rustsec", "https://github.com/rustsec/rustsec/blob/main/cargo-audit/audit.toml.example"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# RustSec cargo-audit: Auditar Cargo.lock do workspace

## Em uma frase
**RustSec cargo-audit — Auditar Cargo.lock do workspace:** cargo-audit examina dependências resolvidas no Cargo.lock contra avisos da base RustSec.

## Por que importa
O recorte de **auditar cargo.lock do workspace** ajuda a detectar dependências Rust vulneráveis e orientar correção ou exceções rastreáveis. A equipe registra risco, evidência e responsável.

## Como funciona
Para **auditar cargo.lock do workspace**, cargo-audit lê lockfile, sincroniza advisory database e relata vulnerabilidades ou avisos aplicáveis às crates. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Rode scan em cada workspace do produto e versione todos os lockfiles relevantes. Teste em staging autorizado.

## Limites e trade-offs
Projeto sem lockfile ou com lock desatualizado pode não refletir dependências do build. Exceções exigem responsável e prazo.

## Como verificar
Compare caminho do lockfile e target com workspace compilado em CI. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cargo-audit-atualizar-advisory-database]] — Complementa o tópico com rustsec cargo-audit: atualizar advisory database.

## Fontes
- [RustSec — cargo-audit repository](https://github.com/rustsec/rustsec) — projeto oficial RustSec e documentação do auditor de Cargo.lock; consultado em 2026-10-04.
- [cargo-audit — Configuration example](https://github.com/rustsec/rustsec/blob/main/cargo-audit/audit.toml.example) — exemplo oficial de configuração e exceções audit.toml; consultado em 2026-10-04.
