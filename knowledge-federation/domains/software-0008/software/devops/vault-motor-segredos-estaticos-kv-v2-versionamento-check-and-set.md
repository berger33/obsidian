---
id: software.devops.tranche10.000907
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

# HashiCorp Vault: gerenciamento de segredos estáticos (KV Secrets Engine v2), versionamento e Check-and-Set (CAS)

## Em uma frase
Para segredos estáticos (chaves de API de terceiros, webhooks e senhas externas que não suportam geração dinâmica), o motor **KV v2** do Vault mantém histórico de versões, exclusão reversível (`delete`/`undelete`), destruição permanente (`destroy`) e proteção contra sobrescrita concorrente (`cas`).

## Por que importa
Embora segredos dinâmicos sejam ideais para bancos de dados e nuvens próprias, toda empresa precisa armazenar chaves estáticas emitidas por parceiros externos (Stripe, Twilio, SendGrid, tokens OAuth). Se alguém sobrescrever acidentalmente uma chave estática em produção sem versionamento, a aplicação cai imediatamente sem possibilidade de rollback rápido.

## Como funciona
Com o motor KV v2 habilitado (`vault secrets enable -version=2 kv`), cada escrita via **`vault kv put kv/minha-app api_key=...`** cria uma nova versão numerada (`version 1`, `version 2`, ... up to `max_versions`, padrão 10) em vez de sobrescrever os bytes anteriores. O operador pode: (1) ler a versão mais recente ou uma versão específica (`vault kv get -version=1 kv/minha-app`); (2) fazer **rollback** (`vault kv rollback -version=1 kv/minha-app`); (3) exigir **Check-And-Set (`-cas=<versão>`)** na escrita para garantir que outro processo não alterou o segredo no meio tempo; e (4) realizar soft-delete (`vault kv delete`, recuperável com `vault kv undelete`) ou destruir criptograficamente os bytes de uma versão (`vault kv destroy`).

## Exemplo
```bash
# Gravar um segredo estático no KV v2 exigindo Check-And-Set (-cas=0 para criação inicial) e inspecionar metadados
vault kv put -cas=0 secret/pagamentos/stripe webhook_secret="whsec_exemplo123"
vault kv metadata get secret/pagamentos/stripe
```

## Limites e trade-offs
Atenção à diferença entre `vault kv delete` e `vault kv destroy`: o comando `vault kv delete` faz apenas uma exclusão lógica (marcando `deletion_time` nos metadados), permitindo que qualquer pessoa com permissão de `undelete` restaure o valor; se uma chave vazou ou precisa ser expurgada definitivamente por conformidade regulatória, utilize **`vault kv destroy -versions=1,2 <caminho>`** (ou `vault kv metadata delete` para apagar todas as versões e o histórico).

## Como verificar
Execute `vault kv metadata get secret/pagamentos/stripe` para verificar o número da versão atual (`current_version`), o histórico de timestamps de criação e se `cas_required` está ativo.

## Conexões
- [[vault-politicas-autorizacao-hcl-caminhos-least-privilege]] — Veja também: HashiCorp Vault: autorização baseada em caminhos (Path-Based Policies em HCL) e princípio do privilégio mínimo.
- [[vault-gerenciamento-certificados-pki-x509-ca-interna]] — Veja também: HashiCorp Vault: emissão automatizada de certificados X.509 de curta duração como Autoridade Certificadora (PKI).
- [[vault-gerenciamento-centralizado-segredos-arquitetura-acesso]] — Referência cruzada direta com vault-gerenciamento-centralizado-segredos-arquitetura-acesso.
- [[externalsecrets-modelo-recursos-secretstore-externalsecret-clustersecretstore]] — Referência cruzada direta com externalsecrets-modelo-recursos-secretstore-externalsecret-clustersecretstore.

## Fontes
- [HashiCorp Vault GitHub — README.md (Secure Secret Storage, Dynamic Secrets, Data Encryption, Leasing/Renewal, Revocation & Go Libraries)](https://raw.githubusercontent.com/hashicorp/vault/main/README.md) — README oficial do HashiCorp Vault cobrindo armazenamento criptografado, segredos dinâmicos sob demanda, criptografia sem armazenamento, leases/revogação, compilação make dev e bibliotecas Go suportadas vault/api e vault/sdk; consultado em 2026-10-03.
- [HashiCorp Vault Documentation — What is Vault? (Architecture, Plugins, Access Control & Storage Backends)](https://developer.hashicorp.com/vault/docs/about-vault/what-is-vault) — Documentação oficial What is Vault? explicando o fluxo de autenticação/autorização por caminhos, categorias de plugins (auth, secret, database) e backends de armazenamento (Integrated Storage Raft, File, External e In-memory); consultado em 2026-10-03.
- [HashiCorp Vault — Official GitHub Repository](https://github.com/hashicorp/vault) — Repositório oficial do HashiCorp Vault; consultado em 2026-10-03.
