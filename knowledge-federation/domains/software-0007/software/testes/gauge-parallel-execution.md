---
id: software.testes.tranche20.001365
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
fontes: ["https://docs.gauge.org/execution", "https://docs.gauge.org/configuration"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gauge: executar em fluxos paralelos

## Em uma frase
A execução aceita especificações em paralelo, distribuindo-as entre processos ou threads conforme o número de fluxos configurado.

## Por que importa
A distribuição reduz o tempo total da suíte, desde que as especificações sejam independentes entre si.

## Como funciona
Ajuste o número de fluxos ao recurso da máquina, mantenha cada especificação autossuficiente e evite compartilhar estado externo sem controle.

## Exemplo
A suíte inteira pode rodar em quatro fluxos, reduzindo o tempo pela metade em máquinas com núcleos disponíveis.

## Limites e trade-offs
Fluxos em excesso degradam a máquina, e especificações que compartilham dados falham de forma intermitente conforme a distribuição.

## Como verificar
Execute a suíte em um e em vários fluxos e confirme que o conjunto de resultados é idêntico nos dois modos.

## Conexões
- [[gauge-data-driven]] — Veja também: Gauge: conduzir cenários por dados.
- [[gauge-environments-and-config]] — Veja também: Gauge: separar configuração por ambiente.

## Fontes
- [Gauge — Executar especificações](https://docs.gauge.org/execution) — ganchos, ambientes, etiquetas e execução paralela; consultado em 2026-10-03.
- [Gauge — Configuração](https://docs.gauge.org/configuration) — propriedades do projeto, ambientes e relatórios; consultado em 2026-10-03.
