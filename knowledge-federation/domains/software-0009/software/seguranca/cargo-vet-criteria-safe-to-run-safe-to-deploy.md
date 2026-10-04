---
id: software.seguranca.tranche17.001624
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
fontes: ["https://mozilla.github.io/cargo-vet/audit-criteria.html", "https://mozilla.github.io/cargo-vet/built-in-criteria.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Critérios do `cargo-vet`: definir o que uma auditoria precisa demonstrar

## Em uma frase
`cargo-vet` inclui os critérios `safe-to-run` e `safe-to-deploy` e permite critérios customizados e políticas por subárvore para descrever o nível de confiança exigido.

## Por que importa
Revisar uma crate para uso durante build pode exigir controles distintos de incluí-la no binário distribuído; critérios explícitos evitam aprovações ambíguas.

## Como funciona
Nomeie critérios com significado documentado, associe-os às áreas responsáveis e faça auditores registrar qual pergunta de segurança foi efetivamente examinada.

## Exemplo
Compare os critérios embutidos `safe-to-run` e `safe-to-deploy` ao separar uma ferramenta de teste de uma crate entregue no produto; a relação de implicação e os requisitos devem ficar documentados na policy.

```text
cargo vet check
```

## Limites e trade-offs
Critérios customizados só são úteis se revisores entendem o vocabulário; mudar a definição sem reavaliar auditorias antigas altera o alcance da confiança.

## Como verificar
Leia a configuração de critérios e políticas, confira cada registro importado ou local e confirme que o check aponta o critério que falta.

## Conexões
- [[cargo-vet-check-novas-dependencias-gate-ci]] — `cargo vet check`: detectar código de terceiro novo no grafo de build.
- [[cargo-vet-differential-audit-diff-versao-crate]] — Auditoria diferencial no `cargo-vet`: revisar a diferença entre versões de uma crate.

## Fontes
- [Cargo Vet — Audit Criteria](https://mozilla.github.io/cargo-vet/audit-criteria.html) — critérios embutidos e criação de critérios customizados; consultado em 2026-10-04.
- [Cargo Vet — Built-in Criteria](https://mozilla.github.io/cargo-vet/built-in-criteria.html) — semântica e relação de `safe-to-run` e `safe-to-deploy`; consultado em 2026-10-04.
