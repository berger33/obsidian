---
id: software.devops.tranche06.000589
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

# Licenciamento BUSL-1.1 do repositório Consul, edição comunitária vs Consul Enterprise

## Em uma frase
Os badges e o texto do README oficial registram duas informações essenciais de governança e licenciamento: o código no repositório `hashicorp/consul` é licenciado sob a **Business Source License 1.1 (`BUSL-1.1`, conforme arquivo `LICENSE`)**, e além da edição comunitária existe uma versão comercial chamada **Consul Enterprise** (`developer.hashicorp.com/consul/docs/enterprise`) que adiciona recursos voltados a grandes corporações (como *Admin Partitions*, *Namespaces* multi-tenant avançados, *Audit Logging* e replicação/redundância avançada de leitura).

## Por que importa
Arquitetos de plataforma e equipes de conformidade jurídica precisam registrar corretamente a licença **`BUSL-1.1`** das versões recentes do Consul no inventário de software da empresa (diferenciando-a da licença MPL-2.0 das versões históricas anteriores à mudança de licença da HashiCorp) e saber quais recursos pertencem ao Consul comunitário versus Consul Enterprise.

## Como funciona
Verifique os termos do arquivo `LICENSE` (`BUSL-1.1`) para garantir conformidade com o seu caso de uso interno (uso em produção interna é permitido pela BUSL-1.1 desde que não ofereça o próprio Consul como serviço gerenciado concorrente a terceiros) e consulte `developer.hashicorp.com/consul/docs/enterprise` antes de desenhar arquiteturas que dependam de *Admin Partitions* ou *Namespaces*.

## Exemplo
Durante a revisão de arquitetura de uma plataforma interna de microsserviços, o arquiteto valida que o uso interno do Consul Service Mesh atende aos termos da licença `BUSL-1.1` e projeta a topologia usando os recursos nativos da versão comunitária.

## Limites e trade-offs
Não inclua blocos de configuração exclusivos do Consul Enterprise (como `partition` ou `namespace` multi-tenant) em manifestos destinados ao binário comunitário do Consul, pois a API retornará erro indicando que o recurso exige licença Enterprise.

## Como verificar
Execute `consul version` para identificar se o binário em execução é a edição padrão ou Enterprise (`+ent`) e sua versão exata.

## Conexões
- [[consul-deployment-topologies-vms-minikube-kind-k8s-and-hcp]] — Veja também: Guias de implantação do Consul: binário standalone em VMs, Minikube, Kind, Kubernetes em produção e HCP Consul.
- [[consul-security-vulnerability-disclosure-hashicorp]] — Veja também: Divulgação responsável de vulnerabilidades de segurança no Consul (security@hashicorp.com).

## Fontes
- [HashiCorp Consul GitHub — README.md (Multi-Datacenter, Service Mesh, API Gateway, Service Discovery, Health Checking, KV & BUSL-1.1)](https://raw.githubusercontent.com/hashicorp/consul/main/README.md) — README oficial do HashiCorp Consul (licenciado sob BUSL-1.1) detalhando operação distribuída multi-datacenter, Consul Service Mesh (mTLS automático, autorização baseada em identidade e Transparent Proxy), Consul API Gateway, Service Discovery via DNS e HTTP (incluindo serviços externos/SaaS), Health Checking com circuit breakers, Dynamic App Configuration via HTTP API, suporte a Linux/macOS/FreeBSD/Solaris/Windows e divulgação de segurança para security@hashicorp.com.; consultado em 2026-10-03.
- [HashiCorp Consul Official Documentation — Concepts & Architecture](https://developer.hashicorp.com/consul/docs) — Documentação oficial completa do HashiCorp Consul para VMs, Kubernetes (Minikube, Kind, produção) e HCP Consul.; consultado em 2026-10-03.
- [HashiCorp Consul — Official GitHub Repository](https://github.com/hashicorp/consul) — Repositório oficial do HashiCorp Consul.; consultado em 2026-10-03.
