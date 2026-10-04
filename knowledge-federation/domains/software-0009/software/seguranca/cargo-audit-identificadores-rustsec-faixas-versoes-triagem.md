---
id: software.seguranca.tranche17.001602
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
fontes: ["https://github.com/RustSec/rustsec/blob/main/cargo-audit/README.md", "https://github.com/RustSec/advisory-db"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Triagem de achados `RUSTSEC-*`: identificador, faixa afetada e versão de correção

## Em uma frase
Um resultado de `cargo-audit` associa a crate vulnerável a um aviso RustSec identificável, permitindo abrir o registro primário antes de planejar uma atualização.

## Por que importa
Nomes parecidos ou uma versão antiga não bastam para decidir impacto; a faixa afetada e as versões corrigidas devem ser lidas no advisory específico.

## Como funciona
Use o identificador do relatório para consultar descrição, versões afetadas, mitigação e notas do mantenedor; registre o lockfile e o caminho transitivo observados na mesma revisão.

## Exemplo
Quando o relatório mostrar um ID RUSTSEC, use exatamente esse identificador para abrir o advisory e cotejar a faixa afetada; não invente um número para ilustrar o caso.

```text
cargo audit
```

## Limites e trade-offs
Os advisories podem mudar e a recomendação depende da versão disponível no ecossistema; cópias locais antigas da base podem atrasar a descoberta de correções recentes.

## Como verificar
Abra o registro pelo ID impresso, confira as faixas de versão e compare com `cargo tree -i crate` para identificar quem fixa a dependência vulnerável.

## Conexões
- [[cargo-audit-fluxo-cargo-lock-rustsec-advisory-db]] — `cargo-audit`: fluxo entre `Cargo.lock`, RustSec Advisory Database e achados por versão.
- [[cargo-audit-lockfile-ausente-risco-cargo-update-projeto-nao-confiavel]] — `cargo-audit` e projeto sem `Cargo.lock`: por que evitar comandos Cargo em código não confiável.

## Fontes
- [RustSec `cargo-audit` — README oficial](https://github.com/RustSec/rustsec/blob/main/cargo-audit/README.md) — IDs de advisories e apresentação de versões afetadas/corrigidas no relatório; consultado em 2026-10-04.
- [RustSec Advisory Database — repositório oficial](https://github.com/RustSec/advisory-db) — registros primários com identificadores e faixas afetadas; consultado em 2026-10-04.
