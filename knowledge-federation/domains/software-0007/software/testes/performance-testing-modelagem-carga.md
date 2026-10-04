---
id: software.testes.performance-load.000001
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
fontes: ["https://grafana.com/docs/k6/latest/testing-guides/api-load-testing/", "https://sre.google/sre-book/service-best-practices/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Performance testing, Load testing, Teste de carga, Teste de desempenho]
lote: software-testes-2000-0001
---

# Performance testing com modelagem de carga

## Em uma frase
Teste de desempenho avalia cenários, carga e critérios de serviço para verificar como latência, erros, disponibilidade e recursos se comportam sob condições definidas.

## Por que importa
Uma aplicação pode responder corretamente com poucas requisições e degradar sob a carga de produção. Testes de carga ajudam a avaliar capacidade, identificar gargalos e verificar objetivos de confiabilidade antes de depender somente de previsões ou incidentes. A validade do resultado depende de representar tanto fluxos de usuários quanto padrões de tráfego relevantes.

## Como funciona
A documentação k6 recomenda começar pelo objetivo: componente ou fluxo, forma de execução e critério de desempenho aceitável. Tipos incluem smoke com carga mínima, carga média, stress acima do usual, spike com aumento repentino, breakpoint para localizar limites e soak de longa duração. Google SRE recomenda load testing para relacionar recursos e capacidade em vez de presumir que medidas antigas continuam válidas. Um modelo pode usar usuários virtuais ou taxa de chegada, mas precisa representar a mistura e duração esperadas.

## Exemplo
Para checkout, teste primeiro um fluxo isolado com carga mínima, depois tráfego esperado e, em ensaio autorizado, um pico plausível. Defina limiares de latência percentil, erros e disponibilidade alinhados ao SLO; durante um soak, observe degradação temporal e consumo de memória. Registre o perfil de carga, dados, versão e limites do gerador.

## Limites e trade-offs
Ambiente de teste, cache, aquecimento, gerador saturado e dependências externas podem distorcer resultados. Uma taxa fixa de requisições não representa necessariamente usuários reais, e alta carga indiscriminada pode afetar serviços compartilhados. Um resultado isolado não garante capacidade futura quando código, tráfego ou infraestrutura mudam.

## Como verificar
Confirme que o gerador não é gargalo, que a carga representa cenários e que os thresholds refletem objetivos de usuários. Registre percentis, erros, throughput e recursos, incluindo versão e configuração. Repita após mudanças relevantes e compare séries compatíveis; evite comparar números obtidos com workloads ou ambientes diferentes como se fossem equivalentes.

## Conexões
- [[testes-hermeticos-dependencias]] — dependências externas e ambientes variáveis afetam reprodutibilidade e resultado.
- [[testes-flaky-determinismo]] — ruído e variância podem ser confundidos com regressão de desempenho.
- [[chaos-experiments-steady-state-blast-radius]] — carga e falhas podem ser combinadas em ensaios controlados de resiliência.

## Fontes
- [Grafana k6 — API load testing](https://grafana.com/docs/k6/latest/testing-guides/api-load-testing/) — planejamento de objetivo, perfil de carga e tipos de ensaio; acesso em 2026-10-01.
- [Google SRE — Production Services Best Practices](https://sre.google/sre-book/service-best-practices/) — uso de load testing para estabelecer capacidade e práticas operacionais; acesso em 2026-10-01.
