---
id: software.testes.tranche19.001342
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://www.archunit.org/userguide/html/000_Index.html", "https://github.com/TNG/ArchUnit"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ArchUnit: aplicar convenções de codificação

## Em uma frase
Regras de codificação verificam nomes, anotações, modificadores, exceções declaradas e uso de recursos proibidos.

## Por que importa
Convenções verificadas automaticamente evitam discussões repetidas de revisão e mantêm consistência em bases grandes.

## Como funciona
Verifique apenas convenções acordadas, explicite exceções com anotação própria e mantenha o conjunto pequeno o bastante para ser cumprido.

## Exemplo
Uma regra pode impedir que exceções genéricas sejam declaradas na camada de serviço.

## Limites e trade-offs
Regras de estilo em excesso transformam a suíte em obstáculo e geram contornos artificiais para satisfazer a verificação.

## Como verificar
Introduza a violação de uma convenção acordada e confirme que a regra correspondente falha apenas nessa classe.

## Conexões
- [[archunit-dependency-rules]] — Veja também: ArchUnit: controlar dependências entre classes e pacotes.
- [[archunit-freezing]] — Veja também: ArchUnit: congelar violações existentes.

## Fontes
- [ArchUnit — User Guide](https://www.archunit.org/userguide/html/000_Index.html) — regras, camadas, fatias, congelamento e verificação por diagrama; consultado em 2026-10-03.
- [ArchUnit — repositório oficial](https://github.com/TNG/ArchUnit) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
