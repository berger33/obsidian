---
id: software.devops.tranche10.000908
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

# HashiCorp Vault: emissão automatizada de certificados X.509 de curta duração como Autoridade Certificadora (PKI)

## Em uma frase
Conforme destacado em `Why should I use Vault?` (`Manage certificates`), o Vault pode atuar como uma Autoridade Certificadora (CA) intermediária interna via motor **PKI**, gerando certificados TLS X.509 e chaves privadas sob demanda com TTL curto e sem fila manual de CSR.

## Por que importa
Em arquiteturas Zero Trust e mTLS entre microsserviços, emitir certificados manualmente com validade de 1 ano e copiá-los em Secrets estáticos leva a quedas catastróficas quando alguém esquece de renovar um certificado vencido; além disso, revogar certificados de longa duração exige distribuir listas CRL pesadas. Com o motor PKI do Vault, os certificados podem durar poucas horas ou dias e ser renovados automaticamente.

## Como funciona
A equipe de segurança habilita o motor PKI (`vault secrets enable pki`), configura uma CA Intermediária assinada pela CA Raiz offline da organização e define um papel (`vault write pki/roles/servico-interno allowed_domains="interno.empresa.com" allow_subdomains=true max_ttl="72h"`). Quando um workload (ou o `cert-manager` no Kubernetes integrado ao Issuer do Vault) solicita um certificado em **`vault write pki/issue/servico-interno common_name="api.interno.empresa.com"`**, o Vault gera o par de chaves, assina o certificado X.509 instantaneamente e o devolve na resposta da API.

## Exemplo
```bash
# Solicitar a emissão instantânea de um certificado TLS X.509 de curta duração (24h) para um serviço interno
vault write pki/issue/servico-interno \
  common_name="checkout.interno.empresa.com" \
  ttl="24h"
```

## Limites e trade-offs
Quando o motor PKI do Vault emite milhares de certificados de curtíssima duração (por exemplo, a cada poucas horas para centenas de pods) com armazenamento padrão de certificados emitidos (`no_store=false`), o estado no storage Raft do Vault crescerá rapidamente com certificados expirados; para evitar inchaço do storage, habilite `no_store=true` no role PKI (quando revogação individual por número de série não for necessária) e configure a limpeza periódica (`vault write pki/tidy ...`).

## Como verificar
Emita um certificado de teste e inspecione a cadeia e a data de expiração com `vault write -field=certificate pki/issue/servico-interno common_name="teste.interno.empresa.com" | openssl x509 -noout -text`.

## Conexões
- [[vault-motor-segredos-estaticos-kv-v2-versionamento-check-and-set]] — Veja também: HashiCorp Vault: gerenciamento de segredos estáticos (KV Secrets Engine v2), versionamento e Check-and-Set (CAS).
- [[vault-integracao-kubernetes-auth-injector-csi-eso]] — Veja também: HashiCorp Vault: padrões de integração com Kubernetes (Kubernetes Auth, Vault Agent Injector, CSI e ESO).
- [[vault-gerenciamento-centralizado-segredos-arquitetura-acesso]] — Referência cruzada direta com vault-gerenciamento-centralizado-segredos-arquitetura-acesso.
- [[vault-segredos-dinamicos-leases-renovacao-revogacao]] — Referência cruzada direta com vault-segredos-dinamicos-leases-renovacao-revogacao.
- [[k3s-gerenciamento-certificados-tls-rotacao-operacoes]] — Referência cruzada direta com k3s-gerenciamento-certificados-tls-rotacao-operacoes.

## Fontes
- [HashiCorp Vault GitHub — README.md (Secure Secret Storage, Dynamic Secrets, Data Encryption, Leasing/Renewal, Revocation & Go Libraries)](https://raw.githubusercontent.com/hashicorp/vault/main/README.md) — README oficial do HashiCorp Vault cobrindo armazenamento criptografado, segredos dinâmicos sob demanda, criptografia sem armazenamento, leases/revogação, compilação make dev e bibliotecas Go suportadas vault/api e vault/sdk; consultado em 2026-10-03.
- [HashiCorp Vault Documentation — What is Vault? (Architecture, Plugins, Access Control & Storage Backends)](https://developer.hashicorp.com/vault/docs/about-vault/what-is-vault) — Documentação oficial What is Vault? explicando o fluxo de autenticação/autorização por caminhos, categorias de plugins (auth, secret, database) e backends de armazenamento (Integrated Storage Raft, File, External e In-memory); consultado em 2026-10-03.
- [HashiCorp Vault — Official GitHub Repository](https://github.com/hashicorp/vault) — Repositório oficial do HashiCorp Vault; consultado em 2026-10-03.
