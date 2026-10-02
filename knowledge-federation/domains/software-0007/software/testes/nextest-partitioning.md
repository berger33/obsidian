---
id: software.testes.tranche15.000945
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
fontes: ["https://nexte.st/docs/partitioning/", "https://nexte.st/docs/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# nextest: dividir a suíte em shards de CI

## Em uma frase
O particionamento divide os testes em fatias ou por hash de identificador, permitindo distribuir a mesma suíte entre executores paralelos.

## Por que importa
Com a suíte crescendo, um único trabalhador vira gargalo, e divisão manual por arquivo desbalanceia a carga e exige manutenção constante.

## Como funciona
Use fatias quando precisar de divisão determinística e hash quando a distribuição por identificador for suficiente, garantindo que todos os shards cubram o total.

## Exemplo
`--partition slice:1/4` seleciona a primeira de quatro fatias, e `--partition hash:1/4` distribui por hash do nome do teste.

## Limites e trade-offs
Nenhum shard individual representa a suíte completa; a agregação dos resultados é responsabilidade do pipeline, que precisa falhar se um executor não reportar.

## Como verificar
Execute todos os shards de uma mesma revisão, una os resultados e confirme que a união corresponde à lista completa de testes descobertos.

## Conexões
- [[nextest-filtersets]] — Veja também: nextest: selecionar testes com filtros.
- [[nextest-junit-report]] — Veja também: nextest: publicar resultado em JUnit XML.

## Fontes
- [nextest — Partitioning](https://nexte.st/docs/partitioning/) — particionamento por fatias e por hash para shards de CI; consultado em 2026-10-02.
- [nextest — Documentation](https://nexte.st/docs/) — visão geral do runner, instalação e operação; consultado em 2026-10-02.
