---
id: software.testes.tranche19.001338
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

# ArchUnit: importar o código e declarar regras

## Em uma frase
A biblioteca importa as classes compiladas para uma estrutura consultável e expressa regras verificáveis com integração ao framework de testes.

## Por que importa
As regras ficam no mesmo lugar dos testes, executando a cada mudança e impedindo que a arquitetura se degrade silenciosamente.

## Como funciona
Importe os pacotes do projeto, declare regras estáticas anotadas e execute como parte da suíte normal.

## Exemplo
Uma verificação pode assegurar que classes de controlador residam no pacote correspondente.

## Limites e trade-offs
Importar pacotes amplos demais inclui dependências de terceiros e gera violações que não pertencem ao projeto.

## Como verificar
Restrinja a importação e confirme que uma classe colocada no pacote errado faz a verificação falhar.

## Conexões
- [[archunit-layered-architecture]] — Veja também: ArchUnit: verificar arquitetura em camadas.

## Fontes
- [ArchUnit — User Guide](https://www.archunit.org/userguide/html/000_Index.html) — regras, camadas, fatias, congelamento e verificação por diagrama; consultado em 2026-10-03.
- [ArchUnit — repositório oficial](https://github.com/TNG/ArchUnit) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
