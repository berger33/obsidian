---
id: software.devops.tranche20.001928
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

# CFSSL Inspeção e Diagnóstico (`cfssl certinfo` e `cfssl scan`): auditoria JSON de certificados X.509 e postura TLS de servidores

## Em uma frase
O CFSSL inclui dois subcomandos de diagnóstico para automação e segurança: **`cfssl certinfo`** (ou o binário `cfssl-certinfo`), que converte qualquer certificado X.509 local (`-cert`) ou remoto (`-domain`) em um documento JSON legível, e **`cfssl scan`** (`cfssl-scan`), que varre um host remoto avaliando sua postura de segurança TLS.

## Por que importa
Fazer parsing de texto da saída humana de `openssl x509 -in cert.pem -text -noout` com `grep`/`awk` em scripts de monitoramento de expiração é frágil; já a saída JSON nativa do `cfssl certinfo` integra-se diretamente com `jq`.

## Como funciona
Com `cfssl certinfo -cert server.pem | jq -r '.not_after, .sans'`, um script de verificação extrai com precisão a data ISO-8601 de expiração (`not_after`), os SANs (`sans`), o Serial Number, o AKI/SKI e o emissor. Já `cfssl scan -family=Connectivity,TLSSession,Certificate <host>` executa scanners modulares contra o endpoint TLS.

## Exemplo
```bash
# Extraindo a data de expiração e os SANs de um certificado em JSON estruturado:
cfssl certinfo -cert ca.pem | jq '{subject: .subject.common_name, not_after: .not_after, sans: .sans}'

# Listando as famílias de scanners TLS disponíveis no cfssl scan:
cfssl scan -list
```

## Limites e trade-offs
Ao usar `cfssl certinfo -domain api.corp.internal:443`, é possível passar a flag `-ip <endereco_ip>` para inspecionar o certificado retornado por uma réplica específica atrás de um balanceador ou DNS round-robin.

## Como verificar
Execute `cfssl certinfo -cert ca.pem` e valide os campos `not_before`, `not_after` e `serial_number`.

## Conexões
- [[cfssl-multirootca-servidor-ca-multiplas-chaves-labels]] — Veja também: CFSSL `multirootca`: operação de servidor de Autoridade Certificadora com múltiplas chaves e perfis isolados por `label`.
- [[cfssl-ocsp-responder-certdb-revogacao-ocspserve-ocspsign]] — Veja também: CFSSL OCSP e Banco de Certificados (`certdb`): rastreamento de certificados emitidos, revogação e servidor `ocspserve`.

## Fontes
- [Cloudflare CFSSL GitHub — README.md (PKI/TLS Swiss Army Knife, CLI Tools, Signing Profiles, CSR Generation, Bundle Flavors & Multirootca)](https://raw.githubusercontent.com/cloudflare/cfssl/master/README.md) — README oficial do cloudflare/cfssl detalhando a suíte de binários, perfis de assinatura, geração de CA/certificados, flavors de bundle e servidor API; consultado em 2026-10-03.
- [Cloudflare CFSSL Official CLI Reference — doc/cmd/cfssl.txt (Subcommands: bundle, certinfo, gencert, gencsr, ocsprefresh, ocspserve, scan & serve)](https://raw.githubusercontent.com/cloudflare/cfssl/master/doc/cmd/cfssl.txt) — Referência oficial de subcomandos e flags da CLI cfssl; consultado em 2026-10-03.
- [Cloudflare CFSSL — Official GitHub Repository](https://github.com/cloudflare/cfssl) — Repositório oficial BSD-2-Clause do Cloudflare CFSSL; consultado em 2026-10-03.
