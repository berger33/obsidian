---
id: software.devops.tranche20.001927
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
fontes: ["https://raw.githubusercontent.com/cloudflare/cfssl/master/README.md", "https://raw.githubusercontent.com/cloudflare/cfssl/master/doc/cmd/cfssl.txt", "https://github.com/cloudflare/cfssl"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# CFSSL `multirootca`: operação de servidor de Autoridade Certificadora com múltiplas chaves e perfis isolados por `label`

## Em uma frase
O binário **`multirootca`** do pacote CFSSL é um servidor de Autoridade Certificadora dedicado capaz de carregar e operar **múltiplas chaves de assinatura independentes** (por exemplo, uma CA para o cluster Kubernetes de produção, outra CA para o etcd e uma terceira CA para clientes VPN) diferenciadas por **`label`** em um arquivo de configuração `.ini`.

## Por que importa
Enquanto `cfssl serve` opera com uma única CA local por processo, manter 10 processos separados para 10 CAs intermediárias diferentes aumenta o overhead operacional.

## Como funciona
No arquivo de configuração do `multirootca`, cada seção `[label_name]` define `private = file://...` (ou PKCS#11), `certificate = ...` e `config = ca-config.json`. Os clientes `cfssl` enviam requisições autenticadas especificando o `label` desejado para assinar o certificado com a CA correspondente.

## Exemplo
```ini
[kube_ca]
private = file:///etc/cfssl/kube-ca-key.pem
certificate = /etc/cfssl/kube-ca.pem
config = /etc/cfssl/ca-config.json

[etcd_ca]
private = file:///etc/cfssl/etcd-ca-key.pem
certificate = /etc/cfssl/etcd-ca.pem
config = /etc/cfssl/ca-config.json
```

## Limites e trade-offs
Proteja as chaves privadas referenciadas pelo `multirootca` com permissões `0400` restritas ao usuário de serviço do processo e exija autenticação `auth_keys` em todos os perfis.

## Como verificar
Inicie `multirootca -roots roots.ini -l default_label` e consulte o certificado público de cada label via endpoint `/api/v1/cfssl/info`.

## Conexões
- [[cfssl-bundle-flavors-optimal-ubiquitous-force-cfssl-trust]] — Veja também: CFSSL Certificate Bundling (`cfssl bundle` e `mkbundle`): montagem de cadeias TLS nos modos `optimal`, `ubiquitous` e `force`.
- [[cfssl-certinfo-scan-inspecao-certificados-auditoria-tls-hosts]] — Veja também: CFSSL Inspeção e Diagnóstico (`cfssl certinfo` e `cfssl scan`): auditoria JSON de certificados X.509 e postura TLS de servidores.

## Fontes
- [Cloudflare CFSSL GitHub — README.md (PKI/TLS Swiss Army Knife, CLI Tools, Signing Profiles, CSR Generation, Bundle Flavors & Multirootca)](https://raw.githubusercontent.com/cloudflare/cfssl/master/README.md) — README oficial do cloudflare/cfssl detalhando a suíte de binários, perfis de assinatura, geração de CA/certificados, flavors de bundle e servidor API; consultado em 2026-10-03.
- [Cloudflare CFSSL Official CLI Reference — doc/cmd/cfssl.txt (Subcommands: bundle, certinfo, gencert, gencsr, ocsprefresh, ocspserve, scan & serve)](https://raw.githubusercontent.com/cloudflare/cfssl/master/doc/cmd/cfssl.txt) — Referência oficial de subcomandos e flags da CLI cfssl; consultado em 2026-10-03.
- [Cloudflare CFSSL — Official GitHub Repository](https://github.com/cloudflare/cfssl) — Repositório oficial BSD-2-Clause do Cloudflare CFSSL; consultado em 2026-10-03.
