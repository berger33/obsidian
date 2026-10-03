---
id: software.devops.tranche19.001841
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-19.md"
fontes: ["https://raw.githubusercontent.com/hashicorp/boundary/main/README.md", "https://developer.hashicorp.com/boundary/docs/what-is-boundary", "https://github.com/hashicorp/boundary"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# HashiCorp Boundary: arquitetura de acesso privilegiado baseado em identidade com `Controller`, `Worker`, PostgreSQL e KMS

## Em uma frase
O **HashiCorp Boundary** é um proxy e sistema de gerenciamento de acesso baseado em identidade (*Identity-Aware Proxy*) que fornece acesso seguro e auditado *just-in-time* a hosts, bancos de dados, clusters Kubernetes e serviços privados sem expor a rede interna via VPN tradicional, sem distribuir credenciais estáticas aos usuários e sem exigir instalação de agentes nos hosts de destino.

## Por que importa
Manter bastiões SSH compartilhados e VPNs corporativas amplas viola o princípio de menor privilégio (qualquer máquina na VPN enxerga a sub-rede inteira) e espalha chaves SSH/senhas de banco nas estações dos engenheiros.

## Como funciona
A arquitetura do Boundary consiste em dois componentes de servidor (executáveis pelo mesmo binário `boundary`): 1) **Controller** (serve a API/UI na porta `9200`, autentica usuários via OIDC/LDAP/Password, avalia permissões RBAC e coordena sessões); e 2) **Workers** (escutam na porta `9202`, realizam o proxy TCP/SSH das sessões autorizadas), apoiados em duas dependências externas: um banco **PostgreSQL** (12+) e um provedor de chaves **KMS** (Cloud KMS ou HashiCorp Vault Transit).

## Exemplo
```bash
# Iniciando um ambiente completo de teste local (Controller + Worker + PostgreSQL em container):
boundary dev
```

## Limites e trade-offs
No modo `boundary dev`, o binário sobe um Controller em `127.0.0.1:9200`, um Worker em `127.0.0.1:9202`, um container PostgreSQL efêmero e chaves KMS em memória com escopos e targets pré-configurados para testes rápidos.

## Como verificar
Execute `boundary dev` em um terminal e em outro autentique com `boundary authenticate password` seguido de `boundary targets list` para inspecionar os recursos criados.

## Conexões
- [[boundary-hierarquia-scopes-global-org-project-iam-roles-grants]] — Veja também: HashiCorp Boundary: modelagem hierárquica de `Scopes` (`global`, `org`, `project`), `Roles` e `Grants`.

## Fontes
- [HashiCorp Boundary GitHub — README.md (Identity-Aware Proxy, Controller & Workers, PostgreSQL & KMS Requirements, Dev Mode & CLI)](https://raw.githubusercontent.com/hashicorp/boundary/main/README.md) — README oficial do hashicorp/boundary detalhando os componentes Controller e Worker, requisitos de banco SQL e KMS, hierarquia de Scopes e boundary connect; consultado em 2026-10-03.
- [HashiCorp Developer — What is Boundary? (Core Workflow, OIDC Authentication, Vault Credential Brokering/Injection, Multi-Hop & Session Recording)](https://developer.hashicorp.com/boundary/docs/what-is-boundary) — Documentação oficial do HashiCorp Boundary cobrindo acesso just-in-time sem agente, credenciais dinâmicas via Vault, sessões transparentes e gravação BSR; consultado em 2026-10-03.
- [HashiCorp Boundary — Official GitHub Repository](https://github.com/hashicorp/boundary) — Repositório oficial do HashiCorp Boundary; consultado em 2026-10-03.
