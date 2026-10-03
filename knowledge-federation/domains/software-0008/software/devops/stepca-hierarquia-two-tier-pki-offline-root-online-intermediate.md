---
id: software.devops.tranche20.001938
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

# Smallstep Two-Tier PKI: operação do `step-ca` como CA Intermediária Online subordinada a uma Root CA Offline

## Em uma frase
O `step-ca` é otimizado para operar uma **PKI de duas camadas (*Two-Tier PKI*)**, onde a chave privada da **Root CA** permanece 100% offline (em um cofre físico, HSM ou YubiKey) e o servidor `step-ca` carrega apenas a chave privada de uma **Intermediate CA**, podendo inclusive ser subordinado a uma Root CA corporativa já existente.

## Por que importa
Se um servidor CA online mantivesse a chave privada da Root CA no disco da VM e sofresse comprometimento, toda a infraestrutura precisaria substituir o certificado raiz instalado em milhares de clientes e dispositivos.

## Como funciona
Na inicialização padrão do `step-ca`, ele já gera uma Root CA (`root_ca.crt` / `root_ca_key`) e uma Intermediate CA (`intermediate_ca.crt` / `intermediate_ca_key`), configurando o `ca.json` para assinar certificados exclusivamente com a `intermediate_ca_key`. Após o `step ca init`, você deve remover `root_ca_key` do servidor e guardá-la em armazenamento offline seguro.

## Exemplo
```bash
# Gerando uma nova CA intermediária assinada por uma Root CA existente para uso no step-ca:
step certificate create "Corp Intermediate CA 2026" \
  intermediate_ca.crt intermediate_ca.key \
  --profile intermediate-ca \
  --ca ./offline-root_ca.crt \
  --ca-key ./offline-root_ca.key
```

## Limites e trade-offs
Nunca deixe o arquivo `secrets/root_ca_key` no disco do servidor onde o processo `step-ca` roda em produção: o daemon `step-ca` precisa apenas de `secrets/intermediate_ca_key` para operar.

## Como verificar
Verifique no arquivo `$(step path)/config/ca.json` que o campo `"key"` aponta para `intermediate_ca_key` e não para `root_ca_key`.

## Conexões
- [[stepca-step-crypto-jose-jwt-jwk-jws-jwe-totp-kdf]] — Veja também: Smallstep `step crypto` e `step oauth`: toolkit de linha de comando para JWT, JWK, JWS, JWE, NaCl, TOTP e fluxos OAuth/OIDC.
- [[stepca-plugins-step-kms-plugin-hsm-tpm-yubikey-cloud-kms]] — Veja também: Smallstep Plugins e KMS (`step-kms-plugin`): proteção das chaves da CA em HSMs (PKCS#11), TPM 2.0, YubiKey e Cloud KMS.

## Fontes
- [Smallstep Certificates GitHub — README.md (step-ca Private Online X.509 & SSH Certificate Authority, ACME Server & Provisioners)](https://raw.githubusercontent.com/smallstep/certificates/master/README.md) — README oficial do smallstep/certificates apresentando a CA online step-ca, suporte ACMEv2, tipos de provisionadores e emissão de certificados X.509 e SSH; consultado em 2026-10-03.
- [Smallstep CLI GitHub — README.md (Zero Trust Swiss Army Knife, step ca/certificate/ssh/crypto/oauth Commands & Examples)](https://raw.githubusercontent.com/smallstep/cli/master/README.md) — README oficial do smallstep/cli detalhando os grupos de comandos step, inspeção/linting de certificados, JOSE/JWT, OAuth e fluxos mTLS/SSH; consultado em 2026-10-03.
- [Smallstep Certificates — Official GitHub Repository](https://github.com/smallstep/certificates) — Repositório oficial Apache-2.0 do Smallstep step-ca; consultado em 2026-10-03.
