---
id: software.seguranca.tranche20.001980
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

# RustSec cargo-audit: Tratar saída como evidência limitada

## Em uma frase
**RustSec cargo-audit — Tratar saída como evidência limitada:** Audit cobre advisories conhecidos para crates presentes no lockfile, não segurança de código próprio.

## Por que importa
O recorte de **tratar saída como evidência limitada** ajuda a detectar dependências Rust vulneráveis e orientar correção ou exceções rastreáveis. A equipe registra risco, evidência e responsável.

## Como funciona
Para **tratar saída como evidência limitada**, cargo-audit lê lockfile, sincroniza advisory database e relata vulnerabilidades ou avisos aplicáveis às crates. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Use resultado junto com revisão de Rust unsafe, fuzzing e análise de dependências mais ampla. Teste em staging autorizado.

## Limites e trade-offs
Passar audit não verifica lógica, configuração ou advisories fora do feed consultado. Exceções exigem responsável e prazo.

## Como verificar
Registre escopo e timestamp e combine com controles complementares do pipeline. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[openssf-badge-entender-escopo-da-autoavaliacao]] — Complementa o tópico com openssf best practices badge: entender escopo da autoavaliação.

## Fontes
- [RustSec — cargo-audit repository](https://github.com/rustsec/rustsec) — projeto oficial RustSec e documentação do auditor de Cargo.lock; consultado em 2026-10-04.
- [cargo-audit — Configuration example](https://github.com/rustsec/rustsec/blob/main/cargo-audit/audit.toml.example) — exemplo oficial de configuração e exceções audit.toml; consultado em 2026-10-04.
