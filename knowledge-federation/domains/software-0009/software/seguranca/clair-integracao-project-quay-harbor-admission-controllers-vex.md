---
id: software.seguranca.tranche07.000700
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

# Clair v4: Integração Nativa com **Project Quay**, Políticas de **Kubernetes Admission Control** e Redução de Superfície com Imagens Mínimas

## Em uma frase
Em uma arquitetura completa de DevSecOps para Kubernetes, o **Clair v4** atua integrado ao registro corporativo (**Project Quay**) e aos controladores de admissão do cluster Kubernetes: nenhuma imagem entra em produção sem ter seu digest `sha256:...` indexado e aprovado pela política de vulnerabilidades.

## Por que importa
Quando um desenvolvedor faz `docker push` / `podman push` para o Project Quay, o Quay envia imediatamente o manifesto ao Clair v4; se uma imagem em produção passar a ter uma vulnerabilidade `Critical` descoberta dias depois, o `Notifier` avisa o Quay e o SOC, enquanto no cluster Kubernetes um **ValidatingAdmissionPolicy / Kyverno / OPA Gatekeeper** exige atestação assinada via Sigstore Cosign/Rekor comprovando que o scan do Clair passou.

## Como funciona
A contramedida estrutural mais eficaz revelada pelos relatórios do Clair v4 é a migração de imagens base pesadas (`ubuntu:latest` / `node:full` com 400+ pacotes Debian e dezenas de CVEs semanais em ferramentas que a aplicação nem usa) para **Builds Multi-Stage** com imagens base mínimas (**`ubi9-micro`**, **`distroless`** ou **`wolfi` / `alpine`**), reduzindo a superfície de pacotes em 90%.

## Exemplo
```dockerfile
# Exemplo de Multi-Stage Dockerfile produzindo imagem final minima para zerar CVEs de ferramentas de build no Clair v4
FROM golang:1.23-alpine AS builder
WORKDIR /src
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -trimpath -o /out/app ./cmd/server

FROM gcr.io/distroless/static-debian12:nonroot
COPY --from=builder /out/app /app
USER 65532:65532
ENTRYPOINT ["/app"]
```

## Limites e trade-offs
Ao migrar para uma imagem `distroless:nonroot` com `Multi-Stage Build`, compare o `IndexReport` do Clair v4 antes e depois: o número de pacotes de sistema operacional cai de centenas para menos de uma dezena, eliminando classes inteiras de falsos alertas e binários de shell/gerenciadores de pacotes.

## Como verificar
Compare a contagem `.vulnerabilities | length` no Clair v4 entre a imagem de build e a imagem final `distroless` para comprovar a redução drástica da superfície de ataque.

## Conexões
- [[clair-enriquecimento-cvss-severidade-normalizada-priorizacao-remediacao]] — Veja também: Clair v4: Normalização de Severidade (`Unknown`, `Negligible`, `Low`, `Medium`, `High`, `Critical`), Enriquecimento CVSS e Priorização.
- [[clair-arquitetura-analise-estatica-containers-claircore-indexer-matcher-notifier]] — Referência cruzada direta com clair-arquitetura-analise-estatica-containers-claircore-indexer-matcher-notifier.
- [[clair-scanners-pacotes-os-dpkg-rpm-apk-linguagens-gobin-python-java]] — Referência cruzada direta com clair-scanners-pacotes-os-dpkg-rpm-apk-linguagens-gobin-python-java.

## Fontes
- [Project Quay Clair v4 Official Documentation — What is ClairV4 & Architecture](https://quay.github.io/clair/whatis.html) — documentação oficial do Clair v4 cobrindo a separação ClairCore, Indexer (IndexReport), Matcher (VulnerabilityReport) e Notifier; consultado em 2026-10-03.
- [Project Quay Clair Official GitHub — Container Vulnerability Static Analysis](https://raw.githubusercontent.com/quay/clair/main/README.md) — repositório oficial do projeto Clair v4 e utilitário de linha de comando clairctl; consultado em 2026-10-03.
- [ClairCore Official Documentation — Layer Indexing & Vulnerability Matching Engine](https://quay.github.io/claircore/) — documentação oficial da biblioteca ClairCore para extração de pacotes de SO/linguagens e updaters de vulnerabilidades; consultado em 2026-10-03.
