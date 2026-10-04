---
id: software.devops.tranche04.000336
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
fontes: ["https://raw.githubusercontent.com/anchore/syft/main/README.md", "https://oss.anchore.com/docs/guides/sbom/getting-started/", "https://github.com/anchore/syft"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Criação de atestações de SBOM assinadas segundo a especificação in-toto com Syft

## Em uma frase
O README oficial do Syft destaca a capacidade de criar **atestações de SBOM assinadas** utilizando a especificação **in-toto** (`github.com/in-toto/attestation`), integrando-se diretamente a ferramentas de assinatura como o Sigstore Cosign. Em vez de distribuir o SBOM como um arquivo JSON solto sem vínculo criptográfico com a imagem, a atestação in-toto envelopa o SBOM como o predicado (`predicate`) de uma declaração (`Statement`) que referencia o digest SHA-256 exato da imagem avaliada.

## Por que importa
Um arquivo SBOM separado pode ser facilmente trocado por engano ou adulterado após o build. Quando o SBOM é emitido e assinado como uma atestação in-toto vinculada ao digest da imagem no registro OCI, controladores de admissão Kubernetes (como o Kyverno) podem verificar criptograficamente o SBOM antes de permitir a execução do pod.

## Como funciona
Gere atestações in-toto de SBOM nos pipelines de release e anexe-as à imagem no registro OCI com o Cosign, permitindo verificação automatizada de proveniência e conteúdo de pacotes no cluster.

## Exemplo
No pipeline de produção, o Syft gera o SBOM no formato compatível com atestação in-toto e o Cosign assina e anexa a atestação ao digest da imagem; na entrada do cluster, uma política verifica que toda imagem possui atestação de SBOM válida assinada pelo CI.

## Limites e trade-offs
Sempre vincule atestações de SBOM ao digest imutável (`@sha256:...`) da imagem e nunca apenas a uma tag mutável.

## Como verificar
Inspecione a atestação gerada confirmando a presença do envelope in-toto com `subject` apontando para o digest SHA-256 correto da imagem e `predicate` contendo o documento SBOM.

## Conexões
- [[syft-squashed-default-versus-all-layers-scope]] — Veja também: Escopo padrão squashed versus análise de todas as camadas com --scope all-layers no Syft.
- [[syft-offline-execution-privacy-and-enrich-flag]] — Veja também: Execução 100% local sem telemetria externa e enriquecimento opcional com --enrich no Syft.

## Fontes
- [Anchore Syft GitHub — README.md (Features, Ecosystems, Formats & CLI Basics)](https://raw.githubusercontent.com/anchore/syft/main/README.md) — README oficial do Anchore Syft descrevendo geração de SBOM para imagens de contêiner, sistemas de arquivos e arquivos compactados, suporte a dezenas de ecossistemas de pacotes, formatos CycloneDX, SPDX e Syft JSON, conversão entre formatos e atestações in-toto.; consultado em 2026-10-03.
- [Anchore Open Source Docs — Syft Getting Started Guide](https://oss.anchore.com/docs/guides/sbom/getting-started/) — Guia oficial de início rápido do Syft detalhando instalação, geração simultânea de tabela, SPDX-JSON e CycloneDX-JSON, inspeção com jq, escopo squashed padrão versus --scope all-layers, enriquecimento opcional --enrich e operação 100% local.; consultado em 2026-10-03.
- [Anchore Syft — Official GitHub Repository](https://github.com/anchore/syft) — Repositório oficial Apache-2.0 do Syft mantido pela Anchore.; consultado em 2026-10-03.
