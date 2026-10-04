---
id: software.seguranca.tranche02.000153
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

# `age` Criptografia para Chaves SSH Existentes (`ssh-ed25519` e `ssh-rsa`): envio seguro usando `~/.ssh/id_ed25519.pub` ou `github.com/<user>.keys`

## Em uma frase
Uma das funcionalidades mais práticas do `age` documentadas em `age(1)` é a capacidade de cifrar arquivos diretamente para **chaves públicas SSH existentes (`ssh-ed25519 AAAA...` e `ssh-rsa AAAA...`)** e decifrá-los usando a chave privada SSH correspondente (`-i ~/.ssh/id_ed25519`).

## Por que importa
Quando você precisa enviar um segredo cifrado para um colega que ainda não gerou uma chave `age1...`, ele já possui chaves públicas SSH publicadas no GitHub (`https://github.com/<usuario>.keys`), GitLab ou no `authorized_keys`.

## Como funciona
Combinando `curl` com `-R -` (lendo a lista de destinatários da entrada padrão `stdin`), você pode cifrar um arquivo diretamente para todas as chaves SSH públicas do GitHub de uma pessoa em um único comando!

## Exemplo
```bash
# Cifrando um arquivo diretamente para as chaves públicas SSH de um usuário no GitHub:
curl -fsSL https://github.com/Benjojo.keys | age -R - -o segredo.age credenciais.txt

# O destinatário decifra usando sua chave privada SSH local:
age --decrypt -i ~/.ssh/id_ed25519 -o credenciais.txt segredo.age
```

## Limites e trade-offs
Caso a chave privada SSH usada em `-i` seja protegida por senha (*passphrase*) ou gerenciada pelo `ssh-agent`, o `age` solicita a senha interativamente de forma segura.

## Como verificar
Teste cifrar um arquivo para o seu próprio `~/.ssh/id_ed25519.pub` (`age -R ~/.ssh/id_ed25519.pub`) e decifrá-lo com `age -d -i ~/.ssh/id_ed25519`.

## Conexões
- [[agecrypt-chaves-nativas-age-keygen-bech32-multiplos-destinatarios-recipients-file]] — Veja também: `age` Gerenciamento de Chaves (`age-keygen`) e Múltiplos Destinatários (`-r` e `-R recipients.txt`).
- [[agecrypt-passphrase-scrypt-protecao-chaves-identidade-em-repouso]] — Veja também: `age` Criptografia por Passphrase (`-p` / `--passphrase` com `scrypt`) e Identidades Protegidas por Senha.

## Fontes
- [FiloSottile age GitHub — README.md (Simple Modern File Encryption Tool, Usage, Multiple Recipients, SSH Keys, Plugins & Go Library)](https://raw.githubusercontent.com/FiloSottile/age/main/README.md) — README oficial do FiloSottile/age documentando filosofia sem opções de configuração, uso de chaves X25519 e SSH, destinatários múltiplos, plugins de hardware e integração no ecossistema; consultado em 2026-10-03.
- [FiloSottile age Official Man Page — doc/age.1.html (Complete Specification of Flags -e/-d/-r/-R/-p/-a/-i/-j, Passphrase-Protected Identities & Format Overhead)](https://raw.githubusercontent.com/FiloSottile/age/main/doc/age.1.html) — Man page oficial age(1) detalhando todas as opções de linha de comando, proteção de TTY, formato ASCII Armor estrito, arquivos de destinatários e identidades cifradas; consultado em 2026-10-03.
- [FiloSottile age — Official GitHub Repository](https://github.com/FiloSottile/age) — Repositório oficial BSD-3-Clause do age; consultado em 2026-10-03.
