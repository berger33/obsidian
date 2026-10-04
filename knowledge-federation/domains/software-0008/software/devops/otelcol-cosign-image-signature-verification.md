---
id: software.devops.tranche01.000005
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/README.md", "https://github.com/open-telemetry/opentelemetry-collector"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Verificação criptográfica de assinaturas das imagens oficiais com Sigstore Cosign

## Em uma frase
A seção Verifying the images signatures do README documenta que as imagens otel/opentelemetry-collector e otel/opentelemetry-collector-contrib são assinadas com a ferramenta sigstore cosign e podem ser verificadas com o comando cosign verify passando --certificate-identity=https://github.com/open-telemetry/opentelemetry-collector-releases/.github/workflows/base-release.yaml@refs/tags/<RELEASE_TAG> e --certificate-oidc-issuer=https://token.actions.githubusercontent.com seguido da referência da imagem.

## Por que importa
Como o Collector roda com acesso privilegiado à rede interna e a credenciais de exportação para back-ends de produção, validar a assinatura keyless via OIDC do GitHub Actions e o log de transparência antes do deploy protege a cadeia de suprimentos contra imagens adulteradas.

## Como funciona
Instale o cosign e inclua a verificação cosign verify com --certificate-identity apontando para a tag exata da release e --certificate-oidc-issuer=https://token.actions.githubusercontent.com no pipeline de promoção de imagens ou no controlador de admissão do cluster.

## Exemplo
No exemplo reproduzido pelo README para a tag v0.98.0 da imagem ghcr.io/open-telemetry/opentelemetry-collector-releases/opentelemetry-collector-contrib:0.98.0, o cosign valida as claims, confirma a presença no transparency log offline e verifica o certificado de assinatura de código.

## Limites e trade-offs
O valor de <RELEASE_TAG> na flag --certificate-identity precisa corresponder exatamente à versão da imagem verificada (por exemplo refs/tags/v0.98.0 para a tag 0.98.0).

## Como verificar
Conferi a seção Verifying the images signatures no README oficial do OpenTelemetry Collector.

## Conexões
- [[otelcol-go-minor-version-compatibility-policy]] — Veja também: Política de suporte a versões menores do Go (N e N-1, remoção de N-2) quando usado como biblioteca.
- [[otelcol-component-stability-tiers-per-signal]] — Veja também: Os seis níveis de estabilidade de componentes por sinal: Development a Unmaintained.

## Fontes
- [OpenTelemetry Collector — README oficial](https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/README.md) — README oficial do OpenTelemetry Collector com proposta vendor-agnostic, cinco objetivos, versão OTLP v1.10.0, política de versões menores N e N-2 do Go, verificação cosign e governança do SIG.; consultado em 2026-10-03.
- [Repositório oficial open-telemetry/opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-collector) — Repositório oficial do OpenTelemetry Collector no GitHub com docs/vision.md, docs/security-best-practices.md, código-fonte e releases.; consultado em 2026-10-03.
