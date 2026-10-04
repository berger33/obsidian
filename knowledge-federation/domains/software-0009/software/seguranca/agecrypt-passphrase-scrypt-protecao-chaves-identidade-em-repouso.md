---
id: software.seguranca.tranche02.000154
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
fontes: ["https://raw.githubusercontent.com/FiloSottile/age/main/doc/age.1.html", "https://raw.githubusercontent.com/FiloSottile/age/main/README.md", "https://github.com/FiloSottile/age"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `age` Criptografia por Passphrase (`-p` / `--passphrase` com `scrypt`) e Identidades Protegidas por Senha

## Em uma frase
A flag **`-p` / `--passphrase`** do `age` cifra um arquivo usando uma senha interativa derivada pela função *memory-hard* **`scrypt`** (e até oferece gerar automaticamente uma passphrase segura de 10 palavras Diceware caso o usuário pressione Enter em branco), além de permitir usar **arquivos de identidade `.age` protegidos por passphrase** diretamente na flag `-i`!

## Por que importa
Um arquivo `key.txt` gerado pelo `age-keygen` contém a chave privada `AGE-SECRET-KEY-1...` em texto plano; se o laptop de um desenvolvedor não tiver criptografia de disco ou se o arquivo vazar, a chave privada estará desprotegida.

## Como funciona
Conforme documentado em `age(1)`, você pode cifrar o seu próprio arquivo `key.txt` com uma passphrase (`age -p -o key.txt.age key.txt`) e passar **`-i key.txt.age`** tanto para decifrar quanto para cifrar (`age -e -i key.txt.age`): o `age` detecta automaticamente que a identidade está cifrada com passphrase e pede a senha no terminal!

## Exemplo
```bash
# 1. Protegendo uma chave privada age-keygen com uma passphrase scrypt:
age-keygen | age -p > key.age

# 2. Extraindo a chave pública ou decifrando arquivos usando diretamente a identidade cifrada:
age-keygen -y key.age
age --decrypt -i key.age dados.tar.gz.age > dados.tar.gz
```

## Limites e trade-offs
Conforme a man page `age(1)`, a flag `-p` (`--passphrase`) **não pode ser combinada** na mesma operação de criptografia com flags de destinatários de chave pública (`-r` / `-R`).

## Como verificar
Teste criar uma identidade cifrada `key.age` e executar `age -d -i key.age` sobre um arquivo de teste.

## Conexões
- [[agecrypt-criptografia-chaves-ssh-ed25519-rsa-github-keys]] — Veja também: `age` Criptografia para Chaves SSH Existentes (`ssh-ed25519` e `ssh-rsa`): envio seguro usando `~/.ssh/id_ed25519.pub` ou `github.com/<user>.keys`.
- [[agecrypt-ascii-armor-pem-strict-base64-protecao-tty]] — Veja também: `age` ASCII Armor (`-a` / `--armor`): codificação PEM canônica estrita (`AGE ENCRYPTED FILE`) e proteção de TTY.

## Fontes
- [FiloSottile age GitHub — README.md (Simple Modern File Encryption Tool, Usage, Multiple Recipients, SSH Keys, Plugins & Go Library)](https://raw.githubusercontent.com/FiloSottile/age/main/doc/age.1.html) — README oficial do FiloSottile/age documentando filosofia sem opções de configuração, uso de chaves X25519 e SSH, destinatários múltiplos, plugins de hardware e integração no ecossistema; consultado em 2026-10-03.
- [FiloSottile age Official Man Page — doc/age.1.html (Complete Specification of Flags -e/-d/-r/-R/-p/-a/-i/-j, Passphrase-Protected Identities & Format Overhead)](https://raw.githubusercontent.com/FiloSottile/age/main/README.md) — Man page oficial age(1) detalhando todas as opções de linha de comando, proteção de TTY, formato ASCII Armor estrito, arquivos de destinatários e identidades cifradas; consultado em 2026-10-03.
- [FiloSottile age — Official GitHub Repository](https://github.com/FiloSottile/age) — Repositório oficial BSD-3-Clause do age; consultado em 2026-10-03.
