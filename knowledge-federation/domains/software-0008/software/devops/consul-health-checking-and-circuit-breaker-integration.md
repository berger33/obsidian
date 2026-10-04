---
id: software.devops.tranche06.000582
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/hashicorp/consul/main/README.md", "https://developer.hashicorp.com/consul/docs", "https://github.com/hashicorp/consul"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Verificação ativa de saúde (Health Checking), prevenção de roteamento para nós falhos e Circuit Breakers no Consul

## Em uma frase
O segundo pilar central documentado no README oficial é o **Health Checking**: o Consul executa verificações contínuas de saúde (no nível do nó e no nível de cada serviço/instância via HTTP, TCP, gRPC, script ou TTL) para alertar rapidamente os operadores sobre qualquer problema no cluster. Mais importante ainda, a **integração direta entre Health Checking e Service Discovery impede que o tráfego seja roteado para hosts não saudáveis** e habilita **circuit breakers no nível de serviço**.

## Por que importa
Um catálogo de serviços que sabe onde um processo foi iniciado mas não verifica continuamente se ele está respondendo saudável acaba enviando tráfego de clientes para processos travados (*deadlock*) ou com banco desconectado. No Consul, assim que um health check falha, a instância é automaticamente removida das respostas DNS e do pool de endpoints da Service Mesh.

## Como funciona
Defina sempre pelo menos um health check específico de aplicação (HTTP `/healthz`, gRPC Health Checking Protocol ou TCP) ao registrar qualquer serviço no Consul, combinando-o com configurações de circuit breaking e limites de conexões na malha de serviços.

## Exemplo
Quando uma das três instâncias do serviço de pagamentos começa a retornar erro HTTP 500 no endpoint de health check, o agente local do Consul marca a checagem como `critical` e o catálogo para imediatamente de entregar o IP daquela instância nas consultas DNS e nos proxies Envoy da malha.

## Limites e trade-offs
Evite health checks que façam consultas pesadas em cascata sobre todos os bancos de dados e serviços vizinhos a cada 2 segundos, pois uma lentidão momentânea em uma dependência secundária poderia fazer todas as réplicas da sua API se declararem `critical` ao mesmo tempo (falha em cascata).

## Como verificar
Inspecione o status das verificações de saúde na API (`/v1/health/state/any`) ou na UI web do Consul e confirme que todas as instâncias produtivas estão com status `passing`.

## Conexões
- [[consul-service-discovery-via-dns-and-http-interfaces]] — Veja também: Descoberta de serviços (Service Discovery) via interfaces DNS e HTTP e registro de serviços externos no Consul.
- [[consul-consul-service-mesh-mtls-and-transparent-proxy]] — Veja também: Consul Service Mesh: criptografia mTLS automática, autorização baseada em identidade (Intentions) e Transparent Proxy.

## Fontes
- [HashiCorp Consul GitHub — README.md (Multi-Datacenter, Service Mesh, API Gateway, Service Discovery, Health Checking, KV & BUSL-1.1)](https://raw.githubusercontent.com/hashicorp/consul/main/README.md) — README oficial do HashiCorp Consul (licenciado sob BUSL-1.1) detalhando operação distribuída multi-datacenter, Consul Service Mesh (mTLS automático, autorização baseada em identidade e Transparent Proxy), Consul API Gateway, Service Discovery via DNS e HTTP (incluindo serviços externos/SaaS), Health Checking com circuit breakers, Dynamic App Configuration via HTTP API, suporte a Linux/macOS/FreeBSD/Solaris/Windows e divulgação de segurança para security@hashicorp.com.; consultado em 2026-10-03.
- [HashiCorp Consul Official Documentation — Concepts & Architecture](https://developer.hashicorp.com/consul/docs) — Documentação oficial completa do HashiCorp Consul para VMs, Kubernetes (Minikube, Kind, produção) e HCP Consul.; consultado em 2026-10-03.
- [HashiCorp Consul — Official GitHub Repository](https://github.com/hashicorp/consul) — Repositório oficial do HashiCorp Consul.; consultado em 2026-10-03.
