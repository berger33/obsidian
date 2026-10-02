---
id: software.testes.tranche10.000403
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
fontes: ["https://java.testcontainers.org/test_framework_integration/junit_5/", "https://java.testcontainers.org/features/advanced_options/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Testcontainers JUnit: não presumir paralelismo seguro da extensão

## Em uma frase
A integração JUnit Jupiter de Testcontainers documenta que execução paralela não é suportada pela extensão.

## Por que importa
Testcontainers aproxima testes de integração de serviços reais, mas containers iniciados não significam necessariamente que o serviço já esteja pronto. Ativar concorrência no runner pode provocar disputa de lifecycle, recurso ou estado sem sincronização apropriada.

## Como funciona
Declare imagem e lifecycle, aguarde um sinal de readiness adequado ao protocolo e isole recursos mutáveis entre casos e workers. Mantenha execução serial para essa integração até validar o suporte da versão adotada e a estratégia de isolamento escolhida.

## Exemplo
A suíte marca a classe que compartilha containers para execução serial e roda testes independentes em outro job sem extensão compartilhada.

## Limites e trade-offs
Integração com Docker, custo de recursos, versão de imagem e comportamento do framework influenciam a reprodutibilidade e a duração da suíte. Containers independentes ainda consomem CPU, memória e portas; serializar a extensão não remove todo risco de recursos.

## Como verificar
Inspecione as propriedades de paralelismo efetivas do runner e observe logs de start/stop sob a configuração real de CI.

## Conexões
- [[testcontainers-junit-static-vs-instance-containers]] — Veja também: Testcontainers JUnit: escolher container compartilhado ou por teste.
- [[testcontainers-manual-lifecycle-cleanup]] — Veja também: Testcontainers: encerrar containers iniciados manualmente.

## Fontes
- [Testcontainers for Java — JUnit 5 integration](https://java.testcontainers.org/test_framework_integration/junit_5/) — containers estáticos/de instância e limitações de paralelismo da extensão; consultado em 2026-10-02.
- [Testcontainers for Java — Advanced options](https://java.testcontainers.org/features/advanced_options/) — opções de inicialização e limites de recursos dos containers; consultado em 2026-10-02.
