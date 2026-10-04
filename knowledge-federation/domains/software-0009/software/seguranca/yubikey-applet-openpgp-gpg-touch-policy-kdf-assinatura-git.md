---
id: software.seguranca.tranche15.001446
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

# Blindando o Applet **OpenPGP** da YubiKey com **`ykman openpgp`**: Ativando **KDF On-Card**, Touch Policy (`on` / `fixed`) para **`sig` / `enc` / `aut`** e Contadores de Tentativas

## Em uma frase
Na Tranche 8 estudamos como mover subchaves do GnuPG para um Smartcard (`keytocard`). Mas quais são os comandos exclusivos do **`ykman openpgp`** na YubiKey que **protegem o applet OpenPGP contra malware local que tente assinar commits Git ou decifrar segredos silenciosamente enquanto a YubiKey está plugada no USB**?

## Por que importa
Três controles de hardware configurados via **`ykman openpgp`** são obrigatórios: **(1) Exigência de Toque Físico (`ykman openpgp keys set-touch`)** para os três slots do OpenPGP — **`sig` (Assinatura)**, **`enc` (Descriptografia)** e **`aut` (Autenticação SSH)**.

## Como funciona
**(2) Política de Toque `FIXED` ou `CACHED-FIXED`** (que impede que até mesmo alguém que conheça o Admin PIN desative a exigência de toque sem zerar a chave!); e **(3) `KDF-DO` (*Key Derivation Function on Card*)** — faz com que o cliente GPG envie um hash iterado do PIN pelo barramento USB em vez do PIN em ASCII!

## Exemplo
```bash
# Inspecionar o applet OpenPGP da YubiKey e exigir toque fisico obrigatorio nas operacoes de Assinatura (sig), Descriptografia (enc) e Autenticacao (aut)
ykman openpgp info
ykman openpgp keys set-touch sig on
ykman openpgp keys set-touch enc on
ykman openpgp keys set-touch aut cached
```

## Limites e trade-offs
Olhe a diferença entre as políticas de toque do **`ykman openpgp keys set-touch <slot> <policy>`**: **`off`** (não exige toque); **`on`** (exige um toque físico na YubiKey para cada operação); **`cached`** (exige um toque físico e permite operações pelos próximos 15 segundos — ótimo para `aut`/`enc` ao abrir múltiplos repositórios!); **`fixed`** (igual a `on`, mas **irreversível** sem dar `ykman openpgp reset`!); e **`cached-fixed`**!

## Como verificar
Com `ykman openpgp keys set-touch sig on` e `enc on` ativos, se um malware na sua estação de trabalho tentar rodar `gpg --decrypt segredo.gpg` ou `ssh servidor` em background mesmo depois que você já digitou o PIN no `gpg-agent`, a YubiKey ficará piscando o LED esperando seu dedo e **jamais realizará a operação criptográfica sem o seu toque físico**!

## Conexões
- [[yubikey-gerenciamento-piv-smartcard-x509-slots-9a-9c-9d-9e-pkcs11]] — Veja também: Smartcard X.509 (**PIV — *Personal Identity Verification* `FIPS 201`**) na YubiKey com **`ykman piv`**: Os Slots `9a`, `9c`, `9d`, `9e` e Hardening de PIN/PUK/Management Key.
- [[yubikey-applet-oath-totp-hotp-ykman-oath-touch-password-cli]] — Veja também: Gerador de Códigos **OATH-TOTP e HOTP** em Hardware com **`ykman oath`**: Aposentando Apps de Celular Vulneráveis com Proteção por Senha e Toque (`--touch`).
- [[yubikey-arquitetura-ykman-aplicacoes-fido2-piv-openpgp-oath-otp]] — Referência cruzada direta com yubikey-arquitetura-ykman-aplicacoes-fido2-piv-openpgp-oath-otp.
- [[gnupg-smartcards-yubikey-openpgp-scdaemon-card-edit-keytocard]] — Referência cruzada direta com gnupg-smartcards-yubikey-openpgp-scdaemon-card-edit-keytocard.

## Fontes
- [YubiKey Manager (`ykman`) Official Repository (`Yubico/yubikey-manager`)](https://raw.githubusercontent.com/Yubico/yubikey-manager/main/README.adoc) — documentação oficial da biblioteca e CLI `ykman` cobrindo gerenciamento de interfaces USB/NFC e applets FIDO2, PIV, OpenPGP, OATH e OTP em YubiKeys; consultado em 2026-10-03.
- [Yubico `pam-u2f` Official Repository and Specification (`Yubico/pam-u2f`)](https://raw.githubusercontent.com/Yubico/pam-u2f/main/README) — documentação oficial do módulo `pam_u2f.so` e utilitário `pamu2fcfg` detalhando `authfile`, `cue`, `pinverification`, `userpresence`, `origin`, `sshformat` e proteção contra chave clonada; consultado em 2026-10-03.
