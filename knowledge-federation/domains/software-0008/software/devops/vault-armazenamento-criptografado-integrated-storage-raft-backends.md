---
id: software.devops.tranche10.000902
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

# HashiCorp Vault: criptografia em repouso (barreira de segurança) e backends de armazenamento (Integrated Storage Raft)

## Em uma frase
O Vault criptografa todos os dados antes de gravá-los no armazenamento persistente — de modo que obter acesso bruto ao disco ou banco não revela os segredos — e recomenda o **Integrated Storage (Raft)** como backend padrão com suporte a alta disponibilidade (HA).

## Por que importa
Em muitos sistemas tradicionais, um invasor que consiga ler um snapshot de disco ou um dump do banco de dados consegue extrair os segredos armazenados. No Vault, a barreira criptográfica separa o motor do Vault do backend de armazenamento físico, e a escolha correta do backend determina se o cluster suporta alta disponibilidade nativa e backups integrados.

## Como funciona
Conforme o README oficial (`Secure Secret Storage`) e a tabela `Where does Vault store data?` em `What is Vault?`, o Vault suporta quatro categorias de armazenamento durável: (1) **Integrated Storage (`raft`)**: opção embutida recomendada para a maioria das implantações de produção, que criptografa e replica os dados entre os nós de um cluster Vault via protocolo de consenso Raft (com suporte a HA: `YES` e snapshots nativos); (2) **File system (`file`)**: persiste os dados criptografados no sistema de arquivos local da máquina (sem suporte a HA: `NO`); (3) **External** (como Consul, AWS, Azure, Google Cloud ou MySQL): sistemas externos de terceiros (HA: `MAYBE`, dependendo do backend); e (4) **In-memory (`inmem`)**: mantém tudo em memória RAM apenas para desenvolvimento (`-dev`) e testes (HA: `NO`).

## Exemplo
```bash
# Gerar um snapshot consistente de backup do Integrated Storage (Raft) em um cluster Vault de produção
vault operator raft snapshot save /tmp/vault-raft-backup.snap
vault operator raft list-peers
```

## Limites e trade-offs
Conforme destaca a documentação oficial, o **Integrated Storage (Raft)** é preferido frente a sistemas de armazenamento externos porque suporta fluxos nativos de backup/restore, alta disponibilidade e recursos de replicação sem depender de um segundo sistema distribuído externo onde o Vault não pode verificar diretamente a segurança e a rastreabilidade de acesso aos dados subjacentes.

## Como verificar
Execute `vault operator raft list-peers` em um cluster com Integrated Storage para verificar o líder (`leader`), os seguidores (`follower`) e a saúde do quórum Raft.

## Conexões
- [[vault-gerenciamento-centralizado-segredos-arquitetura-acesso]] — Veja também: HashiCorp Vault: gerenciamento centralizado de segredos, controle de acesso e trilha de auditoria.
- [[vault-segredos-dinamicos-leases-renovacao-revogacao]] — Veja também: HashiCorp Vault: geração de Segredos Dinâmicos sob demanda, Leases, Renovação e Revogação em árvore.
- [[talos-bootstrap-etcd-gerenciamento-control-plane-ha]] — Referência cruzada direta com talos-bootstrap-etcd-gerenciamento-control-plane-ha.

## Fontes
- [HashiCorp Vault GitHub — README.md (Secure Secret Storage, Dynamic Secrets, Data Encryption, Leasing/Renewal, Revocation & Go Libraries)](https://raw.githubusercontent.com/hashicorp/vault/main/README.md) — README oficial do HashiCorp Vault cobrindo armazenamento criptografado, segredos dinâmicos sob demanda, criptografia sem armazenamento, leases/revogação, compilação make dev e bibliotecas Go suportadas vault/api e vault/sdk; consultado em 2026-10-03.
- [HashiCorp Vault Documentation — What is Vault? (Architecture, Plugins, Access Control & Storage Backends)](https://developer.hashicorp.com/vault/docs/about-vault/what-is-vault) — Documentação oficial What is Vault? explicando o fluxo de autenticação/autorização por caminhos, categorias de plugins (auth, secret, database) e backends de armazenamento (Integrated Storage Raft, File, External e In-memory); consultado em 2026-10-03.
- [HashiCorp Vault — Official GitHub Repository](https://github.com/hashicorp/vault) — Repositório oficial do HashiCorp Vault; consultado em 2026-10-03.
