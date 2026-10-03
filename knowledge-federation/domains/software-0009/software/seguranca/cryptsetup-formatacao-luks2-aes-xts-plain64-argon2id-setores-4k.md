---
id: software.seguranca.tranche08.000722
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

# Cryptsetup: Formatação Segura **LUKS2 (`luksFormat`)** — `aes-xts-plain64` (512 bits), Parâmetros **Argon2id** e Alinhamento de Setores de **4096 Bytes**

## Em uma frase
Ao formatar uma nova partição ou disco criptografado com **`cryptsetup luksFormat --type luks2`**, três parâmetros criptográficos e de armazenamento determinam tanto a resistência contra ataques de força bruta em GPU quanto a performance de I/O em SSDs NVMe modernos.

## Por que importa
Por padrão no LUKS2, a cifra é **`aes-xts-plain64`** com **`--key-size 512`** (lembre-se de que o modo XTS divide a chave ao meio: uma chave de `512` bits fornece **AES-256 XTS**, enquanto `256` bits forneceria AES-128 XTS!) e o KDF padrão é o **`--pbkdf argon2id`**, onde **`--pbkdf-memory`** (em KiB, até 4 GiB; padrão até 1 GiB de RAM) e **`--iter-time`** (ex.: `3000` ms) neutralizam GPUs.

## Como funciona
Em SSDs NVMe e discos modernos, passar **`--sector-size 4096`** (em vez do setor legado de 512 bytes) multiplica o throughput de criptografia e reduz a sobrecarga de CPU do `dm-crypt` ao processar blocos contíguos de 4 KiB.

## Exemplo
```bash
# Formatar uma particao NVMe com LUKS2, AES-256-XTS (512 bits), Argon2id (1 GiB RAM, 3s) e setores nativos de 4096 bytes
sudo cryptsetup luksFormat --type luks2 \
  --cipher aes-xts-plain64 --key-size 512 --hash sha512 \
  --pbkdf argon2id --pbkdf-memory 1048576 --iter-time 3000 \
  --sector-size 4096 \
  --label "CORP_DATA_ENCRYPTED" \
  /dev/nvme0n1p3
```

## Limites e trade-offs
Atenção em máquinas virtuais pequenas ou sistemas embarcados com pouca RAM (ex.: VMs de 1 GB de RAM ou quando o volume é desbloqueado no `initramfs` com memória restrita): se um keyslot for formatado em uma estação potente com `--pbkdf-memory 2097152` (2 GiB de RAM), uma VM com apenas 1 GiB de RAM falhará por falta de memória (`ENOMEM`) ao tentar abrir o disco! Dimensione `--pbkdf-memory` compatível com a menor RAM onde o disco será aberto.

## Como verificar
Execute **`cryptsetup benchmark`** antes da formatação para medir o throughput de `aes-xts` e as iterações do `argon2id` no hardware alvo.

## Conexões
- [[cryptsetup-arquitetura-dm-crypt-luks2-veritysetup-integritysetup]] — Veja também: Linux **`cryptsetup` & LUKS2**: Arquitetura do Subsistema `dm-crypt`, Metadados JSON **LUKS2**, `veritysetup` (`dm-verity`) e `integritysetup` (`dm-integrity`).
- [[cryptsetup-gerenciamento-keyslots-luksaddkey-lukskillslot-lukschangekey]] — Veja também: Cryptsetup: Gestão de **Keyslots LUKS2** (`luksAddKey`, `luksChangeKey`, `luksRemoveKey`, `luksKillSlot`) e Conversão de KDF (`luksConvertKey`).
- [[hashcat-defesa-engenharia-armazenamento-senhas-argon2id-bcrypt-scrypt-passphrases]] — Referência cruzada direta com hashcat-defesa-engenharia-armazenamento-senhas-argon2id-bcrypt-scrypt-passphrases.

## Fontes
- [Cryptsetup Official GitLab Repository — LUKS2, veritysetup & integritysetup Reference](https://gitlab.com/cryptsetup/cryptsetup/-/raw/main/README.md) — documentação oficial do projeto cryptsetup cobrindo LUKS2, Argon2id, dm-verity, dm-integrity e interoperabilidade BitLocker/VeraCrypt; consultado em 2026-10-03.
- [Cryptsetup Official Documentation — Linux Kernel Keyring & VK Caching](https://gitlab.com/cryptsetup/cryptsetup/-/raw/main/docs/Keyring.txt) — especificação oficial do uso de chaves do tipo logon no Linux Kernel Keyring pelo cryptsetup para proteção da Volume Key em memória; consultado em 2026-10-03.
- [LUKS2 On-Disk Format Official Specification](https://gitlab.com/cryptsetup/LUKS2-docs) — especificação oficial do formato de disco LUKS2, metadados JSON, keyslots e tokens; consultado em 2026-10-03.
