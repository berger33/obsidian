---
id: software.devops.tranche19.001845
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
fontes: ["https://developer.hashicorp.com/boundary/docs/what-is-boundary", "https://raw.githubusercontent.com/hashicorp/boundary/main/README.md", "https://github.com/hashicorp/boundary"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# HashiCorp Boundary e HashiCorp Vault: *Credential Brokering* e injeção de credenciais efêmeras por sessão

## Em uma frase
O Boundary integra-se nativamente ao **HashiCorp Vault** como um **Credential Store** dinâmico para emitir credenciais efêmeras *just-in-time* (como usuários temporários PostgreSQL via Database Secrets Engine, certificados SSH assinados ou tokens Kubernetes) para cada sessão autorizada, ou injetá-las diretamente na conexão (*Credential Injection*) sem revelá-las ao usuário.

## Por que importa
Mesmo quando o acesso de rede é restrito, compartilhar a mesma senha de banco de dados ou chave SSH entre dez engenheiros impede revogar o acesso de uma única sessão e expõe a credencial na máquina do usuário.

## Como funciona
Ao vincular uma *Vault Credential Library* a um `Target` no Boundary: 1) no modo **Credential Brokering**, quando o usuário roda `boundary connect`, o Controller solicita uma credencial recém-gerada ao Vault e a entrega à CLI/Desktop para abrir o cliente local (`psql`, `ssh`, `kubectl`), revogando o lease no Vault assim que a sessão termina; 2) no modo **Credential Injection** (para SSH/HTTP), o próprio **Worker** injeta a credencial no protocolo a caminho do servidor alvo, proporcionando uma experiência *passwordless* onde o usuário nunca vê a senha ou chave privada.

## Exemplo
```bash
boundary credential-stores create vault \
  -scope-id p_1234567890 \
  -vault-address "https://vault.corp.internal:8200" \
  -vault-token "s.periodic-service-token" \
  -name "prod-vault-store"
```

## Limites e trade-offs
O token do Vault fornecido ao `boundary credential-stores create vault` deve ser um **periodic token** e um **orphan token** (com permissões `auth/token/lookup-self`, `auth/token/renew-self` e `auth/token/revoke-self`) para que o Boundary possa renová-lo continuamente.

## Como verificar
Associe uma Credential Library a um Target e execute `boundary connect -target-id <id>` para verificar a geração automática de credenciais dinâmicas no Vault.

## Conexões
- [[boundary-host-catalogs-static-dynamic-aws-azure-host-sets-targets]] — Veja também: HashiCorp Boundary: descoberta automatizada de endpoints com `Host Catalogs` dinâmicos, `Host Sets` e `Targets`.
- [[boundary-connect-helpers-ssh-postgres-kube-rdp-transparent-sessions]] — Veja também: HashiCorp Boundary `boundary connect`: helpers nativos de CLI (`ssh`, `postgres`, `kube`, `http`, `rdp`) e sessões transparentes.

## Fontes
- [HashiCorp Boundary GitHub — README.md (Identity-Aware Proxy, Controller & Workers, PostgreSQL & KMS Requirements, Dev Mode & CLI)](https://developer.hashicorp.com/boundary/docs/what-is-boundary) — README oficial do hashicorp/boundary detalhando os componentes Controller e Worker, requisitos de banco SQL e KMS, hierarquia de Scopes e boundary connect; consultado em 2026-10-03.
- [HashiCorp Developer — What is Boundary? (Core Workflow, OIDC Authentication, Vault Credential Brokering/Injection, Multi-Hop & Session Recording)](https://raw.githubusercontent.com/hashicorp/boundary/main/README.md) — Documentação oficial do HashiCorp Boundary cobrindo acesso just-in-time sem agente, credenciais dinâmicas via Vault, sessões transparentes e gravação BSR; consultado em 2026-10-03.
- [HashiCorp Boundary — Official GitHub Repository](https://github.com/hashicorp/boundary) — Repositório oficial do HashiCorp Boundary; consultado em 2026-10-03.
