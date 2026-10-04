---
id: software.seguranca.tranche03.000259
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
fontes: ["https://raw.githubusercontent.com/in-toto/attestation/main/README.md", "https://raw.githubusercontent.com/in-toto/in-toto/develop/README.md", "https://github.com/in-toto/attestation"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# in-toto SDKs e Protobuf Bindings (`in-toto-golang`, `in-toto-rs`, `Python`, `Java`): geração e validação de atestados em código

## Em uma frase
Conforme documentado no README oficial de `in-toto/attestation` (*"We provide protobuf definitions of the spec. We currently provide language bindings for Go, Python, Rust and Java"*), o projeto mantém definições **Protocol Buffers (`protos/`)** e bibliotecas oficiais para gerar, serializar e validar Statements e Predicados com segurança de tipos em **Go**, **Python**, **Rust** e **Java**.

## Por que importa
Construir JSON de atestados concatenando strings manualmente em scripts bash corre o risco de gerar tipos inválidos ou omitir campos obrigatórios da especificação v1.

## Como funciona
Usando os pacotes gerados a partir dos Protobufs oficiais (ex.: `github.com/in-toto/attestation/go/v1` em Go ou `in_toto_attestation` em Python), sua ferramenta de plataforma valida estruturalmente todos os campos de `Statement`, `ResourceDescriptor` e `Predicates` antes de assinar o envelope DSSE.

## Exemplo
```python
# Exemplo em Python usando o modelo do in-toto para validar a presença de subject e digest:
import json

with open("provenance.statement.json", encoding="utf-8") as f:
    stmt = json.load(f)

assert stmt["_type"] == "https://in-toto.io/Statement/v1"
assert len(stmt["subject"]) >= 1
assert "sha256" in stmt["subject"][0]["digest"]
```

## Limites e trade-offs
Nos objetos `ResourceDescriptor` dentro de `subject`, além de `name` e `digest`, você pode preencher `uri`, `mediaType` e `annotations` para enriquecer a rastreabilidade do artefato.

## Como verificar
Valide seus arquivos JSON de Statement contra as definições do repositório `in-toto/attestation`.

## Conexões
- [[intoto-sign-assinatura-multiplas-chaves-thresholds-gpg-ssh-ed25519]] — Veja também: in-toto Assinaturas e Quorum (`in-toto-sign` e `threshold`): exigência de múltiplas assinaturas independentes em `Layout` e `Steps`.
- [[intoto-interseccao-slsa-witness-archivista-sigstore-admission-control]] — Veja também: in-toto + `SLSA`, `Witness` e `Sigstore`: implementação prática de cadeias verificáveis do commit ao Kubernetes.

## Fontes
- [CNCF in-toto GitHub — README.md (Supply Chain Layout, Functionaries, Artifact Rules, in-toto-run, in-toto-record, Inspections & in-toto-verify)](https://raw.githubusercontent.com/in-toto/attestation/main/README.md) — README oficial do in-toto/in-toto documentando a estrutura de layouts, regras de encadeamento de materials/products, geração de links e verificação final; consultado em 2026-10-03.
- [CNCF in-toto Attestation Framework GitHub — README.md (Statement v1 Specification, Vetted Predicates, DSSE, SLSA Intersection & Language Bindings)](https://raw.githubusercontent.com/in-toto/in-toto/develop/README.md) — README oficial do in-toto/attestation descrevendo a especificação do Attestation Framework v1, catálogo de predicados, definições Protobuf e interseção com SLSA; consultado em 2026-10-03.
- [CNCF in-toto — Official GitHub Repository](https://github.com/in-toto/attestation) — Repositório oficial Apache-2.0 do CNCF in-toto; consultado em 2026-10-03.
