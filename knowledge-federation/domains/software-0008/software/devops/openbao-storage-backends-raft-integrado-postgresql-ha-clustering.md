---
id: software.devops.tranche20.001942
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://raw.githubusercontent.com/openbao/openbao/main/README.md", "https://openbao.org/docs/what-is-openbao/", "https://github.com/openbao/openbao"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenBao Storage Backends e Alta Disponibilidade: armazenamento integrado `raft` vs `postgresql` e barreira criptográfica

## Em uma frase
O OpenBao protege todos os dados em repouso por meio de uma **barreira criptográfica**: todo segredo é criptografado em memória pelo OpenBao **antes** de ser gravado no backend de armazenamento persistente (**Integrated Storage `raft`**, **PostgreSQL** ou sistema de arquivos `file`), de modo que o acesso direto ao banco ou disco bruto jamais revela os segredos.

## Por que importa
Em ambientes corporativos que já operam clusters PostgreSQL altamente disponíveis com rotinas de backup consolidadas, ou em clusters Kubernetes que preferem consenso Raft embutido sem dependências externas, a escolha do backend de storage define a topologia de HA.

## Como funciona
No arquivo HCL do servidor (`config.hcl`), você configura o bloco `storage "raft"` (que forma um cluster de consenso Raft nativo entre 3 ou 5 nós OpenBao) ou `storage "postgresql"` (suportado nativamente no OpenBao com coordenação de líder HA).

## Exemplo
```hcl
ui = true
cluster_addr = "https://10.0.1.10:8201"
api_addr     = "https://10.0.1.10:8200"

storage "raft" {
  path    = "/var/lib/openbao/data"
  node_id = "openbao-node-1"
}

listener "tcp" {
  address     = "0.0.0.0:8200"
  tls_cert_file = "/etc/openbao/tls/tls.crt"
  tls_key_file  = "/etc/openbao/tls/tls.key"
}
```

## Limites e trade-offs
Em um cluster Raft do OpenBao, mantenha sempre um número **ímpar** de nós votantes (3 ou 5 nós) para tolerar a falha de $(N-1)/2$ nós sem perder o quórum.

## Como verificar
Execute `bao operator raft list-peers` para verificar o `leader`, os `followers` e o estado do quórum Raft do cluster.

## Conexões
- [[openbao-arquitetura-open-source-secrets-encryption-management-openssf]] — Veja também: OpenBao: arquitetura do sistema open-source (OpenSSF/Linux Foundation) de gerenciamento de segredos e criptografia (`bao`).
- [[openbao-seal-unseal-shamir-auto-unseal-kms-pkcs11-inicializacao]] — Veja também: OpenBao Seal/Unseal e Inicialização: chaves Shamir vs Auto-Unseal com KMS/PKCS#11 e inicialização declarativa.

## Fontes
- [OpenBao GitHub — README.md (OpenSSF/Linux Foundation Community-Driven Secrets & Encryption Management System)](https://raw.githubusercontent.com/openbao/openbao/main/README.md) — README oficial do openbao/openbao apresentando governança OpenSSF sob MPL-2.0, compilação e documentação; consultado em 2026-10-03.
- [OpenBao Official Documentation — What is OpenBao? (Authenticate/Validate/Authorize/Access Pipeline, Dynamic Secrets, Leasing & Revocation)](https://openbao.org/docs/what-is-openbao/) — Documentação oficial de arquitetura do OpenBao explicando o fluxo de 4 estágios (Authenticate, Validate, Authorize, Access), segredos dinâmicos, leases e revogação; consultado em 2026-10-03.
- [OpenBao — Official GitHub Repository](https://github.com/openbao/openbao) — Repositório oficial MPL-2.0 do OpenBao na OpenSSF; consultado em 2026-10-03.
