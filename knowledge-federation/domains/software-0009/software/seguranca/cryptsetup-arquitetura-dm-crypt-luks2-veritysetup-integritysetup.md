---
id: software.seguranca.tranche08.000721
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

# Linux **`cryptsetup` & LUKS2**: Arquitetura do Subsistema `dm-crypt`, Metadados JSON **LUKS2**, `veritysetup` (`dm-verity`) e `integritysetup` (`dm-integrity`)

## Em uma frase
**`cryptsetup`** (`gitlab.com/cryptsetup/cryptsetup`, GPLv2+/LGPLv2.1+, biblioteca `libcryptsetup`) é a suíte padrão do ecossistema Linux para configurar criptografia de dispositivos de bloco no kernel (`dm-crypt`), verificação criptográfica de integridade somente-leitura (`veritysetup` / `dm-verity`) e integridade autenticada de blocos (`integritysetup` / `dm-integrity`).

## Por que importa
O padrão **LUKS2 (*Linux Unified Key Setup v2*)** substituiu o antigo cabeçalho binário rígido do LUKS1 por uma área de metadados **JSON redundante e extensível** gravada no início da partição, suportando **até 32 Keyslots independentes**, funções de derivação de chave resistentes a GPU (**`argon2id`** por padrão), **Tokens de Hardware** (TPM2, FIDO2, PKCS#11, Kernel Keyring, Clevis) e recriptografia online com resiliência a quedas de energia.

## Como funciona
Além do formato nativo LUKS1/LUKS2, o `cryptsetup` abre nativamente volumes **BitLocker (`bitlk`)**, **TrueCrypt / VeraCrypt (`tcrypt`)**, **FileVault2 (`fvault2`)** e `plain` sobre o mesmo motor `dm-crypt` do kernel.

## Exemplo
```bash
# Verificar a versao do cryptsetup e inspecionar o cabecalho JSON, Keyslots, Tokens e Digests de um volume LUKS2
cryptsetup --version
sudo cryptsetup luksDump /dev/nvme0n1p3
```

## Limites e trade-offs
Nunca use o modo `--type plain` em discos de dados permanentes sem cabeçalho LUKS2: no modo `plain`, não há verificação de senha (digitar uma senha errada com 1 letra trocada simplesmente monta o dispositivo com uma chave errada e corrompe silenciosamente o sistema de arquivos se você tentar gravar nele!), nem é possível trocar a senha sem recriptografar o disco inteiro.

## Como verificar
Inspecione com `sudo cryptsetup luksDump <dispositivo>` que `Version: 2` está ativo e que o PBKDF dos keyslots utiliza `argon2id`.

## Conexões
- [[cryptsetup-formatacao-luks2-aes-xts-plain64-argon2id-setores-4k]] — Veja também: Cryptsetup: Formatação Segura **LUKS2 (`luksFormat`)** — `aes-xts-plain64` (512 bits), Parâmetros **Argon2id** e Alinhamento de Setores de **4096 Bytes**.
- [[cryptsetup-gerenciamento-keyslots-luksaddkey-lukskillslot-lukschangekey]] — Referência cruzada direta com cryptsetup-gerenciamento-keyslots-luksaddkey-lukskillslot-lukschangekey.
- [[veracrypt-interoperabilidade-nativa-linux-cryptsetup-tcrypt-open]] — Referência cruzada direta com veracrypt-interoperabilidade-nativa-linux-cryptsetup-tcrypt-open.

## Fontes
- [Cryptsetup Official GitLab Repository — LUKS2, veritysetup & integritysetup Reference](https://gitlab.com/cryptsetup/cryptsetup/-/raw/main/README.md) — documentação oficial do projeto cryptsetup cobrindo LUKS2, Argon2id, dm-verity, dm-integrity e interoperabilidade BitLocker/VeraCrypt; consultado em 2026-10-03.
- [Cryptsetup Official Documentation — Linux Kernel Keyring & VK Caching](https://gitlab.com/cryptsetup/cryptsetup/-/raw/main/docs/Keyring.txt) — especificação oficial do uso de chaves do tipo logon no Linux Kernel Keyring pelo cryptsetup para proteção da Volume Key em memória; consultado em 2026-10-03.
- [LUKS2 On-Disk Format Official Specification](https://gitlab.com/cryptsetup/LUKS2-docs) — especificação oficial do formato de disco LUKS2, metadados JSON, keyslots e tokens; consultado em 2026-10-03.
