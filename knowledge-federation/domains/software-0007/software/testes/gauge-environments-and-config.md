---
id: software.testes.tranche20.001366
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
fontes: ["https://docs.gauge.org/configuration", "https://docs.gauge.org/execution"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gauge: separar configuração por ambiente

## Em uma frase
O projeto mantém diretórios de ambiente com arquivos de propriedades, e uma execução escolhe o ambiente pelo nome.

## Por que importa
A separação evita endereços e credenciais fixos nos passos e permite a mesma suíte rodar em contextos distintos.

## Como funciona
Mantenha o padrão no diretório padrão, declare diferenças por ambiente e passe o nome escolhido na execução.

## Exemplo
O endereço do serviço pode vir do ambiente de teste local e o endereço de homologação do ambiente correspondente.

## Limites e trade-offs
Valores sensíveis versionados no diretório de ambiente expõem credenciais, e propriedades divergentes entre ambientes geram falhas que só aparecem na esteira.

## Como verificar
Troque o ambiente da execução e confirme que os passos usam os valores declarados no arquivo correspondente.

## Conexões
- [[gauge-parallel-execution]] — Veja também: Gauge: executar em fluxos paralelos.
- [[gauge-reports-and-ci]] — Veja também: Gauge: publicar relatórios na esteira.

## Fontes
- [Gauge — Configuração](https://docs.gauge.org/configuration) — propriedades do projeto, ambientes e relatórios; consultado em 2026-10-03.
- [Gauge — Executar especificações](https://docs.gauge.org/execution) — ganchos, ambientes, etiquetas e execução paralela; consultado em 2026-10-03.
