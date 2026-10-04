---
id: software.seguranca.tranche15.001442
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

# Gerenciamento de **FIDO2 / WebAuthn e Passkeys (`Discoverable / Resident Credentials`)** na YubiKey com **`ykman fido`**

## Em uma frase
Qual é a diferença técnica entre uma credencial **FIDO2 Non-Resident (Server-Side Credential)** e uma **Passkey FIDO2 Resident / Discoverable (`rk`)** armazenada dentro da YubiKey, e como usar o **`ykman fido`** para gerenciar o PIN FIDO2, exigir verificação sempre (`always-uv`) e listar ou apagar Passkeys antigas que estão ocupando slots na chave?

## Por que importa
Na credencial **Non-Resident**, a YubiKey não guarda nada na sua memória NVRAM: ela deriva a chave privada sob demanda a partir de uma semente mestra interna + o `keyHandle` cifrado que o site devolve no login! Já em uma **Passkey Resident / Discoverable (`ssh-keygen -t ed25519-sk -O resident` ou login WebAuthn sem digitar username)**, o par de chaves, o `rp_id` (ex.: `github.com`, `kanidm.exemplo.br`) e o `user_id` ficam gravados dentro dos **slots de credenciais residentes da memória NVRAM da YubiKey (até 100 Passkeys residentes no firmware 5.7+!)**!

## Como funciona
Com a subfamília de comandos **`ykman fido`**, você configura o **PIN FIDO2** (`ykman fido access change-pin`), define comprimento mínimo de PIN (`set-pin-length`), audita todas as Passkeys residentes salvas na chave (`ykman fido credentials list`) e remove credenciais obsoletas (`ykman fido credentials delete`)!

## Exemplo
```bash
# Verificar o status do applet FIDO2 (tentativas restantes de PIN), listar todas as Passkeys residentes na YubiKey e exigir PIN minimo de 8 caracteres
ykman fido info
ykman fido access change-pin
ykman fido access set-pin-length 8
ykman fido credentials list
```

## Limites e trade-offs
Cuidado fundamental com o **PIN FIDO2** da YubiKey: após **8 tentativas consecutivas de PIN incorretas**, o applet FIDO2 da YubiKey se bloqueia permanentemente por segurança contra força bruta! A única forma de desbloquear um applet FIDO2 travado é executar **`ykman fido reset`** (com a chave recém-inserida nos primeiros 5 segundos e confirmando com toque físico), o que **destrói permanentemente a semente FIDO2 e invalida todas as credenciais FIDO2/U2F registradas naquela chave** (sem afetar `PIV`, `OpenPGP` ou `OATH`)!

## Como verificar
Por isso, a regra de ouro ao usar YubiKeys para FIDO2/Passkeys é: **sempre registre pelo menos 2 chaves físicas (YubiKey Principal + YubiKey de Backup guardada no cofre)** em todas as suas contas críticas!

## Conexões
- [[yubikey-arquitetura-ykman-aplicacoes-fido2-piv-openpgp-oath-otp]] — Veja também: Arquitetura da **YubiKey** e CLI Oficial **`ykman` (`Yubico/yubikey-manager`)**: Os 5 Applets Isolados em Hardware (`FIDO2`, `PIV`, `OpenPGP`, `OATH`, `OTP`) e Interfaces USB/NFC.
- [[yubikey-chaves-ssh-hardware-ed25519-sk-resident-verify-required]] — Veja também: Chaves SSH Presas ao Hardware da YubiKey (**`ed25519-sk` e `ecdsa-sk`**): `resident`, `verify-required`, `no-touch-required` e Portabilidade com `ssh-keygen -K`.
- [[kanidm-autenticacao-passkeys-webauthn-attested-passkeys-politicas]] — Referência cruzada direta com kanidm-autenticacao-passkeys-webauthn-attested-passkeys-politicas.

## Fontes
- [YubiKey Manager (`ykman`) Official Repository (`Yubico/yubikey-manager`)](https://raw.githubusercontent.com/Yubico/yubikey-manager/main/README.adoc) — documentação oficial da biblioteca e CLI `ykman` cobrindo gerenciamento de interfaces USB/NFC e applets FIDO2, PIV, OpenPGP, OATH e OTP em YubiKeys; consultado em 2026-10-03.
- [Yubico `pam-u2f` Official Repository and Specification (`Yubico/pam-u2f`)](https://raw.githubusercontent.com/Yubico/pam-u2f/main/README) — documentação oficial do módulo `pam_u2f.so` e utilitário `pamu2fcfg` detalhando `authfile`, `cue`, `pinverification`, `userpresence`, `origin`, `sshformat` e proteção contra chave clonada; consultado em 2026-10-03.
