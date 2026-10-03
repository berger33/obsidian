---
id: software.devops.tranche20.001939
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
fontes: ["https://raw.githubusercontent.com/smallstep/cli/master/README.md", "https://raw.githubusercontent.com/smallstep/certificates/master/README.md", "https://github.com/smallstep/cli"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Smallstep Plugins e KMS (`step-kms-plugin`): proteção das chaves da CA em HSMs (PKCS#11), TPM 2.0, YubiKey e Cloud KMS

## Em uma frase
O ecossistema Smallstep suporta plugins executáveis no formato `step-<name>-plugin` (como o **`step-kms-plugin`**) e integração nativa de KMS no `step-ca`, permitindo armazenar e operar as chaves privadas da CA dentro de **HSMs (PKCS#11)**, **TPM 2.0**, **YubiKeys (PIV)**, **AWS KMS**, **Google Cloud KMS** e **Azure Key Vault**.

## Por que importa
Mesmo removendo a Root CA para armazenamento offline, a chave privada da Intermediate CA precisa ficar disponível online para o `step-ca` assinar certificados; se ela for um simples arquivo `.pem` em disco, um invasor com leitura de arquivos pode copiá-la e emitir certificados fora do servidor.

## Como funciona
Ao configurar a seção `"kms"` no `ca.json` (por exemplo `"type": "cloudkms"`, `"awskms"`, `"pkcs11"` ou `"yubikey"`) e apontar `"key"` para a URI da chave no KMS/HSM, a chave privada da Intermediate CA jamais entra em disco e todas as assinaturas X.509/SSH ocorrem dentro do módulo criptográfico.

## Exemplo
```bash
# Listando ou utilizando chaves armazenadas em KMS/YubiKey através do step-kms-plugin:
step kms --help
```

## Limites e trade-offs
Verifique se a versão do binário `step-ca` (ou container) instalada inclui o suporte compilado para o driver KMS escolhido (como `pkcs11` CGo para HSMs ou SDKs de Cloud KMS).

## Como verificar
Inspecione os plugins instalados em `$STEPPATH/plugins` ou no `$PATH` executando `step --help`.

## Conexões
- [[stepca-hierarquia-two-tier-pki-offline-root-online-intermediate]] — Veja também: Smallstep Two-Tier PKI: operação do `step-ca` como CA Intermediária Online subordinada a uma Root CA Offline.
- [[stepca-templates-x509-ssh-customizacao-claims-extensoes-rbac]] — Veja também: Smallstep Certificate Templates: customização de extensões X.509 e `principals`/extensões SSH com templates Go no `step-ca`.

## Fontes
- [Smallstep Certificates GitHub — README.md (step-ca Private Online X.509 & SSH Certificate Authority, ACME Server & Provisioners)](https://raw.githubusercontent.com/smallstep/cli/master/README.md) — README oficial do smallstep/certificates apresentando a CA online step-ca, suporte ACMEv2, tipos de provisionadores e emissão de certificados X.509 e SSH; consultado em 2026-10-03.
- [Smallstep CLI GitHub — README.md (Zero Trust Swiss Army Knife, step ca/certificate/ssh/crypto/oauth Commands & Examples)](https://raw.githubusercontent.com/smallstep/certificates/master/README.md) — README oficial do smallstep/cli detalhando os grupos de comandos step, inspeção/linting de certificados, JOSE/JWT, OAuth e fluxos mTLS/SSH; consultado em 2026-10-03.
- [Smallstep Certificates — Official GitHub Repository](https://github.com/smallstep/cli) — Repositório oficial Apache-2.0 do Smallstep step-ca; consultado em 2026-10-03.
