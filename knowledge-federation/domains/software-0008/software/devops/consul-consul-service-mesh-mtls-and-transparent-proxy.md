---
id: software.devops.tranche06.000583
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

# Consul Service Mesh: criptografia mTLS automática, autorização baseada em identidade (Intentions) e Transparent Proxy

## Em uma frase
Conforme descreve o README oficial, o **Consul Service Mesh** (historicamente conhecido como Consul Connect) habilita comunicação segura serviço-para-serviço com **criptografia TLS mútua (mTLS) automática** e **autorização baseada em identidade** (independente de endereço IP, através de *Service Intentions*). As aplicações utilizam proxies sidecar (tipicamente Envoy) na configuração de service mesh para estabelecer conexões TLS de entrada (inbound) e de saída (outbound) de forma transparente com o modo **Transparent Proxy**.

## Por que importa
Em redes cloud e híbridas onde múltiplos serviços compartilham sub-redes, firewalls tradicionais baseados em IP/porta são difíceis de manter quando IPs mudam a cada minuto. Na Consul Service Mesh, cada serviço recebe um certificado TLS X.509 com identidade SPIFFE emitido pelo Consul e as políticas dizem simplesmente: *"o serviço `checkout` pode chamar o serviço `pagamentos`, mas o serviço `catalogo` não pode"*.

## Como funciona
Habilite o Consul Service Mesh com **Transparent Proxy** nos seus pods Kubernetes ou máquinas virtuais para que chamadas de saída para nomes de serviço da malha sejam interceptadas automaticamente pelo sidecar proxy, autenticadas via mTLS e validadas contra as *Service Intentions*.

## Exemplo
Com Transparent Proxy ativo e a política padrão *deny-all* configurada nas Intentions, o serviço `web` faz uma chamada HTTP comum para `api.virtual.consul`; o sidecar proxy intercepta a chamada, estabelece mTLS com o sidecar de `api` e o acesso só é permitido após a criação da Intention explícita `web -> api: allow`.

## Limites e trade-offs
Antes de mudar a política padrão de Intentions de `allow` para `deny` em um cluster existente, audite o grafo de tráfego na UI/métricas do Consul para cadastrar previamente todas as Intentions legítimas entre os serviços em produção.

## Como verificar
Verifique no painel do Consul ou via CLI (`consul intention check web api`) que a política de autorização entre dois serviços está ativa e que o certificado mTLS foi emitido para os sidecars.

## Conexões
- [[consul-health-checking-and-circuit-breaker-integration]] — Veja também: Verificação ativa de saúde (Health Checking), prevenção de roteamento para nós falhos e Circuit Breakers no Consul.
- [[consul-consul-api-gateway-north-south-traffic-and-policies]] — Veja também: Gerenciamento de tráfego de entrada (Norte-Sul) e políticas de acesso com Consul API Gateway.

## Fontes
- [HashiCorp Consul GitHub — README.md (Multi-Datacenter, Service Mesh, API Gateway, Service Discovery, Health Checking, KV & BUSL-1.1)](https://raw.githubusercontent.com/hashicorp/consul/main/README.md) — README oficial do HashiCorp Consul (licenciado sob BUSL-1.1) detalhando operação distribuída multi-datacenter, Consul Service Mesh (mTLS automático, autorização baseada em identidade e Transparent Proxy), Consul API Gateway, Service Discovery via DNS e HTTP (incluindo serviços externos/SaaS), Health Checking com circuit breakers, Dynamic App Configuration via HTTP API, suporte a Linux/macOS/FreeBSD/Solaris/Windows e divulgação de segurança para security@hashicorp.com.; consultado em 2026-10-03.
- [HashiCorp Consul Official Documentation — Concepts & Architecture](https://developer.hashicorp.com/consul/docs) — Documentação oficial completa do HashiCorp Consul para VMs, Kubernetes (Minikube, Kind, produção) e HCP Consul.; consultado em 2026-10-03.
- [HashiCorp Consul — Official GitHub Repository](https://github.com/hashicorp/consul) — Repositório oficial do HashiCorp Consul.; consultado em 2026-10-03.
