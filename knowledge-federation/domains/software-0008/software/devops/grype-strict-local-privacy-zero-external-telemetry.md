---
id: software.devops.tranche04.000348
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

# Privacidade estrita no Grype: execução 100% local sem envio de dados externos

## Em uma frase
À pergunta oficial do FAQ *"What data does Grype send externally?"*, a documentação da Anchore responde de forma categórica: **"Nothing. Grype runs entirely locally and doesn’t send any data to external services."** Todo o processo de catalogação dos pacotes, leitura de SBOMs e cruzamento com o banco de vulnerabilidades ocorre exclusivamente na máquina local onde o binário do Grype está sendo executado.

## Por que importa
Ferramentas de segurança que enviam a lista de pacotes internos, nomes de binários proprietários ou hashes de arquivos para uma nuvem externa violam políticas de confidencialidade e soberania de dados em setores financeiro, governamental e de saúde.

## Como funciona
Adote o Grype com segurança em pipelines que auditam código proprietário e imagens internas críticas, sabendo que nenhuma informação sobre os pacotes encontrados ou vulnerabilidades detectadas é transmitida para fora do ambiente.

## Exemplo
Durante a homologação de ferramentas de DevSecOps pelo time de governança e privacidade, a arquitetura comprova pela documentação oficial e por captura de tráfego de rede que o Grype apenas baixa o feed público de CVEs e processa todas as correspondências localmente.

## Limites e trade-offs
Não confunda o download inicial do banco público de vulnerabilidades com envio de telemetria; se desejar eliminar até mesmo a conexão de download da base durante o build, pré-carregue o banco de dados no ambiente.

## Como verificar
Execute `grype sbom:./sbom.json` com o banco de dados já presente em cache local e monitore o tráfego de saída para confirmar que zero pacotes de dados dos artefatos analisados são enviados externamente.

## Conexões
- [[grype-vulnerability-database-management-and-offline-scanning]] — Veja também: Gerenciamento do banco de dados de vulnerabilidades e operação offline no Grype.
- [[grype-ci-cd-severity-gates-and-fixed-status-filtering]] — Veja também: Gates de severidade em pipelines CI/CD e distinção entre vulnerabilidades fixed e not-fixed no Grype.

## Fontes
- [Anchore Grype GitHub — README.md (Features, Ecosystems, EPSS, KEV, Risk Scoring & OpenVEX)](https://raw.githubusercontent.com/anchore/grype/main/README.md) — README oficial do Anchore Grype detalhando varredura de vulnerabilidades em imagens de contêiner, sistemas de arquivos e SBOMs, suporte a pacotes de SO e linguagens, priorização de ameaças e risco com EPSS, KEV e risk scoring, e filtragem/aumento de resultados com OpenVEX.; consultado em 2026-10-03.
- [Anchore Open Source Docs — Grype Getting Started Guide](https://oss.anchore.com/docs/guides/vulnerability/getting-started/) — Guia oficial de início rápido do Grype cobrindo instalação, varredura de imagens (grype alpine:latest), leitura de saída por severidade e status (fixed/not-fixed/ignored), varredura de SBOMs, relatórios JSON (--output json) e FAQ de operação offline e privacidade.; consultado em 2026-10-03.
- [Anchore Grype — Official GitHub Repository](https://github.com/anchore/grype) — Repositório oficial Apache-2.0 do scanner de vulnerabilidades Grype mantido pela Anchore.; consultado em 2026-10-03.
