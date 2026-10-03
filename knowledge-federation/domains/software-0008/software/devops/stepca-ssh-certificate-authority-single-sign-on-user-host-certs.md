---
id: software.devops.tranche20.001934
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
fontes: ["https://raw.githubusercontent.com/smallstep/certificates/master/README.md", "https://raw.githubusercontent.com/smallstep/cli/master/README.md", "https://github.com/smallstep/cli"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Smallstep `step-ca` SSH Certificate Authority: substituição de `authorized_keys` e `known_hosts` por certificados SSH via SSO

## Em uma frase
Quando inicializado com `--ssh`, o `step-ca` atua como uma **Autoridade Certificadora OpenSSH online**, emitindo certificados SSH de usuário de curta duração (ex.: 16 horas) em troca de autenticação Single Sign-On (OIDC) e certificados SSH de host em troca de identidade de nuvem ou token de provisionamento.

## Por que importa
Manter arquivos `~/.ssh/authorized_keys` espalhados em centenas de servidores e receber alertas `WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED` (TOFU) quando VMs são recriadas é inseguro e trabalhoso.

## Como funciona
Com certificados SSH do `step-ca`: 1) os servidores configuram `TrustedUserCAKeys /etc/ssh/ssh_user_ca_key.pub` no `sshd_config` (confiando em qualquer usuário cujo certificado não expirado foi assinado pela CA após login SSO); e 2) as estações configuram `@cert-authority *.corp.internal` no `known_hosts` (eliminando avisos TOFU em qualquer host com certificado assinado pela CA de hosts).

## Exemplo
```bash
# Autenticando via SSO OIDC para carregar um certificado SSH de curta duração no ssh-agent:
step ssh login alice@corp.internal --provisioner sso-keycloak

# Listando e inspecionando o certificado SSH carregado no agente:
step ssh list --raw | step ssh inspect
```

## Limites e trade-offs
Para renovar automaticamente os certificados SSH de host das VMs antes que expirem, utilize o provisioner **`SSHPOP`** (*SSH Proof-of-Possession*) com `step ssh renew` em um timer systemd.

## Como verificar
Execute `step ssh config --roots` para imprimir as chaves públicas das CAs SSH de usuário e de host gerenciadas pelo seu `step-ca`.

## Conexões
- [[stepca-provisioners-oidc-jwk-cloud-iid-aws-gcp-azure-x5c]] — Veja também: Smallstep `step-ca` Provisioners: emissão de certificados em troca de tokens `OIDC`, `JWK`, `X5C`, `Nebula` e Cloud Instance Identity (`AWS`/`GCP`/`Azure`).
- [[stepca-step-certificate-create-inspect-lint-verify-rfc5280]] — Veja também: Smallstep `step certificate`: criação, inspeção, `lint` (RFC 5280 / CA-Browser Forum) e verificação de certificados X.509.

## Fontes
- [Smallstep Certificates GitHub — README.md (step-ca Private Online X.509 & SSH Certificate Authority, ACME Server & Provisioners)](https://raw.githubusercontent.com/smallstep/certificates/master/README.md) — README oficial do smallstep/certificates apresentando a CA online step-ca, suporte ACMEv2, tipos de provisionadores e emissão de certificados X.509 e SSH; consultado em 2026-10-03.
- [Smallstep CLI GitHub — README.md (Zero Trust Swiss Army Knife, step ca/certificate/ssh/crypto/oauth Commands & Examples)](https://raw.githubusercontent.com/smallstep/cli/master/README.md) — README oficial do smallstep/cli detalhando os grupos de comandos step, inspeção/linting de certificados, JOSE/JWT, OAuth e fluxos mTLS/SSH; consultado em 2026-10-03.
- [Smallstep Certificates — Official GitHub Repository](https://github.com/smallstep/cli) — Repositório oficial Apache-2.0 do Smallstep step-ca; consultado em 2026-10-03.
