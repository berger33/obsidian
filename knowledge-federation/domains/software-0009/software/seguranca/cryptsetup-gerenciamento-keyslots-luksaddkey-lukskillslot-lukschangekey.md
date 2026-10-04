---
id: software.seguranca.tranche08.000723
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

# Cryptsetup: Gestão de **Keyslots LUKS2** (`luksAddKey`, `luksChangeKey`, `luksRemoveKey`, `luksKillSlot`) e Conversão de KDF (`luksConvertKey`)

## Em uma frase
No LUKS2, a **Volume Key (Master Key)** que cifra os blocos do disco permanece constante, enquanto até **32 Keyslots (`0` a `31`)** armazenam cópias dessa Volume Key cifradas com diferentes senhas, chaves de recuperação ou tokens de hardware.

## Por que importa
Isso permite que uma empresa configure o **Keyslot 0** para a senha pessoal do usuário (ou token TPM2/FIDO2), o **Keyslot 1** para uma chave de recuperação de emergência de 256 bits guardada no cofre HashiCorp Vault/PAM do SOC, e o **Keyslot 2** para o desbloqueio de rede Clevis/Tang: quando um funcionário é desligado ou perde seu token, o SOC usa a chave de recuperação do Keyslot 1 para apagar instantaneamente o Keyslot 0 com **`cryptsetup luksKillSlot <dev> 0`**!

## Como funciona
Além disso, se um volume LUKS2 antigo ainda tiver um keyslot usando o legado `pbkdf2`, o comando **`cryptsetup luksConvertKey --pbkdf argon2id <dev>`** converte o keyslot para `argon2id` no lugar, sem precisar recriar o volume.

## Exemplo
```bash
# Adicionar uma chave de recuperacao corporativa no Keyslot 1, converter KDF legado para argon2id e revogar um slot comprometido
sudo cryptsetup luksAddKey --key-slot 1 --pbkdf argon2id /dev/nvme0n1p3 /etc/secops/recovery.key
sudo cryptsetup luksKillSlot --key-file /etc/secops/recovery.key /dev/nvme0n1p3 0
```

## Limites e trade-offs
Para testar se uma senha ou arquivo de chave desbloqueia um keyslot específico **sem precisar montar nem ativar o volume**, execute **`sudo cryptsetup open --test-passphrase --key-slot 1 /dev/nvme0n1p3 --verbose`**!

## Como verificar
Verifique no `sudo cryptsetup luksDump /dev/nvme0n1p3` quais slots estão listados sob a seção `Keyslots:` e confirme a remoção de qualquer slot obsoleto.

## Conexões
- [[cryptsetup-formatacao-luks2-aes-xts-plain64-argon2id-setores-4k]] — Veja também: Cryptsetup: Formatação Segura **LUKS2 (`luksFormat`)** — `aes-xts-plain64` (512 bits), Parâmetros **Argon2id** e Alinhamento de Setores de **4096 Bytes**.
- [[cryptsetup-integracao-kernel-keyring-logon-keys-vk-caching]] — Veja também: Cryptsetup & **Linux Kernel Keyring**: Proteção da Volume Key com Chaves do Tipo **`logon`** e Tokens `luks2-keyring`.
- [[cryptsetup-arquitetura-dm-crypt-luks2-veritysetup-integritysetup]] — Referência cruzada direta com cryptsetup-arquitetura-dm-crypt-luks2-veritysetup-integritysetup.
- [[cryptsetup-desbloqueio-hardware-systemd-cryptenroll-tpm2-fido2-pkcs11]] — Referência cruzada direta com cryptsetup-desbloqueio-hardware-systemd-cryptenroll-tpm2-fido2-pkcs11.
- [[clevis-integracao-luks2-clevis-luks-bind-initramfs-dracut-systemd]] — Referência cruzada direta com clevis-integracao-luks2-clevis-luks-bind-initramfs-dracut-systemd.

## Fontes
- [Cryptsetup Official GitLab Repository — LUKS2, veritysetup & integritysetup Reference](https://gitlab.com/cryptsetup/cryptsetup/-/raw/main/README.md) — documentação oficial do projeto cryptsetup cobrindo LUKS2, Argon2id, dm-verity, dm-integrity e interoperabilidade BitLocker/VeraCrypt; consultado em 2026-10-03.
- [Cryptsetup Official Documentation — Linux Kernel Keyring & VK Caching](https://gitlab.com/cryptsetup/cryptsetup/-/raw/main/docs/Keyring.txt) — especificação oficial do uso de chaves do tipo logon no Linux Kernel Keyring pelo cryptsetup para proteção da Volume Key em memória; consultado em 2026-10-03.
- [LUKS2 On-Disk Format Official Specification](https://gitlab.com/cryptsetup/LUKS2-docs) — especificação oficial do formato de disco LUKS2, metadados JSON, keyslots e tokens; consultado em 2026-10-03.
