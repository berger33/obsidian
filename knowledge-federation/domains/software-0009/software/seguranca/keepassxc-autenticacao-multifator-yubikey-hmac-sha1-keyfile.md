---
id: software.seguranca.tranche13.001202
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/keepassxreboot/keepassxc/develop/README.md", "https://keepassxc.org/docs/KeePassXC_UserGuide"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Chave Composta do KeePassXC: Combinando **Senha Mestra + Key File + Hardware Challenge-Response (`YubiKey` / `OnlyKey` HMAC-SHA1)**

## Em uma frase
E se um atacante infectar a estação de um administrador com um *keylogger* que captura a Senha Mestra digitada no teclado e roubar o arquivo `cofre.kdbx` sincronizado no Nextcloud/Dropbox? Como impedir que o invasor consiga descriptografar o banco KDBX?

## Por que importa
O KeePassXC suporta uma **Chave Composta (*Composite Master Key*)** que combina até **três fatores independentes** derivados juntos antes do Argon2id: **(1) Senha Mestra (*Password*)** — algo que você sabe; **(2) Arquivo-Chave (*Key File*)** — um arquivo de 64+ bytes de entropia criptográfica pura armazenado em um pendrive separado (nunca na mesma pasta de nuvem do `.kdbx`!); e **(3) Desafio-Resposta de Hardware (*YubiKey / OnlyKey HMAC-SHA1 Challenge-Response*)** — algo físico que exige toque humano!

## Como funciona
Quando o **YubiKey Challenge-Response** está vinculado ao cofre KDBX 4, o cabeçalho do banco armazena uma semente pública aleatória de 32 bytes (*Challenge*); toda vez que você abre ou salva o banco, o KeePassXC envia esse *Challenge* para o Slot 2 da YubiKey via USB, e o chip seguro calcula internamente o `HMAC-SHA1(Segredo_Interno_YubiKey, Challenge)` para compor a chave mestra! Como o segredo de 20 bytes gravado dentro da YubiKey **nunca pode ser lido ou exportado pelo computador**, roubar o `.kdbx` + a senha digitada é 100% inútil sem a YubiKey física!

## Exemplo
```bash
# Abrir e listar entradas de um cofre KDBX protegido simultaneamente por Senha Mestra, Key File e YubiKey (Slot 2) via keepassxc-cli
keepassxc-cli ls \
  --key-file /media/usb_seguro/admin.keyx \
  --yubikey 2 \
  ./cofre-infraestrutura.kdbx
```

## Limites e trade-offs
Regra crítica de backup ao usar **YubiKey HMAC-SHA1 Challenge-Response**: no momento em que você programar o Slot 2 da sua YubiKey principal no *YubiKey Manager (`ykman otp chalresp --generate 2`)*, **grave imediatamente exatamente o mesmo segredo hexadecimal de 20 bytes em uma segunda YubiKey de backup guardada no cofre físico**! Se você tiver apenas 1 YubiKey e ela for perdida ou danificada sem backup do segredo HMAC, o banco KDBX será matematicamente irrecuperável.

## Como verificar
Nunca sincronize o *Key File* (`.keyx`) no mesmo serviço de armazenamento em nuvem onde reside o arquivo `.kdbx`.

## Conexões
- [[keepassxc-arquitetura-cofre-offline-kdbx4-argon2id-chacha20-aes256]] — Veja também: Arquitetura Criptográfica do **KeePassXC (`keepassxreboot/keepassxc`)**: Formato **KDBX 4**, Derivação **Argon2id** e Cifras **ChaCha20 / AES-256 / Twofish**.
- [[keepassxc-integracao-ssh-agent-chaves-privadas-anexos-lock]] — Veja também: Integração Nativa com **`ssh-agent`** no KeePassXC: Carregamento Automático de Chaves SSH ao Destravar o Cofre e Remoção Automática no Lock.
- [[openssh-chaves-hardware-fido2-u2f-ed25519-sk-resident-keys-touch]] — Referência cruzada direta com openssh-chaves-hardware-fido2-u2f-ed25519-sk-resident-keys-touch.

## Fontes
- [KeePassXC Official GitHub — Cross-Platform Community-Driven Port of Keepass](https://raw.githubusercontent.com/keepassxreboot/keepassxc/develop/README.md) — repositório oficial do KeePassXC cobrindo criptografia KDBX 4 (AES-256, Twofish, ChaCha20), YubiKey/OnlyKey, `keepassxc-cli`, SSH Agent e Secret Service; consultado em 2026-10-03.
- [KeePassXC Official User Guide (`keepassxc.org/docs/KeePassXC_UserGuide`)](https://keepassxc.org/docs/KeePassXC_UserGuide) — guia oficial do usuário do KeePassXC detalhando Auto-Type, integração com navegador, Passkeys, KeeShare, Database Reports (HIBP) e proteção de memória/tela; consultado em 2026-10-03.
