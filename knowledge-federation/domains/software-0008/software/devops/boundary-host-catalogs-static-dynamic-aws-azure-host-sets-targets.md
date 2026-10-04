---
id: software.devops.tranche19.001844
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

# HashiCorp Boundary: descoberta automatizada de endpoints com `Host Catalogs` dinâmicos, `Host Sets` e `Targets`

## Em uma frase
No Boundary, os sistemas de destino são modelados por três recursos dentro de um escopo de projeto: **`Host Catalog`** (estático ou dinâmico integrado a provedores como AWS e Azure), **`Host Set`** (agrupamento de hosts filtrados por tags/atributos) e **`Target`** (que vincula um Host Set à porta TCP/SSH, limites de sessão e credenciais).

## Por que importa
Quando grupos de Auto-Scaling ou clusters Kubernetes substituem máquinas virtuais continuamente, atualizar IPs manualmente em arquivos `~/.ssh/config` ou listas estáticas de bastião fica defasado em minutos.

## Como funciona
Com um *Dynamic Host Catalog* (plugin `aws` ou `azure`), o Boundary consulta a API da nuvem e popula automaticamente os `Host Sets` com todas as instâncias EC2/VMs que possuem determinadas tags (ex.: `tag:Role=postgres-prod`). O usuário final conecta-se apenas ao ID lógico do `Target` (`ttcp_...`), sem sequer precisar saber o IP privado da máquina.

## Exemplo
```bash
boundary host-catalogs create plugin \
  -scope-id p_1234567890 \
  -plugin-name aws \
  -name "prod-aws-catalog" \
  -attr disable_credential_rotation=true \
  -attr region=us-east-1
```

## Limites e trade-offs
A partir de versões recentes do Boundary, um `Target` também pode definir diretamente um endereço de host ou DNS (`-address db.prod.internal`) sem exigir a criação prévia de um `Host Catalog` e `Host Set` quando há apenas um endpoint fixo.

## Como verificar
Liste os targets disponíveis no projeto com `boundary targets list -scope-id p_1234567890` e inspecione os `Host Sets` vinculados.

## Conexões
- [[boundary-kms-key-hierarchy-root-worker-auth-recovery-vault-transit]] — Veja também: HashiCorp Boundary KMS: arquitetura de chaves (`root`, `worker-auth`, `recovery`, `config`) com Cloud KMS ou Vault Transit.
- [[boundary-vault-credential-store-brokering-injecao-credenciais-efemeras]] — Veja também: HashiCorp Boundary e HashiCorp Vault: *Credential Brokering* e injeção de credenciais efêmeras por sessão.

## Fontes
- [HashiCorp Boundary GitHub — README.md (Identity-Aware Proxy, Controller & Workers, PostgreSQL & KMS Requirements, Dev Mode & CLI)](https://developer.hashicorp.com/boundary/docs/what-is-boundary) — README oficial do hashicorp/boundary detalhando os componentes Controller e Worker, requisitos de banco SQL e KMS, hierarquia de Scopes e boundary connect; consultado em 2026-10-03.
- [HashiCorp Developer — What is Boundary? (Core Workflow, OIDC Authentication, Vault Credential Brokering/Injection, Multi-Hop & Session Recording)](https://raw.githubusercontent.com/hashicorp/boundary/main/README.md) — Documentação oficial do HashiCorp Boundary cobrindo acesso just-in-time sem agente, credenciais dinâmicas via Vault, sessões transparentes e gravação BSR; consultado em 2026-10-03.
- [HashiCorp Boundary — Official GitHub Repository](https://github.com/hashicorp/boundary) — Repositório oficial do HashiCorp Boundary; consultado em 2026-10-03.
