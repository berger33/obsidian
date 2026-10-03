---
id: software.seguranca.tranche08.000724
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-08.md"
fontes: ["https://gitlab.com/cryptsetup/cryptsetup/-/raw/main/README.md", "https://gitlab.com/cryptsetup/cryptsetup/-/raw/main/docs/Keyring.txt", "https://gitlab.com/cryptsetup/LUKS2-docs"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Cryptsetup & **Linux Kernel Keyring**: Proteção da Volume Key com Chaves do Tipo **`logon`** e Tokens `luks2-keyring`

## Em uma frase
Conforme detalhado na documentação oficial `docs/Keyring.txt` do repositório `cryptsetup`, desde o kernel Linux 4.10 e `cryptsetup 2.0+`, a **Volume Key (VK)** de dispositivos LUKS2 **não é mais passada diretamente em texto claro na tabela do `dm-crypt`** (onde antes um processo root conseguia lê-la com `dmsetup table --showkeys`): ela é carregada no **Linux Kernel Keyring Service**!

## Por que importa
Mais especificamente, o `cryptsetup` carrega a Volume Key como uma chave de kernel do tipo **`logon`**: chaves do tipo `logon` no kernel Linux possuem a propriedade de segurança fundamental de que **seu payload pode ser lido exclusivamente por subsistemas internos do kernel (como o `dm-crypt`) e JAMAIS pode ser lido de volta pelo espaço de usuário (`keyctl read` ou `keyctl pipe` retornam `EOPNOTSUPP`)**, além de serem desvinculadas automaticamente do thread keyring assim que o processo `cryptsetup` encerra.

## Como funciona
Adicionalmente, o token interno **`luks2-keyring`** (`cryptsetup token add --key-description ...`) permite carregar uma passphrase no keyring do usuário (`keyctl padd user ... @u`) para ativar múltiplos volumes LUKS2 automaticamente em sequência.

## Exemplo
```bash
# Verificar que a tabela do dm-crypt no kernel referencia apenas o descritor do kernel keyring (e nao a chave hex bruta)
sudo dmsetup table --target crypt
```

## Limites e trade-offs
Quando precisar revogar imediatamente da memória RAM do kernel a Volume Key de um volume LUKS2 que ainda está montado (por exemplo, um botão de pânico ou gatilho de intrusão USBGuard/tamper físico), o comando **`sudo cryptsetup erase`** ou **`sudo dmsetup message <nome_ativo> 0 key wipe`** zera a chave na memória do `dm-crypt` instantaneamente (bloqueando todo I/O subsequente até que **`cryptsetup luksResume`** seja executado com a senha)!

## Como verificar
Teste suspender um volume de teste com **`sudo cryptsetup luksSuspend <nome_ativo>`** (que limpa a Volume Key da RAM!) e retomá-lo com **`sudo cryptsetup luksResume <nome_ativo>`**.

## Conexões
- [[cryptsetup-gerenciamento-keyslots-luksaddkey-lukskillslot-lukschangekey]] — Veja também: Cryptsetup: Gestão de **Keyslots LUKS2** (`luksAddKey`, `luksChangeKey`, `luksRemoveKey`, `luksKillSlot`) e Conversão de KDF (`luksConvertKey`).
- [[cryptsetup-desbloqueio-hardware-systemd-cryptenroll-tpm2-fido2-pkcs11]] — Veja também: LUKS2 + **`systemd-cryptenroll`**: Vinculação de Keyslots a Chips **TPM 2.0 (PCRs + PIN)**, Chaves de Segurança **FIDO2 (YubiKey)** e SmartCards **PKCS#11**.
- [[cryptsetup-arquitetura-dm-crypt-luks2-veritysetup-integritysetup]] — Referência cruzada direta com cryptsetup-arquitetura-dm-crypt-luks2-veritysetup-integritysetup.
- [[veracrypt-higiene-memoria-ram-encryption-cold-boot-hibernacao-swap]] — Referência cruzada direta com veracrypt-higiene-memoria-ram-encryption-cold-boot-hibernacao-swap.

## Fontes
- [Cryptsetup Official GitLab Repository — LUKS2, veritysetup & integritysetup Reference](https://gitlab.com/cryptsetup/cryptsetup/-/raw/main/README.md) — documentação oficial do projeto cryptsetup cobrindo LUKS2, Argon2id, dm-verity, dm-integrity e interoperabilidade BitLocker/VeraCrypt; consultado em 2026-10-03.
- [Cryptsetup Official Documentation — Linux Kernel Keyring & VK Caching](https://gitlab.com/cryptsetup/cryptsetup/-/raw/main/docs/Keyring.txt) — especificação oficial do uso de chaves do tipo logon no Linux Kernel Keyring pelo cryptsetup para proteção da Volume Key em memória; consultado em 2026-10-03.
- [LUKS2 On-Disk Format Official Specification](https://gitlab.com/cryptsetup/LUKS2-docs) — especificação oficial do formato de disco LUKS2, metadados JSON, keyslots e tokens; consultado em 2026-10-03.
