---
id: software.seguranca.tranche08.000730
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

# Cryptsetup em DFIR: Abertura Nativa de Discos **Windows BitLocker (`--type bitlk`)**, **Apple FileVault2 (`fvault2`)** e **VeraCrypt (`tcrypt`)** no Linux

## Em uma frase
Em uma estação Linux de Resposta a Incidentes e Forense Digital (DFIR), o analista frequentemente recebe imagens de discos de estações Windows criptografadas com **Microsoft BitLocker** ou Macs antigos com **FileVault2**: em vez de precisar de drivers de terceiros ou montar a imagem em uma máquina Windows (que altera timestamps e monta em escrita por padrão), o **`cryptsetup`** abre todos esses formatos nativamente em **modo somente-leitura (`--readonly`)**!

## Por que importa
Com **`cryptsetup bitlkDump <imagem_particao>`**, o analista inspeciona instantaneamente a versão do BitLocker, a cifra (`aes-xts-plain64` ou `aes-cbc`), o GUID do volume e todos os *VMK (Volume Master Key) Protectors* ativos (`Passphrase`, `Recovery Password` de 48 dígitos numéricos, `Startup Key .BEK` ou `TPM`).

## Como funciona
Em seguida, **`sudo cryptsetup open --type bitlk --readonly <imagem_particao> evidencia_win`** aceita diretamente na entrada de senha quer a senha do usuário, quer a **Recovery Password numérica de 48 dígitos** (`XXXXXX-XXXXXX-...`) recuperada do Active Directory ou Entra ID!

## Exemplo
```bash
# Inspecionar os protetores VMK de uma imagem forense BitLocker e abri-la em modo estritamente somente-leitura (--readonly)
sudo cryptsetup bitlkDump /cases/forensics/win11_os_partition.raw
sudo cryptsetup open --type bitlk --readonly /cases/forensics/win11_os_partition.raw win11_forensic_ro
```

## Limites e trade-offs
Caso o volume BitLocker utilize arquivo de chave de inicialização (`.BEK` / *Startup Key*), passe-o via **`--key-file=/cases/forensics/chave.bek`** junto com `--type bitlk --readonly`.

## Como verificar
Após abrir o dispositivo em `/dev/mapper/win11_forensic_ro`, verifique com **`sudo blockdev --getro /dev/mapper/win11_forensic_ro`** que o kernel retorna `1` (bloqueio estrito de escrita no nível de bloco) antes de rodar o Plaso/Timesketch.

## Conexões
- [[cryptsetup-backup-restauracao-cabecalho-luksheaderbackup-luksheaderrestore]] — Veja também: Cryptsetup: Backup e Restauração de Cabeçalho LUKS2 (`luksHeaderBackup` / `luksHeaderRestore`), `--header` Destacado e `discard` (TRIM).
- [[cryptsetup-arquitetura-dm-crypt-luks2-veritysetup-integritysetup]] — Referência cruzada direta com cryptsetup-arquitetura-dm-crypt-luks2-veritysetup-integritysetup.
- [[veracrypt-interoperabilidade-nativa-linux-cryptsetup-tcrypt-open]] — Referência cruzada direta com veracrypt-interoperabilidade-nativa-linux-cryptsetup-tcrypt-open.
- [[timesketch-ingestao-plaso-log2timeline-jsonl-csv-timesketch-importer]] — Referência cruzada direta com timesketch-ingestao-plaso-log2timeline-jsonl-csv-timesketch-importer.

## Fontes
- [Cryptsetup Official GitLab Repository — LUKS2, veritysetup & integritysetup Reference](https://gitlab.com/cryptsetup/cryptsetup/-/raw/main/README.md) — documentação oficial do projeto cryptsetup cobrindo LUKS2, Argon2id, dm-verity, dm-integrity e interoperabilidade BitLocker/VeraCrypt; consultado em 2026-10-03.
- [Cryptsetup Official Documentation — Linux Kernel Keyring & VK Caching](https://gitlab.com/cryptsetup/cryptsetup/-/raw/main/docs/Keyring.txt) — especificação oficial do uso de chaves do tipo logon no Linux Kernel Keyring pelo cryptsetup para proteção da Volume Key em memória; consultado em 2026-10-03.
- [LUKS2 On-Disk Format Official Specification](https://gitlab.com/cryptsetup/LUKS2-docs) — especificação oficial do formato de disco LUKS2, metadados JSON, keyslots e tokens; consultado em 2026-10-03.
