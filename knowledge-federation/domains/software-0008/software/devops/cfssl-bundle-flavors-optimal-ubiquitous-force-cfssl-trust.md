---
id: software.devops.tranche20.001926
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

# CFSSL Certificate Bundling (`cfssl bundle` e `mkbundle`): montagem de cadeias TLS nos modos `optimal`, `ubiquitous` e `force`

## Em uma frase
O subcomando **`cfssl bundle`** (apoiado pelo repositório de metadados `cfssl_trust` e pelo utilitário `mkbundle`) recebe um certificado folha (`-cert`) ou domínio remoto (`-domain`) e monta automaticamente a cadeia completa de certificados intermediários (*certificate bundle*) em três sabores (`-flavor`): **`optimal`**, **`ubiquitous`** e **`force`**.

## Por que importa
Servidores TLS mal configurados frequentemente enviam apenas o certificado folha sem os certificados intermediários (causando erro `x509: certificate signed by unknown authority` em clientes CLI/Go/Python que não fazem *AIA chasing*) ou enviam cadeias longas com algoritmos legados.

## Como funciona
Os três valores de `-flavor` atendem cenários distintos: 1) **`optimal`** constrói a cadeia mais curta possível priorizando os algoritmos criptográficos mais modernos; 2) **`ubiquitous`** constrói a cadeia com maior compatibilidade ampla entre diferentes navegadores e sistemas operacionais; e 3) **`force`** valida e preserva um bundle idêntico ao arquivo de entrada.

## Exemplo
```bash
# Construindo e verificando o bundle ótimo de um certificado local ou de um domínio remoto:
cfssl bundle -ca-bundle ca-bundle.crt \
  -int-bundle int-bundle.crt \
  -flavor optimal \
  -cert leaf.pem
```

## Limites e trade-offs
O JSON retornado por `cfssl bundle` inclui diagnósticos ricos no objeto `status` (`rebundled`, `expiring_SKIs`, `untrusted_root_stores`, `ocsp_support`, `crl_support`), alertando se algum intermediário da cadeia está próximo de expirar.

## Como verificar
Execute `cfssl bundle -cert server.pem` (com os bundles de root/intermediárias informados) e verifique se `status.code` é `0`.

## Conexões
- [[cfssl-serve-api-server-auth-keys-remote-signers-failover]] — Veja também: CFSSL API Server (`cfssl serve`), `auth_keys` e `remotes`: assinatura remota autenticada por HMAC e failover de CAs.
- [[cfssl-multirootca-servidor-ca-multiplas-chaves-labels]] — Veja também: CFSSL `multirootca`: operação de servidor de Autoridade Certificadora com múltiplas chaves e perfis isolados por `label`.

## Fontes
- [Cloudflare CFSSL GitHub — README.md (PKI/TLS Swiss Army Knife, CLI Tools, Signing Profiles, CSR Generation, Bundle Flavors & Multirootca)](https://raw.githubusercontent.com/cloudflare/cfssl/master/README.md) — README oficial do cloudflare/cfssl detalhando a suíte de binários, perfis de assinatura, geração de CA/certificados, flavors de bundle e servidor API; consultado em 2026-10-03.
- [Cloudflare CFSSL Official CLI Reference — doc/cmd/cfssl.txt (Subcommands: bundle, certinfo, gencert, gencsr, ocsprefresh, ocspserve, scan & serve)](https://raw.githubusercontent.com/cloudflare/cfssl/master/doc/cmd/cfssl.txt) — Referência oficial de subcomandos e flags da CLI cfssl; consultado em 2026-10-03.
- [Cloudflare CFSSL — Official GitHub Repository](https://github.com/cloudflare/cfssl) — Repositório oficial BSD-2-Clause do Cloudflare CFSSL; consultado em 2026-10-03.
