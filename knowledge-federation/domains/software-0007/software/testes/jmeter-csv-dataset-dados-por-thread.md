---
id: software.testes.tranche11.000523
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
fontes: ["https://jmeter.apache.org/usermanual/component_reference.html", "https://jmeter.apache.org/usermanual/best-practices.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JMeter: entender leitura CSV por thread e iteração

## Em uma frase
CSV Data Set Config lê registros em variáveis e normalmente fornece linhas diferentes às threads do plano.

## Por que importa
JMeter executa uma árvore ordenada de samplers e elementos hierárquicos; escopo de threads, timers, assertions e dados determina que requests cada elemento realmente afeta. Usar a mesma conta para muitos usuários pode causar conflito e medir contenção artificial em vez do comportamento pretendido.

## Como funciona
Crie ou depure o plano em GUI, execute carga em CLI, reutilize dados controlados e limite listeners/assertions ao objetivo de medição; registre plano, propriedades e arquivo de resultado. Forneça dados descartáveis únicos por thread, configure delimiter e política de EOF e verifique volume suficiente para iterações.

## Exemplo
Arquivo contém header user_id; com campo Variable Names vazio JMeter usa primeira linha como nomes e distribui dados.

## Limites e trade-offs
Árvore de JMeter pode gerar tráfego diferente do esperado por escopo ou ordem. GUI, listeners e gerador limitado podem alterar medidas, e propriedades globais têm compartilhamento mais amplo que variáveis de thread. Ordem em que linhas chegam a threads depende do scheduler e execução, não use arquivo como garantia de ordenação entre usuários.

## Como verificar
Registre ids usados em amostra e confirme ausência de repetição conforme política de recycle/EOF.

## Conexões
- [[jmeter-assertion-aplica-por-escopo]] — Veja também: JMeter: limitar Assertion ao sampler que representa o contrato.
- [[jmeter-thread-variables-properties-compartilhamento]] — Veja também: JMeter: distinguir variáveis de thread de propriedades compartilhadas.

## Fontes
- [Apache JMeter — Component Reference](https://jmeter.apache.org/usermanual/component_reference.html) — CSV Data Set, assertions, timers, extractors e controllers; consultado em 2026-10-02.
- [Apache JMeter — Best Practices](https://jmeter.apache.org/usermanual/best-practices.html) — uso de CSV, redução de recursos e execução eficiente de carga; consultado em 2026-10-02.
