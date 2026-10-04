---
id: software.seguranca.tranche20.001976
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

# RustSec cargo-audit: Separar falha de ferramenta de finding

## Em uma frase
**RustSec cargo-audit — Separar falha de ferramenta de finding:** Pipeline precisa distinguir erro ao baixar base ou ler lockfile de resultado sem advisories.

## Por que importa
O recorte de **separar falha de ferramenta de finding** ajuda a detectar dependências Rust vulneráveis e orientar correção ou exceções rastreáveis. A equipe registra risco, evidência e responsável.

## Como funciona
Para **separar falha de ferramenta de finding**, cargo-audit lê lockfile, sincroniza advisory database e relata vulnerabilidades ou avisos aplicáveis às crates. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Simule falha de rede e finding em jobs diferentes e configure estados de saída distintos. Teste em staging autorizado.

## Limites e trade-offs
Tratar erro operacional como sucesso produz falso verde. Exceções exigem responsável e prazo.

## Como verificar
Verifique códigos de saída e logs sem mascarar falhas do scanner. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cargo-audit-executar-auditoria-em-ci]] — Complementa o tópico com rustsec cargo-audit: executar auditoria em ci.

## Fontes
- [RustSec — cargo-audit repository](https://github.com/rustsec/rustsec) — projeto oficial RustSec e documentação do auditor de Cargo.lock; consultado em 2026-10-04.
- [cargo-audit — Configuration example](https://github.com/rustsec/rustsec/blob/main/cargo-audit/audit.toml.example) — exemplo oficial de configuração e exceções audit.toml; consultado em 2026-10-04.
