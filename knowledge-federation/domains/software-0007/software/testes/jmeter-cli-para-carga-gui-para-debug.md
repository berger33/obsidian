---
id: software.testes.tranche11.000525
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
fontes: ["https://jmeter.apache.org/usermanual/get-started.html", "https://jmeter.apache.org/usermanual/build-test-plan.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JMeter: usar GUI para depurar e CLI para medir carga

## Em uma frase
Manual recomenda GUI para criar/debuggar plano e CLI mode para load test com menor overhead de interface.

## Por que importa
JMeter executa uma árvore ordenada de samplers e elementos hierárquicos; escopo de threads, timers, assertions e dados determina que requests cada elemento realmente afeta. Executar grande carga em GUI pode consumir recursos do mesmo processo e distorcer resultado ou tornar máquina de geração o gargalo.

## Como funciona
Crie ou depure o plano em GUI, execute carga em CLI, reutilize dados controlados e limite listeners/assertions ao objetivo de medição; registre plano, propriedades e arquivo de resultado. Valide plano com poucos usuários e debugging visual, depois execute `-n -t` com arquivo de resultado e opções controladas.

## Exemplo
Pipeline roda `jmeter -n -t plan.jmx -l results.jtl` e arquiva log/resultados após confirmar exit code.

## Limites e trade-offs
Árvore de JMeter pode gerar tráfego diferente do esperado por escopo ou ordem. GUI, listeners e gerador limitado podem alterar medidas, e propriedades globais têm compartilhamento mais amplo que variáveis de thread. Modo CLI não corrige plano errado nem elimina listeners custosos ou limites de hardware.

## Como verificar
Compare execução de fumaça em GUI com execução headless curta e confira amostras, assertions e códigos de saída.

## Conexões
- [[jmeter-thread-variables-properties-compartilhamento]] — Veja também: JMeter: distinguir variáveis de thread de propriedades compartilhadas.
- [[jmeter-execution-order-processors]] — Veja também: JMeter: respeitar ordem de config, preprocessors, sampler e assertions.

## Fontes
- [Apache JMeter — Getting Started](https://jmeter.apache.org/usermanual/get-started.html) — modo CLI para load tests e opções de execução; consultado em 2026-10-02.
- [Apache JMeter — Building a Test Plan](https://jmeter.apache.org/usermanual/build-test-plan.html) — edição/debug em GUI, execução em CLI e elementos do plano; consultado em 2026-10-02.
