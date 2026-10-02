---
id: software.testes.tranche11.000522
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
fontes: ["https://jmeter.apache.org/usermanual/test_plan.html", "https://jmeter.apache.org/usermanual/component_reference.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JMeter: limitar Assertion ao sampler que representa o contrato

## Em uma frase
Assertions são executadas após samplers no escopo onde aparecem e verificam campos de request/response configurados.

## Por que importa
JMeter executa uma árvore ordenada de samplers e elementos hierárquicos; escopo de threads, timers, assertions e dados determina que requests cada elemento realmente afeta. Assertion em controller amplo pode avaliar samplers auxiliares, confundindo resultados e inflando failures.

## Como funciona
Crie ou depure o plano em GUI, execute carga em CLI, reutilize dados controlados e limite listeners/assertions ao objetivo de medição; registre plano, propriedades e arquivo de resultado. Aninhe assertion sob sampler específico ou use controller com descendentes intencionais e escolha explicitamente o campo avaliado.

## Exemplo
Response Assertion verifica código e texto de GET /health sem ser aplicada ao login e ao download de fixture.

## Limites e trade-offs
Árvore de JMeter pode gerar tráfego diferente do esperado por escopo ou ordem. GUI, listeners e gerador limitado podem alterar medidas, e propriedades globais têm compartilhamento mais amplo que variáveis de thread. Assertion de texto não substitui parsing JSON/schema e status HTTP pode ter regra própria no sampler.

## Como verificar
Introduza falha somente no sampler alvo e confirme que nenhuma assertion de outro ramo é disparada.

## Conexões
- [[jmeter-timer-before-samplers-scope]] — Veja também: JMeter: lembrar que timers atrasam samplers dentro de seu escopo.
- [[jmeter-csv-dataset-dados-por-thread]] — Veja também: JMeter: entender leitura CSV por thread e iteração.

## Fontes
- [Apache JMeter — Elements of a Test Plan](https://jmeter.apache.org/usermanual/test_plan.html) — Thread Groups, timers, assertions, execução e regras de escopo; consultado em 2026-10-02.
- [Apache JMeter — Component Reference](https://jmeter.apache.org/usermanual/component_reference.html) — CSV Data Set, assertions, timers, extractors e controllers; consultado em 2026-10-02.
