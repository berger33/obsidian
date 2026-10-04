---
id: software.seguranca.tranche17.001632
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
fontes: ["https://github.com/geiger-rs/cargo-geiger", "https://doc.rust-lang.org/cargo/reference/workspaces.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Executar `cargo geiger` na raiz do workspace e delimitar o grafo analisado

## Em uma frase
O README orienta executar `cargo geiger` no diretório do `Cargo.toml` que se deseja analisar, para produzir estatísticas do crate e de suas dependências.

## Por que importa
A pasta de execução e a resolução do workspace determinam quais pacotes aparecem; uma leitura incompleta pode levar a comparar conjuntos diferentes.

## Como funciona
Escolha explicitamente o manifest de produção, mantenha Cargo.lock e opções de build sob revisão e registre se a análise cobre workspace inteiro ou um componente.

## Exemplo
Em um monorepo, rode a análise para os manifests de cada binário publicado e salve uma saída separada para evitar misturar dependências de ferramentas de teste.

```text
cd path/to/crate && cargo geiger
```

## Limites e trade-offs
Uma execução local não garante que todos os targets ou features foram incluídos; valide o grafo real de release antes de usar a métrica como inventário.

## Como verificar
Confira o diretório atual, o manifest selecionado e a lista de crates mostrada; compare com o grafo obtido por Cargo na configuração de produção.

## Conexões
- [[cargo-geiger-proposito-estatisticas-unsafe-rust]] — `cargo-geiger`: medir presença de `unsafe` sem converter contagem em nota de segurança.
- [[cargo-geiger-blocos-unsafe-review-invariantes]] — Transformar os pontos `unsafe` do `cargo-geiger` em uma fila de revisão de invariantes.

## Fontes
- [`cargo-geiger` — repositório oficial](https://github.com/geiger-rs/cargo-geiger) — comando do plugin Cargo e execução sobre o manifest/workspace selecionado; consultado em 2026-10-04.
- [Cargo Reference — Workspaces](https://doc.rust-lang.org/cargo/reference/workspaces.html) — membros e fronteiras do workspace que determinam o grafo selecionado; consultado em 2026-10-04.
