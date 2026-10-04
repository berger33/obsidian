---
id: software.devops.tranche04.000345
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
fontes: ["https://raw.githubusercontent.com/anchore/grype/main/README.md", "https://oss.anchore.com/docs/guides/vulnerability/getting-started/", "https://github.com/anchore/grype"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Varredura ultrarrápida de SBOMs existentes via grype sbom:arquivo ou pipe Unix

## Em uma frase
Conforme demonstrado no README e no Getting Started oficial do Grype, além de escanear imagens diretamente, o Grype pode escanear um documento SBOM previamente gerado pelo Syft (ou por outra ferramenta compatível com SPDX/CycloneDX) usando `grype sbom:./sbom.json`, `grype alpine_latest-spdx.json` ou via pipe padrão Unix (`cat ./sbom.json | grype`).

## Por que importa
Analisar uma imagem de contêiner de vários gigabytes exige baixar camadas da rede, descompactar tarballs e varrer o sistema de arquivos; já analisar um arquivo SBOM JSON de poucos kilobytes leva milissegundos ou poucos segundos, tornando viável reavaliar milhares de artefatos sempre que o banco de CVEs é atualizado.

## Como funciona
Nos pipelines de CI/CD, gere o SBOM uma única vez com o Syft e passe o arquivo resultante diretamente para `grype sbom:./sbom.json`; armazene o SBOM para reexecuções contínuas fora do build.

## Exemplo
Um pipeline de build gera `alpine_latest-spdx.json` com o Syft e em seguida executa `grype alpine_latest-spdx.json`, obtendo os mesmos matches de vulnerabilidade instantaneamente sem reprocessar os blobs da imagem.

## Limites e trade-offs
Certifique-se de que o SBOM utilizado como entrada para o Grype foi gerado a partir da imagem exata (mesmo digest SHA-256) e com o escopo adequado, pois pacotes omitidos no SBOM não poderão ser avaliados pelo scanner.

## Como verificar
Compare o resultado de `grype alpine:latest` com `syft alpine:latest -o json | grype` e confirme que ambos produzem exatamente os mesmos matches de vulnerabilidade.

## Conexões
- [[grype-openvex-filtering-and-result-augmentation]] — Veja também: Filtragem e enriquecimento de resultados de scan com suporte a OpenVEX no Grype.
- [[grype-json-vulnerability-reports-and-stderr-progress]] — Veja também: Geração de relatórios de vulnerabilidade em JSON (--output json) com progresso separado em stderr.

## Fontes
- [Anchore Grype GitHub — README.md (Features, Ecosystems, EPSS, KEV, Risk Scoring & OpenVEX)](https://raw.githubusercontent.com/anchore/grype/main/README.md) — README oficial do Anchore Grype detalhando varredura de vulnerabilidades em imagens de contêiner, sistemas de arquivos e SBOMs, suporte a pacotes de SO e linguagens, priorização de ameaças e risco com EPSS, KEV e risk scoring, e filtragem/aumento de resultados com OpenVEX.; consultado em 2026-10-03.
- [Anchore Open Source Docs — Grype Getting Started Guide](https://oss.anchore.com/docs/guides/vulnerability/getting-started/) — Guia oficial de início rápido do Grype cobrindo instalação, varredura de imagens (grype alpine:latest), leitura de saída por severidade e status (fixed/not-fixed/ignored), varredura de SBOMs, relatórios JSON (--output json) e FAQ de operação offline e privacidade.; consultado em 2026-10-03.
- [Anchore Grype — Official GitHub Repository](https://github.com/anchore/grype) — Repositório oficial Apache-2.0 do scanner de vulnerabilidades Grype mantido pela Anchore.; consultado em 2026-10-03.
