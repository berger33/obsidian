---
id: software.seguranca.tranche15.001444
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

# Autenticação Linux Local e 2FA com **`pam-u2f` (`pam_u2f.so` e `pamu2fcfg`)**: Protegendo `sudo`, `gdm`/`sddm`, `polkit` e `sshd` com YubiKey FIDO2

## Em uma frase
Como configurar sua estação de trabalho ou servidor Linux para que o comando **`sudo`**, o desbloqueio de tela (**GDM / SDDM / Swaylock**) e o login exijam **um toque físico na sua YubiKey via módulo oficial `pam_u2f.so` (`Yubico/pam-u2f`)**?

## Por que importa
Conforme a documentação oficial do **`pam-u2f`** (construído sobre a biblioteca `libfido2`), o processo leva menos de 2 minutos em duas etapas: **(Etapa 1 — Registro com `pamu2fcfg`)**: você pluga a YubiKey Principal e roda `pamu2fcfg > /etc/Yubico/u2f_keys`, e em seguida pluga a YubiKey de Backup e roda **`pamu2fcfg -n >> /etc/Yubico/u2f_keys`** (a flag `-n` omite o nome do usuário e anexa a segunda chave após `:` na mesma linha do usuário: `usuario:KeyHandle1,PubKey1:KeyHandle2,PubKey2`!).

## Como funciona
**(Etapa 2 — Configuração do `/etc/pam.d/sudo`)**: adiciona a linha `auth required pam_u2f.so authfile=/etc/Yubico/u2f_keys cue`!

## Exemplo
```bash
# Registrar a YubiKey principal e a YubiKey de backup no arquivo central /etc/Yubico/u2f_keys usando pamu2fcfg com origin e appid explicitos
mkdir -p /etc/Yubico
pamu2fcfg -o pam://estacao-secops -i pam://estacao-secops > /etc/Yubico/u2f_keys
pamu2fcfg -n -o pam://estacao-secops -i pam://estacao-secops >> /etc/Yubico/u2f_keys
chmod 0644 /etc/Yubico/u2f_keys
```

## Limites e trade-offs
Preste atenção a três argumentos de segurança importantíssimos do **`pam_u2f.so`** documentados no `README` oficial: **(1) `cue`** — exibe no terminal a mensagem amigável `"Please touch the device."` para o usuário saber que o `sudo` está aguardando o toque na YubiKey; **(2) `origin=pam://meu-host` e `appid=pam://meu-host` explícitos** — por padrão o `pam-u2f` usa `pam://$HOSTNAME`, o que significa que se você mudar o hostname da máquina no futuro, o hash `rp_id` mudará e a YubiKey rejeitará o login a menos que você tenha fixado `origin=` no `pamu2fcfg` e no `/etc/pam.d/`!; e **(3) `pinverification=1` (ou `userverification=1`)** para exigir o PIN FIDO2 além do toque!

## Como verificar
E a regra de ouro de segurança destacada em caixa alta no `README` do `pam-u2f`: **SEMPRE mantenha um segundo terminal com shell `root` aberto enquanto edita `/etc/pam.d/sudo` ou `/etc/pam.d/common-auth`** e teste `sudo -k && sudo ls` em outra janela antes de fechar o terminal `root`!

## Conexões
- [[yubikey-chaves-ssh-hardware-ed25519-sk-resident-verify-required]] — Veja também: Chaves SSH Presas ao Hardware da YubiKey (**`ed25519-sk` e `ecdsa-sk`**): `resident`, `verify-required`, `no-touch-required` e Portabilidade com `ssh-keygen -K`.
- [[yubikey-gerenciamento-piv-smartcard-x509-slots-9a-9c-9d-9e-pkcs11]] — Veja também: Smartcard X.509 (**PIV — *Personal Identity Verification* `FIPS 201`**) na YubiKey com **`ykman piv`**: Os Slots `9a`, `9c`, `9d`, `9e` e Hardening de PIN/PUK/Management Key.
- [[yubikey-arquitetura-ykman-aplicacoes-fido2-piv-openpgp-oath-otp]] — Referência cruzada direta com yubikey-arquitetura-ykman-aplicacoes-fido2-piv-openpgp-oath-otp.
- [[sssd-autenticacao-smartcards-pkcs11-certmap-fido2-passkeys]] — Referência cruzada direta com sssd-autenticacao-smartcards-pkcs11-certmap-fido2-passkeys.

## Fontes
- [YubiKey Manager (`ykman`) Official Repository (`Yubico/yubikey-manager`)](https://raw.githubusercontent.com/Yubico/yubikey-manager/main/README.adoc) — documentação oficial da biblioteca e CLI `ykman` cobrindo gerenciamento de interfaces USB/NFC e applets FIDO2, PIV, OpenPGP, OATH e OTP em YubiKeys; consultado em 2026-10-03.
- [Yubico `pam-u2f` Official Repository and Specification (`Yubico/pam-u2f`)](https://raw.githubusercontent.com/Yubico/pam-u2f/main/README) — documentação oficial do módulo `pam_u2f.so` e utilitário `pamu2fcfg` detalhando `authfile`, `cue`, `pinverification`, `userpresence`, `origin`, `sshformat` e proteção contra chave clonada; consultado em 2026-10-03.
