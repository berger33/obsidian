---
id: software.seguranca.tranche17.001610
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
fontes: ["https://github.com/RustSec/rustsec/blob/main/cargo-audit/README.md", "https://github.com/rustsec/audit-check"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `cargo-audit` em CI: política de falha, atualização da base e trilha do relatório

## Em uma frase
O projeto recomenda integrar a auditoria em automação, inclusive por meio da action oficial `rustsec/audit-check`, para verificar mudanças e executar auditorias agendadas.

## Por que importa
Uma execução apenas local perde cobertura quando lockfiles mudam em branches ou quando novos advisories surgem depois do merge.

## Como funciona
Defina a versão do scanner, a política de falha, artefatos de saída e processo de exceção; programe também uma verificação recorrente para detectar avisos recém-publicados.

## Exemplo
No pull request, audite o lockfile alterado e anexe os IDs encontrados; em execução periódica, crie tarefas de remediação para advisories ainda não resolvidos.

```text
cargo audit
```

## Limites e trade-offs
Uma action não decide aplicabilidade nem elimina falsos positivos, e uma saída verde só significa que aquela base e aquele lockfile não produziram bloqueios.

## Como verificar
Confirme que a action roda no mesmo lockfile usado pelo build, que falha conforme a política documentada e que o relatório pode ser ligado ao commit auditado.

## Conexões
- [[cargo-audit-fix-dry-run-remediacao-experimental]] — `cargo audit fix --dry-run`: avaliar remediação antes de alterar dependências.

## Fontes
- [RustSec `cargo-audit` — README oficial](https://github.com/RustSec/rustsec/blob/main/cargo-audit/README.md) — recomendação de integração da auditoria e semântica dos achados; consultado em 2026-10-04.
- [RustSec `audit-check` — GitHub Action oficial](https://github.com/rustsec/audit-check) — ação GitHub que executa cargo-audit em pull requests e por agendamento; consultado em 2026-10-04.
