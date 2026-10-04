---
id: software.seguranca.tranche20.001978
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

# RustSec cargo-audit: Considerar advisories de manutenção

## Em uma frase
**RustSec cargo-audit — Considerar advisories de manutenção:** Base pode incluir avisos além de exploração técnica, conforme categoria e conteúdo do advisory.

## Por que importa
O recorte de **considerar advisories de manutenção** ajuda a detectar dependências Rust vulneráveis e orientar correção ou exceções rastreáveis. A equipe registra risco, evidência e responsável.

## Como funciona
Para **considerar advisories de manutenção**, cargo-audit lê lockfile, sincroniza advisory database e relata vulnerabilidades ou avisos aplicáveis às crates. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Leia advisory completo antes de decidir correção ou exceção para crate sem manutenção. Teste em staging autorizado.

## Limites e trade-offs
Ausência de patch disponível não remove risco de dependência abandonada. Exceções exigem responsável e prazo.

## Como verificar
Registre decisão e prazo para migrar ou substituir crate sem manutenção. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cargo-audit-fixar-toolchain-e-comando-de-auditoria]] — Complementa o tópico com rustsec cargo-audit: fixar toolchain e comando de auditoria.

## Fontes
- [RustSec — cargo-audit repository](https://github.com/rustsec/rustsec) — projeto oficial RustSec e documentação do auditor de Cargo.lock; consultado em 2026-10-04.
- [cargo-audit — Configuration example](https://github.com/rustsec/rustsec/blob/main/cargo-audit/audit.toml.example) — exemplo oficial de configuração e exceções audit.toml; consultado em 2026-10-04.
