---
id: software.devops.tranche06.000584
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

# Gerenciamento de tráfego de entrada (Norte-Sul) e políticas de acesso com Consul API Gateway

## Em uma frase
Ao lado da Service Mesh (que governa o tráfego Leste-Oeste entre serviços internos), o README oficial destaca o **Consul API Gateway**, que **gerencia o acesso de clientes externos aos serviços implantados dentro da Consul Service Mesh**, permitindo aos operadores definir políticas de roteamento de tráfego (HTTP, TCP, gRPC), terminação TLS e políticas de autorização para expor serviços da malha com segurança.

## Por que importa
Usar um controlador de entrada externo que não participa nativamente da identidade mTLS da Service Mesh exige gambiarras para entregar pacotes aos sidecars internos. O Consul API Gateway atua como um membro nativo da malha (e implementa a especificação Kubernetes Gateway API quando em Kubernetes), roteando tráfego externo diretamente para os serviços internos via mTLS.

## Como funciona
Implante o Consul API Gateway na borda do cluster para concentrar a terminação TLS externa, roteamento baseado em cabeçalhos/caminhos, divisão de tráfego canário e controle de acesso antes de encaminhar as requisições para os serviços da Consul Service Mesh.

## Exemplo
Para expor a API pública da plataforma mantendo os microsserviços internos em rede fechada com mTLS obrigatório, a equipe configura um listener HTTPS no Consul API Gateway e rotas que encaminham `/v1/orders` ao serviço `orders` dentro da malha.

## Limites e trade-offs
Defina sempre uma Intention explícita permitindo que a identidade do `api-gateway` chame apenas os serviços de borda (BFFs/APIs públicas) que realmente devem ser expostos externamente, nunca concedendo ao gateway acesso irrestrito a bancos de dados ou serviços internos profundos.

## Como verificar
Inspecione o status do Consul API Gateway e de suas rotas associadas e valide uma requisição HTTPS externa sendo roteada com sucesso até o serviço da malha.

## Conexões
- [[consul-consul-service-mesh-mtls-and-transparent-proxy]] — Veja também: Consul Service Mesh: criptografia mTLS automática, autorização baseada em identidade (Intentions) e Transparent Proxy.
- [[consul-multi-datacenter-awareness-and-wan-federation]] — Veja também: Arquitetura nativa Multi-Datacenter do Consul para operação multi-região sem configuração complexa.

## Fontes
- [HashiCorp Consul GitHub — README.md (Multi-Datacenter, Service Mesh, API Gateway, Service Discovery, Health Checking, KV & BUSL-1.1)](https://raw.githubusercontent.com/hashicorp/consul/main/README.md) — README oficial do HashiCorp Consul (licenciado sob BUSL-1.1) detalhando operação distribuída multi-datacenter, Consul Service Mesh (mTLS automático, autorização baseada em identidade e Transparent Proxy), Consul API Gateway, Service Discovery via DNS e HTTP (incluindo serviços externos/SaaS), Health Checking com circuit breakers, Dynamic App Configuration via HTTP API, suporte a Linux/macOS/FreeBSD/Solaris/Windows e divulgação de segurança para security@hashicorp.com.; consultado em 2026-10-03.
- [HashiCorp Consul Official Documentation — Concepts & Architecture](https://developer.hashicorp.com/consul/docs) — Documentação oficial completa do HashiCorp Consul para VMs, Kubernetes (Minikube, Kind, produção) e HCP Consul.; consultado em 2026-10-03.
- [HashiCorp Consul — Official GitHub Repository](https://github.com/hashicorp/consul) — Repositório oficial do HashiCorp Consul.; consultado em 2026-10-03.
