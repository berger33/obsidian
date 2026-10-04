---
id: software.seguranca.tranche15.001448
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

# Configurando os **Slots 1 e 2 do Applet `OTP` (`ykman otp`)**: **HMAC-SHA1 Challenge-Response** para **KeePassXC e LUKS2**, Senha Estática e Yubico OTP

## Em uma frase
O applet **`OTP`** da YubiKey possui **2 Slots de configuração independentes**: o **Slot 1** (acionado por um **toque curto** de 0,3 a 1,5 segundo no sensor capacitivo) e o **Slot 2** (acionado por um **toque longo** de 2 a 5 segundos, ou acessado programaticamente via software!). Quais são os 4 modos que você pode gravar em cada um desses dois slots usando o **`ykman otp`**?

## Por que importa
Os 4 modos suportados pelo `ykman otp` são: **(1) `chalresp` (*HMAC-SHA1 Challenge-Response*)** — o modo mais importante para criptografia local: a YubiKey guarda uma chave secreta de 20 bytes (`160 bits`) no Slot 2 e responde a desafios enviados pelo **KeePassXC** (para abrir cofres `.kdbx`!) ou pelo **`yubikey-luks`** sem jamais digitar nada no teclado!; **(2) `yubiotp`** — o OTP simétrico AES-128 validado na YubiCloud ou servidor interno (Vaultwarden/FreeRADIUS).

## Como funciona
**(3) `hotp`** (OATH-HOTP de 6 ou 8 dígitos digitado via teclado USB); e **(4) `static`** (uma senha aleatória estática de até 38 caracteres)!

## Exemplo
```bash
# Inspecionar os Slots 1 e 2 do applet OTP, programar uma chave HMAC-SHA1 Challenge-Response no Slot 2 (--touch) e testar o calculo de resposta
ykman otp info
ykman otp chalresp --generate --touch 2
ykman otp calculate 2 "desafio-teste-hex-ou-string"
```

## Limites e trade-offs
Dica de ouro de usabilidade e segurança com **`ykman otp`**: como o Slot 1 vem de fábrica com `Yubico OTP` no toque curto (que digita 44 letras na tela toda vez que você encosta na chave sem querer!), se você não usa *Yubico OTP* legado, execute **`ykman otp delete 1`** (ou troque os slots com `ykman otp swap`) e mantenha no **Slot 2** a sua chave **`HMAC-SHA1 Challenge-Response` com `--touch`** para destravar seu cofre **KeePassXC**!

## Como verificar
Ao gerar a chave Challenge-Response no Slot 2 com `ykman otp chalresp --generate --touch 2`, anote ou copie imediatamente o segredo hexadecimal exibido na tela para gravar exatamente a mesma chave (`ykman otp chalresp --touch 2 <HEX>`) na sua **YubiKey de Backup**!

## Conexões
- [[yubikey-applet-oath-totp-hotp-ykman-oath-touch-password-cli]] — Veja também: Gerador de Códigos **OATH-TOTP e HOTP** em Hardware com **`ykman oath`**: Aposentando Apps de Celular Vulneráveis com Proteção por Senha e Toque (`--touch`).
- [[yubikey-bloqueio-interfaces-config-lock-code-usb-nfc-enterprise]] — Veja também: Hardening Corporativo da YubiKey com **`ykman config`**: Desabilitando Interfaces USB/NFC e Travando Configurações com **`--lock-code` (`Configuration Lock`)**.
- [[yubikey-arquitetura-ykman-aplicacoes-fido2-piv-openpgp-oath-otp]] — Referência cruzada direta com yubikey-arquitetura-ykman-aplicacoes-fido2-piv-openpgp-oath-otp.
- [[keepassxc-autenticacao-multifator-yubikey-hmac-sha1-keyfile]] — Referência cruzada direta com keepassxc-autenticacao-multifator-yubikey-hmac-sha1-keyfile.
- [[vaultwarden-autenticacao-2fa-webauthn-fido2-yubikey-totp-duo-email]] — Referência cruzada direta com vaultwarden-autenticacao-2fa-webauthn-fido2-yubikey-totp-duo-email.

## Fontes
- [YubiKey Manager (`ykman`) Official Repository (`Yubico/yubikey-manager`)](https://raw.githubusercontent.com/Yubico/yubikey-manager/main/README.adoc) — documentação oficial da biblioteca e CLI `ykman` cobrindo gerenciamento de interfaces USB/NFC e applets FIDO2, PIV, OpenPGP, OATH e OTP em YubiKeys; consultado em 2026-10-03.
- [Yubico `pam-u2f` Official Repository and Specification (`Yubico/pam-u2f`)](https://raw.githubusercontent.com/Yubico/pam-u2f/main/README) — documentação oficial do módulo `pam_u2f.so` e utilitário `pamu2fcfg` detalhando `authfile`, `cue`, `pinverification`, `userpresence`, `origin`, `sshformat` e proteção contra chave clonada; consultado em 2026-10-03.
