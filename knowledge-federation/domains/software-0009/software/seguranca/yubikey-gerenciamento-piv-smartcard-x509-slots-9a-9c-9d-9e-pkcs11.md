---
id: software.seguranca.tranche15.001445
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

# Smartcard X.509 (**PIV — *Personal Identity Verification* `FIPS 201`**) na YubiKey com **`ykman piv`**: Os Slots `9a`, `9c`, `9d`, `9e` e Hardening de PIN/PUK/Management Key

## Em uma frase
Como funciona o applet **PIV (*Personal Identity Verification*, padrão NIST SP 800-73 / FIPS 201)** da YubiKey — usado para guardar certificados X.509 corporativos de Active Directory / FreeIPA, mTLS no navegador/VPN (`strongSwan` / `OpenVPN`), assinatura de código e chaves SSH via PKCS#11 (`ykcs11`) — e qual é a diferença entre os **4 Slots principais do PIV (`9a`, `9c`, `9d`, `9e`)**?

## Por que importa
O padrão PIV organiza o armazenamento de chaves RSA (`2048`/`3072`/`4096` no firmware 5.7+) e ECC (`ECCP256`/`ECCP384`/`Ed25519`) em **4 Slots com políticas de PIN distintas**: **(1) `Slot 9a` (*PIV Authentication*)** — usado para login no sistema operacional (SSSD/AD Smartcard Logon), VPN e SSH PKCS#11 (pede o PIN uma vez por sessão); **(2) `Slot 9c` (*Digital Signature*)** — usado para assinatura de documentos/código (exige digitar o PIN **a cada operação individual de assinatura**!); **(3) `Slot 9d` (*Key Management*)** — usado para descriptografia de e-mails S/MIME, arquivos CMS ou discos; e **(4) `Slot 9e` (*Card Authentication*)** — usado para controle de acesso físico sem exigir PIN!

## Como funciona
Antes de usar o applet PIV para qualquer chave real, você **DEVE trocar imediatamente as 3 credenciais padrão de fábrica do PIV** com `ykman piv access`: **(A) PIN padrão (`123456`)**, **(B) PUK padrão (`12345678`)** e **(C) Management Key padrão (`010203040506070801020304050607080102030405060708`)**!

## Exemplo
```bash
# Blindar o applet PIV da YubiKey trocando PIN, PUK e Management Key padrao de fabrica e gerando uma chave ECCP256 no slot 9a exigindo toque fisico
ykman piv info
ykman piv access change-pin --pin 123456
ykman piv access change-puk --puk 12345678
ykman piv access change-management-key --generate --protect
ykman piv keys generate --algorithm ECCP256 --pin-policy ONCE --touch-policy ALWAYS 9a ./chave_publica_9a.pem
```

## Limites e trade-offs
Veja duas flags fundamentais nos comandos **`ykman piv`** acima: **(1) `ykman piv access change-management-key --generate --protect`** — gera uma chave administrativa AES/TDES aleatória criptograficamente forte e a armazena protegida pelo seu PIN dentro da própria YubiKey; e **(2) `--touch-policy ALWAYS` (ou `CACHED` por 15s)** ao gerar a chave no slot `9a`/`9c` — exigindo que o usuário toque fisicamente na YubiKey toda vez que um processo tentar usar o certificado via PKCS#11!

## Como verificar
Para usar as chaves do applet PIV no OpenSSH ou no SSSD/OpenSSL via PKCS#11, utilize o módulo oficial **`libykcs11.so`** (do pacote `yubico-piv-tool`, ex.: `ssh -I /usr/lib/x86_64-linux-gnu/libykcs11.so`).

## Conexões
- [[yubikey-autenticacao-linux-pam-u2f-pamu2fcfg-sudo-login-ssh]] — Veja também: Autenticação Linux Local e 2FA com **`pam-u2f` (`pam_u2f.so` e `pamu2fcfg`)**: Protegendo `sudo`, `gdm`/`sddm`, `polkit` e `sshd` com YubiKey FIDO2.
- [[yubikey-applet-openpgp-gpg-touch-policy-kdf-assinatura-git]] — Veja também: Blindando o Applet **OpenPGP** da YubiKey com **`ykman openpgp`**: Ativando **KDF On-Card**, Touch Policy (`on` / `fixed`) para **`sig` / `enc` / `aut`** e Contadores de Tentativas.
- [[yubikey-arquitetura-ykman-aplicacoes-fido2-piv-openpgp-oath-otp]] — Referência cruzada direta com yubikey-arquitetura-ykman-aplicacoes-fido2-piv-openpgp-oath-otp.
- [[sssd-autenticacao-smartcards-pkcs11-certmap-fido2-passkeys]] — Referência cruzada direta com sssd-autenticacao-smartcards-pkcs11-certmap-fido2-passkeys.

## Fontes
- [YubiKey Manager (`ykman`) Official Repository (`Yubico/yubikey-manager`)](https://raw.githubusercontent.com/Yubico/yubikey-manager/main/README.adoc) — documentação oficial da biblioteca e CLI `ykman` cobrindo gerenciamento de interfaces USB/NFC e applets FIDO2, PIV, OpenPGP, OATH e OTP em YubiKeys; consultado em 2026-10-03.
- [Yubico `pam-u2f` Official Repository and Specification (`Yubico/pam-u2f`)](https://raw.githubusercontent.com/Yubico/pam-u2f/main/README) — documentação oficial do módulo `pam_u2f.so` e utilitário `pamu2fcfg` detalhando `authfile`, `cue`, `pinverification`, `userpresence`, `origin`, `sshformat` e proteção contra chave clonada; consultado em 2026-10-03.
