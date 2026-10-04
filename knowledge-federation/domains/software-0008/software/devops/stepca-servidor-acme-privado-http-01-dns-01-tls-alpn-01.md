---
id: software.devops.tranche20.001932
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

# Smallstep `step-ca` como Servidor ACMEv2 Privado: desafios `http-01`, `dns-01` e `tls-alpn-01` para automação TLS interna

## Em uma frase
O `step-ca` inclui um servidor **ACMEv2 (RFC 8555)** completo integrado por meio do provisioner do tipo `ACME`, trazendo a mesma experiência automatizada do Let's Encrypt para domínios privados internos (`.corp.internal`, `.svc.cluster.local`) usando qualquer cliente ACME padrão (`cert-manager`, Caddy, Traefik, Certbot, `acme.sh`, `lego` ou a própria `step` CLI).

## Por que importa
Let's Encrypt não emite certificados para domínios privados internos nem endereços IP privados; porém, renovar certificados internos manualmente a cada ano causa outages recorrentes em produção.

## Como funciona
Basta adicionar um provisioner ACME com `step ca provisioner add acme --type ACME`: o `step-ca` passa a expor o diretório ACME em `/acme/acme/directory` e valida automaticamente os três desafios padrão: **`http-01`** (token HTTP na porta 80), **`dns-01`** (registro TXT no DNS interno) e **`tls-alpn-01`** (negociação na camada TLS na porta 443, usada nativamente por Caddy e Traefik).

## Exemplo
```bash
# Adicionando o provisioner ACME ao step-ca e solicitando um certificado via ACME:
step ca provisioner add acme --type ACME
step ca certificate --provisioner acme \
  internal-api.corp.internal \
  internal-api.crt internal-api.key
```

## Limites e trade-offs
Ao integrar o `cert-manager` do Kubernetes com o `step-ca` via ACME, configure um `ClusterIssuer` apontando `spec.acme.server` para `https://ca.corp.internal:9000/acme/acme/directory` e `spec.acme.caBundle` com o conteúdo em base64 do `root_ca.crt`.

## Como verificar
Consulte `curl -s --cacert $(step path)/certs/root_ca.crt https://ca.corp.internal:9000/acme/acme/directory` para validar os endpoints ACMEv2 expostos.

## Conexões
- [[stepca-arquitetura-online-ca-smallstep-x509-ssh-step-cli]] — Veja também: Smallstep `step-ca` e `step` CLI: arquitetura de Autoridade Certificadora online para certificados X.509 e SSH de curta duração.
- [[stepca-provisioners-oidc-jwk-cloud-iid-aws-gcp-azure-x5c]] — Veja também: Smallstep `step-ca` Provisioners: emissão de certificados em troca de tokens `OIDC`, `JWK`, `X5C`, `Nebula` e Cloud Instance Identity (`AWS`/`GCP`/`Azure`).

## Fontes
- [Smallstep Certificates GitHub — README.md (step-ca Private Online X.509 & SSH Certificate Authority, ACME Server & Provisioners)](https://raw.githubusercontent.com/smallstep/certificates/master/README.md) — README oficial do smallstep/certificates apresentando a CA online step-ca, suporte ACMEv2, tipos de provisionadores e emissão de certificados X.509 e SSH; consultado em 2026-10-03.
- [Smallstep CLI GitHub — README.md (Zero Trust Swiss Army Knife, step ca/certificate/ssh/crypto/oauth Commands & Examples)](https://raw.githubusercontent.com/smallstep/cli/master/README.md) — README oficial do smallstep/cli detalhando os grupos de comandos step, inspeção/linting de certificados, JOSE/JWT, OAuth e fluxos mTLS/SSH; consultado em 2026-10-03.
- [Smallstep Certificates — Official GitHub Repository](https://github.com/smallstep/certificates) — Repositório oficial Apache-2.0 do Smallstep step-ca; consultado em 2026-10-03.
