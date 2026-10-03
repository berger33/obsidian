---
id: software.devops.tranche20.001921
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

# CFSSL: arquitetura do toolkit de PKI e TLS da Cloudflare (`cfssl`, `cfssljson`, `mkbundle`, `multirootca` e `cfssl-scan`)

## Em uma frase
O **CFSSL** é o "canivete suíço" open-source de PKI e TLS desenvolvido pela **Cloudflare** em Go, funcionando tanto como uma suíte de utilitários de linha de comando quanto como um servidor de API HTTP para geração de chaves, assinatura de CSRs, empacotamento de cadeias de certificados (*bundling*) e resposta OCSP.

## Por que importa
Automatizar a criação de uma Autoridade Certificadora (CA) raiz, CAs intermediárias e dezenas de certificados de servidor/cliente usando o comando `openssl ca` tradicional exige manter arquivos `openssl.cnf` crípticos, diretórios `newcerts/` e arquivos `index.txt`/`serial` difíceis de versionar.

## Como funciona
No CFSSL, toda a entrada e saída utiliza **JSON estruturado**: 1) o binário principal **`cfssl`** executa operações (`genkey`, `gencert`, `sign`, `bundle`, `serve`, `selfsign`, `print-defaults`); 2) o utilitário **`cfssljson`** lê o JSON emitido pelo `cfssl` no `stdout` e grava no disco os arquivos `.pem` (certificado), `-key.pem` (chave privada) e `.csr`; 3) o **`multirootca`** serve múltiplas chaves de assinatura; e 4) o **`mkbundle`** / **`cfssl-bundle`** constrói pools de certificados.

## Exemplo
```bash
# Imprimindo os templates JSON padrão de configuração e CSR do CFSSL:
cfssl print-defaults config > ca-config.json
cfssl print-defaults csr > ca-csr.json
cfssl version
```

## Limites e trade-offs
Conforme documentado no README oficial do CFSSL, determinadas distribuições Linux baseadas em RHEL removem certas curvas/algoritmos do pacote Go dos repositórios oficiais da distro; nesses sistemas, instale a distribuição oficial do Go (`golang.org/dl`) para compilar o CFSSL.

## Como verificar
Execute `cfssl version` e `cfssl print-defaults config` para validar a instalação dos binários `cfssl` e `cfssljson`.

## Conexões
- [[cfssl-inicializacao-root-ca-intermediate-ca-genkey-initca-ca-constraint]] — Veja também: CFSSL Inicialização de Root CA e Intermediate CA: uso de `cfssl gencert -initca`, `cfssljson -bare` e `ca_constraint`.

## Fontes
- [Cloudflare CFSSL GitHub — README.md (PKI/TLS Swiss Army Knife, CLI Tools, Signing Profiles, CSR Generation, Bundle Flavors & Multirootca)](https://raw.githubusercontent.com/cloudflare/cfssl/master/README.md) — README oficial do cloudflare/cfssl detalhando a suíte de binários, perfis de assinatura, geração de CA/certificados, flavors de bundle e servidor API; consultado em 2026-10-03.
- [Cloudflare CFSSL Official CLI Reference — doc/cmd/cfssl.txt (Subcommands: bundle, certinfo, gencert, gencsr, ocsprefresh, ocspserve, scan & serve)](https://raw.githubusercontent.com/cloudflare/cfssl/master/doc/cmd/cfssl.txt) — Referência oficial de subcomandos e flags da CLI cfssl; consultado em 2026-10-03.
- [Cloudflare CFSSL — Official GitHub Repository](https://github.com/cloudflare/cfssl) — Repositório oficial BSD-2-Clause do Cloudflare CFSSL; consultado em 2026-10-03.
