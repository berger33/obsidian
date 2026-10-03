---
id: software.devops.tranche10.000965
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/goreleaser/goreleaser/main/README.md", "https://goreleaser.com/getting-started/quick-start/", "https://github.com/goreleaser/goreleaser"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# GoReleaser: segurança de cadeia de suprimentos com checksums SHA-256, geração de SBOM (Syft) e assinatura (Cosign / GPG)

## Em uma frase
O GoReleaser gera por padrão o arquivo `checksums.txt` (SHA-256) de todos os artefatos produzidos e integra nativamente a geração de **Software Bills of Materials (`sboms:` via Syft)** e a assinatura criptográfica de artefatos e containers (**`signs:` e `docker_signs:` via Sigstore Cosign ou GPG**).

## Por que importa
Em conformidade moderna de segurança de cadeia de suprimentos (SLSA / OpenSSF Scorecard), publicar binários soltos em uma página de GitHub Releases sem checksums autenticados, sem assinatura criptográfica e sem SBOM impede que usuários e sistemas automatizados verifiquem se o binário baixado foi adulterado.

## Como funciona
Durante o pipeline do `goreleaser release`: (1) **`checksum:`**: calcula o hash SHA-256 de todos os arquivos gerados em `archives`, `nfpms`, etc., gravando `<projeto>_<versão>_checksums.txt`; (2) **`sboms:`**: invoca o `syft` sobre cada arquivo ou binário construído para gerar arquivos `.sbom.json` (SPDX ou CycloneDX) e incluí-los nos assets da release; e (3) **`signs:` / `docker_signs:`**: invoca o `cosign` (suportando assinatura *keyless* via OIDC no GitHub Actions com `cmd: cosign`) ou `gpg` para assinar o arquivo `checksums.txt` (ou todos os artefatos) e as imagens de container publicadas, gerando os arquivos `.sig` e `.pem` de verificação.

## Exemplo
```yaml
# Exemplo de geração automática de SBOMs (via Syft) e assinatura keyless do arquivo de checksums (via Cosign) no .goreleaser.yaml
sboms:
  - artifacts: archive
signs:
  - cmd: cosign
    certificate: "${artifact}.pem"
    args:
      - sign-blob
      - "--output-certificate=${certificate}"
      - "--output-signature=${signature}"
      - "${artifact}"
      - "--yes"
    artifacts: checksum
```

## Limites e trade-offs
Para que os passos `sboms:` (que chama `syft` por padrão) e `signs:` (que chama `cosign` ou `gpg`) funcionem durante o `goreleaser release`, os respectivos binários (`syft` e `cosign`) precisam estar instalados no runner de CI (verificável previamente com `goreleaser healthcheck`), e no GitHub Actions o job precisa declarar a permissão `id-token: write` para assinatura keyless do Cosign.

## Como verificar
Execute `goreleaser healthcheck` após adicionar `sboms:` e `signs:` ao `.goreleaser.yaml` para confirmar que o `syft` e o `cosign` foram detectados no ambiente.

## Conexões
- [[goreleaser-empacotamento-archives-nfpm-deb-rpm-apk-homebrew]] — Veja também: GoReleaser: empacotamento em arquivos (.tar.gz/.zip), pacotes Linux via nFPM (.deb, .rpm, .apk) e gerenciadores (Homebrew/Scoop/Winget).
- [[goreleaser-imagens-containers-dockers-buildx-ko-manifests]] — Veja também: GoReleaser: publicação de imagens de container multi-arquitetura (dockers, docker_manifests e integração ko).
- [[goreleaser-automacao-release-engineering-multilinguagem]] — Referência cruzada direta com goreleaser-automacao-release-engineering-multilinguagem.
- [[goreleaser-integracao-github-actions-permissoes-token-ci]] — Referência cruzada direta com goreleaser-integracao-github-actions-permissoes-token-ci.
- [[ko-cicd-github-actions-assinatura-cosign-slsa-seguranca]] — Referência cruzada direta com ko-cicd-github-actions-assinatura-cosign-slsa-seguranca.

## Fontes
- [GoReleaser Official Documentation — Quick Start (goreleaser init, check, healthcheck, build --single-target, release --snapshot & GITHUB_TOKEN)](https://raw.githubusercontent.com/goreleaser/goreleaser/main/README.md) — Guia oficial Quick Start do GoReleaser (v2.18+) demonstrando inicialização, builders para Go/Rust/Node.js/Zig/Bun/Deno/uv/Poetry, --snapshot, --single-target, check, healthcheck, --skip=publish e permissões GITHUB_TOKEN; consultado em 2026-10-03.
- [GoReleaser GitHub — README.md (Release Engineering Automation & Multi-Language Support)](https://goreleaser.com/getting-started/quick-start/) — README oficial do projeto goreleaser/goreleaser (MIT); consultado em 2026-10-03.
- [GoReleaser — Official GitHub Repository](https://github.com/goreleaser/goreleaser) — Repositório oficial do GoReleaser; consultado em 2026-10-03.
