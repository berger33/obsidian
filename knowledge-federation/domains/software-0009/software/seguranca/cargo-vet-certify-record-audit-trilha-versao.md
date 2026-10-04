---
id: software.seguranca.tranche17.001628
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
fontes: ["https://mozilla.github.io/cargo-vet/commands.html#cargo-vet-certify", "https://mozilla.github.io/cargo-vet/recording-audits.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `cargo vet certify`: registrar uma auditoria ligada à versão revisada

## Em uma frase
Depois da inspeção, `certify` registra que uma versão foi auditada sob determinado critério e mantém o resultado junto à política do projeto.

## Por que importa
A trilha local permite revisar quem introduziu a decisão e que versão do código foi coberta quando dependências são atualizadas novamente.

## Como funciona
Confirme a crate, versão, critério e conteúdo efetivamente lido antes de certificar; use revisão por pares para mudanças nos arquivos da supply chain.

## Exemplo
Após revisar uma crate, gere a certificação na branch dedicada e peça aprovação do code owner antes de integrar o novo registro.

```text
cargo vet certify
```

## Limites e trade-offs
O registro não contém automaticamente a qualidade do raciocínio nem prova que a pessoa leu todo código relevante.

## Como verificar
Abra `audits.toml` no diff, confira identificador e critério e confirme que a versão registrada corresponde ao grafo que passou em CI.

## Conexões
- [[cargo-vet-suggest-priorizar-backlog-auditoria]] — `cargo vet suggest`: priorizar backlog de auditorias com mudanças menores.
- [[cargo-vet-record-violation-integridade-audits]] — `cargo vet record-violation`: registrar que uma versão contradiz uma auditoria.

## Fontes
- [Cargo Vet — Commands: certify](https://mozilla.github.io/cargo-vet/commands.html#cargo-vet-certify) — registro de auditoria de versão ou delta; consultado em 2026-10-04.
- [Cargo Vet — Recording Audits](https://mozilla.github.io/cargo-vet/recording-audits.html) — campos de auditoria, autoria, versão e critério gravados; consultado em 2026-10-04.
