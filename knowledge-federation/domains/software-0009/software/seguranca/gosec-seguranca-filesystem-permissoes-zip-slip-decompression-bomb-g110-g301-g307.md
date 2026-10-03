---
id: software.seguranca.tranche03.000275
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

# `gosec` Segurança de Sistema de Arquivos (`G110` *Decompression Bomb*, `G301`–`G307` Permissões Octais e `G305` *Zip Slip*)

## Em uma frase
A família **`G3xx`** (junto com **`G110`**) do `gosec` audita operações de arquivo e descompactação em Go: **`G110`** detecta o uso de `io.Copy` sem limite ao descomprimir streams `gzip`/`zlib`/`zip` (*Decompression Bomb / Zip Bomb*), **`G305`** detecta extração de arquivos `.zip`/`.tar` vulnerável a *Zip Slip* (`../../etc/cron.d/pwn`) e **`G301`, `G302`, `G306`, `G307`** auditam permissões POSIX excessivamente abertas em diretórios e arquivos.

## Por que importa
Em Go, `os.Create("secret.txt")` cria o arquivo com permissão **`0666`** (antes da `umask`), permitindo que outros usuários locais na mesma máquina leiam o arquivo se a `umask` for permissiva (`G307`); já `os.WriteFile("key", data, 0644)` expõe o arquivo para leitura global quando `G306` exige no máximo **`0600`**!

## Como funciona
Da mesma forma, ao descomprimir qualquer payload `gzip` ou arquivo `zip` enviado por um usuário, usar `io.Copy(dst, zipReader)` direto permite que um arquivo `.zip` de 100 KB expanda para 50 GB e derrube o processo por *Out-Of-Memory*; a regra **`G110`** exige usar **`io.CopyN`** ou **`io.LimitReader`**!

## Exemplo
```go
package storage

import (
	"io"
	"os"
)

func SaveCompressedSafely(path string, compressedReader io.Reader) error {
	// Aprovado por G302/G306/G307: abre arquivo com permissão estrita 0600 (apenas dono lê/escreve)
	f, err := os.OpenFile(path, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, 0600)
	if err != nil {
		return err
	}
	defer f.Close()

	// Aprovado por G110: limita a leitura descompactada a no máximo 10 MiB contra Decompression Bomb
	limited := io.LimitReader(compressedReader, 10*1024*1024)
	_, err = io.Copy(f, limited)
	return err
}
```

## Limites e trade-offs
Conforme documentado em `RULES.md`, o ID **`G307`** costumava verificar `defer f.Close()`, mas essa verificação antiga foi aposentada e hoje **`G307`** verifica especificamente o uso de `os.Create` (que usa permissão `0666` fixa em vez de `os.OpenFile` com `0600`).

## Como verificar
Execute `gosec -include=G110,G301,G302,G304,G305,G306,G307 ./...` para auditar toda manipulação de arquivos.

## Conexões
- [[gosec-seguranca-http-cookies-serializacao-segredos-g117-g120-g124]] — Veja também: `gosec` Hardening de Serviços Web e Serialização: exposição de segredos em JSON/YAML (`G117`), `ParseMultipartForm` (`G120`) e Cookies (`G124`).
- [[gosec-criptografia-tls-ssh-g401-a-g408-math-rand-vs-crypto-rand]] — Veja também: `gosec` Criptografia, TLS e SSH (`G401`–`G408` e `G501`–`G507`): `crypto/rand`, `MinVersion: tls.VersionTLS13`, IVs hardcoded e SSH.

## Fontes
- [Securego gosec Official Rules Documentation — RULES.md (Complete Catalog of G1xx-G7xx Rules, AST/SSA/Taint Implementations & Per-Rule JSON Config)](https://raw.githubusercontent.com/securego/gosec/master/RULES.md) — Catálogo oficial RULES.md detalhando todas as regras G1xx a G7xx, distinção entre motores AST, SSA e Taint Analysis e configuração JSON; consultado em 2026-10-03.
- [Securego gosec GitHub — README.md (Go Security Checker, CLI Flags, SARIF Code Scanning, Private Modules GOPRIVATE & Bazel nogo)](https://raw.githubusercontent.com/securego/gosec/master/README.md) — README oficial do securego/gosec documentando instalação, códigos de saída, seleção de regras, supressões e integração em pipelines CI/CD; consultado em 2026-10-03.
- [Securego gosec — Official GitHub Repository](https://github.com/securego/gosec) — Repositório oficial Apache-2.0 do Securego gosec; consultado em 2026-10-03.
