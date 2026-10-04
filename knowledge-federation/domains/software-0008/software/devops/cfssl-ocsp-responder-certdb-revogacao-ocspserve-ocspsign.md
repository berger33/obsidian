---
id: software.devops.tranche20.001929
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
fontes: ["https://raw.githubusercontent.com/cloudflare/cfssl/master/doc/cmd/cfssl.txt", "https://raw.githubusercontent.com/cloudflare/cfssl/master/README.md", "https://github.com/cloudflare/cfssl"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# CFSSL OCSP e Banco de Certificados (`certdb`): rastreamento de certificados emitidos, revogação e servidor `ocspserve`

## Em uma frase
Para ambientes que exigem revogação ativa e verificação de status de certificados via **OCSP (*Online Certificate Status Protocol*)** ou **CRL**, o CFSSL integra-se a um banco de dados relacional (`-db-config`, suportando SQLite, PostgreSQL e MySQL via migrações `goose`) e fornece os subcomandos **`ocspPolicy`**, **`ocspsign`**, **`ocsprefresh`**, **`ocspdump`** e **`ocspserve`**.

## Por que importa
Sem um banco de dados (`certdb`) configurado no `cfssl serve`, a CA assina certificados de forma *stateless* sem manter inventário dos números de série emitidos, o que impede revogar um certificado específico ou pré-gerar respostas OCSP assinadas.

## Como funciona
Com `-db-config=db-config.json`, cada certificado emitido é registrado na tabela `certificates`. Quando um certificado é revogado via `cfssl revoke`, o comando `cfssl ocsprefresh` recalcula e assina as respostas OCSP (usando um certificado com extensão `ocsp signing` e `ocsp_no_check: true`) e o `cfssl ocspserve` responde às consultas RFC 2560 dos clientes.

## Exemplo
```bash
# Gerando e servindo respostas OCSP a partir do banco de certificados do CFSSL:
cfssl ocsprefresh -db-config=db-config.json \
  -responder=ocsp.pem -responder-key=ocsp-key.pem -ca=ca.pem
cfssl ocspdump -db-config=db-config.json > ocsp-responses.txt
cfssl ocspserve -port=8889 -responses=ocsp-responses.txt
```

## Limites e trade-offs
Conforme documentado em `doc/cmd/cfssl.txt`, o perfil que emite o certificado do próprio *OCSP Responder* deve incluir `"usages": ["digital signature", "ocsp signing"]` e `"ocsp_no_check": true` (extensão `id-pkix-ocsp-nocheck` da RFC 2560).

## Como verificar
Verifique no perfil do OCSP Responder a presença de `ocsp signing` e `ocsp_no_check: true` usando `cfssl certinfo`.

## Conexões
- [[cfssl-certinfo-scan-inspecao-certificados-auditoria-tls-hosts]] — Veja também: CFSSL Inspeção e Diagnóstico (`cfssl certinfo` e `cfssl scan`): auditoria JSON de certificados X.509 e postura TLS de servidores.
- [[cfssl-bootstrap-pki-kubernetes-etcd-front-proxy-service-account]] — Veja também: CFSSL para Kubernetes "The Hard Way": automação completa das CAs de cluster (`kubernetes-ca`, `etcd-ca` e `front-proxy-ca`).

## Fontes
- [Cloudflare CFSSL GitHub — README.md (PKI/TLS Swiss Army Knife, CLI Tools, Signing Profiles, CSR Generation, Bundle Flavors & Multirootca)](https://raw.githubusercontent.com/cloudflare/cfssl/master/doc/cmd/cfssl.txt) — README oficial do cloudflare/cfssl detalhando a suíte de binários, perfis de assinatura, geração de CA/certificados, flavors de bundle e servidor API; consultado em 2026-10-03.
- [Cloudflare CFSSL Official CLI Reference — doc/cmd/cfssl.txt (Subcommands: bundle, certinfo, gencert, gencsr, ocsprefresh, ocspserve, scan & serve)](https://raw.githubusercontent.com/cloudflare/cfssl/master/README.md) — Referência oficial de subcomandos e flags da CLI cfssl; consultado em 2026-10-03.
- [Cloudflare CFSSL — Official GitHub Repository](https://github.com/cloudflare/cfssl) — Repositório oficial BSD-2-Clause do Cloudflare CFSSL; consultado em 2026-10-03.
