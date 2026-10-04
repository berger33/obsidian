---
id: software.devops.tranche20.001949
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
fontes: ["https://raw.githubusercontent.com/openbao/openbao/main/README.md", "https://openbao.org/docs/what-is-openbao/", "https://github.com/openbao/openbao"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenBao PKI Secrets Engine: operação de CA Intermediária X.509 interna, suporte a ACME e emissão de certificados TLS efêmeros

## Em uma frase
O **PKI Secrets Engine** do OpenBao (`bao secrets enable pki`) transforma o OpenBao em uma Autoridade Certificadora X.509 completa capaz de gerar CSRs de CA intermediária, assinar certificados TLS de curta duração sob demanda (`pki/issue/<role>`) ou via protocolo **ACME** integrado e publicar CRLs/OCSP.

## Por que importa
Em vez de manter uma infraestrutura separada apenas para emitir certificados mTLS internos para microsserviços e jobs, o mesmo cluster OpenBao que já autentica os workloads pode emitir certificados TLS válidos por poucas horas direto em memória.

## Como funciona
Com `no_store=true` configurado na role do PKI Engine para certificados de curtíssima duração (ex.: TTL de 24h), o OpenBao assina e devolve o certificado instantaneamente sem gravar cada certificado folha no storage Raft/PostgreSQL, permitindo emitir milhares de certificados por minuto sem inflar o banco.

## Exemplo
```bash
bao secrets enable -path=pki_int pki
bao write pki_int/roles/k8s-internal \
  allowed_domains="svc.cluster.local" \
  allow_subdomains=true \
  max_ttl="72h" \
  no_store=true
bao write pki_int/issue/k8s-internal common_name="payments.prod.svc.cluster.local" ttl="24h"
```

## Limites e trade-offs
Se você habilitar `no_store=true` em uma role PKI para alta escala, mantenha o `max_ttl` curto (horas), pois certificados não armazenados no backend não podem ser revogados individualmente por número de série na CRL.

## Como verificar
Emita um certificado de teste com `bao write pki_int/issue/k8s-internal ...` e verifique sua cadeia e validade com `openssl x509 -noout -text`.

## Conexões
- [[openbao-autenticacao-kubernetes-serviceaccount-jwt-token-reviewer]] — Veja também: OpenBao Kubernetes Auth Method: autenticação de Pods via `ServiceAccount` JWT (`TokenRequest` API) sem segredos estáticos.
- [[openbao-audit-devices-logs-estruturados-hmac-dados-sensiveis-sdk]] — Veja também: OpenBao Audit Devices e SDK Go (`api/v2`): trilha de auditoria à prova de falha com HMAC e bibliotecas oficiais.

## Fontes
- [OpenBao GitHub — README.md (OpenSSF/Linux Foundation Community-Driven Secrets & Encryption Management System)](https://raw.githubusercontent.com/openbao/openbao/main/README.md) — README oficial do openbao/openbao apresentando governança OpenSSF sob MPL-2.0, compilação e documentação; consultado em 2026-10-03.
- [OpenBao Official Documentation — What is OpenBao? (Authenticate/Validate/Authorize/Access Pipeline, Dynamic Secrets, Leasing & Revocation)](https://openbao.org/docs/what-is-openbao/) — Documentação oficial de arquitetura do OpenBao explicando o fluxo de 4 estágios (Authenticate, Validate, Authorize, Access), segredos dinâmicos, leases e revogação; consultado em 2026-10-03.
- [OpenBao — Official GitHub Repository](https://github.com/openbao/openbao) — Repositório oficial MPL-2.0 do OpenBao na OpenSSF; consultado em 2026-10-03.
