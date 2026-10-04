---
id: software.seguranca.tranche03.000258
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
fontes: ["https://raw.githubusercontent.com/in-toto/in-toto/develop/README.md", "https://raw.githubusercontent.com/in-toto/attestation/main/README.md", "https://github.com/in-toto/in-toto"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# in-toto Assinaturas e Quorum (`in-toto-sign` e `threshold`): exigência de múltiplas assinaturas independentes em `Layout` e `Steps`

## Em uma frase
O utilitário **`in-toto-sign`** e o campo **`threshold`** em cada etapa do `layout` permitem exigir que um `layout` (ou até mesmo uma etapa crítica de aprovação/release) seja assinado por **M de N chaves distintas** (suportando chaves criptográficas Ed25519, RSA, ECDSA e GPG).

## Por que importa
Se o `root.layout` for assinado por uma única chave de administrador e o laptop desse administrador for comprometido, o atacante poderá publicar um layout malicioso autorizando sua própria chave como functionary.

## Como funciona
Assinando o `root.layout` com as chaves offline de múltiplos *Project Owners* (`in-toto-sign -f root.layout -k alice.key -a` seguido de `in-toto-sign -f root.layout -k bob.key -a`) e passando ambas as chaves públicas em `in-toto-verify --verification-keys alice.pub bob.pub`, um único comprometimento de chave não permite alterar as regras da cadeia de suprimentos!

## Exemplo
```bash
# 1. Alice assina o layout inicial e Bob adiciona sua assinatura em quorum (--append):
in-toto-sign -f unsigned.layout -k alice-owner-key -o root.layout
in-toto-sign -f root.layout -k bob-owner-key --append -o root.layout

# 2. Verificando as assinaturas do layout contra as chaves públicas de Alice e Bob:
in-toto-sign -f root.layout --verify -k alice-owner.pub bob-owner.pub
```

## Limites e trade-offs
Dentro de um `step` do layout, você também pode configurar `"threshold": 2` e listar 3 chaves em `"pubkeys"`, exigindo que pelo menos 2 sistemas de build independentes (*reproducible builds*) produzam e assinem o mesmo hash de binário!

## Como verificar
Teste `in-toto-sign --verify` omitindo uma das chaves públicas para confirmar que a verificação falha sem o quorum completo.

## Conexões
- [[intoto-dsse-dead-simple-signing-envelope-pae-prevencao-ambiguidade]] — Veja também: in-toto Envelope de Assinatura `DSSE` (*Dead Simple Signing Envelope*) e `PAE`: proteção contra ataques de confusão de parser e tipo.
- [[intoto-bindings-go-python-rust-java-protobuf-validacao-programatica]] — Veja também: in-toto SDKs e Protobuf Bindings (`in-toto-golang`, `in-toto-rs`, `Python`, `Java`): geração e validação de atestados em código.

## Fontes
- [CNCF in-toto GitHub — README.md (Supply Chain Layout, Functionaries, Artifact Rules, in-toto-run, in-toto-record, Inspections & in-toto-verify)](https://raw.githubusercontent.com/in-toto/in-toto/develop/README.md) — README oficial do in-toto/in-toto documentando a estrutura de layouts, regras de encadeamento de materials/products, geração de links e verificação final; consultado em 2026-10-03.
- [CNCF in-toto Attestation Framework GitHub — README.md (Statement v1 Specification, Vetted Predicates, DSSE, SLSA Intersection & Language Bindings)](https://raw.githubusercontent.com/in-toto/attestation/main/README.md) — README oficial do in-toto/attestation descrevendo a especificação do Attestation Framework v1, catálogo de predicados, definições Protobuf e interseção com SLSA; consultado em 2026-10-03.
- [CNCF in-toto — Official GitHub Repository](https://github.com/in-toto/in-toto) — Repositório oficial Apache-2.0 do CNCF in-toto; consultado em 2026-10-03.
