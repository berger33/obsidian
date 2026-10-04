---
id: software.testes.tranche10.000400
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
fontes: ["https://java.testcontainers.org/features/startup_and_waits/", "https://java.testcontainers.org/test_framework_integration/junit_5/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Testcontainers: distinguir container iniciado de serviço pronto

## Em uma frase
Startup checks detectam o estado de inicialização do container; wait strategies aguardam uma condição de readiness do serviço.

## Por que importa
Testcontainers aproxima testes de integração de serviços reais, mas containers iniciados não significam necessariamente que o serviço já esteja pronto. Um processo pode estar em execução enquanto ainda aplica migrations ou recusa conexões.

## Como funciona
Declare imagem e lifecycle, aguarde um sinal de readiness adequado ao protocolo e isole recursos mutáveis entre casos e workers. Configure uma espera que observe o contrato usado pelo teste, como porta, endpoint HTTP, healthcheck ou mensagem de log.

## Exemplo
O container de banco abre a porta, mas o teste só conecta depois que a readiness indica aceitação de consultas.

## Limites e trade-offs
Integração com Docker, custo de recursos, versão de imagem e comportamento do framework influenciam a reprodutibilidade e a duração da suíte. Uma porta aberta não prova que o schema, usuário ou dependência esteja pronto para o cenário.

## Como verificar
Force inicialização lenta e confirme que o teste aguarda readiness e não depende de atraso fixo.

## Conexões
- [[testcontainers-wait-endpoint-readiness-contract]] — Veja também: Testcontainers: escolher wait strategy alinhada ao protocolo.

## Fontes
- [Testcontainers for Java — Startup and waits](https://java.testcontainers.org/features/startup_and_waits/) — startup checks e estratégias de espera por readiness; consultado em 2026-10-02.
- [Testcontainers for Java — JUnit 5 integration](https://java.testcontainers.org/test_framework_integration/junit_5/) — containers estáticos/de instância e limitações de paralelismo da extensão; consultado em 2026-10-02.
