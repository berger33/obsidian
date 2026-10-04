---
id: software.testes.tranche24.001798
tipo: tecnica
dominio: software
subdominio: testes
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-24.md"
fontes: ["https://raw.githubusercontent.com/google/honggfuzz/master/README.md", "https://github.com/google/honggfuzz"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Trophies: a lista de CVEs como currículo

## Em uma frase
A seção Trophies do README documenta o histórico real: no OpenSSL, CVE-2016-6309 marcada "(Critical, Potential RCE)" mais três CVEs; em Apache HTTPD, CVE-2017-7659 (remote crash do mod_http2) e CVE-2017-9789 (use-after-free) entre outras; Samba com três CVEs; ProFTPD CVE-2019-18217 (DoS); FreeType 2 com a série CVE-2010-2497 até CVE-2010-2527; VLC double-free RCE; Adobe Flash CVE-2015-0316; ImageIO do iOS/macOS "Multiple security problems (Project Zero)"; e até panics do Rust em regex, h2, sleep-parser e lewton.

## Por que importa
Para justificar investimento em fuzzing, um currículo de CVEs em software amplamente auditado (OpenSSL, OpenSSH pre-auth crash, BIND) responde à pergunta "isto acha bugs que testes de unidade não acham?" com exemplos nomeados, não com retórica.

## Como funciona
Use a lista como mapa de onde fuzzing rende: parsing de rede (HTTPD, SSH), formatos de mídia (TIFF, JPEG, FreeType) e parsers de linguagem — e procure os IDs citados no tracker público de cada projeto antes de concluir por analogia com o seu alvo.

## Exemplo
A entrada "Rust: Panics/safety issues in regex, h2, sleep-parser, lewton" mostra que o fuzzing vale também em memória-safe: panic é crash detectável, mesmo sem corrupção.

## Limites e trade-offs
A lista é a autodeclaração do projeto, organizadas por categoria com IDs específicos; verifique cada CVE no documento oficial de segurança do software afetado antes de repetir qualquer afirmação além da linha citada.

## Como verificar
Os itens foram lidos diretamente da seção Trophies do README oficial, incluindo os marcadores de severidade.

## Conexões
- [[honggfuzz-input-placeholder]] — Veja também: ___FILE___: o contrato do input por arquivo.
- [[honggfuzz-adopters-not-google]] — Veja também: Quem adota — e o disclaimer de que não é produto Google.

## Fontes
- [Honggfuzz — README oficial](https://raw.githubusercontent.com/google/honggfuzz/master/README.md) — README oficial do Honggfuzz com recursos de cobertura por hardware/software, modo persistente, ptrace, build wrappers, placeholder ___FILE___ e trophies.; consultado em 2026-10-03.
- [Repositório oficial google/honggfuzz](https://github.com/google/honggfuzz) — Repositório oficial do Honggfuzz no GitHub com código-fonte, wrappers hfuzz_cc, exemplos e documentação.; consultado em 2026-10-03.
