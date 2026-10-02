---
id: software.testes.tranche11.000524
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://jmeter.apache.org/usermanual/hints_and_tips.html", "https://jmeter.apache.org/usermanual/component_reference.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JMeter: distinguir variáveis de thread de propriedades compartilhadas

## Em uma frase
Variáveis de JMeter têm escopo de thread, enquanto properties são compartilhadas entre threads do processo.

## Por que importa
Usar property para dados de usuário pode criar race e substituição de valor entre VUs; usar variable para coordenação global não compartilha estado.

## Como funciona
Use JMeter variables para contexto local e properties apenas para configuração ou coordenação explicitamente global.

## Exemplo
Cada thread guarda seu token em variável própria; propriedade `baseUrl` configura destino comum da execução.

## Limites e trade-offs
Compartilhamento de property entre threads não implica distribuição automática de atualizações a engines remotos sem configuração.

## Como verificar
Execute duas threads com valores sentinela distintos e confirme que variáveis permanecem separadas enquanto configuração global é comum.

## Conexões
- [[jmeter-csv-dataset-dados-por-thread]] — Veja também: JMeter: entender leitura CSV por thread e iteração.
- [[jmeter-cli-para-carga-gui-para-debug]] — Veja também: JMeter: usar GUI para depurar e CLI para medir carga.

## Fontes
- [Apache JMeter — Hints and Tips](https://jmeter.apache.org/usermanual/hints_and_tips.html) — escopo de variáveis por thread e uso de propriedades compartilhadas; consultado em 2026-10-02.
- [Apache JMeter — Component Reference](https://jmeter.apache.org/usermanual/component_reference.html) — CSV Data Set, assertions, timers, extractors e controllers; consultado em 2026-10-02.
