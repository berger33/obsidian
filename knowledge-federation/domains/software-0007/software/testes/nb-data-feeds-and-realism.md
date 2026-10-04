---
id: software.testes.tranche20.001456
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://www.nuget.org/packages/NBomber", "https://github.com/PragmaticFlow/NBomber"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# NBomber: alimentar cenários com dados

## Em uma frase
A biblioteca permite fornecer dados variados por iteração, aproximando a carga do padrão real de uso.

## Por que importa
Dados sempre iguais geram cache artificial e medem um caminho que não representa o uso efetivo do serviço.

## Como funciona
Alimente os cenários com dados variados e realistas, evite repetir o mesmo identificador e prepare o conjunto antes da execução.

## Exemplo
Um catálogo de identificadores pode ser percorrido de forma variada para simular consultas distintas sob carga.

## Limites e trade-offs
Repetir o mesmo identificador mede cache em vez de processamento, e dados inválidos geram falhas que não indicam problema real do serviço.

## Como verificar
Compare a latência com dados repetidos e com dados variados e explique a diferença encontrada.

## Conexões
- [[nb-http-metrics-and-plugins]] — Veja também: NBomber: medir detalhes de protocolo.
- [[nb-distributed-cluster]] — Veja também: NBomber: executar em cluster distribuído.

## Fontes
- [NBomber — Pacote publicado](https://www.nuget.org/packages/NBomber) — versões, dependências e documentação do pacote; consultado em 2026-10-03.
- [NBomber — repositório oficial](https://github.com/PragmaticFlow/NBomber) — código-fonte, integrações e documentação do projeto; consultado em 2026-10-03.
