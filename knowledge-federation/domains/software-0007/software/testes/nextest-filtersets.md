---
id: software.testes.tranche15.000944
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://nexte.st/docs/running/", "https://nexte.st/docs/configuration/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# nextest: selecionar testes com filtros

## Em uma frase
Expressões de filtro permitem selecionar casos por nome, pacote, tipo de teste e outras propriedades diretamente na linha de comando.

## Por que importa
Executar a suíte completa durante o diagnóstico é lento, e filtros por substring selecionam mais ou menos casos do que a intenção original.

## Como funciona
Use a expressão de filtro para o conjunto desejado, combine condições quando precisar restringir e registre o comando usado junto do resultado.

## Exemplo
`cargo nextest run -E 'test(/network_/)'` seleciona por padrão de nome, enquanto condições por pacote restringem o alvo dentro do workspace.

## Limites e trade-offs
Filtros que não casam com nada podem terminar sem erro e dar impressão de sucesso; overrides de configuração também podem alterar retries e tempo limite de subconjuntos silenciosamente.

## Como verificar
Liste os testes selecionados antes de executar e compare a seleção com a lista completa, garantindo que nenhum caso crítico ficou de fora.

## Conexões
- [[nextest-slow-timeout]] — Veja também: nextest: detectar e interromper testes lentos.
- [[nextest-partitioning]] — Veja também: nextest: dividir a suíte em shards de CI.

## Fontes
- [nextest — Running tests](https://nexte.st/docs/running/) — execução, filtros, saída, listagem e testes ignorados; consultado em 2026-10-02.
- [nextest — Configuration](https://nexte.st/docs/configuration/) — perfis, overrides, retries, timeouts e grupos de teste; consultado em 2026-10-02.
