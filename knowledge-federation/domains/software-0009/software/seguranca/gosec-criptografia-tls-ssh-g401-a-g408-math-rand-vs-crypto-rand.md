---
id: software.seguranca.tranche03.000276
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/securego/gosec/master/RULES.md", "https://raw.githubusercontent.com/securego/gosec/master/README.md", "https://github.com/securego/gosec"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `gosec` Criptografia, TLS e SSH (`G401`–`G408` e `G501`–`G507`): `crypto/rand`, `MinVersion: tls.VersionTLS13`, IVs hardcoded e SSH

## Em uma frase
As categorias **`G4xx`** e **`G5xx`** do `gosec` auditam o uso de primitivas criptográficas e protocolos de segurança em Go: **`G401`/`G405`/`G406`** e **`G501`–`G507`** bloqueiam algoritmos quebrados (`md5`, `sha1`, `des`, `rc4`, `md4`, `ripemd160`), **`G402`** audita configurações `tls.Config` inseguras (`InsecureSkipVerify: true` ou `MinVersion` antiga), **`G403`** exige chaves RSA >= 2048 bits, **`G404`** proíbe `math/rand` para segurança, **`G407` (SSA)** detecta IV/nonce estático hardcoded em cifras AEAD/CBC e **`G408` (SSA)** detecta bypass de autenticação em `ssh.PublicKeyCallback`!

## Por que importa
Reutilizar um **nonce/IV constante (hardcoded)** no `aes.NewGCM` (`G407`) destrói completamente a confidencialidade e a autenticidade do AES-GCM na segunda mensagem cifrada; e configurar `InsecureIgnoreHostKey()` no cliente SSH (`G106`) ou `InsecureSkipVerify: true` no `tls.Config` (`G402`) abre a conexão para ataques *Man-in-the-Middle (MitM)*.

## Como funciona
Use sempre **`crypto/rand.Read`** para gerar chaves e nonces aleatórios e defina **`MinVersion: tls.VersionTLS12`** (ou `tls.VersionTLS13`) em toda instância de `tls.Config`.

## Exemplo
```go
package transport

import (
	"crypto/rand"
	"crypto/tls"
	"io"
)

func NewSecureTLSConfig() (*tls.Config, []byte, error) {
	nonce := make([]byte, 12)
	// Aprovado por G404 e G407: gera nonce aleatório via CSPRNG do sistema operacional (crypto/rand)
	if _, err := io.ReadFull(rand.Reader, nonce); err != nil {
		return nil, nil, err
	}
	// Aprovado por G402: exige TLS 1.3 mínimo e mantém verificação de certificado ativa
	cfg := &tls.Config{
		MinVersion: tls.VersionTLS13,
	}
	return cfg, nonce, nil
}
```

## Limites e trade-offs
Observe a regra **`G123` (SSA)** em `RULES.md`: ao usar o callback customizado `VerifyPeerCertificate` no `tls.Config`, configure também `VerifyConnection`, pois sessões TLS retomadas (*resumption*) não invocam `VerifyPeerCertificate`!

## Como verificar
Rode `gosec -include=G106,G123,G401,G402,G403,G404,G407,G408 ./...` sobre seus pacotes de rede e criptografia.

## Conexões
- [[gosec-seguranca-filesystem-permissoes-zip-slip-decompression-bomb-g110-g301-g307]] — Veja também: `gosec` Segurança de Sistema de Arquivos (`G110` *Decompression Bomb*, `G301`–`G307` Permissões Octais e `G305` *Zip Slip*).
- [[gosec-configuracao-regras-json-g101-entropia-g104-erros-allowlist]] — Veja também: `gosec` Configuração Fina por Regra (`-conf config.json`): ajuste de entropia em `G101`, allowlist de erros em `G104` e permissões em `G301`/`G306`.

## Fontes
- [Securego gosec Official Rules Documentation — RULES.md (Complete Catalog of G1xx-G7xx Rules, AST/SSA/Taint Implementations & Per-Rule JSON Config)](https://raw.githubusercontent.com/securego/gosec/master/RULES.md) — Catálogo oficial RULES.md detalhando todas as regras G1xx a G7xx, distinção entre motores AST, SSA e Taint Analysis e configuração JSON; consultado em 2026-10-03.
- [Securego gosec GitHub — README.md (Go Security Checker, CLI Flags, SARIF Code Scanning, Private Modules GOPRIVATE & Bazel nogo)](https://raw.githubusercontent.com/securego/gosec/master/README.md) — README oficial do securego/gosec documentando instalação, códigos de saída, seleção de regras, supressões e integração em pipelines CI/CD; consultado em 2026-10-03.
- [Securego gosec — Official GitHub Repository](https://github.com/securego/gosec) — Repositório oficial Apache-2.0 do Securego gosec; consultado em 2026-10-03.
