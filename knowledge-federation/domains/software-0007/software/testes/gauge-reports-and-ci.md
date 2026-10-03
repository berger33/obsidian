---
id: software.testes.tranche20.001367
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
fontes: ["https://docs.gauge.org/configuration", "https://github.com/getgauge/gauge"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gauge: publicar relatórios na esteira

## Em uma frase
Cada execução gera relatórios, incluindo o formato navegável em HTML e relatórios estruturados de acordo com os plugins instalados.

## Por que importa
O relatório navegável serve à investigação da falha, e o formato estruturado integra o resultado ao acompanhamento da esteira.

## Como funciona
Instale os plugins de relatório necessários, publique a pasta de relatórios como artefato e mantenha a execução em ambiente com dependências fixadas.

## Exemplo
O trabalho pode publicar o relatório de cada execução e falhar conforme o resultado agregado dos cenários.

## Limites e trade-offs
Sem publicação de artefato, a falha exige reprodução local, e plugins desatualizados podem gerar relatório incompleto.

## Como verificar
Execute a suíte e abra o relatório publicado, conferindo que a contagem de cenários coincide com a saída do terminal.

## Conexões
- [[gauge-environments-and-config]] — Veja também: Gauge: separar configuração por ambiente.
- [[gauge-limits-and-practices]] — Veja também: Gauge: reconhecer limites e boas práticas.

## Fontes
- [Gauge — Configuração](https://docs.gauge.org/configuration) — propriedades do projeto, ambientes e relatórios; consultado em 2026-10-03.
- [Gauge — repositório oficial](https://github.com/getgauge/gauge) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
