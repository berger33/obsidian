---
id: software.devops.tranche20.001931
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
fontes: ["https://raw.githubusercontent.com/smallstep/certificates/master/README.md", "https://raw.githubusercontent.com/smallstep/cli/master/README.md", "https://github.com/smallstep/certificates"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Smallstep `step-ca` e `step` CLI: arquitetura de Autoridade Certificadora online para certificados X.509 e SSH de curta duração

## Em uma frase
O **`step-ca`** (`smallstep/certificates`) e sua ferramenta cliente **`step` CLI** (`smallstep/cli`), mantidos pela Smallstep Labs sob licença Apache 2.0, formam uma Autoridade Certificadora (CA) online automatizada de duas camadas (*Root CA* + *Intermediate CA*) projetada para emitir certificados **X.509 (TLS/HTTPS)** compatíveis com a RFC 5280 e **certificados SSH** (para usuários e hosts) de curta duração.

## Por que importa
Certificados de longa duração (1 a 5 anos) exigem listas de revogação (CRL/OCSP) complexas que muitos clientes ignoram; já certificados de curta duração (ex.: 16–24 horas) com renovação automática eliminam chaves estáticas e implementam *revogação passiva*.

## Como funciona
Com um único comando (`step ca init`), a ferramenta inicializa uma hierarquia PKI X.509 e/ou uma CA SSH, configurando o arquivo `ca.json` com suporte aos bancos de dados **Badger**, **BoltDB**, **PostgreSQL** e **MySQL**. Os clientes fazem bootstrap seguro da confiança usando apenas a URL da CA e o fingerprint SHA-256 da raiz (`step ca bootstrap`).

## Exemplo
```bash
# Inicializando uma CA X.509 e SSH local e fazendo bootstrap de um cliente:
step ca init --name "Internal DevOps CA" \
  --dns "ca.corp.internal" \
  --address ":9000" \
  --provisioner "admin@corp.internal"

step ca fingerprint $(step path)/certs/root_ca.crt
```

## Limites e trade-offs
O comando `step certificate install $(step path)/certs/root_ca.crt` instala o certificado raiz da sua CA diretamente no trust store do sistema operacional e dos navegadores locais, permitindo HTTPS válido em ambientes de desenvolvimento e pré-produção.

## Como verificar
Execute `step ca health --ca-url https://ca.corp.internal:9000 --root $(step path)/certs/root_ca.crt` para verificar que o servidor `step-ca` responde `ok`.

## Conexões
- [[stepca-servidor-acme-privado-http-01-dns-01-tls-alpn-01]] — Veja também: Smallstep `step-ca` como Servidor ACMEv2 Privado: desafios `http-01`, `dns-01` e `tls-alpn-01` para automação TLS interna.

## Fontes
- [Smallstep Certificates GitHub — README.md (step-ca Private Online X.509 & SSH Certificate Authority, ACME Server & Provisioners)](https://raw.githubusercontent.com/smallstep/certificates/master/README.md) — README oficial do smallstep/certificates apresentando a CA online step-ca, suporte ACMEv2, tipos de provisionadores e emissão de certificados X.509 e SSH; consultado em 2026-10-03.
- [Smallstep CLI GitHub — README.md (Zero Trust Swiss Army Knife, step ca/certificate/ssh/crypto/oauth Commands & Examples)](https://raw.githubusercontent.com/smallstep/cli/master/README.md) — README oficial do smallstep/cli detalhando os grupos de comandos step, inspeção/linting de certificados, JOSE/JWT, OAuth e fluxos mTLS/SSH; consultado em 2026-10-03.
- [Smallstep Certificates — Official GitHub Repository](https://github.com/smallstep/certificates) — Repositório oficial Apache-2.0 do Smallstep step-ca; consultado em 2026-10-03.
