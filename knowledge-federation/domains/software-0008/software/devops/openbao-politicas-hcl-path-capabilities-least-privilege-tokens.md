---
id: software.devops.tranche20.001947
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
fontes: ["https://openbao.org/docs/what-is-openbao/", "https://raw.githubusercontent.com/openbao/openbao/main/README.md", "https://github.com/openbao/openbao"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenBao Políticas HCL (*Path-Based Policies*): controle declarativo de capacidades (`create`, `read`, `update`, `delete`, `list`, `sudo`)

## Em uma frase
A autorização no OpenBao é governada por **políticas declarativas em HCL** associadas aos tokens dos clientes, onde tudo é **negado por padrão (*deny-by-default*)** e cada bloco `path "..."` concede explicitamente uma lista de `capabilities` (`create`, `read`, `update`, `patch`, `delete`, `list`, `sudo` ou `deny`).

## Por que importa
Conceder permissões amplas `path "secret/*" { capabilities = ["read"] }` permite que um serviço leia segredos de todas as demais aplicações do cluster.

## Como funciona
No motor `kv-v2`, lembre-se de que os valores dos segredos residem no subcaminho **`data/`** (`secret/data/prod/app`) e os metadados/listagem residem em **`metadata/`** (`secret/metadata/prod/*`). Além disso, Políticas suportam **Identity Templates** dinâmicos (como `path "secret/data/teams/{{identity.entity.aliases.auth_kubernetes_xxx.metadata.service_account_namespace}}/*"`), permitindo que uma única política atenda dezenas de namespaces com isolamento estrito.

## Exemplo
```hcl
# Política HCL de menor privilégio para leitura de segredos KV-v2 e uso do Transit:
path "secret/data/prod/payment-api" {
  capabilities = ["read"]
}

path "transit/encrypt/customer-pii" {
  capabilities = ["update"]
}
```

## Limites e trade-offs
A capacidade `deny` sempre prevalece sobre qualquer outra capacidade concedida a um caminho, mesmo que outra política anexada ao mesmo token conceda `read` ou `sudo`.

## Como verificar
Grave a política com `bao policy write payment-app policy.hcl` e teste as permissões efetivas de um caminho com `bao token capabilities <token> secret/data/prod/payment-api`.

## Conexões
- [[openbao-transit-secrets-engine-encryption-as-a-service-key-rotation]] — Veja também: OpenBao Transit Secrets Engine (*Encryption as a Service*): criptografia em trânsito sem armazenar dados, assinaturas e rotação de chaves.
- [[openbao-autenticacao-kubernetes-serviceaccount-jwt-token-reviewer]] — Veja também: OpenBao Kubernetes Auth Method: autenticação de Pods via `ServiceAccount` JWT (`TokenRequest` API) sem segredos estáticos.

## Fontes
- [OpenBao GitHub — README.md (OpenSSF/Linux Foundation Community-Driven Secrets & Encryption Management System)](https://openbao.org/docs/what-is-openbao/) — README oficial do openbao/openbao apresentando governança OpenSSF sob MPL-2.0, compilação e documentação; consultado em 2026-10-03.
- [OpenBao Official Documentation — What is OpenBao? (Authenticate/Validate/Authorize/Access Pipeline, Dynamic Secrets, Leasing & Revocation)](https://raw.githubusercontent.com/openbao/openbao/main/README.md) — Documentação oficial de arquitetura do OpenBao explicando o fluxo de 4 estágios (Authenticate, Validate, Authorize, Access), segredos dinâmicos, leases e revogação; consultado em 2026-10-03.
- [OpenBao — Official GitHub Repository](https://github.com/openbao/openbao) — Repositório oficial MPL-2.0 do OpenBao na OpenSSF; consultado em 2026-10-03.
