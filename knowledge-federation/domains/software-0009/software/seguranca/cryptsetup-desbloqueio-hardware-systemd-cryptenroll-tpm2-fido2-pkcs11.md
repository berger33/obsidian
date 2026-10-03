---
id: software.seguranca.tranche08.000725
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

# LUKS2 + **`systemd-cryptenroll`**: Vinculação de Keyslots a Chips **TPM 2.0 (PCRs + PIN)**, Chaves de Segurança **FIDO2 (YubiKey)** e SmartCards **PKCS#11**

## Em uma frase
O formato de metadados JSON do LUKS2 suporta nativamente objetos **`Tokens`**, permitindo que a ferramenta oficial **`systemd-cryptenroll`** vincule o desbloqueio de discos criptografados Linux diretamente a um chip **TPM 2.0 (`--tpm2-device=auto`)**, a um token de hardware **FIDO2 / WebAuthn (`--fido2-device=auto`)**, a um SmartCard **PKCS#11 (`--pkcs11-token-uri=auto`)** ou a uma **Recovery Key** legível em grupos de 8 caracteres (`--recovery-key`).

## Por que importa
Ao vincular um disco LUKS2 ao **TPM 2.0**, nunca vincule apenas aos registradores PCR de firmware sem PIN em notebooks que saem do escritório (pois um atacante com acesso físico ao notebook que roube a máquina e consiga explorar uma vulnerabilidade pós-boot ou farejar o barramento SPI/LPC sem `--tpm2-with-pin=yes` obteria o desbloqueio automático): use **`--tpm2-pcrs=0+2+7`** (ou assinatura de política de kernel unificado `--tpm2-public-key=`) combinado com **`--tpm2-with-pin=yes`**!

## Como funciona
Já com **`--fido2-device=auto --fido2-with-client-pin=yes --fido2-with-user-presence=yes`**, o notebook só decifra o disco LUKS2 se a chave YubiKey FIDO2 física estiver espetada na porta USB, o PIN for digitado e o usuário tocar no sensor capacitivo usando a extensão **`hmac-secret`** do FIDO2.

## Exemplo
```bash
# Gerar uma Recovery Key oficial de emergencia e registrar um token FIDO2 (YubiKey hmac-secret) no volume LUKS2
sudo systemd-cryptenroll --recovery-key /dev/nvme0n1p3
sudo systemd-cryptenroll --fido2-device=auto \
  --fido2-with-client-pin=yes \
  --fido2-with-user-presence=yes \
  /dev/nvme0n1p3
```

## Limites e trade-offs
Para listar todos os slots e o tipo de cada chave/token (senha, `tpm2`, `fido2`, `pkcs11`, `recovery`) ou limpar tokens antigos em um único comando, execute **`systemd-cryptenroll /dev/nvme0n1p3`** ou `sudo systemd-cryptenroll --wipe-slot=tpm2 /dev/nvme0n1p3`.

## Como verificar
Verifique na seção `Tokens:` do `sudo cryptsetup luksDump /dev/nvme0n1p3` o registro do token `systemd-fido2` ou `systemd-tpm2`.

## Conexões
- [[cryptsetup-integracao-kernel-keyring-logon-keys-vk-caching]] — Veja também: Cryptsetup & **Linux Kernel Keyring**: Proteção da Volume Key com Chaves do Tipo **`logon`** e Tokens `luks2-keyring`.
- [[cryptsetup-recriptografia-online-cryptsetup-reencrypt-resiliencia]] — Veja também: Cryptsetup: **Criptografia e Recriptografia Online (`cryptsetup reencrypt`)** de Volumes LUKS2 Montados com *Crash Recovery* em Metadados.
- [[cryptsetup-arquitetura-dm-crypt-luks2-veritysetup-integritysetup]] — Referência cruzada direta com cryptsetup-arquitetura-dm-crypt-luks2-veritysetup-integritysetup.
- [[cryptsetup-gerenciamento-keyslots-luksaddkey-lukskillslot-lukschangekey]] — Referência cruzada direta com cryptsetup-gerenciamento-keyslots-luksaddkey-lukskillslot-lukschangekey.
- [[clevis-integracao-luks2-clevis-luks-bind-initramfs-dracut-systemd]] — Referência cruzada direta com clevis-integracao-luks2-clevis-luks-bind-initramfs-dracut-systemd.

## Fontes
- [Cryptsetup Official GitLab Repository — LUKS2, veritysetup & integritysetup Reference](https://gitlab.com/cryptsetup/cryptsetup/-/raw/main/README.md) — documentação oficial do projeto cryptsetup cobrindo LUKS2, Argon2id, dm-verity, dm-integrity e interoperabilidade BitLocker/VeraCrypt; consultado em 2026-10-03.
- [Cryptsetup Official Documentation — Linux Kernel Keyring & VK Caching](https://gitlab.com/cryptsetup/cryptsetup/-/raw/main/docs/Keyring.txt) — especificação oficial do uso de chaves do tipo logon no Linux Kernel Keyring pelo cryptsetup para proteção da Volume Key em memória; consultado em 2026-10-03.
- [LUKS2 On-Disk Format Official Specification](https://gitlab.com/cryptsetup/LUKS2-docs) — especificação oficial do formato de disco LUKS2, metadados JSON, keyslots e tokens; consultado em 2026-10-03.
