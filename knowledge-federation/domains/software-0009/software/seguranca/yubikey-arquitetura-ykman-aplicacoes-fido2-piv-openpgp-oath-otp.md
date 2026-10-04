---
id: software.seguranca.tranche15.001441
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

# Arquitetura da **YubiKey** e CLI Oficial **`ykman` (`Yubico/yubikey-manager`)**: Os 5 Applets Isolados em Hardware (`FIDO2`, `PIV`, `OpenPGP`, `OATH`, `OTP`) e Interfaces USB/NFC

## Em uma frase
Por que uma única **YubiKey 5 Series** física consegue atuar simultaneamente como: **(1) Passkey FIDO2 / WebAuthn**, **(2) Smartcard X.509 corporativo (`PIV`)**, **(3) Cartão Criptográfico `OpenPGP` (para GPG e SSH)**, **(4) Autenticador `OATH-TOTP/HOTP` de 6 dígitos** e **(5) Emulador de teclado `Yubico OTP` / `HMAC-SHA1 Challenge-Response`** — sem que os dados ou PINs de um protocolo interfiram no outro?

## Por que importa
Porque internamente o elemento seguro (*Secure Element*) da YubiKey executa **5 aplicações criptográficas independentes (Applets)** sobre **3 interfaces USB/NFC distintas (`OTP/HID Keyboard`, `FIDO/CTAPHID` e `CCID SmartCard` via `pcscd`)**!

## Como funciona
Para auditar, configurar PINs, gerar chaves e habilitar/desabilitar applets na linha de comando em Linux, macOS e Windows, a Yubico mantém a ferramenta oficial em Python **`ykman` (`yubikey-manager`)**!

## Exemplo
```bash
# Listar todas as YubiKeys conectadas (numeros de serie), exibir informacoes de firmware/applets ativos e rodar diagnostico completo
ykman list --serials
ykman info
ykman --diagnose
```

## Limites e trade-offs
Veja na saída de **`ykman info`** a tabela `Enabled USB interfaces` e `Enabled NFC interfaces`: em ambientes corporativos onde os usuários batem por acidente no sensor capacitivo da YubiKey e ela digita uma string de 44 caracteres de *Yubico OTP* no meio do código ou do chat (porque o Slot 1 de fábrica vem com `Yubico OTP` na interface de teclado HID!), você pode **desabilitar apenas o applet `OTP` mantendo `FIDO2`, `PIV`, `OpenPGP` e `OATH` 100% ativos** usando **`ykman config usb --disable OTP`**!

## Como verificar
No Linux, certifique-se de que o daemon **`pcscd` (`pcsc-lite`)** esteja instalado e ativo (`systemctl enable --now pcscd.socket`) para comunicar com os applets SmartCard (`PIV`, `OpenPGP` e `OATH`) e que as regras `udev` (`libfido2` / `u2f-udev`) estejam presentes para acesso `FIDO2` sem precisar de `sudo`.

## Conexões
- [[yubikey-gerenciamento-fido2-passkeys-resident-keys-pin-credenciais]] — Veja também: Gerenciamento de **FIDO2 / WebAuthn e Passkeys (`Discoverable / Resident Credentials`)** na YubiKey com **`ykman fido`**.
- [[yubikey-gerenciamento-piv-smartcard-x509-slots-9a-9c-9d-9e-pkcs11]] — Referência cruzada direta com yubikey-gerenciamento-piv-smartcard-x509-slots-9a-9c-9d-9e-pkcs11.
- [[yubikey-autenticacao-linux-pam-u2f-pamu2fcfg-sudo-login-ssh]] — Referência cruzada direta com yubikey-autenticacao-linux-pam-u2f-pamu2fcfg-sudo-login-ssh.

## Fontes
- [YubiKey Manager (`ykman`) Official Repository (`Yubico/yubikey-manager`)](https://raw.githubusercontent.com/Yubico/yubikey-manager/main/README.adoc) — documentação oficial da biblioteca e CLI `ykman` cobrindo gerenciamento de interfaces USB/NFC e applets FIDO2, PIV, OpenPGP, OATH e OTP em YubiKeys; consultado em 2026-10-03.
- [Yubico `pam-u2f` Official Repository and Specification (`Yubico/pam-u2f`)](https://raw.githubusercontent.com/Yubico/pam-u2f/main/README) — documentação oficial do módulo `pam_u2f.so` e utilitário `pamu2fcfg` detalhando `authfile`, `cue`, `pinverification`, `userpresence`, `origin`, `sshformat` e proteção contra chave clonada; consultado em 2026-10-03.
