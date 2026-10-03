---
id: software.seguranca.tranche08.000726
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

# Cryptsetup: **Criptografia e Recriptografia Online (`cryptsetup reencrypt`)** de Volumes LUKS2 Montados com *Crash Recovery* em Metadados

## Em uma frase
Se um servidor em produção já possui um volume de dados ext4/XFS em texto claro (ou se a chave mestra de um volume LUKS2 precisa ser rotacionada sem janela de downtime), o comando **`cryptsetup reencrypt`** do LUKS2 permite **criptografar um disco existente no lugar ou rotacionar a Volume Key com o volume montado e em uso online**!

## Por que importa
Nas versões antigas do LUKS1, uma queda de energia no meio de uma recriptografia corrompia o disco porque não havia onde gravar o cursor de progresso no cabeçalho; no **LUKS2**, o `cryptsetup reencrypt` grava um metadado transacional de *hotzone / resilience (`checksums` ou `journal`)* diretamente na área JSON do LUKS2 a cada passo.

## Como funciona
Se o servidor desligar abruptamente durante a recriptografia de um volume de 10 TB, no próximo boot o LUKS2 monta normalmente (sendo metade do disco lida com a chave antiga e metade com a chave nova de forma transparente!) e retoma a recriptografia exatamente do setor onde parou.

## Exemplo
```bash
# Rotacionar a Volume Key (Master Key) de um volume LUKS2 online com resiliencia por checksums contra queda de energia
sudo cryptsetup reencrypt --resilience checksum /dev/nvme0n1p3
```

## Limites e trade-offs
Para criptografar no lugar uma partição existente que ainda está em **texto claro** (`--encrypt`), é preciso primeiro reduzir o tamanho do sistema de arquivos em pelo menos **32 MiB** (`resize2fs`) no final da partição para abrir espaço para o cabeçalho LUKS2 (`--reduce-device-size 32M`).

## Como verificar
Acompanhe o progresso e a velocidade em MiB/s do `cryptsetup reencrypt` e confirme ao término no `luksDump` que o digest da nova Volume Key foi atualizado.

## Conexões
- [[cryptsetup-desbloqueio-hardware-systemd-cryptenroll-tpm2-fido2-pkcs11]] — Veja também: LUKS2 + **`systemd-cryptenroll`**: Vinculação de Keyslots a Chips **TPM 2.0 (PCRs + PIN)**, Chaves de Segurança **FIDO2 (YubiKey)** e SmartCards **PKCS#11**.
- [[cryptsetup-integridade-autenticada-aead-dm-integrity-chacha20-poly1305]] — Veja também: Cryptsetup & **`integritysetup` (`dm-integrity`)**: Criptografia Autenticada (**AEAD**) de Disco contra Adulteração Offline (*Evil Maid / Bit-Flipping*).
- [[cryptsetup-arquitetura-dm-crypt-luks2-veritysetup-integritysetup]] — Referência cruzada direta com cryptsetup-arquitetura-dm-crypt-luks2-veritysetup-integritysetup.
- [[cryptsetup-backup-restauracao-cabecalho-luksheaderbackup-luksheaderrestore]] — Referência cruzada direta com cryptsetup-backup-restauracao-cabecalho-luksheaderbackup-luksheaderrestore.
- [[cryptsetup-gerenciamento-keyslots-luksaddkey-lukskillslot-lukschangekey]] — Referência cruzada direta com cryptsetup-gerenciamento-keyslots-luksaddkey-lukskillslot-lukschangekey.

## Fontes
- [Cryptsetup Official GitLab Repository — LUKS2, veritysetup & integritysetup Reference](https://gitlab.com/cryptsetup/cryptsetup/-/raw/main/README.md) — documentação oficial do projeto cryptsetup cobrindo LUKS2, Argon2id, dm-verity, dm-integrity e interoperabilidade BitLocker/VeraCrypt; consultado em 2026-10-03.
- [Cryptsetup Official Documentation — Linux Kernel Keyring & VK Caching](https://gitlab.com/cryptsetup/cryptsetup/-/raw/main/docs/Keyring.txt) — especificação oficial do uso de chaves do tipo logon no Linux Kernel Keyring pelo cryptsetup para proteção da Volume Key em memória; consultado em 2026-10-03.
- [LUKS2 On-Disk Format Official Specification](https://gitlab.com/cryptsetup/LUKS2-docs) — especificação oficial do formato de disco LUKS2, metadados JSON, keyslots e tokens; consultado em 2026-10-03.
