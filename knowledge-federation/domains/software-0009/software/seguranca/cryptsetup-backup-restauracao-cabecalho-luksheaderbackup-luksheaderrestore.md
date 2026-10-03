---
id: software.seguranca.tranche08.000729
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

# Cryptsetup: Backup e Restauração de Cabeçalho LUKS2 (`luksHeaderBackup` / `luksHeaderRestore`), `--header` Destacado e `discard` (TRIM)

## Em uma frase
Em qualquer volume LUKS1 ou LUKS2, os primeiros megabytes da partição (por padrão `16 MiB` no LUKS2) contêm os metadados JSON e a área binária dos Keyslots cifrados: se essa região de 16 MiB for sobrescrita por um comando `fdisk`/`parted`/`dd` equivocado, todos os terabytes do disco tornam-se irrecuperáveis mesmo que o administrador saiba a senha de cor.

## Por que importa
Por isso, o procedimento operacional obrigatório logo após criar qualquer volume LUKS2 de servidor é executar **`cryptsetup luksHeaderBackup <dispositivo> --header-backup-file <arquivo.hdr>`** e armazenar o arquivo `.hdr` (cifrado adicionalmente com `age` ou `gpg`) no cofre de recuperação de desastres.

## Como funciona
O `cryptsetup` também suporta **Cabeçalho Destacado (`--header /caminho/cabecalho.img`)**, onde a partição de dados no disco contém 100% de blocos cifrados sem nenhum cabeçalho LUKS visível na frente, e o cabeçalho reside em uma mídia USB separada.

## Exemplo
```bash
# Realizar backup integro do cabecalho LUKS2 e validar o arquivo de backup gerado com luksDump
sudo cryptsetup luksHeaderBackup /dev/nvme0n1p3 \
  --header-backup-file /cases/backups/nvme0n1p3_luks2.hdr

sudo cryptsetup luksDump /cases/backups/nvme0n1p3_luks2.hdr
```

## Limites e trade-offs
Quanto à opção **`discard` (TRIM em SSDs)** em `/etc/crypttab` (`--allow-discards`): habilitar TRIM em um SSD melhora a performance e vida útil do SSD, mas revela a um observador físico do disco desligado *quais blocos de 4 KiB estão vazios (zerados pelo TRIM) vs quais estão ocupados*, o que é aceitável na maioria dos servidores corporativos, mas deve permanecer desativado se você precisar ocultar o volume exato de dados gravados.

## Como verificar
Verifique que o backup `.hdr` abre normalmente no `cryptsetup luksDump` e possui o mesmo `UUID` da partição.

## Conexões
- [[cryptsetup-verificacao-imutavel-veritysetup-dm-verity-roothash-secure-boot]] — Veja também: Cryptsetup **`veritysetup` (`dm-verity`)**: Verificação Criptográfica por Árvore de Merkle (**Root Hash**) para Sistemas Operacionais e Containers Imutáveis.
- [[cryptsetup-abertura-volumes-bitlocker-veracrypt-truecrypt-forense]] — Veja também: Cryptsetup em DFIR: Abertura Nativa de Discos **Windows BitLocker (`--type bitlk`)**, **Apple FileVault2 (`fvault2`)** e **VeraCrypt (`tcrypt`)** no Linux.
- [[cryptsetup-arquitetura-dm-crypt-luks2-veritysetup-integritysetup]] — Referência cruzada direta com cryptsetup-arquitetura-dm-crypt-luks2-veritysetup-integritysetup.
- [[veracrypt-backup-restauracao-cabecalho-volume-emergencia-corrupcao]] — Referência cruzada direta com veracrypt-backup-restauracao-cabecalho-volume-emergencia-corrupcao.

## Fontes
- [Cryptsetup Official GitLab Repository — LUKS2, veritysetup & integritysetup Reference](https://gitlab.com/cryptsetup/cryptsetup/-/raw/main/README.md) — documentação oficial do projeto cryptsetup cobrindo LUKS2, Argon2id, dm-verity, dm-integrity e interoperabilidade BitLocker/VeraCrypt; consultado em 2026-10-03.
- [Cryptsetup Official Documentation — Linux Kernel Keyring & VK Caching](https://gitlab.com/cryptsetup/cryptsetup/-/raw/main/docs/Keyring.txt) — especificação oficial do uso de chaves do tipo logon no Linux Kernel Keyring pelo cryptsetup para proteção da Volume Key em memória; consultado em 2026-10-03.
- [LUKS2 On-Disk Format Official Specification](https://gitlab.com/cryptsetup/LUKS2-docs) — especificação oficial do formato de disco LUKS2, metadados JSON, keyslots e tokens; consultado em 2026-10-03.
