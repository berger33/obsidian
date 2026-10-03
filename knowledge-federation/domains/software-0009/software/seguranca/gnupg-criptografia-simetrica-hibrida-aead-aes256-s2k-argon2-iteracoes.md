---
id: software.seguranca.tranche08.000707
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
fontes: ["https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG.html", "https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG_002dAGENT.html", "https://www.gnupg.org/documentation/manuals/gnupg/Option-Index.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# GnuPG: Criptografia Simétrica (`-c`) e Híbrida Assimétrica (`-e -r`), **S2K (`s2k-count` / Argon2)** e Preferências de Cifra (`AES256`, `SHA512`)

## Em uma frase
O GnuPG suporta tanto **criptografia híbrida de chave pública (`gpg --encrypt --sign -r <destinatario>`)** — onde uma chave de sessão efêmera `AES-256` cifra o arquivo e é envelopada para a chave pública `Cv25519`/`RSA` de cada destinatário — quanto **criptografia puramente simétrica baseada em passphrase (`gpg --symmetric --cipher-algo AES256`)**.

## Por que importa
Ao usar criptografia simétrica (`-c`) ou ao proteger chaves privadas no disco, a resistência contra quebra offline por GPUs (Hashcat modo `-m 17010` / `-m 22400`) depende diretamente do mecanismo **S2K (*String-to-Key*)**: no GnuPG 2.2/2.4 deve-se configurar **`s2k-cipher-algo AES256`**, **`s2k-digest-algo SHA512`**, **`s2k-mode 3`** (*Iterated and Salted*) e **`s2k-count 65011712`** (o valor máximo de 65 milhões de octetos processados, ou KDF **Argon2** do RFC 9580 nas versões 2.4+).

## Como funciona
Da mesma forma, definir `personal-cipher-preferences AES256 AES192 AES` e `personal-digest-preferences SHA512 SHA384 SHA256` em `~/.gnupg/gpg.conf` impede downgrade para algoritmos legados como `3DES`, `CAST5` ou `SHA-1`.

## Exemplo
```ini
# ~/.gnupg/gpg.conf — Preferencias criptograficas endurecidas (AES-256, SHA-512, S2K maximo e exibicao de fingerprints)
personal-cipher-preferences AES256 AES192 AES
personal-digest-preferences SHA512 SHA384 SHA256
personal-compress-preferences ZLIB BZIP2 ZIP Uncompressed
default-preference-list SHA512 SHA384 SHA256 AES256 AES192 AES ZLIB BZIP2 ZIP Uncompressed
cert-digest-algo SHA512
s2k-cipher-algo AES256
s2k-digest-algo SHA512
s2k-mode 3
s2k-count 65011712
keyid-format 0xlong
with-fingerprint
no-emit-version
```

## Limites e trade-offs
Nunca identifique chaves OpenPGP por *Short Key IDs* de 32 bits (`8 caracteres hex`, colidíveis em segundos) ou *Long Key IDs* de 64 bits (`16 caracteres hex`); use **sempre** o **Fingerprint completo de 160/256 bits (`40` ou `64` caracteres hexadecimais)**.

## Como verificar
Cifre um arquivo de teste e inspecione os pacotes OpenPGP gerados (`PKESK`, `SKESK`, `SEIPD` com MDC/AEAD) usando **`gpg --list-packets arquivo.gpg`**.

## Conexões
- [[gnupg-assinatura-commits-tags-git-allowed-signers-verificacao-ci]] — Veja também: GnuPG: Assinatura Criptográfica de **Commits e Tags Git (`commit.gpgsign`, `tag.gpgSign`)** e Gate de Verificação em Pipelines de CI/CD.
- [[gnupg-distribuicao-chaves-wkd-web-key-directory-dane-keyservers-dirmngr]] — Veja também: GnuPG & `dirmngr`: Descoberta Segura de Chaves Públicas via **WKD (*Web Key Directory*)** e **OPENPGPKEY DANE (RFC 7929)** vs Keyservers HKP.
- [[gnupg-arquitetura-openpgp-gpg2-gpg-agent-scdaemon-dirmngr]] — Referência cruzada direta com gnupg-arquitetura-openpgp-gpg2-gpg-agent-scdaemon-dirmngr.
- [[hashcat-defesa-engenharia-armazenamento-senhas-argon2id-bcrypt-scrypt-passphrases]] — Referência cruzada direta com hashcat-defesa-engenharia-armazenamento-senhas-argon2id-bcrypt-scrypt-passphrases.

## Fontes
- [GnuPG Official Manual — Invoking GPG & Command Options](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG.html) — manual oficial do GnuPG (gpg) cobrindo geração e gestão de chaves e subchaves OpenPGP, verificação, cifragem e formatos de chaveiro; consultado em 2026-10-03.
- [GnuPG Official Manual — Invoking GPG-AGENT & SSH Support](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG_002dAGENT.html) — manual oficial do daemon gpg-agent cobrindo cache de credenciais, pinentry, scdaemon e emulação de ssh-agent; consultado em 2026-10-03.
- [GnuPG Official Manual — Complete Option Index](https://www.gnupg.org/documentation/manuals/gnupg/Option-Index.html) — índice oficial de opções de configuração do GnuPG; consultado em 2026-10-03.
