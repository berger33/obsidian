---
id: software.seguranca.tranche08.000706
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

# GnuPG: Assinatura Criptográfica de **Commits e Tags Git (`commit.gpgsign`, `tag.gpgSign`)** e Gate de Verificação em Pipelines de CI/CD

## Em uma frase
Sem assinatura criptográfica nos commits e tags Git, qualquer pessoa com permissão de `git push` pode configurar `git config user.email "ceo@empresa.com"` e forjar a autoria de qualquer commit no histórico do repositório.

## Por que importa
Configurar o Git para assinar todos os commits e tags com a subchave de assinatura OpenPGP **`[S]`** (`user.signingkey <FINGERPRINT>!` com ponto de exclamação final para travar a subchave exata) garante autenticidade, integridade e não-repúdio sobre a árvore Merkle do Git.

## Como funciona
No pipeline de CI/CD antes do build de produção, um gate obrigatório executa **`git verify-commit HEAD`** (ou **`git verify-tag v1.4.0 --raw`**) validando contra um chaveiro versionado das chaves públicas autorizadas dos mantenedores (`GNUPGHOME` efêmero no runner).

## Exemplo
```bash
# Configurar o Git para assinar obrigatoriamente todos os commits e tags com uma subchave OpenPGP especifica
git config --global user.signingkey "0123456789ABCDEF0123456789ABCDEF01234567!"
git config --global commit.gpgsign true
git config --global tag.gpgSign true
git config --global gpg.program gpg
```

## Limites e trade-offs
Observe o ponto de exclamação **`!`** ao final do fingerprint em `user.signingkey`: no GnuPG, adicionar `!` ao final do ID/fingerprint força o `gpg` a usar exatamente aquela subchave específica, em vez de escolher automaticamente a subchave mais recente do pacote.

## Como verificar
Execute `git log --show-signature -n 1` (ou `git verify-commit --raw HEAD`) para inspecionar a linha `[GNUPG:] VALIDSIG` do último commit.

## Conexões
- [[gnupg-verificacao-assinaturas-pacotes-gpgv-status-fd-automacao]] — Veja também: GnuPG (`gpgv` & `--status-fd`): Verificação Determinística de Assinaturas de Releases e Pacotes sem Efeitos Colaterais em Scripts e CI/CD.
- [[gnupg-criptografia-simetrica-hibrida-aead-aes256-s2k-argon2-iteracoes]] — Veja também: GnuPG: Criptografia Simétrica (`-c`) e Híbrida Assimétrica (`-e -r`), **S2K (`s2k-count` / Argon2)** e Preferências de Cifra (`AES256`, `SHA512`).
- [[gnupg-hierarquia-chave-mestra-certify-offline-subchaves-sign-encrypt-auth]] — Referência cruzada direta com gnupg-hierarquia-chave-mestra-certify-offline-subchaves-sign-encrypt-auth.

## Fontes
- [GnuPG Official Manual — Invoking GPG & Command Options](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG.html) — manual oficial do GnuPG (gpg) cobrindo geração e gestão de chaves e subchaves OpenPGP, verificação, cifragem e formatos de chaveiro; consultado em 2026-10-03.
- [GnuPG Official Manual — Invoking GPG-AGENT & SSH Support](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG_002dAGENT.html) — manual oficial do daemon gpg-agent cobrindo cache de credenciais, pinentry, scdaemon e emulação de ssh-agent; consultado em 2026-10-03.
- [GnuPG Official Manual — Complete Option Index](https://www.gnupg.org/documentation/manuals/gnupg/Option-Index.html) — índice oficial de opções de configuração do GnuPG; consultado em 2026-10-03.
