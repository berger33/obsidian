---
id: software.seguranca.tranche15.001450
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/Yubico/yubikey-manager/main/README.adoc", "https://raw.githubusercontent.com/Yubico/pam-u2f/main/README"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Verificação Criptográfica de Autenticidade e Origem de Hardware (**PIV Attestation & FIDO Attestation**) na YubiKey: Provando que uma Chave Foi Gerada *On-Chip*!

## Em uma frase
Em uma empresa com requisitos estritos de PKI ou conformidade **FIPS 140-3 / WebAuthn Attested Passkeys**, se um funcionário enviar uma Requisição de Assinatura de Certificado (`CSR`) ou uma chave pública SSH/PIV para a Autoridade Certificadora interna, **como a CA pode ter 100% de certeza matemática de que aquela chave privada foi gerada dentro do silício de uma YubiKey genuína (e NUNCA existiu como arquivo `.pem` no disco do computador do funcionário antes de ser importada para a YubiKey)**?

## Por que importa
Através do comando de **Atestação de Chave On-Chip (`ykman piv keys attest`)**!

## Como funciona
Toda YubiKey 4.3+ e YubiKey 5 sai da fábrica da Yubico na Suécia/EUA com uma chave e certificado de atestação exclusivos gravados no **Slot `f9` (*Attestation Key*)** assinados pela **Yubico PIV Root CA**! Quando você executa **`ykman piv keys attest 9a attest_9a.pem`**, o chip da YubiKey emite um certificado X.509 assinado pelo Slot `f9` que **só pode ser emitido pelo firmware se a chave do Slot `9a` tiver sido gerada internamente dentro do hardware da YubiKey (`Generated on chip`)** — se a chave tiver sido gerada no OpenSSL e importada (`ykman piv keys import`), o chip da YubiKey se recusa a atestá-la!

## Exemplo
```bash
# Emitir o certificado de atestacao de hardware para a chave do Slot 9a, exportar o certificado intermediario f9 da YubiKey e validar na cadeia Yubico
ykman piv keys attest 9a ./atestado_slot_9a.pem
ykman piv certificates export f9 ./intermediario_f9_yubi.pem
openssl verify -CAfile ./yubico-piv-root-ca.pem -untrusted ./intermediario_f9_yubi.pem ./atestado_slot_9a.pem
```

## Limites e trade-offs
Veja o que o certificado `./atestado_slot_9a.pem` validado pelo `openssl verify` acima comprova criptograficamente para a sua Autoridade Certificadora (como o **Step-CA**, **FreeIPA** ou **Teleport**): **(1) O modelo exato e versão de firmware da YubiKey**, **(2) O Número de Série físico da YubiKey**, **(3) A política de PIN (`ONCE`/`ALWAYS`) e de Toque (`ALWAYS`/`CACHED`) configurada no slot** e **(4) A prova irrefutável de que a chave privada nasceu no silício e é não-exportável**!

## Como verificar
De forma análoga, no protocolo **FIDO2 / WebAuthn**, o servidor **Kanidm** ou **Authentik** valida o certificado de atestação FIDO da YubiKey contra o **FIDO Alliance Metadata Service (MDS)** para aceitar apenas chaves físicas corporativas homologadas!

## Conexões
- [[yubikey-bloqueio-interfaces-config-lock-code-usb-nfc-enterprise]] — Veja também: Hardening Corporativo da YubiKey com **`ykman config`**: Desabilitando Interfaces USB/NFC e Travando Configurações com **`--lock-code` (`Configuration Lock`)**.
- [[yubikey-arquitetura-ykman-aplicacoes-fido2-piv-openpgp-oath-otp]] — Referência cruzada direta com yubikey-arquitetura-ykman-aplicacoes-fido2-piv-openpgp-oath-otp.
- [[yubikey-gerenciamento-piv-smartcard-x509-slots-9a-9c-9d-9e-pkcs11]] — Referência cruzada direta com yubikey-gerenciamento-piv-smartcard-x509-slots-9a-9c-9d-9e-pkcs11.
- [[kanidm-autenticacao-passkeys-webauthn-attested-passkeys-politicas]] — Referência cruzada direta com kanidm-autenticacao-passkeys-webauthn-attested-passkeys-politicas.

## Fontes
- [YubiKey Manager (`ykman`) Official Repository (`Yubico/yubikey-manager`)](https://raw.githubusercontent.com/Yubico/yubikey-manager/main/README.adoc) — documentação oficial da biblioteca e CLI `ykman` cobrindo gerenciamento de interfaces USB/NFC e applets FIDO2, PIV, OpenPGP, OATH e OTP em YubiKeys; consultado em 2026-10-03.
- [Yubico `pam-u2f` Official Repository and Specification (`Yubico/pam-u2f`)](https://raw.githubusercontent.com/Yubico/pam-u2f/main/README) — documentação oficial do módulo `pam_u2f.so` e utilitário `pamu2fcfg` detalhando `authfile`, `cue`, `pinverification`, `userpresence`, `origin`, `sshformat` e proteção contra chave clonada; consultado em 2026-10-03.
