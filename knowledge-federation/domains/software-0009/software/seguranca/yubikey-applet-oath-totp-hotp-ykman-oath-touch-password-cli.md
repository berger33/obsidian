---
id: software.seguranca.tranche15.001447
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

# Gerador de Códigos **OATH-TOTP e HOTP** em Hardware com **`ykman oath`**: Aposentando Apps de Celular Vulneráveis com Proteção por Senha e Toque (`--touch`)

## Em uma frase
Onde a maioria das pessoas guarda suas sementes secretas (`Base32`) de autenticação de dois fatores **TOTP (`RFC 6238`, códigos de 6 dígitos que mudam a cada 30 segundos)** para serviços que ainda não suportam FIDO2/Passkeys? Em aplicativos de celular ou extensões de navegador onde a semente Base32 fica salva na memória do sistema operacional!

## Por que importa
O applet **`OATH`** da **YubiKey** (gerenciado via **`ykman oath`** ou pelo app gráfico *Yubico Authenticator*) permite guardar até **64 contas OATH-TOTP/HOTP (no firmware 5.7+)** diretamente dentro do elemento seguro da YubiKey — de onde **a semente secreta Base32 jamais pode ser extraída após gravada (`Write-Only Secret`)**!

## Como funciona
Além disso, ao adicionar uma conta com **`ykman oath accounts add --touch`** e definir uma senha no applet OATH (**`ykman oath access change`**), gerar um código de 6 dígitos na linha de comando (`ykman oath accounts code`) exige **tanto a senha do applet OATH quanto um toque físico no sensor da YubiKey**!

## Exemplo
```bash
# Proteger o applet OATH da YubiKey com senha, cadastrar uma semente TOTP exigindo toque fisico (--touch) e gerar o codigo de 6 digitos no terminal
ykman oath info
ykman oath access change
ykman oath accounts add --touch --oath-type TOTP "AWS:root-conta-prod" JBSWY3DPEHPK3PXP
ykman oath accounts code "AWS:root-conta-prod"
```

## Limites e trade-offs
Por que o applet **OATH-TOTP** da YubiKey precisa do aplicativo **`ykman` (ou Yubico Authenticator)** rodando no computador/celular via NFC para calcular o código de 6 dígitos? Porque o chip da YubiKey não possui uma bateria interna para manter um relógio de tempo real (*RTC*) quando está desconectado do USB: quando você roda `ykman oath accounts code`, o `ykman` envia o timestamp Unix atual do computador para o applet OATH da YubiKey, e **o chip da YubiKey calcula o `HMAC-SHA1(Secret, Timestamp/30)` internamente sem nunca revelar o `Secret`**!

## Como verificar
Ao escanear um QR Code de TOTP em serviços críticos (como a conta Root da AWS), salve a semente simultaneamente na sua YubiKey Principal e na sua YubiKey de Backup no exato momento do cadastro!

## Conexões
- [[yubikey-applet-openpgp-gpg-touch-policy-kdf-assinatura-git]] — Veja também: Blindando o Applet **OpenPGP** da YubiKey com **`ykman openpgp`**: Ativando **KDF On-Card**, Touch Policy (`on` / `fixed`) para **`sig` / `enc` / `aut`** e Contadores de Tentativas.
- [[yubikey-applet-otp-slots-challenge-response-hmac-sha1-luks-keepassxc]] — Veja também: Configurando os **Slots 1 e 2 do Applet `OTP` (`ykman otp`)**: **HMAC-SHA1 Challenge-Response** para **KeePassXC e LUKS2**, Senha Estática e Yubico OTP.
- [[yubikey-arquitetura-ykman-aplicacoes-fido2-piv-openpgp-oath-otp]] — Referência cruzada direta com yubikey-arquitetura-ykman-aplicacoes-fido2-piv-openpgp-oath-otp.
- [[freeipa-autenticacao-2fa-otp-totp-hotp-passkeys-radius-pkinit]] — Referência cruzada direta com freeipa-autenticacao-2fa-otp-totp-hotp-passkeys-radius-pkinit.
- [[keepassxc-autenticacao-multifator-yubikey-hmac-sha1-keyfile]] — Referência cruzada direta com keepassxc-autenticacao-multifator-yubikey-hmac-sha1-keyfile.

## Fontes
- [YubiKey Manager (`ykman`) Official Repository (`Yubico/yubikey-manager`)](https://raw.githubusercontent.com/Yubico/yubikey-manager/main/README.adoc) — documentação oficial da biblioteca e CLI `ykman` cobrindo gerenciamento de interfaces USB/NFC e applets FIDO2, PIV, OpenPGP, OATH e OTP em YubiKeys; consultado em 2026-10-03.
- [Yubico `pam-u2f` Official Repository and Specification (`Yubico/pam-u2f`)](https://raw.githubusercontent.com/Yubico/pam-u2f/main/README) — documentação oficial do módulo `pam_u2f.so` e utilitário `pamu2fcfg` detalhando `authfile`, `cue`, `pinverification`, `userpresence`, `origin`, `sshformat` e proteção contra chave clonada; consultado em 2026-10-03.
