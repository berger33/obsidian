---
id: software.devops.tranche19.001847
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

# HashiCorp Boundary Workers e Multi-Hop Sessions: encadeamento de Ingress e Egress Workers para redes privadas sem rota de entrada

## Em uma frase
Os **Boundary Workers** realizam todo o transporte de sessão e suportam **Multi-Hop Sessions** (encadeando um *Ingress Worker* na DMZ com um *Egress Worker* dentro de uma VPC privada ou enclave isolado), onde a conexão entre os Workers é iniciada de dentro para fora (reverse connection).

## Por que importa
Em redes corporativas de alta segurança, sub-redes de bancos de dados ou clusters on-premises não permitem abrir portas de firewall de entrada a partir da internet ou da DMZ.

## Como funciona
No modelo Multi-Hop, o *Egress Worker* roda dentro da sub-rede privada (com acesso apenas de saída para a porta `9202` do *Ingress Worker* e tags como `type = ["prod-private-vpc"]`). No `Target`, um filtro `egress_worker_filter` (`"prod-private-vpc" in "/tags/type"`) instrui o Boundary a rotear a sessão do cliente -> *Ingress Worker* -> *Egress Worker* -> servidor alvo, sem abrir nenhuma porta de entrada no firewall da rede privada.

## Exemplo
```hcl
# Em worker-egress.hcl dentro da rede privada:
worker {
  public_addr = "10.50.1.10"
  initial_upstreams = ["ingress-worker.dmz.corp.io:9202"]
  tags {
    type = ["prod-private-vpc"]
    region = ["sa-east-1"]
  }
}
```

## Limites e trade-offs
Os Workers do Boundary são totalmente stateless em relação ao banco PostgreSQL: apenas os **Controllers** precisam de conectividade de rede com o banco de dados PostgreSQL.

## Como verificar
Execute `boundary workers list` para verificar que os Workers de ingresso e egresso aparecem registrados e reportam suas tags corretamente.

## Conexões
- [[boundary-connect-helpers-ssh-postgres-kube-rdp-transparent-sessions]] — Veja também: HashiCorp Boundary `boundary connect`: helpers nativos de CLI (`ssh`, `postgres`, `kube`, `http`, `rdp`) e sessões transparentes.
- [[boundary-session-controls-max-connections-timeout-cancelamento-auditoria]] — Veja também: HashiCorp Boundary Session Controls: limites de conexões por sessão, `session_max_seconds` e revogação em tempo real.

## Fontes
- [HashiCorp Boundary GitHub — README.md (Identity-Aware Proxy, Controller & Workers, PostgreSQL & KMS Requirements, Dev Mode & CLI)](https://developer.hashicorp.com/boundary/docs/what-is-boundary) — README oficial do hashicorp/boundary detalhando os componentes Controller e Worker, requisitos de banco SQL e KMS, hierarquia de Scopes e boundary connect; consultado em 2026-10-03.
- [HashiCorp Developer — What is Boundary? (Core Workflow, OIDC Authentication, Vault Credential Brokering/Injection, Multi-Hop & Session Recording)](https://raw.githubusercontent.com/hashicorp/boundary/main/README.md) — Documentação oficial do HashiCorp Boundary cobrindo acesso just-in-time sem agente, credenciais dinâmicas via Vault, sessões transparentes e gravação BSR; consultado em 2026-10-03.
- [HashiCorp Boundary — Official GitHub Repository](https://github.com/hashicorp/boundary) — Repositório oficial do HashiCorp Boundary; consultado em 2026-10-03.
