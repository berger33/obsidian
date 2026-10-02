---
id: software.testes.tranche08.000246
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://docs.docker.com/build/building/best-practices/", "https://docs.docker.com/build/checks/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Docker: validar healthcheck sem confundi-lo com readiness

## Em uma frase
Teste o comando de healthcheck e diferencie saúde do processo de prontidão para receber tráfego.

## Por que importa
Container em execução pode não estar pronto; healthcheck mal calibrado pode marcar unhealthy serviço funcional ou saudável serviço sem dependência.

## Como funciona
Defina condição barata e representativa, configure intervalo e timeout conforme startup e conecte status ao orquestrador apropriado.

## Exemplo
Healthcheck aguarda endpoint local após inicialização e falha quando processo deixa de responder; readiness externa verifica dependências requeridas.

## Limites e trade-offs
Docker health status isolado não reinicia ou retira tráfego automaticamente em todo runtime; comportamento depende da plataforma que o consome.

## Como verificar
Teste startup lento, endpoint indisponível e processo encerrado; confira status e ação do orquestrador sem criar loop de carga.

## Conexões
- [[docker-image-test-smoke-entrypoint]] — Veja também: Docker: testar a imagem final com smoke test.
- [[android-test-flakiness-reproducao-dispositivo]] — Veja também: Android: tornar falhas instrumentadas reproduzíveis.

## Fontes
- [Docker — Building best practices](https://docs.docker.com/build/building/best-practices/) — multi-stage, pinning, cache e testes de imagens; consultado em 2026-10-02.
- [Docker — Build checks](https://docs.docker.com/build/checks/) — checks estáticos de Dockerfile durante build; consultado em 2026-10-02.
