---
id: software.seguranca.tranche17.001606
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
fontes: ["https://github.com/RustSec/rustsec/blob/main/cargo-audit/audit.toml.example", "https://github.com/RustSec/rustsec/blob/main/cargo-audit/README.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `audit.toml` versionado: governança das exceções locais do `cargo-audit`

## Em uma frase
O arquivo de configuração do `cargo-audit` pode registrar IDs ignorados, deixando a decisão revisável junto ao código e ao lockfile do projeto.

## Por que importa
Uma exceção só é reproduzível quando todos os desenvolvedores e o CI conhecem o mesmo escopo; flags locais invisíveis produzem auditorias divergentes.

## Como funciona
Mantenha a configuração mínima, explique cada ID com referência a evidência e revise diferenças no pull request; não converta o arquivo em allowlist ampla de advisories.

## Exemplo
Um revisor pode comparar a lista de IDs ignorados entre duas revisões e exigir que cada entrada nova venha acompanhada de análise de aplicabilidade e prazo de retorno.

```text
git diff -- Cargo.lock audit.toml
```

## Limites e trade-offs
A configuração compartilhada não valida por si mesma o raciocínio humano, e uma justificativa antiga pode deixar de ser verdadeira com mudanças no código.

## Como verificar
Execute o mesmo comando local e na CI com a configuração versionada, confira a versão da ferramenta e examine o diff de `audit.toml` em cada pull request.

## Conexões
- [[cargo-audit-ignorar-advisory-justificativa-expiracao]] — Ignorar um advisory em `cargo-audit`: exceção rastreável, justificativa e reavaliação.
- [[cargo-audit-bin-inventario-dependencias-binario-rust]] — `cargo audit bin`: leitura de dependências em binários Rust distribuídos.

## Fontes
- [RustSec `cargo-audit` — exemplo oficial de `audit.toml`](https://github.com/RustSec/rustsec/blob/main/cargo-audit/audit.toml.example) — formato de configuração de ignores e campos suportados pelo cargo-audit; consultado em 2026-10-04.
- [RustSec `cargo-audit` — README oficial](https://github.com/RustSec/rustsec/blob/main/cargo-audit/README.md) — precedência de atualização e suporte a ignores pela configuração local; consultado em 2026-10-04.
