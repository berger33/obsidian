---
id: software.seguranca.tranche02.000159
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

# `age` como Biblioteca Nativa em Go (`filippo.io/age`): `age.Encrypt`, `age.Decrypt` e `armor` em aplicações sem processos externos

## Em uma frase
Além da ferramenta de linha de comando, o pacote **`filippo.io/age`** (e `filippo.io/age/armor`) é uma biblioteca Go oficial com API mínima baseada nas interfaces padrão `io.Reader` e `io.Writer` (`age.Encrypt(dst io.Writer, recipients ...age.Recipient)` e `age.Decrypt(src io.Reader, identities ...age.Identity)`).

## Por que importa
Em serviços backend em Go que precisam cifrar relatórios confidenciais, dumps de banco ou artefatos de clientes antes de fazer upload para o S3, invocar `os/exec` em um binário externo é desnecessário quando `filippo.io/age` opera diretamente em streaming.

## Como funciona
Um cuidado essencial ao usar `age.Encrypt` em Go: você **deve** chamar **`w.Close()`** no `io.WriteCloser` retornado por `age.Encrypt` e verificar seu erro antes de finalizar o arquivo, pois o último chunk autenticado `STREAM` (que previne truncamento malicioso do final do arquivo) é gravado no `Close()`!

## Exemplo
```go
package main

import (
	"bytes"
	"filippo.io/age"
	"io"
)

func encryptBuffer(plaintext []byte, pubKey string) ([]byte, error) {
	recipient, err := age.ParseX25519Recipient(pubKey)
	if err != nil {
		return nil, err
	}
	var out bytes.Buffer
	w, err := age.Encrypt(&out, recipient)
	if err != nil {
		return nil, err
	}
	if _, err := io.Copy(w, bytes.NewReader(plaintext)); err != nil {
		return nil, err
	}
	if err := w.Close(); err != nil {
		return nil, err
	}
	return out.Bytes(), nil
}
```

## Limites e trade-offs
Da mesma forma, para interoperabilidade em **Rust** e **TypeScript/Browser/Node/Deno**, o README oficial recomenda as implementações compatíveis **[rage](https://github.com/str4d/rage)** (Rust) e **[typage](https://github.com/FiloSottile/typage)** (TypeScript).

## Como verificar
Escreva um teste unitário em Go cifrando com `age.GenerateX25519Identity()` e decifrando com `age.Decrypt`.

## Conexões
- [[agecrypt-suporte-pos-quantico-pq-ml-kem-x25519-especificacao-c2sp]] — Veja também: `age` Criptografia Pós-Quântica Híbrida e Verificação de Binários com `Sigsum`: proteção contra *Harvest Now, Decrypt Later*.
- [[agecrypt-integracao-gitops-sops-flux-argocd-chezmoi-pass]] — Veja também: `age` em Pipelines GitOps e Dotfiles: integração com `SOPS` (`SOPS_AGE_KEY_FILE`), `Flux CD`, `Argo CD`, `passage` e `chezmoi`.

## Fontes
- [FiloSottile age GitHub — README.md (Simple Modern File Encryption Tool, Usage, Multiple Recipients, SSH Keys, Plugins & Go Library)](https://raw.githubusercontent.com/FiloSottile/age/main/README.md) — README oficial do FiloSottile/age documentando filosofia sem opções de configuração, uso de chaves X25519 e SSH, destinatários múltiplos, plugins de hardware e integração no ecossistema; consultado em 2026-10-03.
- [FiloSottile age Official Man Page — doc/age.1.html (Complete Specification of Flags -e/-d/-r/-R/-p/-a/-i/-j, Passphrase-Protected Identities & Format Overhead)](https://raw.githubusercontent.com/FiloSottile/age/main/doc/age.1.html) — Man page oficial age(1) detalhando todas as opções de linha de comando, proteção de TTY, formato ASCII Armor estrito, arquivos de destinatários e identidades cifradas; consultado em 2026-10-03.
- [FiloSottile age — Official GitHub Repository](https://github.com/FiloSottile/age) — Repositório oficial BSD-3-Clause do age; consultado em 2026-10-03.
