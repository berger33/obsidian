---
id: software.seguranca.tranche17.001633
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
fontes: ["https://docs.rs/crate/cargo-geiger/latest/source/README.md", "https://doc.rust-lang.org/nomicon/meet-safe-and-unsafe.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Transformar os pontos `unsafe` do `cargo-geiger` em uma fila de revisão de invariantes

## Em uma frase
Uma ocorrência de `unsafe` indica que parte das garantias de segurança precisa ser sustentada por contratos que o compilador não comprova integralmente.

## Por que importa
A pergunta útil não é quantos blocos existem isoladamente, mas quais invariantes tornam cada operação válida e se chamadores podem preservá-los.

## Como funciona
Use a contagem para localizar módulos, leia comentários de safety, siga caminhos de entrada e revise ownership, alinhamento, aliasing e limites aplicáveis.

## Exemplo
Para um wrapper de FFI, registre pré-condições de ponteiros, duração dos buffers e regras de aliasing antes de aprovar a abstração pública.

```text
cargo geiger
```

## Limites e trade-offs
O contador não entende semântica de invariantes e não mede a qualidade dos testes; um único bloco mal especificado pode ser mais importante que dezenas triviais.

## Como verificar
Associe cada região prioritária a revisão de código, teste de propriedade ou sanitizador apropriado e confirme que o comentário de safety explica a obrigação do chamador.

## Conexões
- [[cargo-geiger-execucao-workspace-grafo-dependencias]] — Executar `cargo geiger` na raiz do workspace e delimitar o grafo analisado.
- [[cargo-geiger-uso-unsafe-necessario-encapsulamento]] — Interpretar `unsafe` no contexto: FFI, abstrações de baixo nível e encapsulamento seguro.

## Fontes
- [`cargo-geiger` — README publicado no Docs.rs](https://docs.rs/crate/cargo-geiger/latest/source/README.md) — uso do plugin Cargo, estatísticas de `unsafe`, instalação, intenção de auditoria e limitações reconhecidas pelo projeto; consultado em 2026-10-04.
- [The Rustonomicon — Meet Safe and Unsafe](https://doc.rust-lang.org/nomicon/meet-safe-and-unsafe.html) — distinção entre Safe Rust e Unsafe Rust, responsabilidades de invariantes e possíveis usos de operações unsafe; consultado em 2026-10-04.
