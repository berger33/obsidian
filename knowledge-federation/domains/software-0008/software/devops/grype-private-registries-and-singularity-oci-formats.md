---
id: software.devops.tranche04.000350
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

# Suporte a registros privados e formatos de imagem Docker, OCI e Singularity no Grype

## Em uma frase
O Grype suporta nativamente múltiplos formatos de imagem de contêiner — incluindo **Docker**, **OCI** e **Singularity** (`github.com/sylabs/singularity`, muito utilizado em computação científica e HPC) — além de autenticação para registros de contêineres privados documentada no guia oficial (`oss.anchore.com/docs/guides/private-registries/`).

## Por que importa
Organizações que operam tanto clusters Kubernetes corporativos (com imagens OCI/Docker em registros privados) quanto ambientes de computação de alto desempenho e IA (com imagens Singularity) conseguem padronizar um único motor de varredura de vulnerabilidades em toda a infraestrutura.

## Como funciona
Utilize as credenciais de registro privado configuradas no ambiente para permitir que o Grype inspecione imagens diretamente nos registros internos ou aponte o Grype para arquivos de imagem OCI, Docker ou Singularity locais no pipeline de homologação.

## Exemplo
Um laboratório de pesquisa e engenharia que executa cargas de treinamento em Singularity e microsserviços de inferência em OCI usa o mesmo binário do Grype nos dois pipelines para auditar vulnerabilidades antes do deploy.

## Limites e trade-offs
Ao autenticar o Grype em registros privados dentro de runners compartilhados, utilize tokens de leitura de escopo mínimo e curta duração em vez de credenciais administrativas permanentes.

## Como verificar
Execute o Grype contra uma imagem armazenada em registro privado ou arquivo OCI local e confirme o sucesso das etapas `Loaded image` e `Parsed image sha256:...`.

## Conexões
- [[grype-ci-cd-severity-gates-and-fixed-status-filtering]] — Veja também: Gates de severidade em pipelines CI/CD e distinção entre vulnerabilidades fixed e not-fixed no Grype.

## Fontes
- [Anchore Grype GitHub — README.md (Features, Ecosystems, EPSS, KEV, Risk Scoring & OpenVEX)](https://raw.githubusercontent.com/anchore/grype/main/README.md) — README oficial do Anchore Grype detalhando varredura de vulnerabilidades em imagens de contêiner, sistemas de arquivos e SBOMs, suporte a pacotes de SO e linguagens, priorização de ameaças e risco com EPSS, KEV e risk scoring, e filtragem/aumento de resultados com OpenVEX.; consultado em 2026-10-03.
- [Anchore Open Source Docs — Grype Getting Started Guide](https://oss.anchore.com/docs/guides/vulnerability/getting-started/) — Guia oficial de início rápido do Grype cobrindo instalação, varredura de imagens (grype alpine:latest), leitura de saída por severidade e status (fixed/not-fixed/ignored), varredura de SBOMs, relatórios JSON (--output json) e FAQ de operação offline e privacidade.; consultado em 2026-10-03.
- [Anchore Grype — Official GitHub Repository](https://github.com/anchore/grype) — Repositório oficial Apache-2.0 do scanner de vulnerabilidades Grype mantido pela Anchore.; consultado em 2026-10-03.
