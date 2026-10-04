---
id: software.devops.tranche10.000904
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

# HashiCorp Vault: criptografia de dados como serviço (Encryption as a Service) sem armazenar os dados no Vault

## Em uma frase
A capacidade de **Data Encryption** (implementada pelo motor `transit`) permite que o Vault criptografe e descriptografe dados em trânsito via API sem armazená-los no Vault, delegando à equipe de segurança o controle dos parâmetros criptográficos e da rotação de chaves.

## Por que importa
Quando desenvolvedores precisam criptografar colunas sensíveis (como CPF, números de documentos ou tokens financeiros) antes de gravar em um banco SQL convencional, implementar criptografia manualmente em cada linguagem de programação frequentemente leva a escolhas inseguras de algoritmos/IVs e ao problema de onde guardar e como rotacionar a chave de criptografia na aplicação. O README oficial (`Data Encryption`) destaca como o Vault resolve esse problema.

## Como funciona
A equipe de segurança habilita o motor de criptografia (`vault secrets enable transit`) e cria uma chave nomeada (`vault write -f transit/keys/pagamentos-key`) definindo o algoritmo e políticas de rotação. Quando a aplicação precisa proteger um dado sensível antes de fazer `INSERT` no seu próprio banco SQL, ela envia o texto em base64 para **`transit/encrypt/pagamentos-key`** e recebe de volta o texto cifrado prefixado (`vault:v1:...`), gravando esse ciphertext no banco SQL. O Vault **nunca armazena o dado da aplicação**: ele apenas executa a operação criptográfica em memória e retorna o resultado; para ler o dado depois, a aplicação envia o ciphertext para **`transit/decrypt/pagamentos-key`**.

## Exemplo
```bash
# Habilitar o motor transit, criar uma chave de criptografia e cifrar um dado sem armazená-lo no Vault
vault secrets enable transit
vault write -f transit/keys/app-pii-key
vault write transit/encrypt/app-pii-key plaintext=$(echo -n "dado-sensivel-123" | base64)
```

## Limites e trade-offs
Como toda operação de `encrypt` e `decrypt` faz uma chamada de rede HTTP/HTTPS para o cluster Vault, cifrar milhares de linhas individualmente dentro de um loop em uma única requisição web adicionará latência de rede; para alto volume, utilize o suporte a **batch input** (`batch_input` na API do `transit`) ou envelope encryption (gerando uma Data Key local via `transit/datakey/plaintext/<key>`).

## Como verificar
Execute `vault write -f transit/keys/app-pii-key/rotate` para rotacionar a chave para a versão `v2` e confirme que textos antigos (`vault:v1:...`) continuam sendo descriptografados normalmente enquanto novos textos saem com `vault:v2:...`.

## Conexões
- [[vault-segredos-dinamicos-leases-renovacao-revogacao]] — Veja também: HashiCorp Vault: geração de Segredos Dinâmicos sob demanda, Leases, Renovação e Revogação em árvore.
- [[vault-ecossistema-plugins-auth-secrets-database]] — Veja também: HashiCorp Vault: arquitetura modular de plugins (Authentication, General Secrets e Database Plugins).
- [[vault-gerenciamento-centralizado-segredos-arquitetura-acesso]] — Referência cruzada direta com vault-gerenciamento-centralizado-segredos-arquitetura-acesso.
- [[sops-editor-arquivos-criptografados-yaml-json-env-ini]] — Referência cruzada direta com sops-editor-arquivos-criptografados-yaml-json-env-ini.

## Fontes
- [HashiCorp Vault GitHub — README.md (Secure Secret Storage, Dynamic Secrets, Data Encryption, Leasing/Renewal, Revocation & Go Libraries)](https://raw.githubusercontent.com/hashicorp/vault/main/README.md) — README oficial do HashiCorp Vault cobrindo armazenamento criptografado, segredos dinâmicos sob demanda, criptografia sem armazenamento, leases/revogação, compilação make dev e bibliotecas Go suportadas vault/api e vault/sdk; consultado em 2026-10-03.
- [HashiCorp Vault Documentation — What is Vault? (Architecture, Plugins, Access Control & Storage Backends)](https://developer.hashicorp.com/vault/docs/about-vault/what-is-vault) — Documentação oficial What is Vault? explicando o fluxo de autenticação/autorização por caminhos, categorias de plugins (auth, secret, database) e backends de armazenamento (Integrated Storage Raft, File, External e In-memory); consultado em 2026-10-03.
- [HashiCorp Vault — Official GitHub Repository](https://github.com/hashicorp/vault) — Repositório oficial do HashiCorp Vault; consultado em 2026-10-03.
