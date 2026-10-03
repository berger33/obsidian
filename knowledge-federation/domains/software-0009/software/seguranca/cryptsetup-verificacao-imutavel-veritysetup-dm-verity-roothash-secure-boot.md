---
id: software.seguranca.tranche08.000728
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

# Cryptsetup **`veritysetup` (`dm-verity`)**: Verificação Criptográfica por Árvore de Merkle (**Root Hash**) para Sistemas Operacionais e Containers Imutáveis

## Em uma frase
Incluído no projeto `cryptsetup`, o utilitário **`veritysetup`** configura o módulo de kernel **`dm-verity`**, que transforma qualquer dispositivo de bloco somente-leitura (como a partição `/usr` de servidores imutáveis Flatcar/Fedora CoreOS/Bottlerocket, Android Verified Boot ou imagens de sistema) em uma **Árvore de Merkle SHA-256** verificada transparentemente pelo kernel em cada leitura de página!

## Por que importa
Quando o `veritysetup format <dispositivo_dados> <dispositivo_hashes>` é executado no momento do build da imagem do sistema operacional, ele calcula o hash SHA-256 de cada bloco de 4 KiB, depois o hash dos blocos de hashes em árvore até chegar a um único **Root Hash de 256 bits**.

## Como funciona
Durante o boot (protegido por UEFI Secure Boot / Unified Kernel Image assinada que embute o **Root Hash**), o kernel monta a partição via `dm-verity`: se um rootkit ou atacante físico tiver alterado **um único bit** de qualquer binário em `/usr/bin` no disco, o hash do bloco falha na subida da árvore de Merkle contra o *Root Hash* e o kernel bloqueia imediatamente a leitura (ou reinicia/entra em pânico com `--restart-on-corruption`)!

## Exemplo
```bash
# Gerar a arvore de Merkle dm-verity para uma imagem de filesystem somente-leitura e capturar o Root Hash resultante
veritysetup format \
  /cases/images/immutable_usr.squashfs \
  /cases/images/immutable_usr.verity \
  | tee /cases/images/verity_summary.txt
```

## Limites e trade-offs
A partir do Linux 5.4+ e `veritysetup` moderno, você pode assinar o **Root Hash** com uma chave privada X.509/PKCS#7 e passar **`--root-hash-signature=<arquivo.p7s>`** ao `veritysetup open`, fazendo o próprio kernel Linux verificar a assinatura contra o keyring de chaves confiáveis da plataforma (`.builtin_trusted_keys` / `.machine`)!

## Como verificar
Teste abrir a imagem com **`sudo veritysetup open <dados> verity_usr <hashes> <ROOT_HASH>`** e verifique o status com `sudo veritysetup status verity_usr`.

## Conexões
- [[cryptsetup-integridade-autenticada-aead-dm-integrity-chacha20-poly1305]] — Veja também: Cryptsetup & **`integritysetup` (`dm-integrity`)**: Criptografia Autenticada (**AEAD**) de Disco contra Adulteração Offline (*Evil Maid / Bit-Flipping*).
- [[cryptsetup-backup-restauracao-cabecalho-luksheaderbackup-luksheaderrestore]] — Veja também: Cryptsetup: Backup e Restauração de Cabeçalho LUKS2 (`luksHeaderBackup` / `luksHeaderRestore`), `--header` Destacado e `discard` (TRIM).
- [[cryptsetup-arquitetura-dm-crypt-luks2-veritysetup-integritysetup]] — Referência cruzada direta com cryptsetup-arquitetura-dm-crypt-luks2-veritysetup-integritysetup.

## Fontes
- [Cryptsetup Official GitLab Repository — LUKS2, veritysetup & integritysetup Reference](https://gitlab.com/cryptsetup/cryptsetup/-/raw/main/README.md) — documentação oficial do projeto cryptsetup cobrindo LUKS2, Argon2id, dm-verity, dm-integrity e interoperabilidade BitLocker/VeraCrypt; consultado em 2026-10-03.
- [Cryptsetup Official Documentation — Linux Kernel Keyring & VK Caching](https://gitlab.com/cryptsetup/cryptsetup/-/raw/main/docs/Keyring.txt) — especificação oficial do uso de chaves do tipo logon no Linux Kernel Keyring pelo cryptsetup para proteção da Volume Key em memória; consultado em 2026-10-03.
- [LUKS2 On-Disk Format Official Specification](https://gitlab.com/cryptsetup/LUKS2-docs) — especificação oficial do formato de disco LUKS2, metadados JSON, keyslots e tokens; consultado em 2026-10-03.
