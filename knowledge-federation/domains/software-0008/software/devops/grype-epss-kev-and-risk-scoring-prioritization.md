---
id: software.devops.tranche04.000343
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

# Priorização de ameaças e risco no Grype com EPSS, KEV e pontuação de risco (risk scoring)

## Em uma frase
Um dos recursos de destaque no README oficial do Grype é a **priorização de ameaças e risco** usando **EPSS** (Exploit Prediction Scoring System), o catálogo **KEV** (Known Exploited Vulnerabilities) e **pontuação de risco (risk scoring)**, documentados no guia de interpretação de resultados (`oss.anchore.com/docs/guides/vulnerability/interpreting-results/`). Além da severidade estática do CVSS (`Critical`, `High`, `Medium`, `Low`), essas métricas indicam a probabilidade estatística de exploração real e se a vulnerabilidade já está sendo ativamente explorada em ataques confirmados.

## Por que importa
Tratar centenas de CVEs apenas pela nota de severidade estática sobrecarrega as equipes de engenharia com alertas teóricos enquanto uma vulnerabilidade de severidade `High` presente no catálogo KEV (com exploração ativa comprovada) pode ficar na fila. Combinar severidade, disponibilidade de correção (`FIXED-IN`), EPSS e KEV foca a remediação no risco real.

## Como funciona
Extraia o relatório detalhado do Grype (`--output json`) nos pipelines de segurança para priorizar imediatamente qualquer vulnerabilidade marcada no catálogo KEV ou com alto score EPSS e versão de correção disponível (`fixed`).

## Exemplo
Durante a triagem semanal de segurança, a equipe filtra os relatórios do Grype priorizando vulnerabilidades que possuem simultaneamente patch disponível (`status: fixed`) e presença em KEV ou alto percentil EPSS, remediando primeiro os riscos exploráveis.

## Limites e trade-offs
Não ignore uma vulnerabilidade `High` ou `Medium` apenas porque o gate de CI bloqueia somente `Critical` se ela constar no catálogo KEV de vulnerabilidades ativamente exploradas.

## Como verificar
Inspecione a saída enriquecida do Grype (ou o relatório JSON) e verifique os indicadores de risco, EPSS, KEV e o resumo `by severity` / `by status: fixed, not-fixed, ignored`.

## Conexões
- [[grype-os-and-language-specific-package-scanning]] — Veja também: Suporte do Grype a pacotes de sistemas operacionais e dependências de linguagens.
- [[grype-openvex-filtering-and-result-augmentation]] — Veja também: Filtragem e enriquecimento de resultados de scan com suporte a OpenVEX no Grype.

## Fontes
- [Anchore Grype GitHub — README.md (Features, Ecosystems, EPSS, KEV, Risk Scoring & OpenVEX)](https://raw.githubusercontent.com/anchore/grype/main/README.md) — README oficial do Anchore Grype detalhando varredura de vulnerabilidades em imagens de contêiner, sistemas de arquivos e SBOMs, suporte a pacotes de SO e linguagens, priorização de ameaças e risco com EPSS, KEV e risk scoring, e filtragem/aumento de resultados com OpenVEX.; consultado em 2026-10-03.
- [Anchore Open Source Docs — Grype Getting Started Guide](https://oss.anchore.com/docs/guides/vulnerability/getting-started/) — Guia oficial de início rápido do Grype cobrindo instalação, varredura de imagens (grype alpine:latest), leitura de saída por severidade e status (fixed/not-fixed/ignored), varredura de SBOMs, relatórios JSON (--output json) e FAQ de operação offline e privacidade.; consultado em 2026-10-03.
- [Anchore Grype — Official GitHub Repository](https://github.com/anchore/grype) — Repositório oficial Apache-2.0 do scanner de vulnerabilidades Grype mantido pela Anchore.; consultado em 2026-10-03.
