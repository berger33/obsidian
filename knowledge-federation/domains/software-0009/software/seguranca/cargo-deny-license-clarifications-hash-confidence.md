---
id: software.seguranca.tranche17.001616
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
fontes: ["https://embarkstudios.github.io/cargo-deny/checks/licenses/cfg.html", "https://spdx.org/licenses/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Clarificações de licença no `cargo-deny`: expressão, arquivo e hash

## Em uma frase
Quando a licença não é detectada com confiança suficiente, a configuração pode declarar uma expressão SPDX e amarrá-la ao hash de um arquivo de licença.

## Por que importa
Uma clarificação manual não deve sobreviver silenciosamente a uma troca do texto legal; associar a decisão ao arquivo torna alterações relevantes detectáveis.

## Como funciona
Use-a apenas após revisão humana da licença, limite a crate e versão adequadas e atualize a clarificação quando o arquivo de referência mudar.

## Exemplo
Ao reconhecer manualmente uma licença não identificada, registre `expression` e o caminho/hash indicado pelo check, e peça revisão legal antes de aceitar o resultado.

```text
cargo deny check licenses
```

## Limites e trade-offs
Hash estável prova igualdade de bytes do arquivo consultado, não validade jurídica nem correspondência perfeita entre código e licença declarada.

## Como verificar
Edite o arquivo de licença em um teste controlado e confirme que a clarificação deixa de corresponder; depois valide a nova decisão separadamente.

## Conexões
- [[cargo-deny-licencas-spdx-allowlist-exceptions]] — Política de licenças em `cargo-deny`: expressões SPDX e exceções explícitas.
- [[cargo-deny-bans-versoes-duplicadas-dependencias-proibidas]] — `[bans]` no `cargo-deny`: dependências proibidas e versões múltiplas.

## Fontes
- [`cargo-deny` — configuração de licenças](https://embarkstudios.github.io/cargo-deny/checks/licenses/cfg.html) — clarifications, expressões, limiar de confiança e hash de arquivos; consultado em 2026-10-04.
- [SPDX — License List](https://spdx.org/licenses/) — expressões e identificadores SPDX declarados na clarificação; consultado em 2026-10-04.
