---
id: software.seguranca.tranche02.000152
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

# `age` Gerenciamento de Chaves (`age-keygen`) e Múltiplos Destinatários (`-r` e `-R recipients.txt`)

## Em uma frase
O utilitário **`age-keygen`** gera pares de chaves X25519 codificados em **Bech32** — onde a chave pública começa com **`age1...`** e a chave secreta começa com **`AGE-SECRET-KEY-1...`** — e o binário `age` permite cifrar um único arquivo para **múltiplos destinatários independentes** repetindo `-r` (`--recipient`) ou passando um arquivo de lista com **`-R` (`--recipients-file`)**.

## Por que importa
Em uma equipe de DevSecOps ou SRE, cifrar um backup ou segredo para uma única chave compartilhada obriga todos a terem a mesma chave privada; cifrar com `-R team-recipients.txt` permite que cada engenheiro (e o servidor de produção) decifre com sua própria identidade individual.

## Como funciona
Conforme documentado na man page `age(1)`, um arquivo passado em `-R recipients.txt` contém um destinatário por linha e **ignora linhas vazias e comentários iniciados por `#`**, tornando-o ideal para versionar na raiz do repositório Git com o nome de cada membro da equipe acima da sua chave pública!

## Exemplo
```text
# Arquivo team-recipients.txt versionado no repositório Git:
# Alice (SRE Lead)
age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p
# Bob (Security Engineer)
age1lggyhqrw2nlhcxprm67z43rta597azn8gknawjehu9d9dl0jq3yqqvfafg
```

## Limites e trade-offs
Para converter uma chave privada existente (`key.txt`) em sua respectiva chave pública sem abrir o arquivo manualmente, execute **`age-keygen -y key.txt`**.

## Como verificar
Cifre um arquivo de teste usando `age -R team-recipients.txt -o test.age input.txt` e decifre com qualquer uma das identidades listadas.

## Conexões
- [[agecrypt-arquitetura-filosottile-age-criptografia-arquivos-x25519-chacha20]] — Veja também: FiloSottile `age`: arquitetura da ferramenta e formato moderno de criptografia de arquivos (`X25519`, `ChaCha20-Poly1305` e `STREAM`).
- [[agecrypt-criptografia-chaves-ssh-ed25519-rsa-github-keys]] — Veja também: `age` Criptografia para Chaves SSH Existentes (`ssh-ed25519` e `ssh-rsa`): envio seguro usando `~/.ssh/id_ed25519.pub` ou `github.com/<user>.keys`.

## Fontes
- [FiloSottile age GitHub — README.md (Simple Modern File Encryption Tool, Usage, Multiple Recipients, SSH Keys, Plugins & Go Library)](https://raw.githubusercontent.com/FiloSottile/age/main/README.md) — README oficial do FiloSottile/age documentando filosofia sem opções de configuração, uso de chaves X25519 e SSH, destinatários múltiplos, plugins de hardware e integração no ecossistema; consultado em 2026-10-03.
- [FiloSottile age Official Man Page — doc/age.1.html (Complete Specification of Flags -e/-d/-r/-R/-p/-a/-i/-j, Passphrase-Protected Identities & Format Overhead)](https://raw.githubusercontent.com/FiloSottile/age/main/doc/age.1.html) — Man page oficial age(1) detalhando todas as opções de linha de comando, proteção de TTY, formato ASCII Armor estrito, arquivos de destinatários e identidades cifradas; consultado em 2026-10-03.
- [FiloSottile age — Official GitHub Repository](https://github.com/FiloSottile/age) — Repositório oficial BSD-3-Clause do age; consultado em 2026-10-03.
