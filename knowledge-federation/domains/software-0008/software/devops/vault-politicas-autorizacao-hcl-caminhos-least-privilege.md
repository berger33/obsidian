---
id: software.devops.tranche10.000906
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/hashicorp/vault/main/README.md", "https://developer.hashicorp.com/vault/docs/about-vault/what-is-vault", "https://github.com/hashicorp/vault"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# HashiCorp Vault: autorização baseada em caminhos (Path-Based Policies em HCL) e princípio do privilégio mínimo

## Em uma frase
No Vault, toda operação (mesmo após autenticação bem-sucedida) é negada por padrão (`default deny`) até que uma **Policy** associada ao token conceda explicitamente as capacidades (`create`, `read`, `update`, `delete`, `list`, `sudo`) sobre o caminho de recurso (`path`) solicitado.

## Por que importa
Em um cofre centralizado que guarda segredos de dezenas de equipes e ambientes (`dev`, `staging`, `prod`), autenticar um pod ou engenheiro não significa dar acesso a todos os segredos do cluster: cada aplicação deve conseguir ler exclusivamente o seu próprio prefixo de segredos. A seção `Who can access data in Vault?` da documentação oficial descreve esse modelo de autorização por caminhos.

## Como funciona
Como tudo no Vault é exposto através de uma hierarquia de caminhos (`paths`, como `secret/data/pagamentos/prod` ou `database/creds/pagamentos-ro`), as políticas do Vault são escritas em **HCL (HashiCorp Configuration Language)** ou JSON associando padrões de caminhos (com suporte a wildcards `*` e parâmetros de identidade) a uma lista de **`capabilities`**: `create`, `read`, `update`, `patch`, `delete`, `list`, `sudo` e `deny`. Quando o cliente faz uma requisição com seu access token, o Vault avalia todas as políticas vinculadas ao token/entidade contra o `path` solicitado (onde `deny` sempre prevalece sobre qualquer permissão).

## Exemplo
```hcl
# Exemplo de política HCL (pagamentos-prod-ro.hcl) concedendo leitura apenas aos segredos da aplicação pagamentos
path "secret/data/pagamentos/prod/*" {
  capabilities = ["read"]
}

path "database/creds/pagamentos-readonly" {
  capabilities = ["read"]
}
```

## Limites e trade-offs
No motor **KV Secrets Engine v2** (versionado), os dados reais de um segredo ficam no subcaminho **`<mount>/data/<caminho>`** enquanto a listagem e os metadados de versões ficam em **`<mount>/metadata/<caminho>`**; um erro clássico ao escrever políticas HCL para o KV v2 é conceder permissão em `secret/pagamentos/*` em vez de `secret/data/pagamentos/*`, o que resulta em erro `403 permission denied` quando a aplicação tenta ler o segredo.

## Como verificar
Após carregar uma política com `vault policy write pagamentos-ro pagamentos-prod-ro.hcl`, teste as permissões efetivas usando `vault token capabilities <token> secret/data/pagamentos/prod/db`.

## Conexões
- [[vault-ecossistema-plugins-auth-secrets-database]] — Veja também: HashiCorp Vault: arquitetura modular de plugins (Authentication, General Secrets e Database Plugins).
- [[vault-motor-segredos-estaticos-kv-v2-versionamento-check-and-set]] — Veja também: HashiCorp Vault: gerenciamento de segredos estáticos (KV Secrets Engine v2), versionamento e Check-and-Set (CAS).
- [[vault-gerenciamento-centralizado-segredos-arquitetura-acesso]] — Referência cruzada direta com vault-gerenciamento-centralizado-segredos-arquitetura-acesso.
- [[externalsecrets-seguranca-rbac-least-privilege-multi-controller]] — Referência cruzada direta com externalsecrets-seguranca-rbac-least-privilege-multi-controller.

## Fontes
- [HashiCorp Vault GitHub — README.md (Secure Secret Storage, Dynamic Secrets, Data Encryption, Leasing/Renewal, Revocation & Go Libraries)](https://raw.githubusercontent.com/hashicorp/vault/main/README.md) — README oficial do HashiCorp Vault cobrindo armazenamento criptografado, segredos dinâmicos sob demanda, criptografia sem armazenamento, leases/revogação, compilação make dev e bibliotecas Go suportadas vault/api e vault/sdk; consultado em 2026-10-03.
- [HashiCorp Vault Documentation — What is Vault? (Architecture, Plugins, Access Control & Storage Backends)](https://developer.hashicorp.com/vault/docs/about-vault/what-is-vault) — Documentação oficial What is Vault? explicando o fluxo de autenticação/autorização por caminhos, categorias de plugins (auth, secret, database) e backends de armazenamento (Integrated Storage Raft, File, External e In-memory); consultado em 2026-10-03.
- [HashiCorp Vault — Official GitHub Repository](https://github.com/hashicorp/vault) — Repositório oficial do HashiCorp Vault; consultado em 2026-10-03.
