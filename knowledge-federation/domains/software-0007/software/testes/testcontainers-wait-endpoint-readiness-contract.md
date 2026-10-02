---
id: software.testes.tranche10.000401
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-10.md"
fontes: ["https://java.testcontainers.org/features/startup_and_waits/", "https://java.testcontainers.org/modules/docker_compose/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Testcontainers: escolher wait strategy alinhada ao protocolo

## Em uma frase
A wait strategy pode observar condições diferentes, incluindo porta, resposta HTTP, healthcheck e logs.

## Por que importa
Testcontainers aproxima testes de integração de serviços reais, mas containers iniciados não significam necessariamente que o serviço já esteja pronto. Esperar apenas pelo processo pode liberar o teste antes de rota, banco ou broker aceitar o uso real.

## Como funciona
Declare imagem e lifecycle, aguarde um sinal de readiness adequado ao protocolo e isole recursos mutáveis entre casos e workers. Prefira a condição que represente a primeira operação do cliente e configure timeout compatível com a inicialização.

## Exemplo
Um serviço HTTP só libera o teste depois que GET /health responde sucesso com o estado esperado.

## Limites e trade-offs
Integração com Docker, custo de recursos, versão de imagem e comportamento do framework influenciam a reprodutibilidade e a duração da suíte. Health endpoint pode ficar saudável antes de dependências específicas ou dados de teste estarem disponíveis.

## Como verificar
Retarde a dependência e verifique que a readiness escolhida impede uma conexão prematura.

## Conexões
- [[testcontainers-startup-check-vs-readiness]] — Veja também: Testcontainers: distinguir container iniciado de serviço pronto.
- [[testcontainers-junit-static-vs-instance-containers]] — Veja também: Testcontainers JUnit: escolher container compartilhado ou por teste.

## Fontes
- [Testcontainers for Java — Startup and waits](https://java.testcontainers.org/features/startup_and_waits/) — startup checks e estratégias de espera por readiness; consultado em 2026-10-02.
- [Testcontainers for Java — Docker Compose module](https://java.testcontainers.org/modules/docker_compose/) — serviços Compose expostos e configuração de readiness; consultado em 2026-10-02.
