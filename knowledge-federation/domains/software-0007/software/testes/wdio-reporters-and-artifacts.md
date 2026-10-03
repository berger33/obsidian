---
id: software.testes.tranche18.001174
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://webdriver.io/docs/gettingstarted", "https://github.com/webdriverio/webdriverio"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WebdriverIO: escolher relatórios e evidências

## Em uma frase
A suíte pode gerar relatórios em formatos diferentes, incluir capturas em falhas e publicar resultados para consumo no pipeline.

## Por que importa
Evidência organizada acelera a análise de falhas e mantém histórico comparável entre execuções.

## Como funciona
Declare o relatório principal, capture imagens apenas em falhas e preserve o diretório como artefato do trabalho.

## Exemplo
Um relatório com passo, mensagem de erro e captura permite entender a falha sem reproduzir a execução localmente.

## Limites e trade-offs
Relatórios muito detalhados crescem rapidamente e podem carregar dados sensíveis das telas capturadas.

## Como verificar
Gere o relatório de uma execução com falha controlada e confirme que o passo responsável aparece identificado.

## Conexões
- [[wdio-configuration]] — Veja também: WebdriverIO: estruturar a configuração.
- [[wdio-parallel-execution]] — Veja também: WebdriverIO: executar em paralelo.

## Fontes
- [WebdriverIO — Documentation](https://webdriver.io/docs/gettingstarted) — configuração, modos de execução, serviços e paralelismo; consultado em 2026-10-03.
- [WebdriverIO — repositório oficial](https://github.com/webdriverio/webdriverio) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
