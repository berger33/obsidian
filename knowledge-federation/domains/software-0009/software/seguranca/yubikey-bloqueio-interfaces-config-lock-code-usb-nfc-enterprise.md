---
id: software.seguranca.tranche15.001449
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

# Hardening Corporativo da YubiKey com **`ykman config`**: Desabilitando Interfaces USB/NFC e Travando Configurações com **`--lock-code` (`Configuration Lock`)**

## Em uma frase
Quando o time de Segurança Corporativa distribui 500 YubiKeys pré-configuradas para os colaboradores da empresa (ou quando um viajante executivo atravessa fronteiras com a chave no bolso), como: **(1) Desabilitar completamente a antena `NFC` (ou desativar applets não utilizados)** para impedir leitura sem fio não autorizada em transporte público e **(2) Impedir que um usuário ou malware altere quais interfaces/applets estão habilitados na YubiKey**?

## Por que importa
Usando o subcomando **`ykman config`** com um **Configuration Lock Code de 16 bytes (`--lock-code` / `ykman config set-lock-code`)**!

## Como funciona
Com **`ykman config nfc --disable-all`** (ou habilitando no NFC apenas `FIDO2` e `OATH` com `ykman config nfc --enable FIDO2 --enable OATH`), você desliga no firmware da YubiKey qualquer resposta por aproximação nos demais protocolos. E ao definir um código de bloqueio de 32 caracteres hexadecimais com **`ykman config set-lock-code --generate`**, nenhuma alteração de `ykman config usb` ou `ykman config nfc` é aceita pela YubiKey sem fornecer `--lock-code`!

## Exemplo
```bash
# Desabilitar a interface OTP (teclado USB) e desligar todos os applets NFC exceto FIDO2, protegendo a configuracao da YubiKey com Lock Code
ykman config usb --disable OTP --force
ykman config nfc --disable-all --force
ykman config nfc --enable FIDO2 --force
ykman config set-lock-code --generate
```

## Limites e trade-offs
Nas YubiKeys com firmware **5.7+** (e linhas *YubiKey Bio* / *YubiKey 5 FIPS*), o `ykman` e o FIDO2 Enterprise suportam ainda recursos avançados de governança corporativa como **Enterprise Attestation (FIDO2)**, exigência de troca forçada de PIN no primeiro uso (`ykman fido access force-change`) e comprimento mínimo de PIN FIDO2 (`set-pin-length`)!

## Como verificar
Guarde o `lock-code` gerado pelo provisionamento corporativo no cofre de administração de TI (Vaultwarden / HashiCorp Vault) vinculado ao número de série (`ykman list --serials`) da chave entregue ao colaborador.

## Conexões
- [[yubikey-applet-otp-slots-challenge-response-hmac-sha1-luks-keepassxc]] — Veja também: Configurando os **Slots 1 e 2 do Applet `OTP` (`ykman otp`)**: **HMAC-SHA1 Challenge-Response** para **KeePassXC e LUKS2**, Senha Estática e Yubico OTP.
- [[yubikey-auditoria-atestado-fido-piv-attestation-verificacao-autenticidade]] — Veja também: Verificação Criptográfica de Autenticidade e Origem de Hardware (**PIV Attestation & FIDO Attestation**) na YubiKey: Provando que uma Chave Foi Gerada *On-Chip*!.
- [[yubikey-arquitetura-ykman-aplicacoes-fido2-piv-openpgp-oath-otp]] — Referência cruzada direta com yubikey-arquitetura-ykman-aplicacoes-fido2-piv-openpgp-oath-otp.
- [[yubikey-gerenciamento-fido2-passkeys-resident-keys-pin-credenciais]] — Referência cruzada direta com yubikey-gerenciamento-fido2-passkeys-resident-keys-pin-credenciais.

## Fontes
- [YubiKey Manager (`ykman`) Official Repository (`Yubico/yubikey-manager`)](https://raw.githubusercontent.com/Yubico/yubikey-manager/main/README.adoc) — documentação oficial da biblioteca e CLI `ykman` cobrindo gerenciamento de interfaces USB/NFC e applets FIDO2, PIV, OpenPGP, OATH e OTP em YubiKeys; consultado em 2026-10-03.
- [Yubico `pam-u2f` Official Repository and Specification (`Yubico/pam-u2f`)](https://raw.githubusercontent.com/Yubico/pam-u2f/main/README) — documentação oficial do módulo `pam_u2f.so` e utilitário `pamu2fcfg` detalhando `authfile`, `cue`, `pinverification`, `userpresence`, `origin`, `sshformat` e proteção contra chave clonada; consultado em 2026-10-03.
