---
id: software.seguranca.tranche07.000692
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-07.md"
fontes: ["https://quay.github.io/clair/whatis.html", "https://raw.githubusercontent.com/quay/clair/main/README.md", "https://quay.github.io/claircore/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Clair v4 (`Indexer` & `ClairCore`): Indexação Endereçada por Conteúdo de Manifestos OCI, Deduplicação de Camadas e `IndexReport`

## Em uma frase
No Clair v4, a análise de uma imagem começa enviando ao **`Indexer`** (`POST /indexer/api/v1/index_report`) um objeto **`Manifest`** JSON que lista o digest SHA-256 da imagem e a lista ordenada de suas camadas (`layers`), onde cada camada informa o seu `hash` (`sha256:...`), a `uri` autenticada para download do blob no Registry e os `headers` de autorização.

## Por que importa
Como 500 microsserviços da empresa frequentemente compartilham as mesmas 3 camadas base (ex.: a imagem base `debian:12-slim` ou `registry.access.redhat.com/ubi9/ubi-minimal`), o `Indexer` verifica no PostgreSQL se o digest `sha256:...` daquela camada já foi escaneado antes: **se já foi, ele reutiliza os artefatos instantaneamente sem baixar nem descompactar a camada novamente**!

## Como funciona
Para cada camada nova, os *Scanners* do `ClairCore` extraem os metadados de pacotes instalados, distribuições e repositórios sem extrair o filesystem completo em disco quando possível, consolidando o resultado em um **`IndexReport`** imutável (exceto quando a versão de um scanner do `ClairCore` é atualizada, o que invalida seletivamente apenas o scanner atualizado).

## Exemplo
```json
{
  "hash": "sha256:6b5f5f2d4b8c9a1e3f4d5c6b7a8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e",
  "layers": [
    {
      "hash": "sha256:1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b",
      "uri": "https://registry.internal.corp/v2/base/ubi9/blobs/sha256:1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b",
      "headers": {
        "Authorization": ["Bearer eyJhbGciOiJSUzI1NiIs..."]
      }
    }
  ]
}
```

## Limites e trade-offs
Consulte `GET /indexer/api/v1/index_state` antes de reenviar um manifesto: se o digest do manifesto já constar no estado atual do `Indexer`, você pode pular o `POST` e pedir diretamente o relatório de vulnerabilidades atualizado ao `Matcher`.

## Como verificar
Submeta um manifesto de teste ao `/indexer/api/v1/index_report` e verifique que o campo `.state` no `IndexReport` retornado atinge `"IndexFinished"`.

## Conexões
- [[clair-arquitetura-analise-estatica-containers-claircore-indexer-matcher-notifier]] — Veja também: Project Quay **Clair v4 & `ClairCore`**: Arquitetura de Análise Estática de Imagens OCI/Docker (`Indexer`, `Matcher` e `Notifier`).
- [[clair-scanners-pacotes-os-dpkg-rpm-apk-linguagens-gobin-python-java]] — Veja também: ClairCore: Matriz de Scanners de Pacotes de Sistema Operacional (`dpkg`, `rpm`, `apk`) e Linguagens (`gobin`, `python`, `java`, `nodejs`, `ruby`, `rust`).
- [[clair-motor-matching-updaters-fontes-ovals-osv-cvss-enrichment]] — Referência cruzada direta com clair-motor-matching-updaters-fontes-ovals-osv-cvss-enrichment.

## Fontes
- [Project Quay Clair v4 Official Documentation — What is ClairV4 & Architecture](https://quay.github.io/clair/whatis.html) — documentação oficial do Clair v4 cobrindo a separação ClairCore, Indexer (IndexReport), Matcher (VulnerabilityReport) e Notifier; consultado em 2026-10-03.
- [Project Quay Clair Official GitHub — Container Vulnerability Static Analysis](https://raw.githubusercontent.com/quay/clair/main/README.md) — repositório oficial do projeto Clair v4 e utilitário de linha de comando clairctl; consultado em 2026-10-03.
- [ClairCore Official Documentation — Layer Indexing & Vulnerability Matching Engine](https://quay.github.io/claircore/) — documentação oficial da biblioteca ClairCore para extração de pacotes de SO/linguagens e updaters de vulnerabilidades; consultado em 2026-10-03.
