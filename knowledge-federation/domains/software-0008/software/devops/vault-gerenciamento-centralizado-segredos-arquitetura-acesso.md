---
id: software.devops.tranche10.000901
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

# HashiCorp Vault: gerenciamento centralizado de segredos, controle de acesso e trilha de auditoria

## Em uma frase
O HashiCorp Vault (`hashicorp/vault`) é uma ferramenta para acesso seguro a segredos (chaves de API, senhas de bancos de dados, certificados e chaves criptográficas) que oferece uma interface unificada, controle de acesso estrito baseado em políticas e registro detalhado de auditoria.

## Por que importa
Em arquiteturas modernas distribuídas, credenciais acabam espalhadas em variáveis de ambiente, arquivos de configuração e pipelines de CI/CD de forma específica para cada plataforma, tornando quase impossível responder quem acessou qual segredo, rotacionar chaves ou revogar credenciais após um incidente. Segundo o README oficial e a página `What is Vault?` (`developer.hashicorp.com/vault/docs/about-vault/what-is-vault`), o Vault centraliza e endurece o gerenciamento de segredos on-premises, em nuvem ou em ambientes híbridos.

## Como funciona
Conforme documenta o fluxo oficial em `What is Vault?`: (1) os clientes autenticam-se no Vault utilizando tokens gerados manualmente, protocolos como LDAP/OIDC ou provedores de nuvem/orquestração como AWS, Azure e Kubernetes; (2) o Vault valida a identidade e gera um **access token** vinculado a uma entidade interna e às políticas de segurança aplicáveis; (3) o cliente interage com segredos e operações de criptografia através de caminhos de recursos (**resource paths**) montados no Vault; (4) o Vault autoriza a requisição contra as políticas definidas para aquele caminho e concede ou nega o acesso; e (5) durante todo o processo, o Vault grava logs de auditoria detalhados independentemente de a autenticação ou autorização ter tido sucesso ou falhado.

## Exemplo
```bash
# Iniciar um servidor Vault local em modo dev para experimentação e verificar o status do cluster
vault server -dev -dev-root-token-id="dev-only-token"
export VAULT_ADDR="http://127.0.0.1:8200"
vault status
```

## Limites e trade-offs
Como ressalta a própria documentação oficial (`When should I not use Vault?`), o Vault é extremamente robusto e flexível, mas planejar, implantar e operar um cluster Vault auto-hospedado em alta disponibilidade exige disciplina operacional (gerenciamento de unseal, backups de storage e políticas); para equipes com necessidades iniciais ou que desejam evitar o overhead operacional de manter servidores, a documentação sugere avaliar o serviço gerenciado `HCP Vault Dedicated`.

## Como verificar
Execute `vault status` apontando para `VAULT_ADDR` e confirme que o servidor responde informando o estado de inicialização (`Initialized: true`), o estado de selamento (`Sealed: false`) e o tipo de armazenamento (`Storage Type`).

## Conexões
- [[vault-armazenamento-criptografado-integrated-storage-raft-backends]] — Veja também: HashiCorp Vault: criptografia em repouso (barreira de segurança) e backends de armazenamento (Integrated Storage Raft).
- [[vault-segredos-dinamicos-leases-renovacao-revogacao]] — Referência cruzada direta com vault-segredos-dinamicos-leases-renovacao-revogacao.
- [[externalsecrets-operador-kubernetes-sincronizacao-segredos-externos]] — Referência cruzada direta com externalsecrets-operador-kubernetes-sincronizacao-segredos-externos.

## Fontes
- [HashiCorp Vault GitHub — README.md (Secure Secret Storage, Dynamic Secrets, Data Encryption, Leasing/Renewal, Revocation & Go Libraries)](https://raw.githubusercontent.com/hashicorp/vault/main/README.md) — README oficial do HashiCorp Vault cobrindo armazenamento criptografado, segredos dinâmicos sob demanda, criptografia sem armazenamento, leases/revogação, compilação make dev e bibliotecas Go suportadas vault/api e vault/sdk; consultado em 2026-10-03.
- [HashiCorp Vault Documentation — What is Vault? (Architecture, Plugins, Access Control & Storage Backends)](https://developer.hashicorp.com/vault/docs/about-vault/what-is-vault) — Documentação oficial What is Vault? explicando o fluxo de autenticação/autorização por caminhos, categorias de plugins (auth, secret, database) e backends de armazenamento (Integrated Storage Raft, File, External e In-memory); consultado em 2026-10-03.
- [HashiCorp Vault — Official GitHub Repository](https://github.com/hashicorp/vault) — Repositório oficial do HashiCorp Vault; consultado em 2026-10-03.
