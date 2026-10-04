---
id: software.devops.tranche10.000905
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

# HashiCorp Vault: arquitetura modular de plugins (Authentication, General Secrets e Database Plugins)

## Em uma frase
Conforme a documentação oficial `What is Vault?`, a arquitetura do Vault é construída em torno de um ecossistema modular de **plugins** divididos em três categorias principais: plugins de autenticação (`auth`), plugins gerais de segredos (`secret`) e plugins de bancos de dados (`database`).

## Por que importa
Nenhuma organização possui exatamente a mesma pilha tecnológica: uma empresa autentica workloads via Kubernetes ServiceAccounts e gera credenciais no PostgreSQL, enquanto outra usa AWS IAM e gerencia certificados PKI internos. Ao isolar cada integração em plugins montados em caminhos de URL (`paths`), o núcleo do Vault permanece enxuto e extensível.

## Como funciona
Conforme explica a seção `What is a plugin?` em `developer.hashicorp.com/vault/docs/about-vault/what-is-vault`, os plugins atuam como blocos de construção que controlam como os dados fluem e como os clientes os acessam: (1) **Authentication plugins (`vault auth enable <tipo>`)**: tratam fluxos de autenticação e vinculam identidades externas (Kubernetes, OIDC/JWT, AppRole, AWS, Azure, LDAP, GitHub) a tokens e políticas do Vault; (2) **General secret plugins (`vault secrets enable <tipo>`)**: geram, armazenam, gerenciam ou transformam informações sensíveis (KV v1/v2, PKI/certificados, Transit, SSH, AWS/GCP/Azure); e (3) **Database secret plugins**: gerenciam credenciais dinâmicas e rotação de senhas para bancos de dados relacionais e NoSQL.

## Exemplo
```bash
# Listar os motores de segredos e os métodos de autenticação atualmente montados e ativos no Vault
vault secrets list -detailed
vault auth list -detailed
```

## Limites e trade-offs
Cada plugin montado no Vault vive isolado dentro do seu próprio caminho de montagem (por exemplo, `secret/`, `pki/`, `database/`) — um segredo ou configuração criado em uma montagem não é visível para outro plugin; ao registrar plugins customizados externos no catálogo do Vault, o administrador deve registrar explicitamente o hash **`sha256`** do binário do plugin por segurança.

## Como verificar
Execute `vault secrets list` e `vault auth list` para auditar todos os plugins ativos, seus caminhos de montagem (`Path`) e suas configurações de TTL padrão.

## Conexões
- [[vault-criptografia-como-servico-transit-data-encryption]] — Veja também: HashiCorp Vault: criptografia de dados como serviço (Encryption as a Service) sem armazenar os dados no Vault.
- [[vault-politicas-autorizacao-hcl-caminhos-least-privilege]] — Veja também: HashiCorp Vault: autorização baseada em caminhos (Path-Based Policies em HCL) e princípio do privilégio mínimo.
- [[vault-gerenciamento-centralizado-segredos-arquitetura-acesso]] — Referência cruzada direta com vault-gerenciamento-centralizado-segredos-arquitetura-acesso.
- [[vault-bibliotecas-go-api-sdk-desenvolvimento-testes]] — Referência cruzada direta com vault-bibliotecas-go-api-sdk-desenvolvimento-testes.

## Fontes
- [HashiCorp Vault GitHub — README.md (Secure Secret Storage, Dynamic Secrets, Data Encryption, Leasing/Renewal, Revocation & Go Libraries)](https://raw.githubusercontent.com/hashicorp/vault/main/README.md) — README oficial do HashiCorp Vault cobrindo armazenamento criptografado, segredos dinâmicos sob demanda, criptografia sem armazenamento, leases/revogação, compilação make dev e bibliotecas Go suportadas vault/api e vault/sdk; consultado em 2026-10-03.
- [HashiCorp Vault Documentation — What is Vault? (Architecture, Plugins, Access Control & Storage Backends)](https://developer.hashicorp.com/vault/docs/about-vault/what-is-vault) — Documentação oficial What is Vault? explicando o fluxo de autenticação/autorização por caminhos, categorias de plugins (auth, secret, database) e backends de armazenamento (Integrated Storage Raft, File, External e In-memory); consultado em 2026-10-03.
- [HashiCorp Vault — Official GitHub Repository](https://github.com/hashicorp/vault) — Repositório oficial do HashiCorp Vault; consultado em 2026-10-03.
