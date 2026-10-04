---
id: software.devops.tranche10.000903
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

# HashiCorp Vault: geração de Segredos Dinâmicos sob demanda, Leases, Renovação e Revogação em árvore

## Em uma frase
Com **Dynamic Secrets**, o Vault gera credenciais efêmeras sob demanda (ex.: chaves IAM da AWS ou usuários SQL em bancos de dados) associadas a um **lease** com tempo de vida (TTL), revogando-as automaticamente ao expirar ou imediatamente em árvore em caso de intrusão.

## Por que importa
Quando 20 instâncias de uma aplicação compartilham a mesma senha estática de banco de dados PostgreSQL por meses, vazar um único log compromete todo o banco e descobrir qual instância fez determinada query é impossível. Segundo o README oficial do Vault (`Dynamic Secrets`, `Leasing and Renewal` e `Revocation`), credenciais dinâmicas com leases curtos eliminam credenciais compartilhadas de longa duração.

## Como funciona
Quando uma aplicação precisa acessar um recurso (como um bucket S3 na AWS ou um banco de dados SQL), ela solicita credenciais ao caminho do secrets engine no Vault: (1) o Vault cria em tempo real um par de chaves/usuário exclusivo no sistema alvo com as permissões exatas e retorna a credencial acompanhada de um **`lease_id`** e **`lease_duration`**; (2) enquanto estiver em uso ativo, o cliente pode estender o prazo chamando a API embutida de renovação (**`vault lease renew <lease_id>`**) até o `max_ttl`; e (3) quando o lease expira — ou quando um operador aciona **`vault lease revoke`** — o Vault conecta-se ao banco/provedor de nuvem e exclui aquela credencial temporária imediatamente, suportando inclusive revogação em árvore (`-prefix`) de todos os segredos lidos por um usuário ou de um tipo inteiro.

## Exemplo
```bash
# Ler credenciais dinâmicas de um papel de banco de dados, renovar o lease e revogar toda uma árvore de leases por prefixo
vault read database/creds/readonly-app
vault lease renew database/creds/readonly-app/2c9a8f1b-exemplo
vault lease revoke -prefix database/creds/readonly-app
```

## Limites e trade-offs
Ao adotar segredos dinâmicos com TTL curto em aplicações que mantêm pools de conexões de longa duração com o banco de dados, a aplicação (ou um agente auxiliar como o Vault Agent / External Secrets) precisa renovar o lease antes do vencimento ou recriar conexões do pool quando as credenciais forem rotacionadas, caso contrário as conexões ativas ou novas falharão quando o Vault apagar o usuário temporário no banco ao fim do lease.

## Como verificar
Gere uma credencial dinâmica no Vault, anote o `lease_id` retornado, execute `vault lease revoke <lease_id>` e tente autenticar no banco de dados com a credencial revogada para confirmar que o usuário já foi removido pelo Vault.

## Conexões
- [[vault-armazenamento-criptografado-integrated-storage-raft-backends]] — Veja também: HashiCorp Vault: criptografia em repouso (barreira de segurança) e backends de armazenamento (Integrated Storage Raft).
- [[vault-criptografia-como-servico-transit-data-encryption]] — Veja também: HashiCorp Vault: criptografia de dados como serviço (Encryption as a Service) sem armazenar os dados no Vault.
- [[vault-gerenciamento-centralizado-segredos-arquitetura-acesso]] — Referência cruzada direta com vault-gerenciamento-centralizado-segredos-arquitetura-acesso.

## Fontes
- [HashiCorp Vault GitHub — README.md (Secure Secret Storage, Dynamic Secrets, Data Encryption, Leasing/Renewal, Revocation & Go Libraries)](https://raw.githubusercontent.com/hashicorp/vault/main/README.md) — README oficial do HashiCorp Vault cobrindo armazenamento criptografado, segredos dinâmicos sob demanda, criptografia sem armazenamento, leases/revogação, compilação make dev e bibliotecas Go suportadas vault/api e vault/sdk; consultado em 2026-10-03.
- [HashiCorp Vault Documentation — What is Vault? (Architecture, Plugins, Access Control & Storage Backends)](https://developer.hashicorp.com/vault/docs/about-vault/what-is-vault) — Documentação oficial What is Vault? explicando o fluxo de autenticação/autorização por caminhos, categorias de plugins (auth, secret, database) e backends de armazenamento (Integrated Storage Raft, File, External e In-memory); consultado em 2026-10-03.
- [HashiCorp Vault — Official GitHub Repository](https://github.com/hashicorp/vault) — Repositório oficial do HashiCorp Vault; consultado em 2026-10-03.
