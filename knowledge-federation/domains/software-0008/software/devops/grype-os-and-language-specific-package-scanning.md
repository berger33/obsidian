---
id: software.devops.tranche04.000342
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

# Suporte do Grype a pacotes de sistemas operacionais e dependências de linguagens

## Em uma frase
O README oficial do Grype documenta cobertura abrangente tanto para os principais ecossistemas de sistemas operacionais — **Alpine, Debian, Ubuntu, RHEL, Oracle Linux, Amazon Linux** e outros (`oss.anchore.com/docs/capabilities/all-os/`) — quanto para pacotes específicos de linguagens de programação — **Ruby, Java, JavaScript, Python, .NET, Go, PHP, Rust** e outros (`oss.anchore.com/docs/capabilities/all-packages/`).

## Por que importa
Muitas ferramentas legadas verificam apenas avisos de segurança da distribuição Linux ou apenas um arquivo de lock de linguagem isolado. O Grype cruza ambos os mundos em uma única varredura, correlacionando pacotes de SO com advisories específicos da distro (que consideram backports de patches) e bibliotecas de linguagem com bancos de CVEs e GHSA.

## Como funciona
Utilize o Grype em imagens de aplicações políglotas para unificar em um único relatório a avaliação de pacotes da distribuição base e de bibliotecas de runtime (como JARs Java, pacotes `pip` Python, módulos Go ou crates Rust).

## Exemplo
Em um serviço corporativo escrito em Java rodando sobre uma imagem base Ubuntu, o Grype avalia os pacotes `.deb` contra os advisories da Canonical/Ubuntu e simultaneamente inspeciona os arquivos `.jar` em busca de CVEs conhecidos do ecossistema Maven.

## Limites e trade-offs
Evite usar imagens base de distribuições obscuras ou sem feed de segurança estruturado quando possível, pois o casamento preciso de status `fixed` em pacotes de SO depende dos feeds oficiais de advisories das distribuições suportadas.

## Como verificar
Inspecione a coluna `TYPE` na saída do Grype (como `apk`, `deb`, `rpm`, `go-module`, `python`, `java-archive`) confirmando que ambas as camadas da aplicação foram avaliadas.

## Conexões
- [[grype-vulnerability-scanner-for-containers-filesystems-and-sboms]] — Veja também: Grype como scanner de vulnerabilidades para imagens de contêiner, diretórios e SBOMs.
- [[grype-epss-kev-and-risk-scoring-prioritization]] — Veja também: Priorização de ameaças e risco no Grype com EPSS, KEV e pontuação de risco (risk scoring).

## Fontes
- [Anchore Grype GitHub — README.md (Features, Ecosystems, EPSS, KEV, Risk Scoring & OpenVEX)](https://raw.githubusercontent.com/anchore/grype/main/README.md) — README oficial do Anchore Grype detalhando varredura de vulnerabilidades em imagens de contêiner, sistemas de arquivos e SBOMs, suporte a pacotes de SO e linguagens, priorização de ameaças e risco com EPSS, KEV e risk scoring, e filtragem/aumento de resultados com OpenVEX.; consultado em 2026-10-03.
- [Anchore Open Source Docs — Grype Getting Started Guide](https://oss.anchore.com/docs/guides/vulnerability/getting-started/) — Guia oficial de início rápido do Grype cobrindo instalação, varredura de imagens (grype alpine:latest), leitura de saída por severidade e status (fixed/not-fixed/ignored), varredura de SBOMs, relatórios JSON (--output json) e FAQ de operação offline e privacidade.; consultado em 2026-10-03.
- [Anchore Grype — Official GitHub Repository](https://github.com/anchore/grype) — Repositório oficial Apache-2.0 do scanner de vulnerabilidades Grype mantido pela Anchore.; consultado em 2026-10-03.
