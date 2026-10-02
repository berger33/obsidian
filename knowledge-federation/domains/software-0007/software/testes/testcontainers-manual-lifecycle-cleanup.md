---
id: software.testes.tranche10.000404
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
fontes: ["https://java.testcontainers.org/test_framework_integration/manual_lifecycle_control/", "https://java.testcontainers.org/test_framework_integration/junit_5/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Testcontainers: encerrar containers iniciados manualmente

## Em uma frase
Controle manual permite iniciar recursos fora do lifecycle automático de uma extensão e usá-los em escopo explícito.

## Por que importa
Testcontainers aproxima testes de integração de serviços reais, mas containers iniciados não significam necessariamente que o serviço já esteja pronto. Sem um owner claro, container pode permanecer ativo e manter estado entre testes ou execuções locais.

## Como funciona
Declare imagem e lifecycle, aguarde um sinal de readiness adequado ao protocolo e isole recursos mutáveis entre casos e workers. Use start e stop em fixture com teardown garantido, ou adote extensão consistente para o escopo da suíte.

## Exemplo
Um recurso compartilhado é iniciado uma vez pelo harness e parado em finally mesmo se uma assertion falhar.

## Limites e trade-offs
Integração com Docker, custo de recursos, versão de imagem e comportamento do framework influenciam a reprodutibilidade e a duração da suíte. Containers reutilizáveis experimentais têm regras diferentes e não devem ser encerrados como recurso manual comum.

## Como verificar
Induza exceção no setup e no teste e confirme que o teardown remove somente o container pertencente ao harness.

## Conexões
- [[testcontainers-junit5-parallel-extension-limit]] — Veja também: Testcontainers JUnit: não presumir paralelismo seguro da extensão.
- [[testcontainers-jdbc-url-configuracao-reprodutivel]] — Veja também: Testcontainers JDBC: declarar driver, banco e dados iniciais.

## Fontes
- [Testcontainers for Java — Manual lifecycle control](https://java.testcontainers.org/test_framework_integration/manual_lifecycle_control/) — controle explícito de start/stop e compartilhamento do ciclo de vida; consultado em 2026-10-02.
- [Testcontainers for Java — JUnit 5 integration](https://java.testcontainers.org/test_framework_integration/junit_5/) — containers estáticos/de instância e limitações de paralelismo da extensão; consultado em 2026-10-02.
