---
id: software.testes.tranche20.001363
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

# Gauge: preparar estado com ganchos e contexto

## Em uma frase
A execução oferece ganchos de suíte, especificação, cenário e passo, e um contexto próprio para guardar valores entre passos.

## Por que importa
A preparação no nível certo evita repetição e mantém os passos focados na verificação em vez de na infraestrutura.

## Como funciona
Registre a preparação mais ampla no gancho de suíte, o estado por cenário no gancho correspondente e limpe os recursos ao final.

## Exemplo
O navegador pode abrir uma vez por suíte e cada cenário receber dados próprios, com captura de tela em caso de falha.

## Limites e trade-offs
Ganchos pesados por passo alongam a execução, e estado guardado no contexto sem limpeza vaza entre cenários.

## Como verificar
Desative temporariamente um gancho de limpeza e confirme que a suíte passa a falhar por dado residual.

## Conexões
- [[gauge-tags-and-filtering]] — Veja também: Gauge: selecionar execuções por etiquetas.
- [[gauge-data-driven]] — Veja também: Gauge: conduzir cenários por dados.

## Fontes
- [Gauge — Executar especificações](https://docs.gauge.org/execution) — ganchos, ambientes, etiquetas e execução paralela; consultado em 2026-10-03.
- [Gauge — Configuração](https://docs.gauge.org/configuration) — propriedades do projeto, ambientes e relatórios; consultado em 2026-10-03.
