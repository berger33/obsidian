---
id: software.seguranca.tranche15.001443
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

# Chaves SSH Presas ao Hardware da YubiKey (**`ed25519-sk` e `ecdsa-sk`**): `resident`, `verify-required`, `no-touch-required` e Portabilidade com `ssh-keygen -K`

## Em uma frase
Como gerar uma chave SSH moderna do **OpenSSH (`sk-ssh-ed25519@openssh.com` — `ed25519-sk`)** onde a chave privada é protegida pelo chip FIDO2 da **YubiKey** e exige simultaneamente: **(1) Digitar o PIN FIDO2 da YubiKey (`-O verify-required`)** e **(2) Tocar fisicamente no sensor dourado da YubiKey a cada conexão SSH**, podendo ainda carregar a chave em qualquer computador novo com um único comando **`ssh-keygen -K`**?

## Por que importa
Executando o comando nativo **`ssh-keygen -t ed25519-sk -O resident -O verify-required -O application=ssh:producao`**!

## Como funciona
Veja o poder da combinação **`-O resident -O verify-required`**: **(1)** Com `-O resident`, a credencial fica guardada dentro da memória segura da própria YubiKey — quando você sentar em uma estação de trabalho nova ou de emergência, basta plugar a YubiKey e rodar **`ssh-keygen -K`** (ou `ssh-add -K` para carregar apenas na memória RAM do `ssh-agent` sem gravar nada no disco da máquina!) para baixar o *key handle*!; e **(2)** Com **`-O verify-required`**, tanto o cliente SSH quanto o servidor OpenSSH remoto exigem que a flag criptográfica `User Verified (UV = 1)` esteja assinada pelo hardware da YubiKey, obrigando a digitação do **PIN FIDO2 + Toque Físico**!

## Exemplo
```bash
# Gerar uma chave SSH Ed25519-SK residente na YubiKey exigindo PIN + toque fisico (verify-required) e carrega-la em memoria via ssh-add -K
ssh-keygen -t ed25519-sk \
  -O resident \
  -O verify-required \
  -O application=ssh:sre-producao \
  -O user=ana.silva \
  -f ~/.ssh/id_ed25519_sk_producao
ssh-add -K
```

## Limites e trade-offs
Como garantir no servidor **OpenSSH (`sshd_config` ou `authorized_keys`)** de destino que ninguém consiga conectar usando uma chave `-sk` que não tenha exigido PIN (`verify-required`) nem toque físico? Adicionando **`PubkeyAuthOptions verify-required`** no `/etc/ssh/sshd_config` (ou prefixando a chave pública no `~/.ssh/authorized_keys` com `verify-required sk-ssh-ed25519@openssh.com AAAAGnNr...`)!

## Como verificar
Dica prática: sempre passe **`-O application=ssh:<nome-descritivo>`** e **`-O user=<identificador>`** ao criar chaves `-O resident`, pois esses dois campos aparecem claramente quando você lista suas chaves com **`ykman fido credentials list`**!

## Conexões
- [[yubikey-gerenciamento-fido2-passkeys-resident-keys-pin-credenciais]] — Veja também: Gerenciamento de **FIDO2 / WebAuthn e Passkeys (`Discoverable / Resident Credentials`)** na YubiKey com **`ykman fido`**.
- [[yubikey-autenticacao-linux-pam-u2f-pamu2fcfg-sudo-login-ssh]] — Veja também: Autenticação Linux Local e 2FA com **`pam-u2f` (`pam_u2f.so` e `pamu2fcfg`)**: Protegendo `sudo`, `gdm`/`sddm`, `polkit` e `sshd` com YubiKey FIDO2.
- [[yubikey-arquitetura-ykman-aplicacoes-fido2-piv-openpgp-oath-otp]] — Referência cruzada direta com yubikey-arquitetura-ykman-aplicacoes-fido2-piv-openpgp-oath-otp.

## Fontes
- [YubiKey Manager (`ykman`) Official Repository (`Yubico/yubikey-manager`)](https://raw.githubusercontent.com/Yubico/yubikey-manager/main/README.adoc) — documentação oficial da biblioteca e CLI `ykman` cobrindo gerenciamento de interfaces USB/NFC e applets FIDO2, PIV, OpenPGP, OATH e OTP em YubiKeys; consultado em 2026-10-03.
- [Yubico `pam-u2f` Official Repository and Specification (`Yubico/pam-u2f`)](https://raw.githubusercontent.com/Yubico/pam-u2f/main/README) — documentação oficial do módulo `pam_u2f.so` e utilitário `pamu2fcfg` detalhando `authfile`, `cue`, `pinverification`, `userpresence`, `origin`, `sshformat` e proteção contra chave clonada; consultado em 2026-10-03.
