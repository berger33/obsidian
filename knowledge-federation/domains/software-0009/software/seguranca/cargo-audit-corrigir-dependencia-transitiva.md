---
id: software.seguranca.tranche20.001974
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

# RustSec cargo-audit: Corrigir dependência transitiva

## Em uma frase
**RustSec cargo-audit — Corrigir dependência transitiva:** Correção pode exigir atualizar crate direta, lockfile ou versão de biblioteca intermediária.

## Por que importa
O recorte de **corrigir dependência transitiva** ajuda a detectar dependências Rust vulneráveis e orientar correção ou exceções rastreáveis. A equipe registra risco, evidência e responsável.

## Como funciona
Para **corrigir dependência transitiva**, cargo-audit lê lockfile, sincroniza advisory database e relata vulnerabilidades ou avisos aplicáveis às crates. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Faça update mínimo em branch e rode testes de workspace e de release. Teste em staging autorizado.

## Limites e trade-offs
Patch pode alterar API ou resolver crate diferente da esperada. Exceções exigem responsável e prazo.

## Como verificar
Confirme versão no lockfile, build limpo e novo resultado do audit. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cargo-audit-governar-ignores-em-audit-toml]] — Complementa o tópico com rustsec cargo-audit: governar ignores em audit.toml.

## Fontes
- [RustSec — cargo-audit repository](https://github.com/rustsec/rustsec) — projeto oficial RustSec e documentação do auditor de Cargo.lock; consultado em 2026-10-04.
- [cargo-audit — Configuration example](https://github.com/rustsec/rustsec/blob/main/cargo-audit/audit.toml.example) — exemplo oficial de configuração e exceções audit.toml; consultado em 2026-10-04.
