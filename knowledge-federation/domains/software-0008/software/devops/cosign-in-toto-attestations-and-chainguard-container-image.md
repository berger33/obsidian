---
id: software.devops.tranche04.000328
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/sigstore/cosign/main/README.md", "https://docs.sigstore.dev/cosign/signing/overview/", "https://github.com/sigstore/cosign"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Suporte a atestações in-toto e uso da imagem oficial ghcr.io/sigstore/cosign/cosign

## Em uma frase
O Cosign possui suporte nativo a **atestações in-toto** (`in-toto.io`), permitindo anexar metadados estruturados e assinados (como proveniência SLSA, SBOMs gerados pelo Syft ou relatórios de scan) às imagens no registro OCI. Além da instalação via binários de release do GitHub ou `go install ./cmd/cosign` (com Go 1.22+), o projeto distribui a imagem oficial `ghcr.io/sigstore/cosign/cosign` (copiando `/ko-app/cosign` sobre imagens mínimas como `cgr.dev/chainguard/static:latest`) e alerta sobre a descontinuação do antigo bucket GCS de releases anunciada em 31 de julho de 2023.

## Por que importa
Enquanto uma assinatura simples (`cosign sign`) afirma apenas que uma identidade aprovou determinado digest de imagem, uma atestação in-toto assinada declara fatos verificáveis por máquina sobre como a imagem foi construída e quais pacotes ela contém.

## Como funciona
Em ambientes containerizados de CI/CD, consuma o binário do Cosign a partir da imagem oficial `ghcr.io/sigstore/cosign/cosign:<tag>` ou dos GitHub Release Assets oficiais, nunca do antigo bucket GCS descontinuado em julho de 2023.

## Exemplo
Em um Dockerfile multi-stage de runner de CI, a equipe copia `/ko-app/cosign` da imagem `ghcr.io/sigstore/cosign/cosign` para `/usr/local/bin/cosign`, utilizando-o para assinar imagens e anexar atestações in-toto de SBOM.

## Limites e trade-offs
Não utilize URLs legadas do Google Cloud Storage (GCS bucket) para baixar binários do Cosign em scripts de automação; utilize exclusivamente os assets de release do GitHub ou `ghcr.io/sigstore/cosign/cosign`.

## Como verificar
Execute `cosign version` no ambiente de CI e confirme que o binário provém de uma release oficial recente da série v2 suportada.

## Conexões
- [[cosign-oci-registry-artifacts-blobs-tekton-wasm-ebpf]] — Veja também: Publicação e assinatura de Blobs, Tekton Bundles, módulos WASM e programas eBPF em registros OCI.
- [[cosign-troubleshooting-rfc3161-timestamps-and-rekor-v2]] — Veja também: Diagnóstico de falhas de verificação no Cosign: RFC3161 timestamps, Rekor v2 e resiliência de serviços.

## Fontes
- [Sigstore Cosign GitHub — README.md (Keyless Signing, Verification, Air-Gapped, Blobs, Attestations)](https://raw.githubusercontent.com/sigstore/cosign/main/README.md) — README oficial do Sigstore Cosign cobrindo assinatura keyless via OIDC, Fulcio e Rekor, assinatura por chave/KMS, verificação online e air-gapped com TUF trusted_root.json, sign-blob/verify-blob e suporte a artefatos OCI (Tekton, WASM, eBPF) e atestações in-toto.; consultado em 2026-10-03.
- [Sigstore Documentation — Cosign Signing Overview](https://docs.sigstore.dev/cosign/signing/overview/) — Documentação oficial do Sigstore sobre fluxos de assinatura e verificação de contêineres e artefatos com Cosign.; consultado em 2026-10-03.
- [Sigstore Cosign — Official GitHub Repository](https://github.com/sigstore/cosign) — Repositório oficial do Cosign no projeto Sigstore com evolução futura convergente para sigstore-go.; consultado em 2026-10-03.
