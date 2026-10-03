---
id: software.devops.tranche11.001004
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
fontes: ["https://www.keycloak.org/server/configuration-production", "https://www.keycloak.org/guides", "https://raw.githubusercontent.com/keycloak/keycloak/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Keycloak em cluster de alta disponibilidade: JGroups, caches distribuídos Infinispan, banco relacional e pilha IPv4/IPv6

## Em uma frase
Em implantações de alta disponibilidade com duas ou mais réplicas, o Keycloak persiste dados de usuários, clientes e realms em um banco de dados relacional de nível produtivo e sincroniza sessões e caches em memória entre os nós usando **Infinispan** e **JGroups** com criptografia TLS por padrão.

## Por que importa
Se uma instância do Keycloak falhar durante o horário comercial, os usuários autenticados não podem perder suas sessões nem ficar impedidos de emitir novos tokens. A combinação de banco relacional compartilhado com caches distribuídos garante continuidade de serviço e evita leituras repetitivas ao banco em cada validação de token.

## Como funciona
Segundo o guia *Configuring Keycloak for production*, o cluster Keycloak apoia-se em **JGroups** (descoberta e transporte de mensagens entre membros do cluster) e **Infinispan** (cache distribuído e replicado), mantendo a comunicação entre nós criptografada com TLS na configuração padrão. Por padrão, o Keycloak aceita conexões IPv4 e IPv6 simultaneamente, mas para formar clusters determinísticos em redes exclusivamente IPv4 ou IPv6 a documentação orienta ajustar as propriedades da JVM via `JAVA_OPTS_APPEND` (`-Djava.net.preferIPv4Stack=true` para IPv4 puro, ou `-Djava.net.preferIPv4Stack=false -Djava.net.preferIPv6Addresses=true` para IPv6 puro) e liberar as portas de rede exigidas pelos caches distribuídos no firewall/NetworkPolicy.

## Exemplo
```bash
# Configurar preferência estrita por pilha IPv4 via JAVA_OPTS_APPEND e iniciar nó em cluster com PostgreSQL
export JAVA_OPTS_APPEND="-Djava.net.preferIPv4Stack=true"
bin/kc.sh start \
  --db=postgres \
  --db-url=jdbc:postgresql://pg-ha.interno:5432/keycloak \
  --db-username=keycloak \
  --db-password="${KC_DB_PASSWORD}" \
  --cache=ispn
```

## Limites e trade-offs
Se as portas de comunicação do JGroups/Infinispan estiverem bloqueadas entre os pods por uma NetworkPolicy restritiva ou se houver mistura inconsistente de resolução IPv4/IPv6 entre os nós, cada réplica formará um cluster isolado de um único nó (*split-brain*), causando invalidação intermitente de sessões e falhas no fluxo de login.

## Como verificar
Verifique nos logs de inicialização do Keycloak a mensagem do JGroups confirmando a visão do cluster (`Received new cluster view` com o número esperado de membros ativos) e consulte as métricas de cache na interface de gerenciamento.

## Conexões
- [[keycloak-protecao-sobrecarga-queued-requests-async-bootstrap]] — Veja também: Keycloak: proteção contra sobrecarga (http-max-queued-requests) e inicialização assíncrona (--server-async-bootstrap).
- [[keycloak-operator-kubernetes-crds-realm-import-clients]] — Veja também: Keycloak Operator no Kubernetes: CRDs para implantação declarativa, importação de Realms e gestão de Clients.
- [[keycloak-configuracao-producao-tls-hostname-v2-reverse-proxy]] — Referência cruzada direta com keycloak-configuracao-producao-tls-hostname-v2-reverse-proxy.

## Fontes
- [Keycloak Official Documentation — Configuring Keycloak for production & Guides](https://www.keycloak.org/server/configuration-production) — Guias oficiais de configuração do Keycloak para produção (TLS, Hostname v2, reverse proxy, http-max-queued-requests, --server-async-bootstrap, JGroups/Infinispan, Operator, OpenTelemetry e especificações modernas); consultado em 2026-10-03.
- [Keycloak GitHub — README.md & Official Documentation Portal](https://www.keycloak.org/guides) — README oficial do projeto CNCF keycloak/keycloak (Apache-2.0) e índice de guias de servidor, operator, observabilidade e segurança de aplicações; consultado em 2026-10-03.
- [Keycloak — Official Guides & Server Reference](https://raw.githubusercontent.com/keycloak/keycloak/main/README.md) — Portal oficial de guias do Keycloak; consultado em 2026-10-03.
