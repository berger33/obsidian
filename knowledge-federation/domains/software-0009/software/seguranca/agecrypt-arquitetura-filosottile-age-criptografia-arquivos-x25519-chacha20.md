---
id: software.seguranca.tranche02.000151
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/FiloSottile/age/main/README.md", "https://raw.githubusercontent.com/FiloSottile/age/main/doc/age.1.html", "https://github.com/FiloSottile/age"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# FiloSottile `age`: arquitetura da ferramenta e formato moderno de criptografia de arquivos (`X25519`, `ChaCha20-Poly1305` e `STREAM`)

## Em uma frase
O **`age`** (`FiloSottile/age`, especificado em `age-encryption.org/v1` por Filippo Valsorda e Ben Cox sob licença BSD-3-Clause) é uma ferramenta de linha de comando, formato de arquivo e biblioteca Go simples, moderna e segura para **criptografia autenticada de arquivos**, projetada para substituir o uso complexo do GnuPG (`gpg`) em automação, backups e GitOps.

## Por que importa
O `gpg` acumula décadas de opções de configuração legadas, keyrings globais mutáveis, algoritmos antigos e armadilhas de parsing onde é fácil cifrar dados sem autenticação moderna ou depender de um estado global em `~/.gnupg`.

## Como funciona
O `age` **não possui nenhuma opção de configuração de algoritmo** (*zero config options*): todo arquivo `.age` usa uma chave de arquivo aleatória de 128 bits que cifra o payload em chunks de **64 KiB** com **`ChaCha20-Poly1305` (construção `STREAM` não-maleável, apenas 16 bytes de overhead por bloco de 64 KiB)**, enquanto a chave de arquivo é encapsulada no cabeçalho para um ou mais destinatários (`X25519`, `scrypt`, `ssh-ed25519`, `ssh-rsa` ou híbrido pós-quântico).

## Exemplo
```bash
# 1. Gerando um par de chaves nativo age (X25519 codificado em Bech32):
age-keygen -o key.txt

# 2. Cifrando um stream tar.gz diretamente para a chave pública age1... em estilo UNIX:
tar czf - ./secrets-dir | age -r age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p > secrets.tar.gz.age

# 3. Decifrando com a chave privada (-i / --identity):
age --decrypt -i key.txt secrets.tar.gz.age > secrets.tar.gz
```

## Limites e trade-offs
Conforme a man page oficial `age(1)`, cada destinatário adiciona apenas cerca de **200 bytes de overhead** no cabeçalho, e o formato binário é estritamente não-maleável.

## Como verificar
Execute `age --version` e `age-keygen -y key.txt` para extrair a chave pública correspondente a um arquivo de identidade.

## Conexões
- [[agecrypt-chaves-nativas-age-keygen-bech32-multiplos-destinatarios-recipients-file]] — Veja também: `age` Gerenciamento de Chaves (`age-keygen`) e Múltiplos Destinatários (`-r` e `-R recipients.txt`).

## Fontes
- [FiloSottile age GitHub — README.md (Simple Modern File Encryption Tool, Usage, Multiple Recipients, SSH Keys, Plugins & Go Library)](https://raw.githubusercontent.com/FiloSottile/age/main/README.md) — README oficial do FiloSottile/age documentando filosofia sem opções de configuração, uso de chaves X25519 e SSH, destinatários múltiplos, plugins de hardware e integração no ecossistema; consultado em 2026-10-03.
- [FiloSottile age Official Man Page — doc/age.1.html (Complete Specification of Flags -e/-d/-r/-R/-p/-a/-i/-j, Passphrase-Protected Identities & Format Overhead)](https://raw.githubusercontent.com/FiloSottile/age/main/doc/age.1.html) — Man page oficial age(1) detalhando todas as opções de linha de comando, proteção de TTY, formato ASCII Armor estrito, arquivos de destinatários e identidades cifradas; consultado em 2026-10-03.
- [FiloSottile age — Official GitHub Repository](https://github.com/FiloSottile/age) — Repositório oficial BSD-3-Clause do age; consultado em 2026-10-03.
