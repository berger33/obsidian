---
id: software.devops.tranche20.001940
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

# Smallstep Certificate Templates: customização de extensões X.509 e `principals`/extensões SSH com templates Go no `step-ca`

## Em uma frase
Os provisioners do `step-ca` suportam **Templates de Certificados X.509 e SSH** escritos na linguagem de templates do Go (JSON para X.509), permitindo transformar claims de um token OIDC ou metadados de instância em extensões X.509 customizadas, `Subject` (`O`, `OU`), SANs restritos ou `principals` e permissões (`permit-port-forwarding`) de certificados SSH.

## Por que importa
Em um cluster Kubernetes onde o `kube-apiserver` autentica usuários por certificados cliente X.509 ou servidores SSH exigem `principals` baseados nos grupos do IdP, o certificado emitido após login OIDC precisa refletir exatamente os grupos do usuário no token.

## Como funciona
Associado ao provisioner no `ca.json`, o template acessa `.Token` (os claims verificados do JWT OIDC, como `.Token.groups` e `.Token.email`) e `.Insecure.CR` (os dados do CSR enviado pelo cliente), garantindo que apenas valores validados pelo provedor de identidade entrem nos campos sensíveis do certificado.

## Exemplo
```json
{
  "subject": {
    "commonName": {{ toJson .Token.email }},
    "organization": {{ toJson .Token.groups }}
  },
  "sans": {{ toJson .SANs }},
  "keyUsage": ["digitalSignature", "keyEncipherment"],
  "extKeyUsage": ["clientAuth"]
}
```

## Limites e trade-offs
Nos templates do `step-ca`, nunca confie cegamente nos atributos vindos de `.Insecure.CR` (controlados pelo cliente que gerou o CSR) para definir permissões ou grupos: extraia grupos e identidades sempre do objeto autenticado `.Token`.

## Como verificar
Valide o certificado emitido por um provisioner com template customizado usando `step certificate inspect <cert.crt>` e confirme os campos `Subject` e `Extended Key Usage`.

## Conexões
- [[stepca-plugins-step-kms-plugin-hsm-tpm-yubikey-cloud-kms]] — Veja também: Smallstep Plugins e KMS (`step-kms-plugin`): proteção das chaves da CA em HSMs (PKCS#11), TPM 2.0, YubiKey e Cloud KMS.

## Fontes
- [Smallstep Certificates GitHub — README.md (step-ca Private Online X.509 & SSH Certificate Authority, ACME Server & Provisioners)](https://raw.githubusercontent.com/smallstep/certificates/master/README.md) — README oficial do smallstep/certificates apresentando a CA online step-ca, suporte ACMEv2, tipos de provisionadores e emissão de certificados X.509 e SSH; consultado em 2026-10-03.
- [Smallstep CLI GitHub — README.md (Zero Trust Swiss Army Knife, step ca/certificate/ssh/crypto/oauth Commands & Examples)](https://raw.githubusercontent.com/smallstep/cli/master/README.md) — README oficial do smallstep/cli detalhando os grupos de comandos step, inspeção/linting de certificados, JOSE/JWT, OAuth e fluxos mTLS/SSH; consultado em 2026-10-03.
- [Smallstep Certificates — Official GitHub Repository](https://github.com/smallstep/certificates) — Repositório oficial Apache-2.0 do Smallstep step-ca; consultado em 2026-10-03.
