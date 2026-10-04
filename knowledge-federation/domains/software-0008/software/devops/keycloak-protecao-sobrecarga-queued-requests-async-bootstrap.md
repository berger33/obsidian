---
id: software.devops.tranche11.001003
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

# Keycloak: proteção contra sobrecarga (http-max-queued-requests) e inicialização assíncrona (--server-async-bootstrap)

## Em uma frase
O Keycloak protege instâncias produtivas contra exaustão em picos de tráfego por meio do limite de enfileiramento `--http-max-queued-requests` (load shedding com HTTP `503`) e evita que o Kubernetes mate containers durante migrações longas de banco de dados graças ao bootstrap assíncrono com endpoints de saúde independentes (`/health/ready`).

## Por que importa
Em tempestades de reconexão (quando milhares de clientes tentam renovar tokens simultaneamente), aceitar requisições infinitamente na fila esgota a memória da JVM e derruba todo o cluster. Da mesma forma, em upgrades de versão com esquemas de banco extensos, se o servidor demorar minutos para abrir a porta de gerenciamento, o `startupProbe`/`livenessProbe` do Kubernetes reiniciará o pod em loop antes do término da migração.

## Como funciona
Conforme detalha a documentação oficial de produção: (1) a opção **`http-max-queued-requests`** limita quantas requisições HTTP que não puderam ser processadas imediatamente aguardam em fila; qualquer requisição acima desse limiar é rejeitada imediatamente com **`503 Server not Available`**, preservando a capacidade de resposta para requisições válidas; e (2) quando os endpoints de health check estão habilitados, o Keycloak abre as portas HTTP(S) e de gerenciamento logo no início enquanto a inicialização (como migrações de banco) avança em background — reportando `UP` nas probes de startup/liveness e `DOWN` em **`/health/ready`** até a conclusão. Se um health check HTTP não puder ser usado no balanceador, pode-se desativar esse comportamento com `--server-async-bootstrap=false`.

## Exemplo
```bash
# Iniciar o Keycloak com limite de requisições enfileiradas (load shedding) e health checks ativos
bin/kc.sh start \
  --http-max-queued-requests=200 \
  --health-enabled=true \
  --metrics-enabled=true
```

## Limites e trade-offs
Com o bootstrap assíncrono padrão ativo, um balanceador de carga configurado apenas com verificação de porta TCP (em vez de checar explicitamente o caminho HTTP `/health/ready` na interface de gerenciamento) roteará tráfego de usuários para instâncias que ainda estão executando migrações de banco; nesses casos, configure `/health/ready` ou passe `--server-async-bootstrap=false`.

## Como verificar
Durante a inicialização do servidor, consulte a porta de gerenciamento (padrão `9000`) em `curl -i http://localhost:9000/health/live` e `curl -i http://localhost:9000/health/ready` para observar a diferença entre liveness (`200`) e readiness.

## Conexões
- [[keycloak-configuracao-producao-tls-hostname-v2-reverse-proxy]] — Veja também: Keycloak em produção: TLS, Hostname v2, separação da URL administrativa e configuração de Reverse Proxy.
- [[keycloak-cluster-alta-disponibilidade-infinispan-jgroups-banco]] — Veja também: Keycloak em cluster de alta disponibilidade: JGroups, caches distribuídos Infinispan, banco relacional e pilha IPv4/IPv6.
- [[keycloak-observabilidade-opentelemetry-metricas-sli-jfr]] — Referência cruzada direta com keycloak-observabilidade-opentelemetry-metricas-sli-jfr.

## Fontes
- [Keycloak Official Documentation — Configuring Keycloak for production & Guides](https://www.keycloak.org/server/configuration-production) — Guias oficiais de configuração do Keycloak para produção (TLS, Hostname v2, reverse proxy, http-max-queued-requests, --server-async-bootstrap, JGroups/Infinispan, Operator, OpenTelemetry e especificações modernas); consultado em 2026-10-03.
- [Keycloak GitHub — README.md & Official Documentation Portal](https://www.keycloak.org/guides) — README oficial do projeto CNCF keycloak/keycloak (Apache-2.0) e índice de guias de servidor, operator, observabilidade e segurança de aplicações; consultado em 2026-10-03.
- [Keycloak — Official Guides & Server Reference](https://raw.githubusercontent.com/keycloak/keycloak/main/README.md) — Portal oficial de guias do Keycloak; consultado em 2026-10-03.
