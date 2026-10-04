---
id: software.seguranca.tranche02.000160
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

# `age` em Pipelines GitOps e Dotfiles: integração com `SOPS` (`SOPS_AGE_KEY_FILE`), `Flux CD`, `Argo CD`, `passage` e `chezmoi`

## Em uma frase
Por ter chaves pequenas de 1 linha sem estado global de keyring, o `age` tornou-se o motor criptográfico padrão preferido para **Mozilla/CNCF SOPS**, **Flux CD (`kustomize-controller`)**, **Argo CD (KSOPS)**, **chezmoi** (gerenciamento de dotfiles) e **passage** (fork moderno do `pass` baseado em `age`).

## Por que importa
Usar PGP/GnuPG dentro de containers minimalistas do Kubernetes (como o `kustomize-controller` do Flux) exigia importar anéis de chaves complexos; com o `age`, basta criar um Kubernetes Secret contendo o arquivo `age.agekey` de 2 linhas!

## Como funciona
No SOPS, você define a chave pública `age: age1...` no arquivo `.sops.yaml` na raiz do repositório Git e aponta a variável de ambiente **`SOPS_AGE_KEY_FILE=~/.config/sops/age/keys.txt`** (ou `SOPS_AGE_KEY` no CI), permitindo cifrar apenas os valores YAML (`data` / `stringData`) mantendo as chaves legíveis em Pull Requests.

## Exemplo
```yaml
# Exemplo de .sops.yaml usando destinatários age para manifests Kubernetes de produção e staging:
creation_rules:
  - path_regex: clusters/production/.*\.ya?ml$
    encrypted_regex: ^(data|stringData)$
    age: >-
      age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p,
      age1lggyhqrw2nlhcxprm67z43rta597azn8gknawjehu9d9dl0jq3yqqvfafg
```

## Limites e trade-offs
Guarde a chave pública `age1...` em comentário dentro do próprio arquivo de chave privada (`# public key: age1...`, como o `age-keygen` já faz por padrão) para facilitar auditorias e rotações.

## Como verificar
Verifique a descriptografia de um manifesto cifrado com `SOPS_AGE_KEY_FILE=./key.txt sops -d secret.enc.yaml`.

## Conexões
- [[agecrypt-biblioteca-go-filippo-io-age-encrypt-decrypt-streams]] — Veja também: `age` como Biblioteca Nativa em Go (`filippo.io/age`): `age.Encrypt`, `age.Decrypt` e `armor` em aplicações sem processos externos.

## Fontes
- [FiloSottile age GitHub — README.md (Simple Modern File Encryption Tool, Usage, Multiple Recipients, SSH Keys, Plugins & Go Library)](https://raw.githubusercontent.com/FiloSottile/age/main/README.md) — README oficial do FiloSottile/age documentando filosofia sem opções de configuração, uso de chaves X25519 e SSH, destinatários múltiplos, plugins de hardware e integração no ecossistema; consultado em 2026-10-03.
- [FiloSottile age Official Man Page — doc/age.1.html (Complete Specification of Flags -e/-d/-r/-R/-p/-a/-i/-j, Passphrase-Protected Identities & Format Overhead)](https://raw.githubusercontent.com/FiloSottile/age/main/doc/age.1.html) — Man page oficial age(1) detalhando todas as opções de linha de comando, proteção de TTY, formato ASCII Armor estrito, arquivos de destinatários e identidades cifradas; consultado em 2026-10-03.
- [FiloSottile age — Official GitHub Repository](https://github.com/FiloSottile/age) — Repositório oficial BSD-3-Clause do age; consultado em 2026-10-03.
