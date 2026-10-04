---
id: software.seguranca.tranche20.001979
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

# RustSec cargo-audit: Fixar toolchain e comando de auditoria

## Em uma frase
**RustSec cargo-audit — Fixar toolchain e comando de auditoria:** Versão da CLI e ambiente do runner influenciam interpretação, flags e reprodutibilidade.

## Por que importa
O recorte de **fixar toolchain e comando de auditoria** ajuda a detectar dependências Rust vulneráveis e orientar correção ou exceções rastreáveis. A equipe registra risco, evidência e responsável.

## Como funciona
Para **fixar toolchain e comando de auditoria**, cargo-audit lê lockfile, sincroniza advisory database e relata vulnerabilidades ou avisos aplicáveis às crates. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Fixe cargo-audit em configuração do job e documente atualização da versão. Teste em staging autorizado.

## Limites e trade-offs
Executar versão antiga pode não suportar novo formato do advisory database. Exceções exigem responsável e prazo.

## Como verificar
Compare output de versão atual e candidata em lockfiles de fixture. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cargo-audit-tratar-saida-como-evidencia-limitada]] — Complementa o tópico com rustsec cargo-audit: tratar saída como evidência limitada.

## Fontes
- [RustSec — cargo-audit repository](https://github.com/rustsec/rustsec) — projeto oficial RustSec e documentação do auditor de Cargo.lock; consultado em 2026-10-04.
- [cargo-audit — Configuration example](https://github.com/rustsec/rustsec/blob/main/cargo-audit/audit.toml.example) — exemplo oficial de configuração e exceções audit.toml; consultado em 2026-10-04.
