---
id: software.testes.tranche17.001061
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://docs.gatling.io/concepts/feeder/", "https://docs.gatling.io/concepts/simulation/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gatling: alimentar cenários com dados externos

## Em uma frase
Os alimentadores fornecem valores a cada iteração, a partir de arquivos, bancos ou código, com estratégias de distribuição entre usuários virtuais.

## Por que importa
Dados fixos no cenário limitam a cobertura e criam contenção artificial quando todos os usuários usam o mesmo registro.

## Como funciona
Escolha a fonte de dados, defina a estratégia de consumo adequada e declare o alimentador antes das ações que usam os campos.

## Exemplo
Uma carga de leitura pode consumir identificadores variados de um arquivo, enquanto um cenário de escrita gera valores únicos por execução.

## Limites e trade-offs
Estratégia inadequada repete dados ou esgota a fonte, e arquivos grandes precisam ser considerados no consumo de memória do gerador.

## Como verificar
Rode a simulação com um arquivo de poucas linhas e confirme, no relatório, que os valores usados variam conforme a estratégia escolhida.

## Conexões
- [[gatling-session-and-extraction]] — Veja também: Gatling: transportar dados pela sessão.
- [[gatling-pauses-and-pacing]] — Veja também: Gatling: representar o tempo de pensamento.

## Fontes
- [Gatling — Feeder](https://docs.gatling.io/concepts/feeder/) — fontes de dados externos e estratégias de distribuição entre usuários; consultado em 2026-10-03.
- [Gatling — Simulation](https://docs.gatling.io/concepts/simulation/) — estrutura da simulação, protocolo, cenários e relatório de execução; consultado em 2026-10-03.
