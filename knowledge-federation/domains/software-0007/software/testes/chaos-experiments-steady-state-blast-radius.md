---
id: software.testes.chaos-engineering.000001
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001.md"
fontes: ["https://principlesofchaos.org/", "https://netflixtechblog.com/chap-chaos-automation-platform-53e6d528371f", "https://docs.aws.amazon.com/fis/latest/userguide/experiment-templates.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Chaos engineering, Chaos experiment, Engenharia do caos, Injeção de falhas]
lote: software-testes-2000-0001
---

# Chaos experiments com steady state e blast radius

## Em uma frase
Chaos engineering executa experimentos controlados com falhas realistas para descobrir fragilidades sistêmicas antes que se manifestem como incidentes amplos.

## Por que importa
Em sistemas distribuídos, componentes podem parecer saudáveis isoladamente enquanto interações, dependências ou eventos raros causam degradação em cadeia. Um experimento permite avaliar resiliência com observação e hipótese explícitas, em vez de assumir que redundância ou documentação de arquitetura garantem recuperação.

## Como funciona
Os Principles of Chaos propõem medir um steady state, formular hipótese para grupos de controle e experimento, introduzir variáveis que representem eventos reais e procurar diferenças na saída mensurável. Métricas podem incluir throughput, erros e percentis de latência. O AWS Fault Injection Service modela experimentos com ações, alvos e stop conditions baseadas em alarmes; quando o limite é atingido, a execução é interrompida. O blast radius deve ser limitado e compatível com autorização, maturidade e risco operacional.

## Exemplo
Hipótese: interromper uma instância de uma dependência não deve reduzir a taxa de sucesso do fluxo de leitura abaixo do SLO porque outra réplica assume o tráfego. Defina a instância-alvo, duração, tráfego, métricas e alarme de parada antes de injetar a falha; compare comportamento observado e controle, reverta e registre discrepâncias.

## Limites e trade-offs
Experimentos podem causar impacto real; controles insuficientes, hipóteses vagas e observabilidade ruim tornam o risco desnecessário e os resultados inconclusivos. Um experimento que não rompe o steady state só dá evidência para os cenários, escala e janela testados. “Rodar em produção” não é regra automática: escopo, autorização, salvaguardas e prontidão precisam ser avaliados.

## Como verificar
Revise a hipótese com responsáveis pelo serviço, determine limites automáticos de parada e plano de recuperação, confirme telemetria e alvo exato. Comece pelo menor escopo viável; interrompa se houver impacto acima do aceito. Após o teste, confronte métricas com o steady state, registre aprendizado e repita só após corrigir falhas relevantes.

## Conexões
- [[testes-hermeticos-dependencias]] — controlabilidade do ambiente ajuda a interpretar ensaios.
- [[performance-testing-modelagem-carga]] — carga é um estímulo possível para experimentar resiliência.
- [[risk-based-testing-priorizacao-risco]] — prioriza cenários e limita o impacto aceitável.

## Fontes
- [Principles of Chaos Engineering](https://principlesofchaos.org/) — steady state, hipótese e eventos realistas; acesso em 2026-10-01.
- [Netflix TechBlog — ChAP: Chaos Automation Platform](https://netflixtechblog.com/chap-chaos-automation-platform-53e6d528371f) — exemplo de comparação entre grupos de controle e experimento, limite de blast radius e parada automática por orçamento de erro; acesso em 2026-10-01.
- [AWS FIS — Experiment template components](https://docs.aws.amazon.com/fis/latest/userguide/experiment-templates.html) — ações, alvos e stop conditions de experimentos; acesso em 2026-10-01.
