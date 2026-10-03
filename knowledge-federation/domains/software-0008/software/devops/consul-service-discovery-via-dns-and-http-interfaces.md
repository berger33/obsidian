---
id: software.devops.tranche06.000581
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

# Descoberta de serviços (Service Discovery) via interfaces DNS e HTTP e registro de serviços externos no Consul

## Em uma frase
O HashiCorp Consul (`developer.hashicorp.com/consul`), distribuído como uma solução altamente disponível e consciente de datacenter (*datacenter aware*), torna simples para os serviços se registrarem e descobrirem outros serviços em infraestruturas dinâmicas e distribuídas. Conforme destaca o README oficial, o pilar **Service Discovery** do Consul oferece duas interfaces nativas de descoberta — **uma interface DNS e uma interface HTTP API** — além de permitir registrar também **serviços externos**, como provedores SaaS ou bancos de dados gerenciados fora do cluster.

## Por que importa
Em ambientes dinâmicos onde contêineres, pods e máquinas virtuais mudam de endereço IP constantemente, codificar IPs estáticos em arquivos de configuração causa indisponibilidade a cada deploy. A interface DNS do Consul (`<servico>.service.consul`) permite que qualquer aplicação existente descubra instâncias saudáveis sem precisar alterar uma única linha de código para importar um SDK específico.

## Como funciona
Registre seus serviços no catálogo do Consul (automaticamente via Kubernetes/Nomad ou via configuração de agente) e utilize consultas DNS padrão (com encaminhamento DNS configurado nos nós) ou a API HTTP `/v1/health/service/<nome>?passing=true` para descobrir apenas endpoints saudáveis.

## Exemplo
Uma aplicação legada que não possui cliente HTTP do Consul é configurada apenas para conectar-se a `postgresql.service.consul`; o servidor DNS do Consul resolve esse nome em tempo real para os endereços IP das réplicas saudáveis do banco de dados, e serviços SaaS externos também são registrados no catálogo para roteamento uniforme.

## Limites e trade-offs
Ao utilizar a interface DNS do Consul para descoberta de serviços em linguagens como Java ou Go, configure o TTL de cache DNS da aplicação/runtime para respeitar o TTL baixo (ou zero) retornado pelo Consul, evitando que a aplicação continue tentando conectar em um IP antigo em cache após o failover de uma instância.

## Como verificar
Consulte um serviço registrado no Consul tanto via DNS (`dig @127.0.0.1 -p 8600 <servico>.service.consul SRV`) quanto via HTTP API e confirme o retorno dos endereços e portas ativos.

## Conexões
- [[consul-health-checking-and-circuit-breaker-integration]] — Veja também: Verificação ativa de saúde (Health Checking), prevenção de roteamento para nós falhos e Circuit Breakers no Consul.

## Fontes
- [HashiCorp Consul GitHub — README.md (Multi-Datacenter, Service Mesh, API Gateway, Service Discovery, Health Checking, KV & BUSL-1.1)](https://raw.githubusercontent.com/hashicorp/consul/main/README.md) — README oficial do HashiCorp Consul (licenciado sob BUSL-1.1) detalhando operação distribuída multi-datacenter, Consul Service Mesh (mTLS automático, autorização baseada em identidade e Transparent Proxy), Consul API Gateway, Service Discovery via DNS e HTTP (incluindo serviços externos/SaaS), Health Checking com circuit breakers, Dynamic App Configuration via HTTP API, suporte a Linux/macOS/FreeBSD/Solaris/Windows e divulgação de segurança para security@hashicorp.com.; consultado em 2026-10-03.
- [HashiCorp Consul Official Documentation — Concepts & Architecture](https://developer.hashicorp.com/consul/docs) — Documentação oficial completa do HashiCorp Consul para VMs, Kubernetes (Minikube, Kind, produção) e HCP Consul.; consultado em 2026-10-03.
- [HashiCorp Consul — Official GitHub Repository](https://github.com/hashicorp/consul) — Repositório oficial do HashiCorp Consul.; consultado em 2026-10-03.
