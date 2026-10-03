---
id: software.testes.tranche19.001347
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

# ArchUnit: reconhecer limites

## Em uma frase
A análise cobre estrutura de classes e dependências no bytecode, sem avaliar qualidade de desenho, desempenho nem coerência semântica das fronteiras.

## Por que importa
Regras verdes podem conviver com arquitetura inadequada ao domínio, dando falsa impressão de desenho saudável.

## Como funciona
Combine as regras com revisão de desenho, testes de comportamento e discussão periódica das fronteiras pretendidas.

## Exemplo
Um projeto pode respeitar as camadas declaradas e ainda assim concentrar responsabilidades na camada de serviço.

## Limites e trade-offs
Tratar a verificação como prova de boa arquitetura substitui o julgamento de desenho por um indicador parcial.

## Como verificar
Escolha uma regra aprovada e avalie se as classes envolvidas fazem sentido no domínio, independentemente da conformidade estrutural.

## Conexões
- [[archunit-ci-failures]] — Veja também: ArchUnit: tratar falhas na esteira.

## Fontes
- [ArchUnit — User Guide](https://www.archunit.org/userguide/html/000_Index.html) — regras, camadas, fatias, congelamento e verificação por diagrama; consultado em 2026-10-03.
- [ArchUnit — repositório oficial](https://github.com/TNG/ArchUnit) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
