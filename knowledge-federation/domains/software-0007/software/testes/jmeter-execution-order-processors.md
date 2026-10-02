---
id: software.testes.tranche11.000526
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

# JMeter: respeitar ordem de config, preprocessors, sampler e assertions

## Em uma frase
JMeter processa elementos da árvore em ordem definida, com configuration elements e preprocessors antes do sampler e postprocessors/assertions depois.

## Por que importa
JMeter executa uma árvore ordenada de samplers e elementos hierárquicos; escopo de threads, timers, assertions e dados determina que requests cada elemento realmente afeta. Extractor que executa depois do sampler não pode fornecer variável a esse mesmo request, e assertion pode ler resultado posterior.

## Como funciona
Crie ou depure o plano em GUI, execute carga em CLI, reutilize dados controlados e limite listeners/assertions ao objetivo de medição; registre plano, propriedades e arquivo de resultado. Coloque preparação e extração nos elementos corretos da sequência e confira parent/child scope de cada um.

## Exemplo
Post-processor extrai id da resposta de login para o próximo sampler, não para o request de login que já foi enviado.

## Limites e trade-offs
Árvore de JMeter pode gerar tráfego diferente do esperado por escopo ou ordem. GUI, listeners e gerador limitado podem alterar medidas, e propriedades globais têm compartilhamento mais amplo que variáveis de thread. Sub-samples e controllers podem alterar qual resultado o processor ou assertion recebe.

## Como verificar
Use Debug Sampler ou resultado do teste para inspecionar variável em cada fronteira da execução.

## Conexões
- [[jmeter-cli-para-carga-gui-para-debug]] — Veja também: JMeter: usar GUI para depurar e CLI para medir carga.
- [[jmeter-listeners-impacto-gerador]] — Veja também: JMeter: limitar listeners pesados durante execução de carga.

## Fontes
- [Apache JMeter — Elements of a Test Plan](https://jmeter.apache.org/usermanual/test_plan.html) — Thread Groups, timers, assertions, execução e regras de escopo; consultado em 2026-10-02.
- [Apache JMeter — Component Reference](https://jmeter.apache.org/usermanual/component_reference.html) — CSV Data Set, assertions, timers, extractors e controllers; consultado em 2026-10-02.
