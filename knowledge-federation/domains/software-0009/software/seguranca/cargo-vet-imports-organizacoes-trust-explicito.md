---
id: software.seguranca.tranche17.001626
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
fontes: ["https://mozilla.github.io/cargo-vet/importing-audits.html", "https://mozilla.github.io/cargo-vet/config.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Imports de auditorias no `cargo-vet`: confiar em organizações de forma explícita

## Em uma frase
O cargo-vet pode importar auditorias mantidas por outras organizações, mas a configuração precisa adicionar explicitamente a fonte ao conjunto de confiança.

## Por que importa
Compartilhar revisões reduz trabalho repetido; a confiança explícita evita depender de um índice central que poderia substituir os arquivos auditados.

## Como funciona
Revise a policy da organização importada, a origem dos arquivos, o mapeamento dos critérios e a origem HTTPS antes de adicionar a entrada em `config.toml`.

## Exemplo
Uma equipe pode importar auditorias de um projeto upstream conhecido e manter no pull request o URL do arquivo, versão e revisão de política.

```text
cargo vet import
```

## Limites e trade-offs
Imports não são transitivos: importar um projeto não importa automaticamente as fontes que ele próprio confia. A equipe delega julgamento às fontes diretas e ainda precisa avaliar seus critérios.

## Como verificar
Confira de onde cada arquivo importado é baixado, quem controla o repositório e se a importação aparece explicitamente na configuração versionada.

## Conexões
- [[cargo-vet-differential-audit-diff-versao-crate]] — Auditoria diferencial no `cargo-vet`: revisar a diferença entre versões de uma crate.
- [[cargo-vet-suggest-priorizar-backlog-auditoria]] — `cargo vet suggest`: priorizar backlog de auditorias com mudanças menores.

## Fontes
- [Cargo Vet — Importing Audits](https://mozilla.github.io/cargo-vet/importing-audits.html) — imports diretos, trust explícito, fontes HTTPS e ausência de transitividade; consultado em 2026-10-04.
- [Cargo Vet — Configuration](https://mozilla.github.io/cargo-vet/config.html) — mapeamento de critérios e estrutura de `imports` local; consultado em 2026-10-04.
