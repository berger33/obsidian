---
id: software.seguranca.tranche20.001972
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

# RustSec cargo-audit: Atualizar advisory database

## Em uma frase
**RustSec cargo-audit — Atualizar advisory database:** A base de advisories evolui e pode alterar resultado entre execuções do mesmo commit.

## Por que importa
O recorte de **atualizar advisory database** ajuda a detectar dependências Rust vulneráveis e orientar correção ou exceções rastreáveis. A equipe registra risco, evidência e responsável.

## Como funciona
Para **atualizar advisory database**, cargo-audit lê lockfile, sincroniza advisory database e relata vulnerabilidades ou avisos aplicáveis às crates. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Sincronize database no job controlado e armazene versão ou commit usado na auditoria. Teste em staging autorizado.

## Limites e trade-offs
Base não sincronizada pode ocultar advisory publicado recentemente. Exceções exigem responsável e prazo.

## Como verificar
Registre timestamp e confirme atualização concluída antes de tratar ausência como resultado. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cargo-audit-interpretar-advisory-por-crate-e-versao]] — Complementa o tópico com rustsec cargo-audit: interpretar advisory por crate e versão.

## Fontes
- [RustSec — cargo-audit repository](https://github.com/rustsec/rustsec) — projeto oficial RustSec e documentação do auditor de Cargo.lock; consultado em 2026-10-04.
- [cargo-audit — Configuration example](https://github.com/rustsec/rustsec/blob/main/cargo-audit/audit.toml.example) — exemplo oficial de configuração e exceções audit.toml; consultado em 2026-10-04.
