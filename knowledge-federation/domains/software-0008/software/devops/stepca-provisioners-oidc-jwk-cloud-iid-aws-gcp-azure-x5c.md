---
id: software.devops.tranche20.001933
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

# Smallstep `step-ca` Provisioners: emissão de certificados em troca de tokens `OIDC`, `JWK`, `X5C`, `Nebula` e Cloud Instance Identity (`AWS`/`GCP`/`Azure`)

## Em uma frase
No `step-ca`, os **Provisioners** definem como diferentes tipos de clientes (humanos, pipelines de CD, VMs de nuvem ou dispositivos) provam sua identidade para obter um certificado assinado sem intervenção manual.

## Por que importa
Um engenheiro humano faz login via SSO (Okta/Keycloak), mas uma VM recém-lançada em um Auto Scaling Group na AWS não tem navegador — ela possui apenas seu *Instance Identity Document (IID)* assinado pelos metadados da nuvem.

## Como funciona
O `step-ca` suporta múltiplos provisioners simultâneos: 1) **OIDC** (troca ID tokens do Okta, Google, Entra ID, Keycloak ou Dex por certificados X.509/SSH); 2) **AWS / GCP / Azure** (valida documentos de identidade de instância da nuvem para emitir o certificado da VM no boot); 3) **JWK** (tokens JWT de uso único gerados por ferramentas de CD como Ansible/Terraform); 4) **X5C** / **Nebula** / **K8sSA**; e 5) **SCEP** e **SSHPOP**.

## Exemplo
```bash
# Adicionando um provisioner OIDC (Keycloak) e um provisioner AWS IID ao step-ca:
step ca provisioner add sso-keycloak --type OIDC \
  --client-id step-ca-cli \
  --configuration-endpoint https://sso.corp.internal/realms/main/.well-known/openid-configuration

step ca provisioner add aws-prod --type AWS --aws-account 123456789012
step ca provisioner list
```

## Limites e trade-offs
Nos provisioners de nuvem (`AWS`, `GCP`, `Azure`), o `step-ca` garante por padrão que uma instância só consiga solicitar um certificado uma única vez logo após o boot (*disableCustomSANs* / janela de idade da instância), evitando que um invasor reemita certificados arbitrários dias depois.

## Como verificar
Execute `step ca provisioner list` para auditar todos os provisioners configurados e suas restrições de duração e SANs.

## Conexões
- [[stepca-servidor-acme-privado-http-01-dns-01-tls-alpn-01]] — Veja também: Smallstep `step-ca` como Servidor ACMEv2 Privado: desafios `http-01`, `dns-01` e `tls-alpn-01` para automação TLS interna.
- [[stepca-ssh-certificate-authority-single-sign-on-user-host-certs]] — Veja também: Smallstep `step-ca` SSH Certificate Authority: substituição de `authorized_keys` e `known_hosts` por certificados SSH via SSO.

## Fontes
- [Smallstep Certificates GitHub — README.md (step-ca Private Online X.509 & SSH Certificate Authority, ACME Server & Provisioners)](https://raw.githubusercontent.com/smallstep/certificates/master/README.md) — README oficial do smallstep/certificates apresentando a CA online step-ca, suporte ACMEv2, tipos de provisionadores e emissão de certificados X.509 e SSH; consultado em 2026-10-03.
- [Smallstep CLI GitHub — README.md (Zero Trust Swiss Army Knife, step ca/certificate/ssh/crypto/oauth Commands & Examples)](https://raw.githubusercontent.com/smallstep/cli/master/README.md) — README oficial do smallstep/cli detalhando os grupos de comandos step, inspeção/linting de certificados, JOSE/JWT, OAuth e fluxos mTLS/SSH; consultado em 2026-10-03.
- [Smallstep Certificates — Official GitHub Repository](https://github.com/smallstep/certificates) — Repositório oficial Apache-2.0 do Smallstep step-ca; consultado em 2026-10-03.
