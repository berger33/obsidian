---
id: software.devops.tranche20.001948
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

# OpenBao Kubernetes Auth Method: autenticação de Pods via `ServiceAccount` JWT (`TokenRequest` API) sem segredos estáticos

## Em uma frase
Para que aplicações rodando no Kubernetes se autentiquem no OpenBao sem embutir tokens fixos em variáveis de ambiente, o método de autenticação **`auth/kubernetes`** valida o token JWT de curta duração da `ServiceAccount` do Pod diretamente contra a API **`TokenReview`** do `kube-apiserver`.

## Por que importa
Distribuir `AppRole` `secret_id` estáticos para Pods no Kubernetes transfere o problema do "segredo zero" para os manifestos de deploy.

## Como funciona
Com o método `kubernetes` habilitado no OpenBao (`bao auth enable kubernetes`), o administrador vincula uma role do OpenBao (ex.: `payment-role`) a nomes específicos de `bound_service_account_names`, `bound_service_account_namespaces` e `policies`. No boot do Pod, o container lê `/var/run/secrets/kubernetes.io/serviceaccount/token` e envia ao endpoint `auth/kubernetes/login` para receber um token OpenBao com TTL curto.

## Exemplo
```bash
bao auth enable kubernetes
bao write auth/kubernetes/role/payment-role \
  bound_service_account_names=payment-sa \
  bound_service_account_namespaces=prod \
  policies=payment-app \
  ttl=1h
```

## Limites e trade-offs
Em clusters Kubernetes 1.24+, utilize tokens de `ServiceAccount` projetados (`projectedVolume` com `expirationSeconds` curto) para que o JWT usado no login também expire rapidamente.

## Como verificar
Teste o login a partir de um Pod autorizado enviando o JWT da ServiceAccount para `v1/auth/kubernetes/login` e inspecione as políticas anexadas com `bao token lookup`.

## Conexões
- [[openbao-politicas-hcl-path-capabilities-least-privilege-tokens]] — Veja também: OpenBao Políticas HCL (*Path-Based Policies*): controle declarativo de capacidades (`create`, `read`, `update`, `delete`, `list`, `sudo`).
- [[openbao-pki-secrets-engine-ca-interna-acme-emissao-certificados]] — Veja também: OpenBao PKI Secrets Engine: operação de CA Intermediária X.509 interna, suporte a ACME e emissão de certificados TLS efêmeros.

## Fontes
- [OpenBao GitHub — README.md (OpenSSF/Linux Foundation Community-Driven Secrets & Encryption Management System)](https://openbao.org/docs/what-is-openbao/) — README oficial do openbao/openbao apresentando governança OpenSSF sob MPL-2.0, compilação e documentação; consultado em 2026-10-03.
- [OpenBao Official Documentation — What is OpenBao? (Authenticate/Validate/Authorize/Access Pipeline, Dynamic Secrets, Leasing & Revocation)](https://raw.githubusercontent.com/openbao/openbao/main/README.md) — Documentação oficial de arquitetura do OpenBao explicando o fluxo de 4 estágios (Authenticate, Validate, Authorize, Access), segredos dinâmicos, leases e revogação; consultado em 2026-10-03.
- [OpenBao — Official GitHub Repository](https://github.com/openbao/openbao) — Repositório oficial MPL-2.0 do OpenBao na OpenSSF; consultado em 2026-10-03.
