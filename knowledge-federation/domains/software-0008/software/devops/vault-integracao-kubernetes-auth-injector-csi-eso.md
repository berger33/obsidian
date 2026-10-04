---
id: software.devops.tranche10.000909
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

# HashiCorp Vault: padrões de integração com Kubernetes (Kubernetes Auth, Vault Agent Injector, CSI e ESO)

## Em uma frase
Em clusters Kubernetes, os workloads autenticam-se no Vault apresentando o JWT de sua `ServiceAccount` ao método de autenticação **Kubernetes Auth**, podendo consumir segredos via **External Secrets Operator (ESO)**, **Vault Agent Sidecar Injector**, **Vault Secrets Operator (VSO)** ou **Secrets Store CSI Driver**.

## Por que importa
Para que os pods no Kubernetes consigam buscar segredos no Vault sem precisar de um token estático do Vault pré-gravado na imagem ou no manifesto YAML (o problema do "secret zero"), o Vault precisa confiar na identidade nativa fornecida pelo API Server do Kubernetes.

## Como funciona
O administrador habilita `vault auth enable kubernetes`, configura o endereço e o certificado do API Server do Kubernetes e cria papéis (`vault write auth/kubernetes/role/minha-app bound_service_account_names=app-sa bound_service_account_namespaces=prod policies=pagamentos-ro ttl=1h`). No momento em que o pod inicia no cluster, o JWT projetado pelo Kubernetes para a ServiceAccount `app-sa` no namespace `prod` é enviado ao endpoint **`auth/kubernetes/login`**: o Vault valida a assinatura do JWT na API `TokenReview` do Kubernetes e devolve um token do Vault com a política `pagamentos-ro`, permitindo que o ESO sincronize `Secret`s ou que o Vault Agent injete templates no pod em `/vault/secrets/`.

## Exemplo
```bash
# Configurar um papel no método de autenticação Kubernetes do Vault vinculando ServiceAccount e Namespace a uma Policy
vault write auth/kubernetes/role/orders-service \
  bound_service_account_names=orders-sa \
  bound_service_account_namespaces=production \
  policies=orders-prod-policy \
  ttl=1h
```

## Limites e trade-offs
Enquanto o **External Secrets Operator (ESO)** e o **Vault Secrets Operator (VSO)** sincronizam segredos do Vault para objetos `Kind=Secret` nativos do Kubernetes (permitindo que as aplicações continuem lendo variáveis de ambiente ou volumes padrão sem saber que o Vault existe), o **Vault Agent Sidecar Injector** renderiza os segredos diretamente em um volume compartilhado em memória (`tmpfs` em `/vault/secrets/`) sem nunca gravar um `Secret` no `etcd` do Kubernetes, ao custo de adicionar um container sidecar em cada pod.

## Como verificar
De dentro de um pod usando a ServiceAccount `orders-sa`, envie o token `/var/run/secrets/kubernetes.io/serviceaccount/token` para `v1/auth/kubernetes/login` e confirme o recebimento do `client_token` do Vault.

## Conexões
- [[vault-gerenciamento-certificados-pki-x509-ca-interna]] — Veja também: HashiCorp Vault: emissão automatizada de certificados X.509 de curta duração como Autoridade Certificadora (PKI).
- [[vault-bibliotecas-go-api-sdk-desenvolvimento-testes]] — Veja também: HashiCorp Vault: compilação a partir do código-fonte (make dev/dev-ui) e bibliotecas oficiais Go (vault/api e vault/sdk).
- [[vault-gerenciamento-centralizado-segredos-arquitetura-acesso]] — Referência cruzada direta com vault-gerenciamento-centralizado-segredos-arquitetura-acesso.
- [[externalsecrets-operador-kubernetes-sincronizacao-segredos-externos]] — Referência cruzada direta com externalsecrets-operador-kubernetes-sincronizacao-segredos-externos.
- [[externalsecrets-modelo-recursos-secretstore-externalsecret-clustersecretstore]] — Referência cruzada direta com externalsecrets-modelo-recursos-secretstore-externalsecret-clustersecretstore.

## Fontes
- [HashiCorp Vault GitHub — README.md (Secure Secret Storage, Dynamic Secrets, Data Encryption, Leasing/Renewal, Revocation & Go Libraries)](https://raw.githubusercontent.com/hashicorp/vault/main/README.md) — README oficial do HashiCorp Vault cobrindo armazenamento criptografado, segredos dinâmicos sob demanda, criptografia sem armazenamento, leases/revogação, compilação make dev e bibliotecas Go suportadas vault/api e vault/sdk; consultado em 2026-10-03.
- [HashiCorp Vault Documentation — What is Vault? (Architecture, Plugins, Access Control & Storage Backends)](https://developer.hashicorp.com/vault/docs/about-vault/what-is-vault) — Documentação oficial What is Vault? explicando o fluxo de autenticação/autorização por caminhos, categorias de plugins (auth, secret, database) e backends de armazenamento (Integrated Storage Raft, File, External e In-memory); consultado em 2026-10-03.
- [HashiCorp Vault — Official GitHub Repository](https://github.com/hashicorp/vault) — Repositório oficial do HashiCorp Vault; consultado em 2026-10-03.
