---
id: software.devops.tranche11.001006
tipo: tecnica
dominio: software
subdominio: devops
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-11.md"
fontes: ["https://www.keycloak.org/guides", "https://www.keycloak.org/server/configuration-production", "https://raw.githubusercontent.com/keycloak/keycloak/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Observabilidade no Keycloak: OpenTelemetry tracing, métricas de eventos, SLIs/SLOs, Exemplars e Java Flight Recorder

## Em uma frase
O Keycloak oferece uma pilha completa de observabilidade exposta em sua interface de gerenciamento isolada, abrangendo health checks REST, métricas Prometheus de sistema e de eventos de usuários, rastreamento distribuído via **OpenTelemetry**, correlação por **Exemplars**, dashboards Grafana oficiais e diagnóstico JVM com thread dumps e **Java Flight Recorder (JFR)**.

## Por que importa
Em uma plataforma onde todas as aplicações dependem do provedor de identidade para autenticar requisições, um aumento de latência no login ou uma taxa elevada de erros de token afeta toda a empresa. A correlação entre métricas de eventos de usuário, SLIs/SLOs e traces OpenTelemetry permite isolar rapidamente se o gargalo está no banco de dados, em um servidor LDAP federado lento ou na própria JVM.

## Como funciona
Conforme documentado na seção *Observability* do guia oficial (`keycloak.org/guides`), os operadores habilitam: (1) **Management Interface** separada da porta pública para servir `/health` e `/metrics` sem expor dados internos na internet; (2) **Event metrics**, que agregam atividades de usuários (logins bem-sucedidos, falhas de autenticação, emissões de token) como métricas Prometheus; (3) **OpenTelemetry tracing** e **Exemplars**, que vinculam picos de latência nos histogramas Prometheus diretamente ao trace ID da requisição lenta; e (4) ferramentas de perfilamento de baixo overhead como captura de thread dumps da JVM e gravações do **Java Flight Recorder (JFR)** para diagnosticar contenção de locks ou pressão de Garbage Collection.

## Exemplo
```bash
# Iniciar o Keycloak habilitando métricas, health checks e exportação de traces OpenTelemetry via OTLP
bin/kc.sh start \
  --health-enabled=true \
  --metrics-enabled=true \
  --tracing-enabled=true \
  --tracing-endpoint=http://otel-collector.monitoring:4317
```

## Limites e trade-offs
Habilitar métricas detalhadas de eventos de usuários com alta cardinalidade de labels (ou amostragem de 100% em tracing OpenTelemetry em clusters com milhares de logins por segundo) aumenta o consumo de memória e tráfego de rede; calibre a taxa de amostragem e restrinja o acesso à Management Interface exclusivamente ao scraper do Prometheus.

## Como verificar
Consulte `curl -s http://localhost:9000/metrics | grep keycloak_` para confirmar a exposição das métricas do servidor e o funcionamento da porta de gerenciamento.

## Conexões
- [[keycloak-operator-kubernetes-crds-realm-import-clients]] — Veja também: Keycloak Operator no Kubernetes: CRDs para implantação declarativa, importação de Realms e gestão de Clients.
- [[keycloak-padroes-modernos-seguranca-dpop-token-exchange-mcp]] — Veja também: Padrões avançados no Keycloak: DPoP, Token Exchange, JWT Authorization Grant, AuthZEN, SSF e servidores MCP.
- [[keycloak-protecao-sobrecarga-queued-requests-async-bootstrap]] — Referência cruzada direta com keycloak-protecao-sobrecarga-queued-requests-async-bootstrap.

## Fontes
- [Keycloak Official Documentation — Configuring Keycloak for production & Guides](https://www.keycloak.org/guides) — Guias oficiais de configuração do Keycloak para produção (TLS, Hostname v2, reverse proxy, http-max-queued-requests, --server-async-bootstrap, JGroups/Infinispan, Operator, OpenTelemetry e especificações modernas); consultado em 2026-10-03.
- [Keycloak GitHub — README.md & Official Documentation Portal](https://www.keycloak.org/server/configuration-production) — README oficial do projeto CNCF keycloak/keycloak (Apache-2.0) e índice de guias de servidor, operator, observabilidade e segurança de aplicações; consultado em 2026-10-03.
- [Keycloak — Official Guides & Server Reference](https://raw.githubusercontent.com/keycloak/keycloak/main/README.md) — Portal oficial de guias do Keycloak; consultado em 2026-10-03.
