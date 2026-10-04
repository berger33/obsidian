---
id: software.seguranca.tranche20.001975
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

# RustSec cargo-audit: Governar ignores em audit.toml

## Em uma frase
**RustSec cargo-audit — Governar ignores em audit.toml:** Configuração pode ignorar advisories específicos, mas exceções precisam de escopo e justificativa.

## Por que importa
O recorte de **governar ignores em audit.toml** ajuda a detectar dependências Rust vulneráveis e orientar correção ou exceções rastreáveis. A equipe registra risco, evidência e responsável.

## Como funciona
Para **governar ignores em audit.toml**, cargo-audit lê lockfile, sincroniza advisory database e relata vulnerabilidades ou avisos aplicáveis às crates. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Adicione advisory id com issue, responsável e data de reavaliação em projeto de teste. Teste em staging autorizado.

## Limites e trade-offs
Ignore amplo ou permanente pode esconder correção futura ou vulnerabilidade reintroduzida. Exceções exigem responsável e prazo.

## Como verificar
Revise lista de ignores e faça scan sem configuração como auditoria de controle. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cargo-audit-separar-falha-de-ferramenta-de-finding]] — Complementa o tópico com rustsec cargo-audit: separar falha de ferramenta de finding.

## Fontes
- [RustSec — cargo-audit repository](https://github.com/rustsec/rustsec) — projeto oficial RustSec e documentação do auditor de Cargo.lock; consultado em 2026-10-04.
- [cargo-audit — Configuration example](https://github.com/rustsec/rustsec/blob/main/cargo-audit/audit.toml.example) — exemplo oficial de configuração e exceções audit.toml; consultado em 2026-10-04.
