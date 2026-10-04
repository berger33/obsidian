---
id: software.seguranca.tranche20.001973
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

# RustSec cargo-audit: Interpretar advisory por crate e versão

## Em uma frase
**RustSec cargo-audit — Interpretar advisory por crate e versão:** Finding identifica crate e faixa de versão afetada segundo advisory publicado.

## Por que importa
O recorte de **interpretar advisory por crate e versão** ajuda a detectar dependências Rust vulneráveis e orientar correção ou exceções rastreáveis. A equipe registra risco, evidência e responsável.

## Como funciona
Para **interpretar advisory por crate e versão**, cargo-audit lê lockfile, sincroniza advisory database e relata vulnerabilidades ou avisos aplicáveis às crates. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Rastreie crate vulnerável até dependência direta ou transitiva no grafo do projeto. Teste em staging autorizado.

## Limites e trade-offs
Advisory não determina sozinho se trecho vulnerável é alcançável pela aplicação. Exceções exigem responsável e prazo.

## Como verificar
Verifique versão resolvida, advisory id e cadeia de dependência. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cargo-audit-corrigir-dependencia-transitiva]] — Complementa o tópico com rustsec cargo-audit: corrigir dependência transitiva.

## Fontes
- [RustSec — cargo-audit repository](https://github.com/rustsec/rustsec) — projeto oficial RustSec e documentação do auditor de Cargo.lock; consultado em 2026-10-04.
- [cargo-audit — Configuration example](https://github.com/rustsec/rustsec/blob/main/cargo-audit/audit.toml.example) — exemplo oficial de configuração e exceções audit.toml; consultado em 2026-10-04.
