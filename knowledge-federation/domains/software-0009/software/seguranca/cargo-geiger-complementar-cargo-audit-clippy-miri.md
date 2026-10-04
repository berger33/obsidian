---
id: software.seguranca.tranche17.001639
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

# Combinar `cargo-geiger` com auditoria de advisories e testes de comportamento inseguro

## Em uma frase
O Geiger mede uso de `unsafe`; `cargo-audit` procura advisories conhecidos, enquanto revisão de invariantes e ferramentas de teste investigam dimensões diferentes.

## Por que importa
Nenhuma métrica isolada cobre inventário, vulnerabilidade publicada, comportamento indefinido e qualidade da API; controles independentes diminuem pontos cegos.

## Como funciona
Use cada resultado para uma pergunta específica, mantenha lockfile auditado e escolha testes de fronteira adequados à biblioteca, em vez de fundir tudo num único score.

## Exemplo
Uma biblioteca de parsing pode combinar Geiger para localizar `unsafe`, `cargo audit` para dependências e testes de fuzzing sobre a API pública.

## Limites e trade-offs
Compor ferramentas não garante que bugs sejam encontrados; resultado verde em cada etapa depende de escopo, versão e cobertura de cada controle.

## Como verificar
Leia os relatórios separadamente e confirme que cada exigência de segurança tem responsável, artefato e critério verificável.

## Conexões
- [[cargo-geiger-relatorio-dados-entrada-auditoria-humana]] — Arquivar saída do `cargo-geiger` como evidência de revisão, não como certificado.
- [[cargo-geiger-politica-nao-bloquear-por-contagem-bruta]] — Evitar gate binário por contagem bruta de `unsafe` sem contexto de risco.

## Fontes
- [`cargo-geiger` — README publicado no Docs.rs](https://docs.rs/crate/cargo-geiger/latest/source/README.md) — uso do plugin Cargo, estatísticas de `unsafe`, instalação, intenção de auditoria e limitações reconhecidas pelo projeto; consultado em 2026-10-04.
- [The Rustonomicon — Meet Safe and Unsafe](https://doc.rust-lang.org/nomicon/meet-safe-and-unsafe.html) — distinção entre Safe Rust e Unsafe Rust, responsabilidades de invariantes e possíveis usos de operações unsafe; consultado em 2026-10-04.
