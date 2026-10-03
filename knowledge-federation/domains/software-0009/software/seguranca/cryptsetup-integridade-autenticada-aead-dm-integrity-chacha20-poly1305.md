---
id: software.seguranca.tranche08.000727
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

# Cryptsetup & **`integritysetup` (`dm-integrity`)**: Criptografia Autenticada (**AEAD**) de Disco contra Adulteração Offline (*Evil Maid / Bit-Flipping*)

## Em uma frase
A criptografia de disco padrão (`aes-xts-plain64`) garante **confidencialidade**, mas o modo XTS **não é um modo autenticado (não possui tag MAC/AEAD por setor)**: embora qualquer alteração de 1 bit em um setor cifrado por um atacante com acesso físico ao disco desligado (*Evil Maid Attack*) embaralhe os 16 bytes do bloco AES correspondente, o `dm-crypt` padrão não sabe detectar criptograficamente que o setor foi adulterado.

## Por que importa
Quando o modelo de ameaça exige **Criptografia de Disco Autenticada (AEAD)** capaz de detectar e rejeitar com erro de I/O (`EILSEQ`) qualquer modificação de bytes no disco desligado, o LUKS2 integra nativamente o subsistema **`dm-integrity`** através da flag **`--integrity`** no `luksFormat`!

## Como funciona
Combinar `--cipher chacha20-random --integrity poly1305` ou **`--cipher aes-gcm-random --integrity aead`** grava no disco, junto a cada setor de 4096 bytes, o nonce e a tag de autenticação criptográfica AEAD daquele setor.

## Exemplo
```bash
# Formatar um volume LUKS2 com Criptografia Autenticada de Bloco (AEAD: ChaCha20-Poly1305 via dm-integrity)
sudo cryptsetup luksFormat --type luks2 \
  --cipher chacha20-random --key-size 256 \
  --integrity poly1305 \
  --sector-size 4096 \
  /cases/vaults/aead_authenticated_disk.img
```

## Limites e trade-offs
Note o *trade-off* importante de performance e espaço: habilitar `--integrity` (AEAD) adiciona metadados por setor e um journal de escrita para manter atomicidade entre o dado e a tag MAC, reduzindo a velocidade de escrita sequencial em ~40–50% frente ao `aes-xts-plain64` puro; por isso, para partições de sistema operacional `/usr` imutáveis, prefira **`dm-verity`** (`veritysetup`, muito mais rápido).

## Como verificar
Verifique com `sudo cryptsetup status <nome_ativo>` a presença das linhas `integrity: aead` e `integrity keysize`.

## Conexões
- [[cryptsetup-recriptografia-online-cryptsetup-reencrypt-resiliencia]] — Veja também: Cryptsetup: **Criptografia e Recriptografia Online (`cryptsetup reencrypt`)** de Volumes LUKS2 Montados com *Crash Recovery* em Metadados.
- [[cryptsetup-verificacao-imutavel-veritysetup-dm-verity-roothash-secure-boot]] — Veja também: Cryptsetup **`veritysetup` (`dm-verity`)**: Verificação Criptográfica por Árvore de Merkle (**Root Hash**) para Sistemas Operacionais e Containers Imutáveis.
- [[cryptsetup-arquitetura-dm-crypt-luks2-veritysetup-integritysetup]] — Referência cruzada direta com cryptsetup-arquitetura-dm-crypt-luks2-veritysetup-integritysetup.
- [[veracrypt-arquitetura-criptografia-volumes-xts-pbkdf2-pim-cabecalho]] — Referência cruzada direta com veracrypt-arquitetura-criptografia-volumes-xts-pbkdf2-pim-cabecalho.

## Fontes
- [Cryptsetup Official GitLab Repository — LUKS2, veritysetup & integritysetup Reference](https://gitlab.com/cryptsetup/cryptsetup/-/raw/main/README.md) — documentação oficial do projeto cryptsetup cobrindo LUKS2, Argon2id, dm-verity, dm-integrity e interoperabilidade BitLocker/VeraCrypt; consultado em 2026-10-03.
- [Cryptsetup Official Documentation — Linux Kernel Keyring & VK Caching](https://gitlab.com/cryptsetup/cryptsetup/-/raw/main/docs/Keyring.txt) — especificação oficial do uso de chaves do tipo logon no Linux Kernel Keyring pelo cryptsetup para proteção da Volume Key em memória; consultado em 2026-10-03.
- [LUKS2 On-Disk Format Official Specification](https://gitlab.com/cryptsetup/LUKS2-docs) — especificação oficial do formato de disco LUKS2, metadados JSON, keyslots e tokens; consultado em 2026-10-03.
