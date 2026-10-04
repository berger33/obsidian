---
id: software.seguranca.tranche07.000694
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

# Clair v4 (`Matcher`): Atualizadores Contínuos de Feeds de Segurança (OVAL, **OSV**, Red Hat VEX/CSAF, Debian/Ubuntu/Alpine SecDB e NVD CVSS Enrichment)

## Em uma frase
O serviço **`Matcher`** do Clair v4 executa em background um conjunto de **Updaters** periódicos que baixam e normalizam os boletins oficiais de segurança diretamente das distribuições Linux e do ecossistema **OSV (*Open Source Vulnerabilities*)**, além de enriquecer os achados com pontuações **CVSS v3.1** da NVD.

## Por que importa
Usar o feed oficial de segurança da própria distribuição (como Red Hat OVAL/CSAF, Ubuntu OVAL, Debian Security Tracker e Alpine SecDB) em vez de comparar apenas números de versão genéricos na NVD é fundamental para **eliminar falsos positivos causados por *backporting***: quando o Debian ou RHEL corrige uma vulnerabilidade aplicando o patch na versão `1.2.3-4+deb12u2`, um scanner ingênuo acusaria falsamente que `1.2.3 < 1.2.4`; já o `Matcher` do Clair consulta o boletim exato da distribuição e sabe que `1.2.3-4+deb12u2` já está corrigido!

## Como funciona
Toda vez que um cliente solicita `GET /matcher/api/v1/vulnerability_report/{manifest_hash}`, o `Matcher` recupera o `IndexReport` persistido e executa o cruzamento em tempo real contra a base de vulnerabilidades mais recente.

## Exemplo
```bash
# Solicitar ao Matcher o VulnerabilityReport atualizado de um manifesto ja indexado e resumir vulnerabilidades
curl -sS "http://127.0.0.1:6060/matcher/api/v1/vulnerability_report/sha256:6b5f5f2d4b8c9a1e3f4d5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f" \
  | jq '{vulns_found: (.vulnerabilities | length), package_vulns: .package_vulnerabilities}'
```

## Limites e trade-offs
Em ambientes corporativos *air-gapped* (desconectados da internet), o Clair v4 permite desativar o download direto nos Updaters (`disable_updaters: true`) e importar pacotes de definições de vulnerabilidades offline via `clairctl import-updaters`.

## Como verificar
Consulte `GET /matcher/api/v1/internal/update_operations` para verificar o timestamp e o fingerprint da última sincronização bem-sucedida de cada Updater (`rhel`, `ubuntu`, `debian`, `alpine`, `osv`, `cvss`).

## Conexões
- [[clair-scanners-pacotes-os-dpkg-rpm-apk-linguagens-gobin-python-java]] — Veja também: ClairCore: Matriz de Scanners de Pacotes de Sistema Operacional (`dpkg`, `rpm`, `apk`) e Linguagens (`gobin`, `python`, `java`, `nodejs`, `ruby`, `rust`).
- [[clair-servico-notificacao-notifier-webhooks-novos-cves-imagens-antigas]] — Veja também: Clair v4 (`Notifier`): Detecção Proativa de **Novos CVEs** em Imagens Já Implantadas e Entrega Confiável via **Webhooks / AMQP / STOMP**.
- [[clair-arquitetura-analise-estatica-containers-claircore-indexer-matcher-notifier]] — Referência cruzada direta com clair-arquitetura-analise-estatica-containers-claircore-indexer-matcher-notifier.
- [[clair-fluxo-indexacao-content-addressable-manifest-layers-indexreport]] — Referência cruzada direta com clair-fluxo-indexacao-content-addressable-manifest-layers-indexreport.

## Fontes
- [Project Quay Clair v4 Official Documentation — What is ClairV4 & Architecture](https://quay.github.io/clair/whatis.html) — documentação oficial do Clair v4 cobrindo a separação ClairCore, Indexer (IndexReport), Matcher (VulnerabilityReport) e Notifier; consultado em 2026-10-03.
- [Project Quay Clair Official GitHub — Container Vulnerability Static Analysis](https://raw.githubusercontent.com/quay/clair/main/README.md) — repositório oficial do projeto Clair v4 e utilitário de linha de comando clairctl; consultado em 2026-10-03.
- [ClairCore Official Documentation — Layer Indexing & Vulnerability Matching Engine](https://quay.github.io/claircore/) — documentação oficial da biblioteca ClairCore para extração de pacotes de SO/linguagens e updaters de vulnerabilidades; consultado em 2026-10-03.
